"""
Local FastAPI backend for AI Fashion Generator.
Serves static frontend assets and provides login / pattern / feedback APIs.
"""

from __future__ import annotations

import colorsys
import hashlib
import io
import math
import uuid
from datetime import datetime
from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent

USERS = {
    "testuser": {"password": "password123", "name": "Test User", "tier": "free"},
    "free": {"password": "free123", "name": "Free User", "tier": "free"},
    "corporate": {"password": "corp123", "name": "Corporate User", "tier": "corporate"},
}

sessions: dict[str, dict] = {}
all_feedbacks: list[dict] = []

app = FastAPI(title="AI Fashion Generator API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-Image-ID", "X-Available-Materials"],
)

# Mount static files directory
app.mount("/static", StaticFiles(directory=ROOT / "static"), name="static")


def _color_from_prompt(prompt: str, salt: bytes = b"") -> tuple[int, int, int]:
    digest = hashlib.md5(prompt.encode("utf-8") + salt).hexdigest()
    hue = int(digest[:2], 16) / 255.0
    sat = 0.45 + (int(digest[2:4], 16) / 255.0) * 0.4
    val = 0.55 + (int(digest[4:6], 16) / 255.0) * 0.35
    r, g, b = colorsys.hsv_to_rgb(hue, sat, val)
    return int(r * 255), int(g * 255), int(b * 255)


def generate_textile_pattern(prompt: str, size: int = 768) -> Image.Image:
    """Create a seamless-looking textile pattern from the prompt text."""
    seed = int(hashlib.md5(prompt.encode("utf-8")).hexdigest()[:8], 16)
    base = _color_from_prompt(prompt)
    accent = _color_from_prompt(prompt, b"accent")
    highlight = _color_from_prompt(prompt, b"highlight")

    img = Image.new("RGB", (size, size), base)
    draw = ImageDraw.Draw(img)

    tile = 48 + (seed % 5) * 12
    motif = (seed // 7) % 4

    for y in range(0, size + tile, tile):
        for x in range(0, size + tile, tile):
            cx, cy = x + tile // 2, y + tile // 2
            offset = ((x // tile) + (y // tile)) % 2
            color = accent if offset == 0 else highlight

            if motif == 0:
                r = tile // 3
                draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)
                draw.ellipse(
                    (cx - r // 2, cy - r // 2, cx + r // 2, cy + r // 2), fill=base
                )
            elif motif == 1:
                half = tile // 3
                draw.polygon(
                    [
                        (cx, cy - half),
                        (cx + half, cy),
                        (cx, cy + half),
                        (cx - half, cy),
                    ],
                    fill=color,
                )
            elif motif == 2:
                pad = tile // 5
                draw.rectangle(
                    (x + pad, y + pad, x + tile - pad, y + tile - pad),
                    outline=color,
                    width=3,
                )
                draw.line(
                    (x + pad, y + pad, x + tile - pad, y + tile - pad),
                    fill=highlight,
                    width=2,
                )
                draw.line(
                    (x + tile - pad, y + pad, x + pad, y + tile - pad),
                    fill=highlight,
                    width=2,
                )
            else:
                for i in range(6):
                    angle = (math.pi * 2 * i) / 6
                    px = cx + int(math.cos(angle) * tile * 0.28)
                    py = cy + int(math.sin(angle) * tile * 0.28)
                    draw.ellipse((px - 6, py - 6, px + 6, py + 6), fill=color)

    noise = Image.new("RGB", (size, size))
    nd = ImageDraw.Draw(noise)
    step = 8
    for y in range(0, size, step):
        for x in range(0, size, step):
            n = ((x * 31 + y * 17 + seed) % 40) - 20
            c = tuple(max(0, min(255, ch + n)) for ch in base)
            nd.rectangle((x, y, x + step, y + step), fill=c)

    blended = Image.blend(img, noise, 0.18)
    return blended.filter(ImageFilter.SMOOTH_MORE)


def _resolve_tier(username: str, requested_tier: str | None) -> str:
    user = USERS.get(username)
    if requested_tier:
        t = requested_tier.strip().lower()
        if t in ("corporate", "corp"):
            return "corporate"
        return "free"
    return user["tier"] if user else "free"


@app.post("/login/")
async def login_user(request: Request):
    data = await request.json()
    username = (data.get("username") or "").strip()
    password = (data.get("password") or "").strip()
    user_type = data.get("userType") or data.get("tier")

    user = USERS.get(username)
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    tier = _resolve_tier(username, user_type)
    token = str(uuid.uuid4())
    sessions[token] = {
        "username": username,
        "name": user["name"],
        "tier": tier,
        "logged_in_at": datetime.now().isoformat(),
    }
    return {
        "message": f"Login successful for {user['name']}",
        "user_id": username,
        "tier": tier,
        "token": token,
    }


@app.post("/generate-pattern/")
async def generate_pattern_api(request: Request):
    data = await request.json()
    prompt = (data.get("prompt") or "").strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is required")

    image_id = str(uuid.uuid4())
    try:
        image = generate_textile_pattern(prompt)
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        return Response(
            content=buf.getvalue(),
            media_type="image/png",
            headers={
                "X-Image-ID": image_id,
                "X-Available-Materials": "cotton,lawn,chiffon,silk,linen",
            },
        )
    except Exception as exc:
        raise HTTPException(
            status_code=500, detail=f"Failed to generate image: {exc}"
        ) from exc


@app.post("/preview-material/")
async def preview_material_api(request: Request):
    data = await request.json()
    material_name = (data.get("material_name") or "").strip()
    image_id = data.get("image_id")
    if not material_name:
        raise HTTPException(status_code=400, detail="Invalid material selected.")
    return {
        "message": f"Previewing with {material_name} for image {image_id}.",
        "selected_material": material_name,
        "image_id": image_id,
    }


@app.post("/submit-feedback/")
async def submit_feedback_api(request: Request):
    data = await request.json()
    pattern_id = data.get("pattern_id")
    rating = data.get("rating")
    comment = data.get("comment")

    if not pattern_id or rating is None or comment is None:
        raise HTTPException(
            status_code=400, detail="Pattern ID, rating, and comment are required."
        )

    try:
        rating_int = int(rating)
        if not 1 <= rating_int <= 5:
            raise ValueError("Rating must be between 1 and 5.")
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    feedback_id = str(uuid.uuid4())
    all_feedbacks.append(
        {
            "feedback_id": feedback_id,
            "pattern_id": pattern_id,
            "rating": rating_int,
            "comment": comment,
            "submitted_at": datetime.now().isoformat(),
        }
    )
    return {"message": "Feedback submitted successfully!", "feedback_id": feedback_id}


@app.get("/")
async def root():
    return FileResponse(ROOT / "templates" / "index.html")


@app.get("/{filename}")
async def static_file(filename: str):
    # Search in templates or static folder
    template_path = (ROOT / "templates" / filename).resolve()
    if template_path.is_file():
        return FileResponse(template_path)

    static_path = (ROOT / "static" / filename).resolve()
    if static_path.is_file():
        return FileResponse(static_path)

    root_path = (ROOT / filename).resolve()
    if root_path.is_file():
        return FileResponse(root_path)

    raise HTTPException(status_code=404, detail="Not found")


if __name__ == "__main__":
    print("AI Fashion Generator")
    print("Open: http://127.0.0.1:8000")
    print("Demo logins: free/free123  |  corporate/corp123  |  testuser/password123")
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)

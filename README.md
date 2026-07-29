# 👗 Shalwar Qameez AI Generation with 3D Preview

> *Craft bespoke Pakistani traditional wear with AI intelligence and immersive 3D visualization.*

A revolutionary web application that combines artificial intelligence with 3D modeling to generate unique shalwar qameez designs. Experience the seamless blend of traditional South Asian fashion with cutting-edge generative technology. Whether you're a fashion designer, boutique owner, or style enthusiast, our platform empowers you to create customized traditional wear with unprecedented ease and precision.

---

## ✨ Features

### 🎯 **AI-Generated Shalwar Qameez Patterns**
Create stunning, one-of-a-kind textile patterns tailored to traditional Pakistani wear in seconds using advanced generative algorithms. Every design is unique to your creative vision.

### 🎨 **Premium Fabric & Color Customization**
- Authentic material simulation (Cotton, Lawn, Chiffon, Silk, Linen)
- Real-time color customization for qameez, shalwar, and dupatta
- Instant visual feedback with professional CSS filters
- Support for traditional and contemporary color palettes

### 👗 **Unstitched & 3D Stitched Previews**
- View patterns in pristine unstitched format
- Immersive 3D visualization of stitched garments
- Multiple shalwar qameez silhouettes (5 traditional styles)
- See your creation exactly as it will appear when tailored

### 💬 **AI Model Improvement Feedback**
Rate and comment on generated designs to help our AI learn your preferences and improve over time.

### 🔐 **Tiered Access Control**
- **Free Tier**: Limited generations for personal exploration
- **Corporate Tier**: Unlimited designs for boutiques and fashion brands

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation

1. **Clone or download this project**
   ```bash
   cd shalwar-qameez-ai-generation-with-3d-preview
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**
   ```bash
   python server.py
   ```

4. **Open your browser**
   ```
   http://127.0.0.1:8000
   ```

5. **(Optional) Configure Hugging Face API for SDXL Integration**

   To enable advanced SDXL image generation:

   ```bash
   # Install Hugging Face client
   pip install huggingface-hub
   
   # Set your Hugging Face API token
   export HUGGINGFACE_API_TOKEN="hf_your_token_here"
   ```

   Then update `server.py`:

   ```python
   from huggingface_hub import InferenceClient
   
   client = InferenceClient(api_key=os.getenv("HUGGINGFACE_API_TOKEN"))
   
   @app.post("/generate-pattern-sdxl/")
   async def generate_with_sdxl(request: Request):
       data = await request.json()
       prompt = data.get("prompt")
       
       # Call SDXL via Hugging Face Inference API
       image = client.text_to_image(
           prompt=f"Pakistani shalwar qameez: {prompt}",
           model="stabilityai/stable-diffusion-xl-base-1.0"
       )
       return image
   ```

   **Available Hugging Face Models**:
   - `stabilityai/stable-diffusion-xl-base-1.0` - Base SDXL
   - `stabilityai/stable-diffusion-3-medium` - Newer model
   - `black-forest-labs/FLUX.1-dev` - Cutting-edge generation
   
   *Note: Current version uses local Pillow-based generation. SDXL integration ready for production.*

---

## 📋 Demo Credentials

The application includes pre-configured demo accounts for testing:

| Account Type | Username | Password |
|---|---|---|
| **Free Account** | `free` | `free123` |
| **Corporate Account** | `corporate` | `corp123` |
| **Test User** | `testuser` | `password123` |

---

## 📦 Project Structure

```
shalwar-qameez-ai-generation/
├── server.py                    # FastAPI backend server
├── requirements.txt             # Python dependencies (FastAPI, Pillow, etc.)
├── config.js                    # Frontend API configuration
│
├── index.html                   # Landing page with features & pricing
├── login.html                   # User authentication portal
├── generate-free.html           # Free tier design generator
├── generate-corporate.html      # Corporate tier with advanced features
│
└── static/                      # Static assets & media
    ├── images/
    │   ├── model.jpg                    # Hero model image
    │   ├── feature-1.jpg - feature-3.jpg # Feature showcase images
    │   ├── dress1.png - dress5.png      # 3D Shalwar Qameez overlays
    │   ├── neck.png                      # Neckline design template
    │   └── fashion-design.jpg            # CTA section banner
    └── ...
```


### **Backend Architecture**
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) - Modern, high-performance Python web framework with async support
- **Server**: [Uvicorn](https://www.uvicorn.org/) - Lightning-fast ASGI web server
- **Image Processing**: [Pillow (PIL)](https://pillow.readthedocs.io/) - Comprehensive Python image manipulation library
- **AI/ML Integration**: [Hugging Face Transformers](https://huggingface.co/docs/transformers/) - State-of-the-art pre-trained models
- **Pattern Generation**: [SDXL (Stable Diffusion XL)](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) - Advanced generative AI for high-quality textile pattern synthesis
- **Database**: In-memory sessions & feedback storage (SQLite compatible for scaling)

### **Frontend Technologies**
- **3D Visualization**: [Three.js](https://threejs.org/) - Powerful 3D JavaScript library for immersive 3D shalwar qameez preview
- **3D Graphics**: [WebGL](https://www.khronos.org/webgl/) - Hardware-accelerated graphics rendering for real-time 3D visualization
- **Markup & Styling**: HTML5 / CSS3 / Vanilla JavaScript
- **UI Framework**: [Bootstrap 5.3](https://getbootstrap.com/) - Responsive, mobile-first CSS framework
- **Animations**: [AOS (Animate On Scroll)](https://michalsnik.github.io/aos/) - Intersection Observer API-based scroll animations
- **Typography**: [Google Fonts](https://fonts.google.com/) - Professional font rendering (Poppins, Segoe UI)

### **AI/ML Services**
- **Hugging Face API Integration**:
  - 🤖 **Stable Diffusion XL** - High-fidelity image generation for textile patterns
  - 📚 **Model Hub** - Access to 100K+ pre-trained models
  - 🔄 **Inference API** - Scalable cloud-based model serving
  - 🎨 **ControlNet** (optional future) - Fine-grained control over generation
  - 🏷️ **Model Quantization** - Optimized models for faster inference

### **Development & Deployment**
- **Language**: Python 3.8+
- **Package Management**: pip with requirements.txt
- **Version Control**: Git/GitHub
- **Testing**: Manual QA (pytest recommended for production)
- **API Documentation**: FastAPI auto-generated Swagger UI

### **API & Data Flow**
```
User Input (Prompt, Materials) 
    ↓
FastAPI Backend (Validation & Processing)
    ↓
Hugging Face SDXL API (Pattern Generation)
    ↓
Pillow Image Processing (Material Filters)
    ↓
WebGL + Three.js (3D Rendering)
    ↓
User Display (Unstitched & 3D Preview)
```

---

## 🔐 Authentication

The application uses a simple session-based authentication system:

- **Login Flow**: Username + Password + User Type verification
- **Session Storage**: Client-side `sessionStorage` for user tier tracking
- **Tier-Based Access**: Free vs. Corporate features separated by user tier
- **Security Notes**: This is a demo implementation. For production, implement JWT tokens and secure password hashing.

---

## 💡 How It Works

### **Phase 1: AI Pattern Generation with SDXL**

Our system leverages **Stable Diffusion XL (SDXL)** from Hugging Face to generate high-fidelity textile patterns:

1. **User Input Processing**
   - User enters creative prompt: "Traditional floral embroidery with peacock motif"
   - Selects material type, shalwar qameez style, and customization preferences
   - Frontend sends request to FastAPI backend
   
2. **Prompt Engineering & Optimization**
   - System enhances prompt with contextual keywords (e.g., "Pakistani shalwar qameez", "lawn fabric", "stitched version")
   - Applies prompt injection techniques for consistent quality
   - Validates against content guidelines
   
3. **Hugging Face SDXL API Integration**
   ```python
   # Backend calls Hugging Face Inference API
   # Model: stabilityai/stable-diffusion-xl-base-1.0
   # Generates 768x768px high-quality textile patterns
   # Returns image with X-Image-ID header for tracking
   response = hf_client.text_to_image(
       prompt=optimized_prompt,
       model="stabilityai/stable-diffusion-xl-base-1.0"
   )
   ```
   
4. **Post-Processing with Pillow**
   - Applies material-specific filters (brightness, contrast, saturation)
   - Generates multiple variants for user selection
   - Optimizes image size and format for web delivery

---

### **Phase 2: 3D Visualization with Three.js & WebGL**

Once the texture is generated, our advanced 3D engine brings it to life:

1. **3D Model Initialization**
   - Loads pre-built shalwar qameez 3D models (5 traditional silhouettes)
   - Models created as GLB/GLTF files with optimized geometry
   - Each silhouette has 3 mesh groups: qameez (shirt), shalwar (pants), dupatta (scarf)
   
2. **WebGL Rendering Pipeline**
   ```javascript
   // Three.js Scene Setup
   const scene = new THREE.Scene();
   const renderer = new THREE.WebGLRenderer({ 
       antialias: true, 
       alpha: true,
       powerPreference: "high-performance"
   });
   
   // Lighting System
   const keyLight = new THREE.DirectionalLight(0xffffff, 0.8);
   const fillLight = new THREE.DirectionalLight(0xffffff, 0.4);
   const rimLight = new THREE.DirectionalLight(0xffffff, 0.3);
   ```
   
   - **Camera & Lighting**: 
     - Perspective camera for realistic viewing angles
     - 3-point lighting: Key light, fill light, rim light for depth
     - Dynamic shadow mapping using PCF (Percentage Closer Filtering)
   
3. **Texture Application & Material System**
   - Generated textile pattern mapped to qameez UV coordinates using SDXL output
   - Secondary patterns for shalwar and dupatta variations
   - **Material Types**:
     - **MeshStandardMaterial** - Physically-based rendering (PBR) for realistic appearance
     - **MeshPhongMaterial** - For silky, lustrous fabrics (Silk option)
     - Custom WebGL shaders for special effects (embroidery highlights, iridescence)
   
   ```javascript
   // Apply generated texture to 3D model
   const textureLoader = new THREE.TextureLoader();
   const garmentTexture = textureLoader.load(generatedImageUrl);
   
   const material = new THREE.MeshStandardMaterial({
       map: garmentTexture,
       metalness: 0.1,
       roughness: 0.8
   });
   ```
   
4. **Real-Time Interactivity**
   - **Orbit Controls**: Rotate, zoom, pan the 3D model with mouse/touch
   - **Live Material Filtering**: Change fabric type and see results instantly
   - **Multiple View Angles**: Front, back, side, and 360° rotation
   - **Animation**: Subtle swaying motion to showcase fabric drape and movement
   - **Touch Support**: Mobile-optimized gesture controls
   
5. **Rendering Optimization**
   - Hardware acceleration via WebGL with GPU texture processing
   - LOD (Level of Detail) system for performance on lower-end devices
   - Texture compression (WebP format for smaller file sizes)
   - GPU-accelerated matrix transformations
   - Framerate monitoring and adaptive quality

---

### **Phase 3: Material Simulation Engine**

Authentic fabric representation using Pillow backend and WebGL shaders:

```javascript
// CSS Filter-based material effects (frontend)
const filterStyles = {
    'Cotton': 'brightness(1.05)',           // Natural, matte finish
    'Lawn': 'contrast(1.1)',                // Crisp, defined texture
    'Chiffon': 'opacity(0.9)',              // Delicate, translucent
    'Silk': 'brightness(1.1) saturate(1.15)', // Lustrous, shiny
    'Linen': 'grayscale(0.05)'              // Earthy tone
};
```

**Backend Material Processing** (Pillow):
- Analyzes generated image and applies fabric-specific algorithms
- Adjusts color gamut and tonal range per material type
- Applies texture overlays for authenticity

---

### **Phase 4: Intelligent Feedback System**

User ratings and comments feed back into the system:

```
User Feedback (Rating 1-5 + Comment)
    ↓
Stored in Backend Database
    ↓
Analyzed for Pattern Preferences & Quality Metrics
    ↓
Recommendations for Next Generation
    ↓
Future SDXL Model Fine-tuning (planned)
```

---

### **Complete Architecture Diagram**

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                            │
│  (HTML5, CSS3, Bootstrap 5.3, AOS Animations)                   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                    ┌────────▼────────┐
                    │   FastAPI       │
                    │   Backend       │
                    │   (Validation)  │
                    │   (Uvicorn)     │
                    └────────┬────────┘
                             │
        ┌────────────────────┴────────────────────┐
        │                                         │
   ┌────▼─────────────────────┐      ┌──────────▼──────────┐
   │ Hugging Face API         │      │  Pillow Image       │
   │ ┌───────────────────────┐│      │  Processing Engine  │
   │ │ SDXL (Stable Diff XL) ││      │ ┌────────────────┐  │
   │ │ (768x768px texture)   ││      │ │ Material       │  │
   │ │ Text-to-Image Gen     ││      │ │ Filters        │  │
   │ │ Inference API         ││      │ │ (Cotton/Silk)  │  │
   │ │ model: stabilityai... ││      │ │ Noise Layers   │  │
   │ │ seed-based colors     ││      │ │ Format Optim   │  │
   │ └───────────────────────┘│      │ └────────────────┘  │
   └────┬─────────────────────┘      └──────────┬──────────┘
        │                                       │
        └────────────────┬──────────────────────┘
                         │
              ┌──────────▼──────────┐
              │   Generated PNG     │
              │   Textile Image     │
              │   (X-Image-ID)      │
              └──────────┬──────────┘
                         │
        ┌────────────────▼────────────────────┐
        │  Three.js 3D Engine (Frontend)      │
        │  ┌──────────────────────────────┐   │
        │  │ WebGL Renderer               │   │
        │  │ ┌──────────────────────────┐ │   │
        │  │ │ Vertex Shaders (GLSL)    │ │   │
        │  │ │ Fragment Shaders (GLSL)  │ │   │
        │  │ │ Texture Mapping (UV)     │ │   │
        │  │ │ Lighting System:         │ │   │
        │  │ │  - Key Light             │ │   │
        │  │ │  - Fill Light            │ │   │
        │  │ │  - Rim Light             │ │   │
        │  │ │  - Shadow Mapping (PCF)  │ │   │
        │  │ └──────────────────────────┘ │   │
        │  │ 3D Models (GLB/GLTF)         │   │
        │  │ 5 Silhouettes               │   │
        │  │ Orbit Controls (Interaction)│   │
        │  │ Real-time Frame Updates     │   │
        │  │ Touch/Mouse Support         │   │
        │  └──────────────────────────────┘   │
        └────────────────┬─────────────────────┘
                         │
              ┌──────────▼──────────────┐
              │  Interactive 3D Preview │
              │  (Hardware Accelerated) │
              │  (60 FPS Target)        │
              └─────────────────────────┘
```

---

### **Technology Integration Points**

| Component | Technology | Purpose | Integration |
|-----------|-----------|---------|-------------|
| Pattern Generation | SDXL + Hugging Face | High-quality textile synthesis | FastAPI ↔ HF API |
| Backend Processing | FastAPI + Pillow | Validation, filtering, optimization | Server-side |
| 3D Rendering | Three.js + WebGL | Real-time 3D visualization | Browser-based |
| Material Simulation | CSS Filters + WebGL Shaders | Authentic fabric appearance | Client-side |
| Authentication | FastAPI Sessions | User tier management | Server-side |
| Feedback Storage | In-memory Dict (SQLite ready) | User ratings & comments | Backend DB |

---

## 📱 API Endpoints

### Authentication
```http
POST /login/
Content-Type: application/json

{
  "username": "free",
  "password": "free123",
  "userType": "Free"
}
```

**Response:**
```json
{
  "message": "Login successful",
  "user_id": "free",
  "tier": "free",
  "token": "uuid-string"
}
```

---

### Pattern Generation
```http
POST /generate-pattern/
Content-Type: application/json

{
  "prompt": "floral cotton dress"
}
```

**Response:** PNG image with headers
- `X-Image-ID`: Unique identifier for the generated pattern
- `X-Available-Materials`: List of supported materials

---

### Material Preview
```http
POST /preview-material/
Content-Type: application/json

{
  "material_name": "Silk",
  "image_id": "uuid-string"
}
```

---

### Feedback Submission
```http
POST /submit-feedback/
Content-Type: application/json

{
  "pattern_id": "uuid-string",
  "rating": 5,
  "comment": "Beautiful pattern!"
}
```

---

## 💰 Pricing Tiers

| Tier | Price | Features |
|---|---|---|
| **Starter** | Free | 10 generations/month, basic customization, email support |
| **Pro** | $15/mo | Unlimited designs, advanced tools, priority support, high-res exports |
| **Enterprise** | $29/mo | Team access (5 members), custom libraries, 1-on-1 support, commercial rights |

---

## 🎯 Use Cases

- **Boutique Owners & Tailors**: Rapidly design custom shalwar qameez for individual clients
- **Fashion Brands**: Generate unique collections inspired by traditional and contemporary aesthetics
- **Wedding & Occasion Designers**: Create premium embroidered and specialty fabrics digitally before production
- **E-commerce & Online Retailers**: Generate custom product visuals and previews for Pakistani ethnic wear
- **Fashion Students**: Learn textile design, pattern creation, and AI-assisted fashion technology
- **Textile Manufacturers**: Explore innovative pattern possibilities for traditional garment production
- **Cultural Fashion Enthusiasts**: Celebrate and modernize South Asian fashion through digital design

---

## 🔮 Future Enhancements

- [ ] Advanced 3D body model integration for realistic virtual try-on
- [ ] ML model refinement with cultural pattern recognition
- [ ] Multi-language support (Urdu, English, regional languages)
- [ ] Design marketplace for buying and selling custom patterns
- [ ] Embroidery & embellishment simulation (zari, sequins, mirrors)
- [ ] Batch processing for boutique collection generation
- [ ] Adobe Illustrator & CAD software integration
- [ ] Social sharing and design collaboration features
- [ ] Export to technical specification formats for manufacturers
- [ ] Augmented Reality (AR) virtual try-on for mobile devices
- [ ] Seasonal trend analysis and AI recommendations
- [ ] Integration with tailoring software for precise measurements

---

## 🚀 Implementation Guide: Three.js & WebGL Setup

### **Setting Up Three.js 3D Preview**

This project uses Three.js for real-time 3D visualization of shalwar qameez designs:

```javascript
// Initialize Three.js Scene
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });

// Configure renderer
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFShadowShadowMap; // Better shadow quality
renderer.outputColorSpace = THREE.SRGBColorSpace; // Correct color handling
document.body.appendChild(renderer.domElement);

// Setup lighting (3-point lighting system)
const keyLight = new THREE.DirectionalLight(0xffffff, 0.8);
keyLight.position.set(5, 5, 5);
keyLight.castShadow = true;
keyLight.shadow.mapSize.width = 2048;

const fillLight = new THREE.DirectionalLight(0xffffff, 0.4);
fillLight.position.set(-5, 3, -5);

const rimLight = new THREE.DirectionalLight(0xffffff, 0.3);
rimLight.position.set(0, -5, 5);

scene.add(keyLight, fillLight, rimLight);
```

### **Loading 3D Models (GLB/GLTF Format)**

```javascript
// Use GLTFLoader to load shalwar qameez models
import { GLTFLoader } from 'https://cdn.jsdelivr.net/npm/three@r128/examples/jsm/loaders/GLTFLoader.js';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@r128/examples/jsm/controls/OrbitControls.js';

const loader = new GLTFLoader();
loader.load('/models/shalwar-qameez-style-1.glb', (gltf) => {
    const model = gltf.scene;
    scene.add(model);
    
    // Access mesh groups for material assignment
    model.traverse((child) => {
        if (child.isMesh) {
            child.receiveShadow = true;
            child.castShadow = true;
        }
    });
});

// Add Orbit Controls for interactivity
const controls = new OrbitControls(camera, renderer.domElement);
controls.autoRotate = true;
controls.autoRotateSpeed = 5;
```

### **Applying Generated Texture to 3D Model**

```javascript
// Load generated textile image from SDXL
const textureLoader = new THREE.TextureLoader();
textureLoader.load('/path/to/generated-textile.png', (texture) => {
    // Optimize texture for performance
    texture.colorSpace = THREE.SRGBColorSpace;
    texture.anisotropy = renderer.capabilities.maxAnisotropy;
    
    // Create PBR material
    const qameezMaterial = new THREE.MeshStandardMaterial({
        map: texture,
        metalness: 0.1,      // Slightly shiny
        roughness: 0.8,      // Fabric-like roughness
        normalScale: new THREE.Vector2(0.5, 0.5)
    });
    
    // Apply to qameez mesh
    scene.getObjectByName('qameez').material = qameezMaterial;
});
```

### **Custom WebGL Shaders for Material Effects**

```glsl
// vertex_shader.glsl - Custom vertex shader
varying vec2 vUv;
varying vec3 vNormal;
varying vec3 vPosition;

void main() {
    vUv = uv;
    vNormal = normalize(normalMatrix * normal);
    vPosition = (modelMatrix * vec4(position, 1.0)).xyz;
    
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
}

// fragment_shader.glsl - Custom fragment shader
uniform sampler2D textureMap;
uniform float materialType; // 0=cotton, 1=silk, etc.
varying vec2 vUv;
varying vec3 vNormal;

void main() {
    vec4 texColor = texture2D(textureMap, vUv);
    vec3 normal = normalize(vNormal);
    
    // Apply fabric-specific shading
    if (materialType == 1.0) { // Silk
        texColor.rgb *= 1.15; // Brighter
        texColor.rgb = mix(texColor.rgb, vec3(1.0), 0.2); // Lustrous
    }
    
    gl_FragColor = texColor;
}
```

### **Performance Optimization Tips**

```javascript
// 1. Use LOD (Level of Detail)
const lod = new THREE.LOD();
const model1 = loader.load('model-high.glb'); // High detail
const model2 = loader.load('model-medium.glb'); // Medium detail
lod.addLevel(model1, 0);
lod.addLevel(model2, 100);
scene.add(lod);

// 2. Compress textures
// Use WebP or AVIF format for smaller file sizes
// Consider texture atlasing for multiple materials

// 3. Monitor FPS
const fps = new function() {
    this.startTime = Date.now();
    this.prevTime = this.startTime;
    this.ms = 0;
    this.msMax = 0;
    this.fps = 0;
};

// 4. Use requestAnimationFrame for smooth animation
function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
    controls.update();
}
animate();
```

---

## 🐛 Troubleshooting

### Server Won't Start
```bash
# Ensure port 8000 is available
# Try a different port:
python -c "import uvicorn; uvicorn.run('server:app', host='127.0.0.1', port=8001, reload=False)"
```

### Static Files Not Loading
- Ensure `static/` directory exists with all image assets
- Check file paths match the references in HTML files

### Login Not Working
- Verify `config.js` has correct `API_BASE_URL`
- Check browser console for CORS errors
- Ensure backend server is running

### Pattern Generation Fails
- Check that Pillow library is installed: `pip install Pillow`
- Verify available disk space for image processing

---

## 📝 License

This project is provided as-is for educational and commercial use. Modify and extend freely!

---

## 🤝 Contributing

We welcome contributions! To improve this project:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📞 Support

For issues, questions, or feature requests:
- **GitHub Issues**: [Create an issue on repository]
- **Email**: support@shalwarqameezai.com
- **Documentation**: Check the [Project Wiki]
- **Community**: Join our fashion tech community forum

---

## 🎓 Learning Resources

### **Core Technologies**
- [FastAPI Documentation](https://fastapi.tiangolo.com/) - Python async web framework
- [Uvicorn ASGI Server](https://www.uvicorn.org/) - High-performance server
- [PIL/Pillow Image Processing](https://pillow.readthedocs.io/) - Image manipulation
- [Bootstrap 5 Framework](https://getbootstrap.com/docs/5.3/) - Responsive UI

### **3D Graphics & Visualization**
- [Three.js Official Docs](https://threejs.org/docs/) - 3D JavaScript library
- [Three.js Examples](https://threejs.org/examples/) - Interactive demonstrations
- [WebGL Fundamentals](https://webglfundamentals.org/) - GPU graphics basics
- [GLSL Shader Language](https://www.khronos.org/opengl/wiki/OpenGL_Shading_Language) - Vertex/fragment shaders
- [Learnable Three.js Course](https://www.udemy.com/course/threejs/) - Video tutorials

### **AI/ML & Generative Models**
- [Hugging Face Hub](https://huggingface.co/) - Model repository & inference
- [Stable Diffusion XL Docs](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) - SDXL model
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/) - Python library
- [Generative AI Guide](https://www.deeplearning.ai/) - ML fundamentals

### **Cultural & Fashion Context**
- [History of Shalwar Qameez](https://en.wikipedia.org/wiki/Shalwar_kameez) - Garment heritage
- [South Asian Textiles](https://www.britannica.com/topic/South-Asian-textiles) - Fabric traditions
- [Generative Design for Fashion](https://www.fashiontech.org/) - AI-fashion intersection

### **Deployment & Performance**
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/) - Production setup
- [WebGL Performance Tips](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Tips_for_production) - Optimization
- [Three.js Performance](https://threejs.org/manual/#en/optimize) - Graphics optimization
- [Browser APIs](https://developer.mozilla.org/en-US/docs/Web/API) - JavaScript capabilities

---

## 🌟 Acknowledgments

- Built with ❤️ for shalwar qameez enthusiasts, designers, and makers worldwide
- Inspired by the rich heritage of South Asian textile traditions and modern generative art
- Celebrating the timeless elegance of Pakistani fashion through technology
- Special thanks to the open-source community and the global fashion tech community

---

## 🎨 Design Philosophy

> *Honoring tradition through innovation. Where AI meets the artistry of shalwar qameez.*

Our platform is designed with three core principles:

1. **Culturally Respectful**: Celebrate authentic South Asian fashion while embracing modernity
2. **Accessible**: Empower anyone—from experienced designers to fashion enthusiasts—to create beautiful traditional wear
3. **Efficient**: Generate sophisticated designs in moments, honoring the craftsmanship that follows

---

<div align="center">

**Crafted with 🧵 tradition and 🤖 innovation**

*Celebrating South Asian Fashion in the Digital Age*

[⬆ Back to Top](#-shalwar-qameez-ai-generation-with-3d-preview)

</div>

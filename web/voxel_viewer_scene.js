import { OrbitControls } from './OrbitControls.js';
import * as THREE from './three.module.js';
import { RoomEnvironment } from './RoomEnvironment.js';

class VoxelViewerScene {
    constructor(container) {
        // Instantiate the renderer
        this.renderer = new THREE.WebGLRenderer({ antialias: true });
        const pmremGenerator = new THREE.PMREMGenerator(this.renderer);
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        container.appendChild(this.renderer.domElement); // Append the renderer to the provided container

        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(0x000000);
        
        // Set up environment (assuming pmremGenerator and RoomEnvironment are defined elsewhere)
        this.scene.environment = pmremGenerator.fromScene(new RoomEnvironment(this.renderer), 0.04).texture;

        // Add grid helper
        this.gridHelper = new THREE.GridHelper(64, 64); // Size and divisions
        this.scene.add(this.gridHelper);

        // Add ambient light
        this.ambientLight = new THREE.AmbientLight(0xffffff);
        this.scene.add(this.ambientLight);

        // Set up camera
        this.camera = new THREE.PerspectiveCamera(40, window.innerWidth / window.innerHeight, 1, 500); // Increased far plane further to zoom out
        this.camera.position.set(70, 10, 0); // Rotated the camera 90 degrees around the model
        this.camera.lookAt(0, 0, 0); // Make the camera look at the origin
        
        // Add point light
        this.pointLight = new THREE.PointLight(0xffffff, 15);
        this.camera.add(this.pointLight);
        this.scene.add(this.camera); // Add camera to the scene

        // Set up controls
        this.controls = new OrbitControls(this.camera, this.renderer.domElement);
        this.controls.target.set(0, 0, 0);
        this.controls.update();
        this.controls.enablePan = true;
        this.controls.enableDamping = true;

        // Start the animation loop
        this.animate();
    }

    animate() {
        requestAnimationFrame(() => this.animate());
        this.controls.update(); // Update controls
        this.renderer.render(this.scene, this.camera); // Render the scene
    }

    getScene() {
        return this.scene;
    }

    getCamera() {
        return this.camera;
    }

    getControls() {
        return this.controls;
    }

    getRenderer() {
        return this.renderer;
    }
}

export default VoxelViewerScene;

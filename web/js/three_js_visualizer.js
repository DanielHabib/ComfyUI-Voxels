console.log(import.meta.url)
// Debugger breakpoint
import * as THREE from './three.module.js';

console.log("Imported classes from THREE:", Object.keys(THREE));


// import { api } from '../../../scripts/api.js'

// import { OrbitControls } from './OrbitControls.js';
// console.log("Methods associated with OrbitControls:");
// console.log(Object.getOwnPropertyNames(OrbitControls.prototype).filter(prop => typeof OrbitControls.prototype[prop] === 'function'));

// import { RoomEnvironment } from './RoomEnvironment.js';

// document.addEventListener("DOMContentLoaded", function () {

//     const visualizer = document.getElementById("visualizer");
//     const container = document.getElementById("container");
//     // // const progressDialog = document.getElementById("progress-dialog");
//     // // const progressIndicator = document.getElementById("progress-indicator");

//     const renderer = new THREE.WebGLRenderer({ antialias: true });
//     renderer.setPixelRatio(window.devicePixelRatio);
//     renderer.setSize(window.innerWidth, window.innerHeight);
//     container.appendChild(renderer.domElement);

//     const pmremGenerator = new THREE.PMREMGenerator(renderer);

//     // // scene
//     const scene = new THREE.Scene();
//     scene.background = new THREE.Color(0x000000);
//     scene.environment = pmremGenerator.fromScene(new RoomEnvironment(renderer), 0.04).texture;

//     const gridHelper = new THREE.GridHelper(10, 10); // Size and divisions
//     scene.add(gridHelper);

//     const ambientLight = new THREE.AmbientLight(0xffffff);

//     const camera = new THREE.PerspectiveCamera(40, window.innerWidth / window.innerHeight, 1, 100);
//     camera.position.set(5, 2, 8);
//     const pointLight = new THREE.PointLight(0xffffff, 15);
//     camera.add(pointLight);

//     const controls = new OrbitControls(camera, renderer.domElement);
//     controls.target.set(0, 0.5, 0);
//     controls.update();
//     controls.enablePan = true;
//     controls.enableDamping = true;

//     // // Handle window reseize event
//     window.onresize = function () {

//         camera.aspect = window.innerWidth / window.innerHeight;
//         camera.updateProjectionMatrix();

//         renderer.setSize(window.innerWidth, window.innerHeight);

//     };


//     var lastFilepath = "";
//     var needUpdate = false;

//     function frameUpdate() {
//         // console.log("Rendering frame..."); // Log when rendering occurs

//         var filepath = visualizer.getAttribute("filepath");
//         if (filepath == lastFilepath) {
//             if (needUpdate) {
//                 controls.update();
//                 renderer.render(scene, camera);
//             }
//             // requestAnimationFrame( frameUpdate );
//         } else {
//             needUpdate = false;
//             scene.clear();
//             // progressDialog.open = true;
//             lastFilepath = filepath;
//             main(JSON.parse(lastFilepath));
//         }
//     }

//     const onProgress = function (xhr) {
//         if (xhr.lengthComputable) {
//             // progressIndicator.value = xhr.loaded / xhr.total * 100;
//         }
//     };
//     const onError = function (e) {
//         console.error(e);
//     };

//     async function main(params) {
//         console.log({ "voxel_block": visualizer.getAttribute("voxel_block") })
//         console.log("INSIDE THREE_JS_VISUALIZER")
      
//         scene.add(ambientLight);
//         scene.add(camera);
//         // Add a cube to the scene
//         const geometry = new THREE.BoxGeometry();
//         const material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
//         const cube = new THREE.Mesh(geometry, material);
//         scene.add(cube);

//         // progressDialog.close();
//         renderer.render(scene, camera);
//         // frameUpdate();
//     }

//    main();
// });
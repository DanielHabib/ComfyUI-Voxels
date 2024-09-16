import * as THREE from './three.module.js';

class VoxelBlockRenderer {
    constructor(voxelBlock) {
        this.voxelBlock = voxelBlock;
        this.meshGroup = this.createMeshGroup();
    }

    createMeshGroup() {
        const group = new THREE.Group();

        const xSize = Math.cbrt(this.voxelBlock.length); // X axis
        console.log({xSize})
        const ySize = xSize
        const zSize = xSize
        const boxScale = 1 
        for (let i = 0; i < this.voxelBlock.length; i++) {
            const voxel = this.voxelBlock[i]; // Accessing the flattened list
            if (voxel) { // Check if voxel is not null
                const r = parseInt(voxel.slice(1, 3), 16);
                const g = parseInt(voxel.slice(3, 5), 16);
                const b = parseInt(voxel.slice(5, 7), 16);
                const a = parseInt(voxel.slice(7, 9), 16);

                if (a > 0) { // Check if alpha channel is greater than 0
                    const geometry = new THREE.BoxGeometry(boxScale, boxScale, boxScale);
                    const material = new THREE.MeshBasicMaterial({ color: new THREE.Color(r / 255, g / 255, b / 255) });
                    const cube = new THREE.Mesh(geometry, material);

                    const z = Math.floor(i / (xSize * ySize));
                    const y = Math.floor((i % (xSize * ySize)) / xSize);
                    const x = i % xSize;

                    cube.position.set(y, z, x); // Map the coordinates directly
                    group.add(cube);
                }
            }
        }
        return group;
    }

    getMeshGroup() {
        return this.meshGroup;
    }
}

export default VoxelBlockRenderer;

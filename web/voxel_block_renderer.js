import * as THREE from './three.module.js';

class VoxelBlockRenderer {
    constructor(voxelBlock) {
        this.voxelBlock = voxelBlock;
        this.meshGroup = this.createMeshGroup();
    }

    createMeshGroup() {
        const group = new THREE.Group();

        const xSize = this.voxelBlock.length;         // X axis
        const ySize = this.voxelBlock[0].length;      // Y axis (height)
        const zSize = this.voxelBlock[0][0].length;   // Z axis (depth)

        for (let x = 0; x < xSize; x++) {
            for (let y = 0; y < ySize; y++) {
                for (let z = 0; z < zSize; z++) {
                    const voxel = this.voxelBlock[x][y][z]; // Mapping axes directly to (x, y, z)
                    if (voxel[3] > 0) { // Assuming voxel is an array [r, g, b, alpha]
                        const geometry = new THREE.BoxGeometry(1, 1, 1);
                        const material = new THREE.MeshBasicMaterial({ color: new THREE.Color(voxel[0] / 255, voxel[1] / 255, voxel[2] / 255) });
                        const cube = new THREE.Mesh(geometry, material);
                        cube.position.set(x, z, y); // Map the coordinates directly
                        group.add(cube);
                    }
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

import * as THREE from './three.module.js';
import VoxelBlockRenderer from './voxel_block_renderer.js';

class VoxelVideoPlayer {
    constructor(viewer, voxelVideoData) {
        console.log("VoxelVideoPlayer constructor")
        console.log({viewer, voxelVideoData})
        this.scene = viewer.scene;
        this.renderer = viewer.renderer;
        this.camera = viewer.camera;
        this.voxelVideoData = voxelVideoData;
        this.currentFrame = 0;
        this.frameRate = voxelVideoData.Framerate || 1;
        this.totalFrames = voxelVideoData.Block_count || 0;

        this.loadVoxelBlocks();
        this.startPlayback();
    }

    loadVoxelBlocks() {
        this.voxelBlocks = this.voxelVideoData.Blocks.map(blockData => {
            const voxelRenderer = new VoxelBlockRenderer(blockData);
            return voxelRenderer.getMeshGroup();
        });
    }

    startPlayback() {
        this.playbackInterval = setInterval(() => {
            this.updateFrame();
        }, 1000 / this.frameRate);
    }

    updateFrame() {
        if (this.currentFrame >= this.totalFrames) {
            this.currentFrame = 0;
        }
        this.scene.clear();
        this.scene.add(this.voxelBlocks[this.currentFrame]);
        this.currentFrame++;
        this.render();
    }

    render() {
        this.renderer.render(this.scene, this.camera);
    }

    stopPlayback() {
        clearInterval(this.playbackInterval);
    }
}

export default VoxelVideoPlayer;
import numpy as np
import random
import glob
import json


class VoxelBlocksIntoVoxelVideo:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "voxel_blocks": ("VOXEL_BLOCK",),
                "framerate": ("INT", {"default": 1, "min": 1, "max": 100, "step": 1}),
            },
        }
    @classmethod
    def IS_CHANGED(voxel_blocks: np.ndarray):
        return random.randint(0, 1000)
    
    INPUT_IS_LIST = True
    RETURN_TYPES = ("VOXEL_VIDEO",)
    RETURN_NAMES = ("voxel_video",)

    FUNCTION = "run"
    OUTPUT_NODE = True
    CATEGORY = "Voxels"

    def run(self, voxel_blocks, framerate): 
        print("Inside VoxelViewer: " + str(len(voxel_blocks)))
        dimensions = voxel_blocks[0].shape
        voxel_blocks_as_list = [voxel_block.tolist() for voxel_block in voxel_blocks]
        voxel_video_json = {
            "version": 0,
            "dimensions": {
                "x": dimensions[0],
                "y": dimensions[1],
                "z": dimensions[2]
            },
            "framerate": framerate,
            "block_count": len(voxel_blocks),
            "title": "Voxel Block",
            "description": "A single frame voxel block.",
            "blocks": voxel_blocks_as_list
        }
        # Write this to a file
                # Find the last voxel_block file
        existing_files = glob.glob("output/voxel_video_*.json")
        last_index = 0

        for file in existing_files:
            index = int(file.split('_')[-1].split('.')[0])
            last_index = max(last_index, index)

        file_name = "voxel_video_%s" % (last_index + 1)
        with open(f"output/{file_name}.json", "w") as outfile:
            json.dump(voxel_video_json, outfile, indent=4)
        return (voxel_video_json,)
    

import numpy as np
import json
import glob
import os
import random

class VoxelBlockLoader:
    def __init__(self):
        pass

    def INPUT_TYPES():
        return {"required": { 
            "voxel_block_directory": ("STRING",),
        }}
        
    @classmethod
    def IS_CHANGED(voxel_block: np.ndarray):
        return random.randint(0, 1000)
    
    RETURN_TYPES = ("VOXEL_BLOCK",)
    OUTPUT_IS_LIST = (True, )
    RETURN_NAMES = ("voxel_blocks",)
    FUNCTION = "run"
    CATEGORY = "Voxels"

    def run(self, voxel_block_directory):
        # Get all JSON files from the specified directory
        voxel_block_files = glob.glob(os.path.join(voxel_block_directory, "*.json"))
        print("Number of blocks to process: " + str(len(voxel_block_files)))
        print(voxel_block_files)
        voxel_blocks = []
        for file in voxel_block_files:
            with open(file, 'r') as f:
                data = json.load(f)
                dimensions = data["Dimensions"]
                x, y, z = dimensions["x"], dimensions["y"], dimensions["z"]
                blocks = data["Blocks"][0]  # Assuming single frame
                voxel_block = np.zeros((x, y, z, 4), dtype=np.uint8)  # Initialize with zeros

                for i, color in enumerate(blocks):
                    if color is not None:
                        r = int(color[1:3], 16)
                        g = int(color[3:5], 16)
                        b = int(color[5:7], 16)
                        a = int(color[7:9], 16)
                        z_layer = i // (x * y)
                        y_row = (i % (x * y)) // x
                        x_voxel = i % x
                        voxel_block[x_voxel, y_row, z_layer] = [r, g, b, a]

                voxel_blocks.append(
                    np.array(voxel_block)   
                    )
        print("Number of voxel blocks: " + str(len(voxel_blocks)))
        return (voxel_blocks,)

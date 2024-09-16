import numpy as np
import random



# # Packages: trimesh
class VoxelVideoViewer:
    def __init__(self):
        self.type="output"
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "voxel_blocks": ("VOXEL_BLOCK",),
            },
        }
    @classmethod
    def IS_CHANGED(voxel_blocks: np.ndarray):
        return random.randint(0, 1000)
    
    INPUT_IS_LIST = True
    RETURN_TYPES = ()
    # RETURN_NAMES = ()

    FUNCTION = "run"
    OUTPUT_NODE = True
    CATEGORY = "Voxels"

    #  voxel_block is a numpy array
    def run(self, voxel_blocks): 
        print("Inside VoxelViewer: " + str(len(voxel_blocks)))
        # print(voxel_block)
        voxel_blocks_as_list = [voxel_block.tolist() for voxel_block in voxel_blocks]
        return {"ui": {"voxel_blocks": voxel_blocks_as_list}}
    

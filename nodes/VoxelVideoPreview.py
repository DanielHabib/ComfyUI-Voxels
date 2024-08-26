import numpy as np
import random
import json
import glob

# # Packages: trimesh
class VoxelVideoPreview:
    def __init__(self):
        self.type="output"
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "voxel_video": ("VOXEL_VIDEO",),
            },
        }
    @classmethod
    def IS_CHANGED(voxel_video: str):
        return random.randint(0, 1000)
    
    
    RETURN_TYPES = ()
    # RETURN_NAMES = ()

    FUNCTION = "run"
    OUTPUT_NODE = True
    CATEGORY = "Voxels"

    #  voxel_block is a numpy array
    def run(self, voxel_video): 
        print("Inside VoxelViewer: " + str(len(voxel_video)))
        # print(voxel_video)
        # Write this to a file
        last_index = 0
        existing_files = glob.glob("output/voxel_video_*.json")

        for file in existing_files:
            index = int(file.split('_')[-1].split('.')[0])
            last_index = max(last_index, index)
        file_name = "voxel_video_%s" % (last_index + 1)
        file_with_path = f"output/{file_name}.json"
        with open(file_with_path, "w") as outfile:
            json.dump(voxel_video, outfile, indent=4)

        return {"ui": {"voxel_video": (voxel_video,)}}
    

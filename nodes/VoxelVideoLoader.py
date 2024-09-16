import numpy as np
import json
import glob
import os
import random


class VoxelVideoLoader:
    def __init__(self):
        pass

    def INPUT_TYPES():
        return {
            "required": {
                "voxel_video_file": ("STRING",),
            }
        }

    @classmethod
    def IS_CHANGED(voxel_video_file: str):
        return random.randint(0, 1000)

    RETURN_TYPES = ("VOXEL_VIDEO",)
    RETURN_NAMES = ("voxel_video",)

    FUNCTION = "run"
    CATEGORY = "Voxels"

    def run(self, voxel_video_file):
        # Get all JSON files from the specified directory
        # Load the JSON file
        with open(voxel_video_file, 'r') as f:
            voxel_video = json.load(f)
        return (voxel_video,)

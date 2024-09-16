import numpy as np
from trimesh import Trimesh
import json
import random
import glob
import os
import pyvista as pv

class VoxelizeMesh:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "mesh": ("MESH",),
                "voxel_size": ("INT", {"default": 20, "min": 1, "max": 100, "step": 1}),
            },
        }
    @classmethod
    def IS_CHANGED(mesh: Trimesh):
       return random.randint(0, 1000)

    RETURN_TYPES = ("VOXEL_BLOCK",)
    RETURN_NAMES = ("Voxel Block",)

    FUNCTION = "run"

    CATEGORY = "Voxels"

    def run(self, mesh, voxel_size): 
        # Define the voxel grid size
        if isinstance(mesh, list) and len(mesh) > 0 and isinstance(mesh[0], Trimesh):
            mesh = mesh[0]
        else:
            raise ValueError("Input mesh is not a valid Trimesh object.")
        
        voxel_grid = np.zeros((voxel_size, voxel_size, voxel_size, 4), dtype=np.float32)  # Last dimension for RGBA
        surface = pv.wrap(mesh)
        print("Surface")
        print(surface)
        voxels = pv.voxelize(surface, density=surface.length / 200)
        print("Voxels")
        print(voxels)
        print(voxels.points)
        # Update the voxel grid with the voxels
        for point in voxels.points:
            x, y, z = point[:3]
            if 0 <= x < voxel_size and 0 <= y < voxel_size and 0 <= z < voxel_size:
                voxel_grid[int(x), int(y), int(z)] = [x, y, z, 1.0]  # Assuming 1.0 for the alpha channel

        return (voxel_grid,)


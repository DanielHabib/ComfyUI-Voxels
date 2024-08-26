import numpy as np
from trimesh import Trimesh
import json
import random
import glob
import os

class MeshToVoxel:
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
        
        # Get the bounding box of the mesh
        bbox_min, bbox_max = mesh.bounds
        
        # Calculate the scale to fit the mesh inside the 64x64x64 voxel grid
        scale = (voxel_size - 1) / (bbox_max - bbox_min).max()
        
        # Scale and shift vertices to the voxel grid
        scaled_vertices = (mesh.vertices - bbox_min) * scale
        
        # Assign vertices to voxel grid coordinates
        voxel_coords = np.floor(scaled_vertices).astype(int)
        voxel_coords = np.clip(voxel_coords, 0, voxel_size - 1)  # Ensure the coordinates stay within bounds
        
        # Aggregate colors into the corresponding voxels
        for i, coord in enumerate(voxel_coords):
            color = mesh.visual.vertex_colors[i][:3]  # Extract RGB from RGBA
            voxel_grid[coord[0], coord[1], coord[2], :3] += color  # Sum colors
            voxel_grid[coord[0], coord[1], coord[2], 3] += 1  # Count number of contributions for averaging
        
        # Average the colors
        non_empty_voxels = voxel_grid[..., 3] > 0  # Find non-empty voxels
        voxel_grid[non_empty_voxels, :3] /= voxel_grid[non_empty_voxels, 3:4]  # Average RGB by count
        voxel_grid = voxel_grid.astype(np.uint8)  # Convert to uint8
        
        # Set alpha channel to 255 for non-empty voxels
        voxel_grid[non_empty_voxels, 3] = 255
        
        return (voxel_grid,)


# # Packages: trimesh
class VoxelViewer:
    def __init__(self):
        self.type="output"
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "voxel_block": ("VOXEL_BLOCK",),
            },
        }
    @classmethod
    def IS_CHANGED(voxel_block: np.ndarray):
        return random.randint(0, 1000)
    RETURN_TYPES = ()
    # RETURN_NAMES = ()

    FUNCTION = "run"
    OUTPUT_NODE = True
    CATEGORY = "Voxels"

    #  voxel_block is a numpy array
    def run(self, voxel_block: np.ndarray): 
        return {"ui": {"voxel_block": voxel_block.tolist()}}
    

class VoxelBlockSaver:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "voxel_block": ("VOXEL_BLOCK",),
            },
        }

    @classmethod
    def IS_CHANGED(voxel_block: np.ndarray):
        return random.randint(0, 1000)

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("filename",)
    OUTPUT_NODE = True
    FUNCTION = "run"

    CATEGORY = "Voxels"

    def run(self, voxel_block: np.ndarray):
        """
        Save a single frame 6dv file according to the specification.
        
        :param voxel_block: numpy array representing the voxel block.
        """
        print("Inside VoxelBlockSaver")
        dimensions = voxel_block.shape
        x, y, z, c = dimensions
        title = "Voxel Block"
        description = "A single frame voxel block."
        framerate = 1
        framecount = 1

        # Initialize the 6dv file structure
        sixdv_data = {
            "Version": 0,
            "Dimensions": {"x": x, "y": y, "z": z},
            "Framerate": framerate,
            "Framecount": framecount,
            "block_count": 1,
            "Title": title,
            "Description": description,
            "Blocks": []
        }

        # Find the last voxel_block file
        output_dir = "output/voxel_blocks"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        existing_files = glob.glob(os.path.join(output_dir, "voxel_block_*.json"))
        last_index = 0

        for file in existing_files:
            index = int(file.split('_')[-1].split('.')[0])
            
            last_index = max(last_index, index)

        file_name = "voxel_block_%s" % (last_index + 1)
        
        # Convert the voxel block to the format [hex | null]
        block_data = []
        for z_layer in range(z):  # Iterate over z-axis layers
            for y_row in range(y):  # Iterate over y-axis rows
                for x_voxel in range(x):  # Iterate over x-axis voxels
                    rgba = voxel_block[x_voxel, y_row, z_layer]  # Get the RGBA values
                    r, g, b, a = rgba  # Extract RGBA components

                    if a == 0:  # Empty/transparent space if alpha is 0
                        block_data.append(None)
                    else:
                        hex_color = f"#{int(r):02x}{int(g):02x}{int(b):02x}{int(a):02x}"  # Convert to hex with RGBA
                        block_data.append(hex_color)

        # Add the processed block data to the Blocks array
        sixdv_data["Blocks"].append(block_data)

        # Save the data to a .json file
        with open(f"output/voxel_blocks/{file_name}.json", "w") as outfile:
            json.dump(sixdv_data, outfile, indent=4)

        print(f"6dv file saved as {file_name}.json")

        return (file_name, )


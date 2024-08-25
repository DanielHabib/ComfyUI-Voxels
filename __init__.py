from .nodes.MeshToVoxel import *


NODE_CLASS_MAPPINGS = {
    "MeshToVoxel": MeshToVoxel,
    "VoxelBlockSaver": VoxelBlockSaver,
    "VoxelViewer": VoxelViewer,
    
    
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MeshToVoxel": "Mesh To Voxel",
    "VoxelBlockSaver": "Voxel Block Saver",
    "VoxelViewer": "Voxel Viewer",
}
WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]



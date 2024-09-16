from .nodes.MeshToVoxel import *
from .nodes.VoxelBlockLoader import *
from .nodes.VoxelVideoViewer import *
from .nodes.VoxelBlocksIntoVoxelVideo import *
from .nodes.VoxelVideoPreview import *
from .nodes.BatchToList import *
from .nodes.VoxelVideoAPINodes import *
from .nodes.VoxelVideoLoader import *
from .nodes.VoxelizeMesh import *

NODE_CLASS_MAPPINGS = {
    "MeshToVoxel": MeshToVoxel,
    "VoxelBlockSaver": VoxelBlockSaver,
    "VoxelViewer": VoxelViewer,
    "VoxelBlockLoader": VoxelBlockLoader,
    "VoxelVideoViewer": VoxelVideoViewer,
    "VoxelBlocksIntoVoxelVideo": VoxelBlocksIntoVoxelVideo,
    "VoxelVideoPreview": VoxelVideoPreview,
    "ImageBatchToImageList": ImageBatchToImageList,
    "MaskBatchToMaskList": MaskBatchToMaskList,
    "VoxelVideoAPIInputNode": VoxelVideoAPIInputNode,
    "VoxelVideoLoader": VoxelVideoLoader,
    "VoxelizeMesh": VoxelizeMesh,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MeshToVoxel": "Mesh To Voxel",
    "VoxelBlockSaver": "Voxel Block Saver",
    "VoxelViewer": "Voxel Viewer",
    "VoxelBlockLoader": "Voxel Block Loader",
    "VoxelVideoViewer": "Voxel Video Viewer",
    "VoxelBlocksIntoVoxelVideo": "Voxel Blocks Into Voxel Video",
    "VoxelVideoPreview": "Voxel Video Preview",
    "ImageBatchToImageList": "Image Batch To Image List",
    "MaskBatchToMaskList": "Mask Batch To Mask List",
    "VoxelVideoAPIInputNode": "Voxel Video API Input Node",
    "VoxelVideoLoader": "Voxel Video Loader",
    "VoxelizeMesh": "Voxelize Mesh",
}
WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

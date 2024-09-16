class ImageBatchToImageList:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"image": ("IMAGE",), }}

    RETURN_TYPES = ("IMAGE",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "doit"

    CATEGORY = "Voxel/Util"

    def doit(self, image):
        images = [image[i:i + 1, ...] for i in range(image.shape[0])]
        return (images, )
    
class MaskBatchToMaskList:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"mask": ("MASK",), }}

    RETURN_TYPES = ("MASK",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "doit"

    CATEGORY = "Voxel/Util"

    def doit(self, mask):
        masks = [mask[i:i + 1, ...] for i in range(mask.shape[0])]
        return (masks, )
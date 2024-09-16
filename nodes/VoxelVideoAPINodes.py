import numpy as np

import json
import random
import requests
import torch
from PIL import Image, ImageOps

import comfy


class VoxelVideoAPIInputNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("STRING",),
                "positive_coordinates": ("STRING",),
            },
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("images", "positive_coordinates")

    FUNCTION = "run"

    CATEGORY = "Voxels"

    def run(self, images, positive_coordinates):
        # Positive coordinates is a json array of coordinates BEFORE they get resized to , its going to be kept proportional but the height will become 512
        # Define the voxel grid size
        # Load the images they are b64 and get them into torch.Tensor with shape [B,H,W,C], C=3
        image_height = None
        image_width = None
        processed_images = []
        try:
            images_list = json.loads(images)  # Assuming images is a JSON array string
            print("Length of images list: ", len(images_list))
            for img_input in images_list:
                if img_input.startswith("http"):
                    import requests
                    from io import BytesIO

                    print("Fetching image from url: ", img_input)
                    response = requests.get(img_input)
                    image = Image.open(BytesIO(response.content))
                elif (
                    img_input.startswith("data:image/png;base64,")
                    or img_input.startswith("data:image/jpeg;base64,")
                    or img_input.startswith("data:image/jpg;base64,")
                ):
                    import base64
                    from io import BytesIO

                    print("Decoding base64 image")
                    base64_image = img_input[img_input.find(",") + 1 :]
                    decoded_image = base64.b64decode(base64_image)
                    image = Image.open(BytesIO(decoded_image))
                else:
                    raise ValueError("Invalid image url or base64 data provided.")

                image = ImageOps.exif_transpose(image)
                image = image.convert("RGB")
                image = np.array(image).astype(np.float32) / 255.0
                image_tensor = torch.from_numpy(image)[None,]
                image_height = image_tensor.shape[1]
                image_width = image_tensor.shape[2]
                processed_images.append(image_tensor)
        except Exception as e:
            print(f"Error processing images: {e}")
            pass

        # if default_value is not None and len(images_list) == 0:
        #     processed_images.append(
        #         default_value
        # )  # Assuming default_value is a pre-processed image tensor

        # Resize images if necessary and concatenate from MakeImageBatch in ImpactPack
        if processed_images:
            base_shape = processed_images[0].shape[
                1:
            ]  # Get the shape of the first image for comparison
            batch_tensor = processed_images[0]
            for i in range(1, len(processed_images)):
                if processed_images[i].shape[1:] != base_shape:
                    # Resize to match the first image's dimensions
                    processed_images[i] = comfy.utils.common_upscale(
                        processed_images[i].movedim(-1, 1),
                        base_shape[1],
                        base_shape[0],
                        "lanczos",
                        "center",
                    ).movedim(1, -1)

                batch_tensor = torch.cat((batch_tensor, processed_images[i]), dim=0)
            # Concatenate using torch.cat
        else:
            batch_tensor = None  # or handle the empty case as needed

        adjusted_positive_coordinates = json.loads(positive_coordinates)
        new_width = 512
        
        if image_width is not None and image_width > 512:
            new_height = int(image_height * (new_width / image_width))

            for coord in adjusted_positive_coordinates:
                coord["x"] = coord["x"] * (new_width / image_width)
                coord["y"] = coord["y"] * (new_height / image_height)
        return (batch_tensor, json.dumps(adjusted_positive_coordinates))

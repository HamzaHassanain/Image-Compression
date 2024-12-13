# import cv2
# import the open cv library

from PIL import Image, ImageFilter
import random as r


def _random():

    string_random = ""

    for i in range(10):
        string_random += str(r.randint(0, 100))

    return string_random


# def reduce_noise(input_image_path, output_image_path):
#     """
#     Reduces noise in an image using Gaussian blur with PIL.

#     Parameters:
#         input_image_path (str): Path to the input image.
#         output_image_path (str): Path to save the output image.
#     """
#     try:
#         # Open the image
#         image = Image.open(input_image_path)

#         # Apply Gaussian blur to reduce noise
#         blurred_image = image.filter(ImageFilter.GaussianBlur(radius=2))

#         # Save the denoised image
#         blurred_image.save(output_image_path)

#         print(f"Denoised image saved to {output_image_path}")
#     except Exception as e:
#         print(f"Error: {e}")


def reduce_noise(image_abs_path, xxx=None):

    try:
        # Open the image
        image = Image.open(image_abs_path)

        # Apply Gaussian blur to reduce noise
        blurred_image = image.filter(
            ImageFilter.MedianFilter(size=5))
        # print("Image denoised")
        # Save the denoised image
        image_ext = image_abs_path.split('.')[-1]
        output_path = image_abs_path.replace(f".{image_ext}", "")

        output_image_path = f"{output_path}_denoised_{_random()}.{image_ext}"

        # Save the denoised image
        blurred_image.save(output_image_path)

        return {
            "Message": "Denoised image saved",
            "Path": output_image_path
        }
    except Exception as e:
        return {
            "Message": f"Error: {e}"
        }

import io
import os
import urllib

import structlog
from PIL import Image

import python_template.config as cf


def download_from_url(filename, url) -> str:
    """
    Downloads the image from the response
    """
    path = os.path.join(os.getcwd(), "images", filename)
    # Create images directory if it does not exist
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    return urllib.request.urlretrieve(url, path)


def load_image_from_url(url, file_extension: str) -> io.BytesIO:
    """
    Loads the image from the URL

    :param url: The URL of the image
    :param file_extension: The file extension of the image

    :return: The image as bytes
    """
    structlog.contextvars.bind_contextvars(function_name="load_image")
    with urllib.request.urlopen(url) as url:
        # Read the image data from the URL
        image_data = url.read()

    # Load the image data into memory using PIL
    image = Image.open(io.BytesIO(image_data))

    cf.logger.info(
        f"""
        Image loaded:
        - Image mode: {image.mode}
        - Image size: {image.size}
        - Image format: {image.format}
        """
    )

    # Convert the image to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format=file_extension)
    image_bytes.seek(0)

    return image_bytes

import os
import cv2
import numpy as np
from PIL import Image, ImageSequence

def interpolate(image1, image2, steps):
    """Generate interpolated frames between two images."""
    frames = []
    for i in range(steps):
        alpha = i / (steps -1) # this varies from 0 to 1
        interpolated_image = cv2.addWeighted(image1, 1-alpha, image2, alpha, 0)
        frames.append(Image.fromarray(cv2.cvtColor(interpolated_image.astype(np.uint8), cv2.COLOR_BGR2RGBA)))
    return frames

def create_gif(images, steps, gif_name):
    """Create a gif from a list of images."""
    # Load the images
    images_cv = [cv2.imread(image).astype(np.float) for image in images]

    # make sure all images are the same size
    assert all(image.shape == images_cv[0].shape for image in images_cv), "Images must be the same shape."

    # generate the gif
    frames = []
    for i in range(len(images_cv) - 1):
        frames += interpolate(images_cv[i], images_cv[i+1], steps)
    frames[0].save(gif_name, save_all=True, append_images=frames[1:], loop=0, duration=100)

# Specify the directory containing the images
image_dir = '../pngs/blockchains'  # Go up one level from the scripts folder, then into pngs/blockchains

# Get the list of image files in the directory
images = sorted([os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.png')])

# create a gif from the images
gif_name = '../gifs/blockchains.gif'  # Go up one level from the scripts folder, then into gifs
create_gif(images, 25, gif_name)

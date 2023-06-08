import os
from PIL import Image

def interpolate(image1, image2, steps):
    """Generate interpolated frames between two images."""
    frames = []
    for i in range(steps):
        alpha = i / (steps - 1)  # this varies from 0 to 1
        interpolated_image = Image.blend(image1, image2, alpha)
        frames.append(interpolated_image)
    return frames

def create_gif(images, steps, gif_name):
    """Create a gif from a list of images."""
    # Load the images
    images_pil = [Image.open(image).convert('RGBA') for image in images]

    # make sure all images are the same size
    assert all(image.size == images_pil[0].size for image in images_pil), "Images must be the same shape."

    # generate the gif
    frames = []
    for i in range(len(images_pil) - 1):
        frames += interpolate(images_pil[i], images_pil[i+1], steps)
    frames[0].save(gif_name, save_all=True, append_images=frames[1:], loop=0, duration=100, transparency=0, disposal=2)

# Specify the directory containing the images
image_dir = '../pngs/bull-bear-lerp'  # Go up one level from the scripts folder, then into pngs/blockchains

# Get the list of image files in the directory
images = sorted([os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.png')])

# create a gif from the images
gif_name = f'../gifs/{os.path.basename(image_dir)}.gif'  # Go up one level from the scripts folder, then into gifs
create_gif(images, 25, gif_name)
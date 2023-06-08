import numpy as np
from PIL import Image

def move_pixel(pixel, start_pos, end_pos, steps, img_size):
    # Calculate the step size for the pixel's movement
    step_size = np.subtract(end_pos, start_pos) / steps

    # Create each frame
    frames = []
    for i in range(steps):
        # Calculate the current position of the pixel
        pos = start_pos + step_size * i

        # Create a new image for this frame
        frame = Image.new('RGBA', img_size)

        # Place the pixel at its current position in this frame
        frame.putpixel(tuple(pos.astype(int)), tuple(pixel.astype(int)))

        # Add the frame to the list of frames
        frames.append(frame)

    return frames

# Open the images
try:
    image1 = Image.open("../pngs/bull-bear-lerp/bull-bear-lerp-1.png")
    image2 = Image.open("../pngs/bull-bear-lerp/bull-bear-lerp-2.png")
    print("Images loaded successfully.")
except FileNotFoundError:
    print("One or both of the images were not found.")
except Exception as e:
    print("An unexpected error occurred:", e)

# Convert images to numpy arrays
img1 = np.array(image1)
img2 = np.array(image2)

# Define the size of the imaginary boxes
box_size = (220, 220)

# Calculate the positions of the boxes
start_box = (0, 0)
end_box = (image1.width - box_size[0], 0)

# Calculate the number of steps for the animation
steps = 25

# Create the transition frames
frames = []
for y in range(box_size[1]):
    for x in range(box_size[0]):
        # Calculate the positions of this pixel in the start and end images
        start_pos = np.array([start_box[0] + x, start_box[1] + y])
        end_pos = np.array([end_box[0] + x, end_box[1] + y])

        # Ensure we're within the image's boundaries
        if max(end_pos) >= min(img2.shape[:2]) or max(start_pos) >= min(img1.shape[:2]):
            continue

        # Get the colors of this pixel in the start and end images
        start_pixel = img1[tuple(start_pos)]
        end_pixel = img2[tuple(end_pos)]

        # Check if the pixel is fully transparent in either image
        if start_pixel[3] == 0 or end_pixel[3] == 0:
            # Skip this pixel
            continue

        # Interpolate the pixel's color
        pixel = np.linspace(start_pixel, end_pixel, steps)

        # Animate this pixel's movement
        pixel_frames = move_pixel(pixel, start_pos, end_pos, steps, image1.size)

        # Add the frames to the list of frames
        frames.extend(pixel_frames)

# Save as a GIF
if frames:
    frames[0].save("../gifs/bull-bear-lerp3.gif", save_all=True, append_images=frames[1:], loop=0, duration=100)
else:
    print("No frames were generated.")
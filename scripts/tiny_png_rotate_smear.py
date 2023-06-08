import numpy as np
from PIL import Image

# Define the size of the imaginary boxes and the whole image
box_size = (25, 25)
img_size = (75, 25)

# Calculate the positions of the boxes
start_box = (0, 0)
end_box = (img_size[0] - box_size[0], 0)

# Define the number of steps for the animation
steps = 10

# Open the image
image = Image.open("../pngs/tiny-bull/tiny-bull.png")

# Convert image to numpy array
img = np.array(image)

# Create an array to hold the frames
frames = []

# Calculate the delta for movement
delta = np.array(end_box) - np.array(start_box)

# Initialize the starting positions of each pixel in the box
positions = np.mgrid[0:box_size[1], 0:box_size[0]].transpose(1, 2, 0) + np.array(start_box)

# For each row in the animation
for row in range(box_size[1]):
    # For each step in the animation
    for step in range(steps):
        # Calculate the new positions of the pixels in the moving box
        positions[row] += delta // steps

        # Create a new image for this frame
        frame = Image.new('RGBA', img_size, (0, 0, 0, 0))

        # Draw each pixel at its new position
        for y in range(box_size[1]):
            for x in range(box_size[0]):
                # Only move the pixels in the current row
                if y <= row:
                    frame.putpixel(tuple(positions[y, x]), tuple(img[start_box[1]+y, start_box[0]+x]))
                # Keep the pixels in the following rows in the start box
                else:
                    frame.putpixel((start_box[0]+x, start_box[1]+y), tuple(img[start_box[1]+y, start_box[0]+x]))

        # Append the frame to the list of frames
        frames.append(frame)

# Save the frames as a GIF
frames[0].save("../gifs/tiny-bull.gif", save_all=True, append_images=frames[1:], loop=0, duration=100)

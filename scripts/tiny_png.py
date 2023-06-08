import numpy as np
from PIL import Image

# Define the size of the imaginary boxes and the whole image
box_size = (25, 25)
img_size = (75, 25)

# Calculate the positions of the boxes
start_box = (0, 0)
end_box = (img_size[0] - box_size[0], 0)

# Define the number of steps for the animation
steps = 25

# Open the image
image = Image.open("../pngs/tiny-bull/tiny-bull.png")

# Convert image to numpy array
img = np.array(image)

# Create an array to hold the frames
frames = []

# Calculate the delta for movement
delta = np.array([end_box[0] - start_box[0], end_box[1] - start_box[1]])

# Initialize the starting positions of each pixel in the box
positions = np.mgrid[0:box_size[1], 0:box_size[0]].transpose(1, 2, 0) + np.array(start_box)

# For each row in the animation
for row in range(box_size[1]):
    # Skip if the row is fully transparent
    if np.all(img[start_box[1]+row, start_box[0]:start_box[0]+box_size[0], 3] == 0):
        continue

    # For each step in the animation
    for step in range(steps):
        # Create a new image for this frame
        frame = Image.new('RGBA', img_size, (0, 0, 0, 0))

        # Calculate the new positions of the pixels in the moving box
        positions[row, :, 0] += delta[0] // steps

        # Draw each pixel at its new position
        for y in range(box_size[1]):
            for x in range(box_size[0]):
                # Only move the pixels in the current row
                if y == row and 0 <= positions[y, x][1] < img_size[0]:
                    frame.putpixel(tuple(positions[y, x][::-1]), tuple(img[start_box[1]+y, start_box[0]+x]))
                # Keep the pixels in the following rows in the start box
                elif 0 <= y + start_box[1] < img_size[1] and 0 <= x + start_box[0] < img_size[0]:
                    frame.putpixel((start_box[0]+x, start_box[1]+y), tuple(img[start_box[1]+y, start_box[0]+x]))

        # Set the pixels in the old positions to transparent
        img[start_box[1]+row, start_box[0]:start_box[0]+box_size[0]] = (0, 0, 0, 0)

        # Append the frame to the list of frames
        frames.append(frame)

# Save the frames as a GIF
frames[0].save("../gifs/tiny-bull.gif", save_all=True, append_images=frames[1:], loop=0, duration=100)

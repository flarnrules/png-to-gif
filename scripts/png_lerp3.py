from PIL import Image
import numpy as np

def transition(image1, image2, steps):
    # Convert images to numpy arrays
    img1 = np.array(image1)
    img2 = np.array(image2)

    # Calculate the difference between the two images
    diff = img2 - img1

    # Create an array to hold the transition frames
    frames = []

    for i in range(steps):
        # Calculate the current frame
        frame = img1 + (diff * (i / (steps - 1)))
        
        # Convert the frame back to an Image object and append it to the frames list
        frames.append(Image.fromarray(frame.astype(np.uint8)))

    return frames

# Open the images
image1 = Image.open("../pngs/bull-bear-lerp/bull-bear-lerp-1.png")
image2 = Image.open("../pngs/bull-bear-lerp/bull-bear-lerp-2.png")

# Create the transition frames
frames = transition(image1, image2, 25)

# Save as a GIF
frames[0].save("../gifs/bull-bear-lerp2.gif", save_all=True, append_images=frames[1:], loop=0, duration=100)

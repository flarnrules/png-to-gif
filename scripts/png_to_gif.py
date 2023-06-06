from PIL import Image
import glob
import os

# Replace this with the folder containing your PNG images
image_folder = "place your image folder here"

# This creates the base name of the folder so the script can work with it
folder_name = os.path.basename(image_folder.strip('/'))

# Sorts the files based on their number, in ascending order (make sure all pngs are named as integers like 1, 2 or 001, 002)


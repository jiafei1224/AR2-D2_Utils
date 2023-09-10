import os
import shutil
from natsort import natsorted
import cv2

def split_images_by_substring(src_folder, dest_folder1, dest_folder2, substring1, substring2):
    """
    Split images from `src_folder` into `dest_folder1` and `dest_folder2` based on whether their filenames contain
    `substring1` or `substring2`.

    Args:
    - src_folder (str): Source folder containing the images.
    - dest_folder1 (str): First destination folder.
    - dest_folder2 (str): Second destination folder.
    - substring1 (str): The first substring to look for in filenames.
    - substring2 (str): The second substring to look for in filenames.
    """

    # Ensure the source folder exists
    if not os.path.exists(src_folder):
        print(f"Source folder {src_folder} does not exist.")
        return
    
    # Create destination folders if they do not exist
    if not os.path.exists(dest_folder1):
        os.makedirs(dest_folder1)
    if not os.path.exists(dest_folder2):
        os.makedirs(dest_folder2)
    
    # Loop through each file in the source folder
    for filename in os.listdir(src_folder):
        # Skip if it's not a file
        if not os.path.isfile(os.path.join(src_folder, filename)):
            continue

        # Check if either of the substrings are in the filename and move accordingly
        if substring1 in filename:
            shutil.move(os.path.join(src_folder, filename), os.path.join(dest_folder1, filename))
        elif substring2 in filename:
            shutil.move(os.path.join(src_folder, filename), os.path.join(dest_folder2, filename))
        else:
            print(f"Skipping file {filename} as it doesn't contain either substring.")


src_folder = "/home/duanj1/CameraCalibration/Process_depth/0"
dest_folder1 = "/home/duanj1/CameraCalibration/Process_depth/AR"
dest_folder2 = "/home/duanj1/CameraCalibration/Process_depth/depth"
substring1 = "ARCapture"
substring2 = "image"

split_images_by_substring(src_folder, dest_folder1, dest_folder2, substring1, substring2)

from PIL import Image
import os

# Set input and output directories
input_dir = '/home/duanj1/CameraCalibration/Process_depth/depth'
output_dir = '/home/duanj1/CameraCalibration/Process_depth/pre_depth'

# Loop through images in input directory
for filename in os.listdir(input_dir):
    # Open image using Pillow
    img = Image.open(os.path.join(input_dir, filename))
    
    # Rotate image by 90 degrees clockwise
    rotated_img = img.transpose(method=Image.ROTATE_90)
    
    # Save rotated image to output directory with the same filename
    rotated_img.save(os.path.join(output_dir, filename))

from PIL import Image
import os
import shutil
from natsort import natsorted

def rename_resize_and_copy_images(src_folder, dest_folder):
    """
    Sorts image filenames in the `src_folder` naturally, resizes them to 192x256,
    renames them from 0.png to N.png, and saves them into a new folder `dest_folder`.

    Args:
    - src_folder (str): Source folder containing the images.
    - dest_folder (str): Destination folder for resized, renamed, and sorted images.
    """

    # Ensure the source folder exists
    if not os.path.exists(src_folder):
        print(f"Source folder {src_folder} does not exist.")
        return

    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Fetch all filenames from the source folder and natsort them
    filenames = [filename for filename in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, filename))]
    sorted_filenames = natsorted(filenames)

    # Rename, resize, and copy the sorted files to the destination folder
    for i, filename in enumerate(sorted_filenames):
        src_path = os.path.join(src_folder, filename)
        dest_path = os.path.join(dest_folder, f"{i}.png")
        
        # Open and resize the image
        with Image.open(src_path) as img:
            img_resized = img.resize((192, 256), Image.ANTIALIAS)
            
            # Save the resized image to the destination folder
            img_resized.save(dest_path)

def rename_and_copy_images(src_folder, dest_folder):
    """
    Sorts image filenames in the `src_folder` naturally, renames them from 0.png to N.png,
    and saves them into a new folder `dest_folder`.

    Args:
    - src_folder (str): Source folder containing the images.
    - dest_folder (str): Destination folder for renamed and sorted images.
    """

    # Ensure the source folder exists
    if not os.path.exists(src_folder):
        print(f"Source folder {src_folder} does not exist.")
        return

    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Fetch all filenames from the source folder and natsort them
    filenames = [filename for filename in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, filename))]
    sorted_filenames = natsorted(filenames)

    # Rename and copy the sorted files to the destination folder
    for i, filename in enumerate(sorted_filenames):
        new_filename = f"{i}.png"
        src_path = os.path.join(src_folder, filename)
        dest_path = os.path.join(dest_folder, new_filename)
        shutil.copy(src_path, dest_path)
src_folder = "/home/duanj1/CameraCalibration/Process_depth/AR"
dest_folder = "/home/duanj1/CameraCalibration/Process_depth/front_rgb"

rename_resize_and_copy_images(src_folder, dest_folder)

src_folder_depth = "/home/duanj1/CameraCalibration/Process_depth/pre_depth"
dest_folder_depth = "/home/duanj1/CameraCalibration/Process_depth/front_depth"

rename_and_copy_images(src_folder_depth,dest_folder_depth)


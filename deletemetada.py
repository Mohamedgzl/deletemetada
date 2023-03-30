import os
# from pathlib import Path
from PIL import Image

# Specify the directory where the files are located
directory = 'path'

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a video or image
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.mp4'):
        # Open the file
        file_path = os.path.join(directory, filename)
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            try:
                image = Image.open(file_path)
                # Remove metadata
                data = list(image.getdata())
                image_without_exif = Image.new(image.mode, image.size)
                image_without_exif.putdata(data)
                # Save the image without metadata
                image_without_exif.save(file_path)
                print(f'Successfully removed metadata from {file_path}')
            except:
                print(f'Could not remove metadata from {file_path}')
        elif filename.endswith('.mp4'):
            try:
                os.system(f'exiftool -all= {file_path}')
                print(f'Successfully removed metadata from {file_path}')
            except:
                print(f'Could not remove metadata from {file_path}')

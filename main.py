from PIL import Image, UnidentifiedImageError
from pathlib import Path
import os


##########  Function  #########
def image_processing(input_folder, output_folder):
    count = 0
    for item in input_folder.iterdir():
        try:
            print(f"Processing: {item.name}")
            img = Image.open(item)
            print(f"Image: {item.name}")
            print(f"Format: {img.format}")
            print(f"Size: {img.size}")
            print(f"Width: {img.size[0]}")
            print(f"Height: {img.size[1]}")
            print(f"Mode: {img.mode}")
            full_path = os.path.join(output_folder, item.name)
            img.save(full_path)
            count += 1
        except UnidentifiedImageError:
            print(f"Skipping {item.name}: not a supported image")
    print("Done!")
    print(f"{count} images processed")

###############################

target_path = Path(".\\output")

try: 
    target_path.mkdir()
    print(f"The '{target_path}' directory now exists!")
except FileExistsError:
    print(f"The '{target_path}' already exists!")
except Exception as e:
    print(e)

folder_path = Path("./input")

if folder_path.exists():
    image_processing(folder_path, target_path)
else:
    print(f"{folder_path.name} does not exist")
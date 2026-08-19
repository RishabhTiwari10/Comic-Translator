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
    # print(f"{folder_path.name} exist")
    image_processing(folder_path, target_path)
else:
    print(f"{folder_path.name} does not exist")

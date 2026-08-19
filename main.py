from PIL import Image, UnidentifiedImageError
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


########################  Function  #######################

def resize_img(width, height, output_folder, img, name):
    print(f"Processing resizing of image: {name}")
    resized_size = (width//2, height//2)
    img_resized = img.resize(resized_size)            
    name = 'resized_' + name
    new_output_folder = output_folder / name
    img_resized.save(new_output_folder)


def crop_img(width, height, output_folder, img, name):
    print(f"Processing Croping of image: {name}")
    crop_width = 400
    crop_height = 500
    left = (width - crop_width) // 2
    upper = (height - crop_height) // 2
    right = (width + crop_width) // 2
    lower = (height + crop_height) // 2
    img_crop = img.crop((left, upper, right, lower))
    name = 'crop_' + name
    new_output_folder = output_folder / name
    img_crop.save(new_output_folder)


def annotated_img(output_folder, img, name):
    print(f"Processing annotation of image: {name}")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", size=45)
    position = (100, 100)
    text = "TEST"
    text_color = (255, 0, 0)  # Red
    draw.text(position, text, font=font, fill=text_color)
    name = 'annotated_' + name
    new_output_folder = output_folder / name
    img.save(new_output_folder)


def image_processing(input_folder, output_folder):
    count = 0
    for item in input_folder.iterdir():
        try:
            print(f"Processing: {item.name}")
            img = Image.open(item)
            print(f"Dimension: {img.size}")
            width = img.size[0]
            height = img.size[1]
            resize_img(width, height, output_folder, img, item.name)
            crop_img(width, height, output_folder, img, item.name)
            annotated_img(output_folder, img, item.name)
            count += 1
        except UnidentifiedImageError:
            print(f"Skipping {item.name}: not a supported image")
        except Exception as e:
            print(e)
    print("Done!")
    print(f"{count} images processed")


###########################################################

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
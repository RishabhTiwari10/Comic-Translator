import pytesseract
from PIL import Image, UnidentifiedImageError
from pathlib import Path

########################  Function  #######################


def comic_processing(input_folder, output_folder):
    count = 0
    for item in input_folder.iterdir():
        try:
            print(f"Processing: {item.name}")
            img = Image.open(item)

            string = pytesseract.image_to_string(image=img, config='--psm 11')
            print(f"Detected text of {item.name}:")
            print(string)

            data = pytesseract.image_to_data(img, config='--psm 11', output_type=pytesseract.Output.DICT)
            # print(data)
            # print(data.keys())
            # print(data['text'])
            # print(data['conf'])
            # print(len(data['text']))
            # print(len(data['conf']))


            for i in range(len(data['text'])):
                text = data['text'][i]
                if text == '':
                    continue
                else:
                    confidence = data["conf"][i]
                    x = data["left"][i]
                    y = data["top"][i]
                    width = data["width"][i]
                    height = data["height"][i]

                    print(text)
                    print(f"  confidence : {confidence}")
                    print(f"  position: x={x}, y={y}")
                    print(f"  size: width={width}, height={height}")
                    
            count += 1
        except UnidentifiedImageError:
            print(f"Skipping {item.name}: not a supported image")
        except Exception as e:
            print(e)
    print("Done!")
    print(f"{count} images processed")


###########################################################

target_path = Path(".\\output")
folder_path = Path(".\\input")

if target_path.exists() and folder_path.exists():
    print(f"{folder_path.name} and {target_path.name} does exist")
    comic_processing(folder_path, target_path)
else:
    print(f"{folder_path.name} and {target_path.name} does not exist")
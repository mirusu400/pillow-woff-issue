
from PIL import ImageFont
import os

# list dir
files = os.listdir("./fonts")
for file in files:
    print(f"Trying to convert {file} ...\t", end="...")
    try:
        fnt = ImageFont.truetype(f'./fonts/{file}')
        print("Success")
    except Exception as e:
        print("Failed " + str(e))


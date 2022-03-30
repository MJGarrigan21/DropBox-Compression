from pathlib import Path
from PIL import Image
import os

directory = "/home/mgarrigan/Jack Capital Group Dropbox/Mission Restoration"
paths = Path(directory).glob('**/*.jpg')
alsoPaths = Path(directory).glob('**/*.JPG')
count = 0

for path in paths:
    try:
        count += 1
        print(path)
        with Image.open(path) as im:
            height = im.height
            width = im.width
            im.resize((int(height/2), int(width/2)))
            im.save(path)
            print(count)
    except:
        continue

for path in alsoPaths:
    try:   
        count += 1
        with Image.open(path) as im:
            height = im.height
            width = im.width
            im.resize((int(height/2), int(width/2)))
            im.save(path)
            print(count)
    except:
        continue
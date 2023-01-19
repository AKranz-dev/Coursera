#!/usr/bin/env python3

import PIL
from PIL import Image
import os

imagesDirectory = r"/home/student-01-6bb66a8e7d9c/supplier-data/images"
newDirectory = r"/home/student-01-6bb66a8e7d9c/supplier-data/images"



os.chdir(imagesDirectory)
for item in os.listdir(imagesDirectory):
    if item != "LICENSE" and item != "README":
        imagePath = os.path.join(imagesDirectory, item)
        newImagePath = os.path.join(newDirectory, item)
        print(item)

        im = Image.open(item)
        
        newFileName = imagePath.replace('.tiff','.jpeg')
        new_im = im.convert('RGB').resize((600,400)).save(newFileName)
        os.remove(imagePath)
    

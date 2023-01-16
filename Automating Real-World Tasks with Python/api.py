import PIL
from PIL import Image
import os


#curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie


#The images received are in the wrong format:
#.tiff format
# Image resolution 192x192 pixel (too large)
# Rotated 90° anti-clockwise

# The images required for the launch should be in this format:
# .jpeg format
# Image resolution 128x128 pixel
# Should be straight
#Send images to the /opt/icons directory



imagesDirectory = r"G:\DevOps\Python\Projects\Coursera\Automating Real-World Tasks with Python\PIL\images"
newDirectory = r"G:\DevOps\Python\Projects\Coursera\Automating Real-World Tasks with Python\PIL\NewImages"

os.chdir(imagesDirectory)
for item in os.listdir(imagesDirectory):
    if item != ".DS_Store":
        imagePath = os.path.join(imagesDirectory, item)
        newImagePath = os.path.join(newDirectory, item)
        print(item)

        im = Image.open(item)
        
        new_im = im.convert('RGB').rotate(270).resize((128,128)).save(newImagePath + ".jpg")
    


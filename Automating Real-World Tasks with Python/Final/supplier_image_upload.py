#!/usr/bin/env python3

import requests
import os


imagesDirectory = r"/home/student-01-6bb66a8e7d9c/supplier-data/images"
uploadURL = "http://34.71.44.146/upload/"

os.chdir(imagesDirectory)


for item in os.listdir(imagesDirectory):
    if item != "LICENSE" and item != "README":
        with open(item, 'rb') as opened:
            r = requests.post(uploadURL, files={'file': opened})






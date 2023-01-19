#!/usr/bin/env python3
import requests
import os


targetPath = r"/home/student-01-6bb66a8e7d9c/supplier-data/descriptions"
os.chdir(targetPath)
dataDict={}

i=1

for item in os.listdir(targetPath):
    with open (item) as file:
        dataDict["name"] = file.readline().strip()
        dataDict["weight"] = int(file.readline().strip().replace("lbs","").strip())
        dataDict["description"] = file.readline().strip()
        if i != 10:
            dataDict["image_name"] = "00" + str(i) + ".jpeg"
        else:
            dataDict["image_name"] = "0" + str(i) + ".jpeg"
        i+=1

    response = requests.post("http://34.71.44.146/fruits/", data=dataDict)
    

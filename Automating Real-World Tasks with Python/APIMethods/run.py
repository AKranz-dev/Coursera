#! /usr/bin/env python3
import os
import requests

filesDirectory = r"/data/feedback"
dataDict={}

os.chdir(filesDirectory)

for item in os.listdir(filesDirectory):
    with open (item) as file:
        dataDict["title"] = file.readline().strip()
        dataDict["name"] = file.readline().strip()
        dataDict["date"] = file.readline().strip()
        dataDict["feedback"] = file.readline().strip()
    
    response = requests.post("http://146.148.63.245/feedback/", data=dataDict)





#!/usr/bin/env python3
import os
import reports
import datetime
import emails


# read text entry:
def getDesc(file):
    os.chdir(r"/home/student-01-6bb66a8e7d9c/supplier-data/descriptions/")
    with open(file) as f:
        lines = f.read().strip().splitlines()
    name_field = "name: {}".format(lines[0])
    weight_field = "weight: {}".format(lines[1])
    return "{}<br/>{}<br/><br/>".format(name_field, weight_field)


def processText():
    txt_dir = r"/home/student-01-6bb66a8e7d9c/supplier-data/descriptions/"

    report_body = ""
    for file in os.listdir(txt_dir):
        if file.endswith(".txt"):
            report_body += getDesc(file)
    return report_body



# def processText():
#     paragraph = ""
#     targetPath = r"/home/student-01-6bb66a8e7d9c/supplier-data/descriptions"
#     os.chdir(targetPath)
#     for item in os.listdir(targetPath):
#         with open (item) as file:
#             name = file.readline().strip()
#             weight = file.readline().strip()
#             paragraph = paragraph + "name: " + name
#             paragraph = paragraph + '\n'
#             paragraph = paragraph + "weight: " + weight
#             paragraph = paragraph + '\n'
#             paragraph = paragraph + '\n'
#     print(paragraph)
#     return(paragraph)


        
if __name__ == "__main__":
    paragraph = processText()
    attachment = "/tmp/processed.pdf"
    title = "Processed Update on " + datetime.datetime.now().strftime("%b %d, %Y")
    
    reports.generate_report(attachment, title, paragraph)

    message = emails.generate_email(attachment)
    emails.send_email(message)


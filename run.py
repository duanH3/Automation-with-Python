#! /usr/bin/env python3
import os
import requests

url = "http://localhost/fruits/"
path = "supplier-data/descriptions/"

list_of_files = os.listdir(path)

for file in list_of_files:
    if file.endswith("txt"):
        with open(path + file, "r") as f:
            file_name = os.path.splitext(file)[0]
            data = f.read()
            data = data.split("\n")
            dic = {"name":data[0], "weight":int(data[1].strip(" lbs")), "description":data[2], "image_name":file_name+".jpeg"}
            response = requests.post(url, json=dic)
            print(response.status_code)

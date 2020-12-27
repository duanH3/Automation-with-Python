#!/usr/bin/env python3
from PIL import Image
import os, sys

size = 600, 400
path = "supplier-data/images/"

for pic in os.listdir(path):
  if 'tiff' in pic:
    file_name = os.path.splitext(pic)[0]    #Grab file name
    outfile = path + file_name + ".jpeg"    #Output file
    try:
      Image.open(path + pic).convert("RGB").resize(size).save(outfile,"JPEG")
    except IOError:
      print("cannot convert", pic) 

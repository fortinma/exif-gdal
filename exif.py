#!/usr/bin/python
# this is a python file requiring gdal used to export lat/long from EXIF information in photos
import os
import osgeo
from osgeo import gdal, osr

directory = '/Users/marcelfortin/Pictures/2018'


for filename in os.listdir(directory):
    if filename.endswith(".JPG") or filename.endswith(".JPEG"):
#        print(os.path.join(directory, filename))
#         f = open(directory + "/" + filename + ".json", 'w+')
        from subprocess import call
        call(["gdalinfo", "-json", directory + "/" + filename]) #this one works
    else:
        continue

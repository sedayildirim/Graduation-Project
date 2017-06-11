# Converts PPM images to JPG images

import os
import sys
from PIL import Image


def convert(path):
    data_file = open(os.path.join(path, 'data.txt'), 'r+')
    jpgdata_file = open(os.path.join(path, 'jpgdata.txt'), 'w+')
    jpgdata_file.truncate()
    
    for file_path in data_file:
        name = file_path.rstrip('\n')        
        im = Image.open(name)
        
        new_name = os.path.splitext(name)[0] + '.jpg'
        im.save(new_name) 

        jpgdata_file.write(str(new_name) + '\n')
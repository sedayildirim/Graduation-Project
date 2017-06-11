#   Returns a number value for the category of the image
#   Left (0), Center (1), or Right (2)

import os
import sys
import ntpath

from read_pgm import read_pgm

def categorize(path):
    #current_dir = os.path.dirname(os.path.realpath(__file__))
    print "Working on directory: ", path
    
    category_file = open(os.path.join(path, 'categories.txt'), 'w+')
    category_file.truncate()
    
    label_file = open(os.path.join(path, 'labels.txt'), 'r+')
    
    rgb_file = open(os.path.join(path, 'jpgdata.txt'), 'r').readlines()

#   create category directories
    for c in range(3):
        cat_path = os.path.join(path, str(c))
        os.makedirs(cat_path)
    
    i = 0       
    for file_path in label_file:
        print "Processing file", file_path
        
#       find category for the rgb file, write to categories.txt        
        category = read_pgm(file_path.rstrip('\n'))        
        category_file.write(str(category) + '\n')

#       create the directory string to move the file to
        new_path = os.path.join(path, str(category))        
        extension_path = "\\"        
        new_path = new_path + extension_path        
        new_path = new_path + ntpath.basename(rgb_file[i].strip())
        
#       move the file
        os.rename(rgb_file[i].strip(), new_path)
        i += 1
import cv2
import numpy
import os
import sys
import ntpath
import numpy as np
import scipy.signal

def read_pgm(file_path):
      
    with open(file_path, 'rb') as infile:
        header = infile.readline()
        width, height, maxval = [int(item) for item in header.split()[1:]]
        ximg = np.fromfile(infile, dtype=np.uint16).reshape((height, width))
        
	# apply  median filter
	img = scipy.signal.medfilt(ximg, 19)
    
	# enumarate L, R, and C
    categories = ['Left', 'Center', 'Right']
    list(enumerate(categories))
    
    # initialize the closest values to be infinity
    closest_left = float("inf")
    closest_center = float("inf")
    closest_right = float("inf")
    
    # go through sections of the image, L = 0, C = 1, R = 2
    for i in range(10, 470):
        for j in range(20, 220):     #evaluate left
            if img[i][j] < closest_left:
                closest_left = img[i][j]
                l_i = i
                l_j = j
        # assume left is closest
        min_depth = closest_left
        category = 0
        coori = l_i
        coorj = l_j
        for j in range(220, 420):   #evaluate center
            if img[i][j] < closest_center:
                closest_center = img[i][j]
                c_i = i
                c_j = j
        # if center is closer, choose center
        if closest_center < min_depth:
            min_depth = closest_center
            category = 1
            coori = c_i
            coorj = c_j
        for j in range(420, 620):   #evaluate right
            if img[i][j] < closest_right:
                closest_right = img[i][j]
                r_i = i
                r_j = j                
        # if right is closer, choose right
        if closest_right < min_depth:
            min_depth = closest_right
            category = 2
            coori = r_i
            coorj = r_j
            
    # print minimum depth values
	print "left:", closest_left
    print "center:", closest_center
    print "right:", closest_right      
      
	# print minimum depth and category
    print "min depth:", min_depth
    print categories[category]
	
	# print coordinates of minimum depth pixel    
    print "coordinates of point", coori, coorj
    return category


def categorize(path):
    print "Working on directory: ", path
    
    category_file = open(os.path.join(path, 'categories.txt'), 'w+')
    category_file.truncate()
    
    label_file = open(os.path.join(path, 'labels.txt'), 'r+')
    
    rgb_file = open(os.path.join(path, 'jpgdata.txt'), 'r').readlines()

	# create category directories
    for c in range(3):
        cat_path = os.path.join(path, str(c))
        os.makedirs(cat_path)
    
    i = 0       
    for file_path in label_file:
        print "Processing file", file_path
        
		# find category for the rgb file, write to categories.txt        
        category = read_pgm(file_path.rstrip('\n'))        
        category_file.write(str(category) + '\n')

		# create the directory string to move the file to
        new_path = os.path.join(path, str(category))        
        extension_path = "\\"        
        new_path = new_path + extension_path        
        new_path = new_path + ntpath.basename(rgb_file[i].strip())
        
		# move the file
        os.rename(rgb_file[i].strip(), new_path)
        i += 1
        
if __name__ == '__main__':
    path = sys.argv[1]
    categorize(path)
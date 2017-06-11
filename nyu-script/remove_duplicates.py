# Removes the duplicate image files in the partial NYU dataset

import os
import sys

def removeduplicates(path):
	#print working directory
    print "Working on directory: ", path
    
	# holds images already seen
    lines_seen = set()
    
    os.path.join(path, 'newdepth.txt')
    
    datafile = open(os.path.join(path, 'data.txt'), "r")
    depthfile = open(os.path.join(path, 'labels.txt'), "r").readlines()
    outdata = open(os.path.join(path, 'newdata.txt'), "w")
    outdepth = open(os.path.join(path, 'newdepth.txt'), "w")
    
    i=0
    for line in datafile:
		# if not a duplicate
        if line not in lines_seen:
            outdata.write(line)
            lines_seen.add(line)
            outdepth.write(depthfile[i])
        i += 1
            
    outdata.close()
    outdepth.close()
    datafile.close()
    
    os.remove(os.path.join(path, 'data.txt'))
    os.remove(os.path.join(path, 'labels.txt'))
    
    os.rename(os.path.join(path, 'newdata.txt'), os.path.join(path, 'data.txt'))
    os.rename(os.path.join(path, 'newdepth.txt'), os.path.join(path, 'labels.txt'))
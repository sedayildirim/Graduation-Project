import os
import sys
import traceback
import ntpath
from PIL import Image

from match_files import match_files
from categorize_files import categorize_files
from convert_to_jpg import convert_to_jpg
from read_pgm import read_pgm
from remove_duplicates import remove_duplicates

if __name__ == '__main__':
    path = sys.argv[1]
    print "Matching files"
    match_files(path)
    print "Removing duplicates"
    remove_duplicates(path)
    print "Converting to JPEG"
    convert_to_jpg(path)
    print "Categorizing files"
    categorize_files(path)
	print "Finished."

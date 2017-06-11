#!/usr/bin/python

import os
import sys
import traceback

from get_matched_rgb_depth_map import get_matched_rgb_depth_map


# print 'Arguments: ', str(sys.argv)

def match(root):
    try:
        matched_map = get_matched_rgb_depth_map(root)
        # for dir_name in os.listdir(sys.argv[1]):
        #     full_name = os.path.join(root, dir_name)
        #     print full_name
        #     tmp_map = get_matched_rgb_depth_map(os.path.join(root, dir_name))
        #     matched_map.update(tmp_map)
        #     print 'returned %r elements' % len(tmp_map)
        #     tmp_map.clear()
        print 'total number of elements in matched map %r' % len(matched_map)

        
        #data_dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'match_data')
        
        #data_dir_path = os.path.join(root, 'match_data')
        #if not os.path.isdir(data_dir_path):
        #    os.mkdir(data_dir_path, 0755)

        label_file = open(os.path.join(root, 'labels.txt'), 'w+')
        label_file.truncate()
        data_file = open(os.path.join(root, 'data.txt'), 'w+')
        data_file.truncate()

        for label_file_name, data_file_name in matched_map.iteritems():
            label_file.write(label_file_name + '\n')
            data_file.write(data_file_name + '\n')


        print 'all files are written'
        label_file.close()
        data_file.close()

#        # Run shuffle script to create train and validation set
#        os.system('./shuffle.sh')
    except Exception:
        print "Exception in user code:"
        print '-' * 60
        traceback.print_exc(file=sys.stdout)
        print '-' * 60


if __name__ == '__main__':
    root = sys.argv[1]
    match(root)
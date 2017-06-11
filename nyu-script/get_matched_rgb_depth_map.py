# Script taken from https://github.com/damienjadeduff/all-your-depths-are-belong-to-us/tree/master/scripts
# Matches RGB images with their corresponding depth images
# Modified for Windows OS

import os
import re
from decimal import *


# Returns a map of matched rgb and depth files by comparing timestamps in the filenames
def get_matched_rgb_depth_map(root_path):

    print 'Processing directory: ', root_path
    depth_file_list = []
    rgb_file_list = []

    depth_rgb_map = {}

    for file_name in os.listdir(root_path):
        full_file_name = os.path.join(root_path, file_name)
        if os.path.isdir(full_file_name):
            # call this function again to get the matched map
            # of this directory and update the map in this cycle
            depth_rgb_map.update(get_matched_rgb_depth_map(full_file_name))
        else:
            # print 'Found file: ', full_file_name
            if re.match('(.*)pgm', file_name):
                depth_file_list.append(full_file_name)
                continue
            elif re.search('(.*)ppm', file_name):
                rgb_file_list.append(full_file_name)
                continue
            else:
                continue
    # for root, dirs, files in os.walk(root_path):
    #     for name in files:
    #         file_name = os.path.join(root, name)
    #         print file_name
    #         if re.match('(.*)pgm', name):
    #             depth_file_list.append(file_name)
    #             continue
    #         elif re.search('(.*)ppm', name):
    #             rgb_file_list.append(file_name)
    #             continue
    #         else:
    #             continue

    depth_file_list.sort()
    rgb_file_list.sort()

    depth_file_list_length = len(depth_file_list)
    rgb_file_list_length = len(rgb_file_list)
    print 'Found %d depth, %d rgb images in %s' % (depth_file_list_length, rgb_file_list_length, root_path)

    rgb_idx = 0

    for depth_idx in range(0, depth_file_list_length):
        # print 'Matching depth image %d/%d. depth_file_name %r, rgb_file_name %r' % (
        #     depth_idx + 1, depth_file_list_length, depth_file_list[depth_idx], rgb_file_list[rgb_idx])
        time_parts_depth = re.split('-', re.split('\\\\', depth_file_list[depth_idx])[-1])
        time_parts_rgb = re.split('-', re.split('\\\\', rgb_file_list[rgb_idx])[-1])

        time_of_depth = Decimal(time_parts_depth[1])
        time_of_rgb = Decimal(time_parts_rgb[1])

        time_diff = abs(time_of_depth - time_of_rgb)
        # Advance until the rgb index until time_diff get worse
        while rgb_idx < rgb_file_list_length - 1:
            time_parts_rgb = re.split('-', re.split('\\\\', rgb_file_list[rgb_idx + 1])[-1][2:])
            time_of_rgb = Decimal(time_parts_rgb[0])

            tmp_diff = abs(time_of_depth - time_of_rgb)
            if tmp_diff > time_diff:
                break
            else:
                # Time difference is better for this one
                time_diff = tmp_diff
                rgb_idx += 1

        # print 'Matched depth %d to rgb %d' % (depth_idx + 1, rgb_idx + 1)
        depth_rgb_map[depth_file_list[depth_idx]] = rgb_file_list[rgb_idx]

    return depth_rgb_map
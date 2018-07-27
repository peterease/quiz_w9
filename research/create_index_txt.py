# To produce trainval.txt to include information on relationships between images and their indexes.

import os
import random
xml_directory = "/home/yupt/workspace/models/research/annotations/xmls" 
output_xml_directory = "/home/yupt/workspace/models/research/annotations"
image_index_list = []
for root, dirs, files in os.walk(xml_directory):
    for file in files:
        if os.path.splitext(file)[1] == '.xml':
            image_index_list.append(os.path.splitext(file)[0])
random.seed(42)
random.shuffle(image_index_list)
trainval = open(os.path.join(output_xml_directory, "trainval.txt"), "w")
for index in range(154):
    trainval.write(str(image_index_list[index] + "\n"))


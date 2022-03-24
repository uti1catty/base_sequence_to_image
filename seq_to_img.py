import numpy as np
import cv2
from PIL import Image

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
black = [0, 0, 0]

def sequences_to_image(sequences, dir_path, img_name):
    #transform the every bases in every sequences to color (RGB and Black)
    sequence_color = np.zeros((sequences.shape[0], sequences.shape[1], 3))
    sequence_color[sequences == 'A'] = red
    sequence_color[sequences == 'T'] = green
    sequence_color[sequences == 'G'] = blue
    sequence_color[sequences == 'C'] = black

    #print(sequence_color)

    # make each sequences to image file
    for i in range(sequence_color.shape[0]):
        one_sequence = np.array(sequence_color[i], np.uint8)
        #print(one_sequence.shape)
        one_sequence = np.reshape(one_sequence, (1, one_sequence.shape[0], one_sequence.shape[1]))
        im = Image.fromarray(one_sequence)
        im.save(dir_path + "/" + img_name + "_{}.png".format(i))


sequences_str = ['ATAAGCTAGATTCGGATACG', 'ATACCATGCAACCGGTAGCA']

sequences_list = []
for i in range(len(sequences_str)):
    #print(np.array(sequences_str[i]))

    sequences_list.extend([char for char in sequences_str[i]])
sequences_list = np.array(sequences_list).reshape((-1, 20))
print(sequences_list)

sequences_to_image(sequences_list, 'test_dir', 'test_img')
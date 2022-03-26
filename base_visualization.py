import numpy as np
import cv2
from PIL import Image
import pandas as pd

#Code wrote by uti1catty

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
black = [0, 0, 0]

np.random.seed(0)
'''
input
sequences: shape(seq_num, seq_len) sequences
dir_path: string type dir_path
img_name: string type img_name

output
saving color image of each sequence
'''
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


# 3~6 AATG, AATC, AGTG
base = ['A', 'T', 'G', 'C']


'''user defining variables'''
cancer_candidate = [['A','A','T','G'], ['A','A','T','C'], ['A','G','T','G']]
#cancer_seq_len = cancer_candidate.shape
cancer_sequence_num = 180
normal_sequence_num = 180
cancer_start_idx = 3
sequence_length = 20
'''user defining variables finished'''

'''cancer'''
'''cancer step 1. Make N sequences'''
cancer_sequences = []
#make 180 cancer_sequence
for idx in range(cancer_sequence_num):
    cancer_point = cancer_candidate[idx % len(cancer_candidate)] #cancer point will rotate 3 candidate
    sequence = []
    for j in range(16):
        sequence.append(base[np.random.randint(4)]) #pick 16 random base
    cancer_sequence = sequence[:cancer_start_idx] + cancer_point + sequence[cancer_start_idx:] #make len=20 cancer_sequence
    cancer_sequences.append(cancer_sequence)
    #print(cancer_sequence)

#make cancer_sequences
cancer_sequences = np.array(cancer_sequences)

print('cancer_sequences shape: ', cancer_sequences.shape)
print('cancer_sequences:\n', cancer_sequences)

'''cancer step 2. Make each sequence to image'''
#saving color image of each cancer sequence
sequences_to_image(cancer_sequences, "cancer_folder", "cancer_seq")


'''normal'''

normal_sequences = []
#make 180 normal sequences
while len(normal_sequences) < normal_sequence_num:
    sequence = []

    # make 'sequence_length' length random sequence
    for i in range(sequence_length):
        sequence.append(base[np.random.randint(4)])

    #if produced sequence is cancer sequence, ignore it.
    if sequence[3:7] in cancer_candidate:
        continue
    
    normal_sequences.append(sequence)

normal_sequences = np.array(normal_sequences)

print('normal_sequences shape: ', normal_sequences.shape)
print('normal_sequences:\n', normal_sequences)

'''normal step 2. Make each sequence to image'''
#saving color image of each cancer sequence
sequences_to_image(normal_sequences, "normal_folder", "normal_seq")


'''step 3. Make every sequences to csv file with label'''
#add label to cancer sequences 
cancer_with_label = cancer_sequences.copy()
cancer_label = [['cancer'] * cancer_sequences.shape[0]]
cancer_label = np.array(cancer_label).T
#print(cancer_label)
cancer_with_label = np.append(cancer_with_label, cancer_label, axis=1)
#print(cancer_with_label)

#add label to normal sequences 
normal_with_label = normal_sequences.copy()
normal_label = [['normal'] * normal_sequences.shape[0]]
normal_label = np.array(normal_label).T
#print(normal_label)
normal_with_label = np.append(normal_with_label, normal_label, axis=1)
#print(normal_with_label)

#make total sequences
total_sequences = np.append(cancer_with_label, normal_with_label, axis=0)

#make csv file
df = pd.DataFrame(total_sequences)
df.to_csv('total_sequences.csv', index=False)
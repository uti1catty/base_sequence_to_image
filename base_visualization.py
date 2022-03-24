import numpy as np
import cv2
from PIL import Image

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
black = [0, 0, 0]


# 3~6 AATG, AATC, AGTG
base = ['A', 'T', 'G', 'C']

#cancer
cancer_candidate = [['A','A','T','G'], ['A','A','T','C'], ['A','G','T','G']]
cancer_sequences = []
for idx in range(180):
    cancer_point = cancer_candidate[idx % 3] #cancer point will rotate 3 candidate
    sequence = []
    for j in range(16):
        sequence.append(base[np.random.randint(3)])
    cancer_sequence = sequence[:3] + cancer_point + sequence[3:]
    cancer_sequences.append(cancer_sequence)
    print(cancer_sequence)

cancer_sequences = np.array(cancer_sequences)
print('cancer_sequences:\n', cancer_sequences)
print('cancer_sequences shape: ', cancer_sequences.shape)

sequence_color = np.zeros((cancer_sequences.shape[0], cancer_sequences.shape[1], 3))
sequence_color[cancer_sequences == 'A'] = red
sequence_color[cancer_sequences == 'T'] = green
sequence_color[cancer_sequences == 'G'] = blue
sequence_color[cancer_sequences == 'C'] = black

print(sequence_color)

for i in range(sequence_color.shape[0]):
    one_sequence = np.array(sequence_color[i], np.uint8)
    #print(one_sequence.shape)
    one_sequence = np.reshape(one_sequence, (1, one_sequence.shape[0], one_sequence.shape[1]))
    im = Image.fromarray(one_sequence)
    im.save("cancer_folder/cancer_seq_{}.png".format(i))


#not_cancer
normal_sequences = []
while len(normal_sequences) < 180:
    sequence = []
    for i in range(20):
        sequence.append(base[np.random.randint(4)])
    #if produced sequence is cancer sequence, ignore it.
    if sequence[3:7] in cancer_candidate:
        continue
    
    normal_sequences.append(sequence)

normal_sequences = np.array(normal_sequences)
print(normal_sequences)

sequence_color = np.zeros((normal_sequences.shape[0], normal_sequences.shape[1], 3))
sequence_color[normal_sequences == 'A'] = red
sequence_color[normal_sequences == 'T'] = green
sequence_color[normal_sequences == 'G'] = blue
sequence_color[normal_sequences == 'C'] = black

for i in range(sequence_color.shape[0]):
    one_sequence = np.array(sequence_color[i], np.uint8)
    #print(one_sequence.shape)
    one_sequence = np.reshape(one_sequence, (1, one_sequence.shape[0], one_sequence.shape[1]))
    im = Image.fromarray(one_sequence)
    im.save("normal_folder/normal_seq_{}.png".format(i))
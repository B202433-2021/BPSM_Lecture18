#!/usr/local/bin/python3

import os, sys, subprocess
import numpy as np
import matplotlib.pyplot as plt

with open("alignment.txt", "r") as infile:
	alignment = infile.read()

# split by newline characters

sequences = alignment.split("\n")
print(len(sequences))
sequence_length = len(sequences[0])
print(sequence_length)
#print(sequences[0:5])

conservation_scores = []
for position in range(sequence_length):
	residues = []
	for sequence in sequences:
		residues.append(sequence[position])
	residue_set = set(residues)
	# make conservation score with 1 being all conserved and 0 being completely different in every single sequence
	conservation_score = 1 - (len(residue_set)-1)/26		# 26 letters + "-" but take away 1
	conservation_scores.append(conservation_score)

#print(conservation_scores)

plt.figure(figsize=(20,8))
plt.plot(conservation_scores)
plt.title("Conservation across a multiple sequence alignment")
plt.ylabel('Conservation')
plt.xlabel('Position on alignment')
plt.savefig("conservation.png",transparent=True)
plt.show()

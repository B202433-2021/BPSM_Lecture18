#!/usr/local/bin/python3

import subprocess
# subprocess.call("pip3 install matplotlib", shell = True)

import os, sys
import numpy as np
import matplotlib.pyplot as plt

with open("ecoli.txt", "r") as infile:
	ecoli = infile.read().replace("\n", "").upper()[0:100000]

window = 1000

ATs = []
for start in range(len(ecoli) - window):
	win = ecoli[start:start+window]
	A_content = win.count("A")
	T_content = win.count("T")
	AT_percent = (A_content + T_content)*100 / window
	ATs.append(AT_percent)

plt.plot(ATs)
plt.title("AT content across Ecoli genome")
plt.ylabel('Percentage')
plt.xlabel('Position on genome')
plt.savefig("Ecoli_ATcontent.png",transparent=True)
plt.show()	

# strings

s = 'hello world'
print(s)

s1 = 'hey "dude"'
s2 = "don't tell me what to do"
print(s1, s2)

print('hey "dude" don\'t tell me what to do')

# no need to ask, he's a string operatorrrrr

# String Functions

# Method Syntax

print(s.upper())
print(s)

print(s.replace('o',''))
print(s.replace('o','').replace('r', 'i'))

# string formatting (f-string)
import math
print(f'{math.pi}')
print(f'{math.pi:e}')
print(f'{1e6 * math.pi:e}')
print(f'{"hello world":>20}')
print(f'{20:<10} {10}')

print('{} {:.3f}'.format('str.format', math.pi))
print('%s %.3f' % ('printf', math.pi))

# indexes

seq = 'GAATTC'
print(seq[0], seq[1])

print(seq[-1])

for nt in seq:
	print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])
	
# slices

s = 'ABCDEFGHIJ'
print(s[0:5])

print(s[0:8:2])

print(s[0:5], s[:5])
print(s[5:len(s)], s[5:])

print(s, s[::], s[::1], s[::-1]) # s[::-1] makes it go backwards

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
	codon = dna[i:i+3]
	print(i, codon)

# tuples

tax = ('Homo', 'sapiens', 9606)
print(tax)

# enumerate()

nts = 'ACGT'
for i in range(len(nts)):
	print(i, nts[i])
	
for i, nt in enumerate(nts):
	print(i, nt)
	
# zip()

names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

# Lists

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

# list()

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph)
print(aas)

# split() and join()

text = 'good day	to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

# searching

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

# practice problems

# 1. Write a function that returns the minimum value of a list.
vals = -1, 0, 1, 2, 3, 4, 5
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
print(minimum(vals))

# 2. Write a function that returns both the minimum and maximum values of a list.

vals = -1,-2, 0, 4, 8
def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini
print(minmax(vals))

# 3. Write a function that returns the mean of the values in a list.

vals = (4, 6, 8)
def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)
print(mean(vals))

# 4. Write a function that computes the entropy of a probability distribution.

probs = (0.3, 0.2, 0.5)
def entropy(probs):
	h = 0
	for p in probs:
		h -= p * math.log2(p)
	return h
print(entropy(probs))
 
# 5. Write a function that computes the Kullback-Leibler distance between two sets of probability distributions.

def dkl(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += p * math.log2(p / q)
	return d
p1 = [0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)
print(dkl(p1, p2))

# Command Line Data

# sys.argv

import sys
print(sys.argv)

# converting types

i = int('42')
x = float('0.61803')
print(i * x)

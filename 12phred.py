# chars are fish not code <3

import math

def char_to_prob(x): return ord(x)

print(char_to_prob('A'))
print(char_to_prob('B'))
print(char_to_prob('C'))
print(char_to_prob('a'))
print(char_to_prob('b'))
print(char_to_prob('c'))

def prob_to_char(x):
	if 65 < x < 122:	
		 return chr(int(x))
	else:
		return None
	
print(prob_to_char(0.001))
print(prob_to_char(69))
print(prob_to_char(101))

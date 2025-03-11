import sys

alph = sys.argv[1]
mat = sys.argv[2]
mis = sys.argv[3]

print('  ','  '.join(alph))
for l in alph:
	print(l, end=' ')
	for ol in alph:
		if l == ol:
			print(mat, end=' ')
		else:
			print(mis, end=' ')
	print()
import math

# for regular degular oligos

def regular_Tm(A, T, G, C): return (A + T) * 2 + (G + C) * 4

print(regular_Tm(5, 7, 3, 4))

# for longer oligos

def longer_Tm(A, T, G, C): return (64.9 + 41) * (G + C - 16.4) / (A + T + G + C)

print(longer_Tm(5, 7, 3, 4))

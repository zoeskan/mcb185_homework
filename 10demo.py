print('hello, again')

# variables

import math

a = 3
b = 4 
c = math.sqrt(a**2 + b**2)
print(c)

print(type(a), type(b), type(c), sep=', ', end='!\n')

# functions

def pythagoras(a, b):
	c = math.sqrt(a**2 + b**2)
	return c

print(pythagoras(3, 4))

# Block Structure

def pythagoras(a, b): return math.sqrt(a**2 + b**2)

def circle_area(r): return math.pi * r**2
def rectangle_area(w, h): return w * h
def triangle_area(w, h): return rectangle_area(w, h) / 2

print(circle_area(5))
print(rectangle_area(4, 6))
print(triangle_area(4, 6))

# Practice 1

def celcius_fahrenheit(c): return (9 / 5) * c + 32

print(celcius_fahrenheit(35))

def fahrenheit_celcius(f): return (5 / 9) * (f - 32)

print(fahrenheit_celcius(50))

def arithmetic_mean(x, y, z): return (x + y + z) / 3

print(arithmetic_mean(5, 5, 5))

def geometric_mean(x, y, z): return math.sqrt(x * y * z) ** 1/3

print(geometric_mean(3, 3, 3)) 

def od260(A, e = 50, l = 1):
	return A / (e * l)
print(od260(100))

def dist_2points(x1, y1, x2, y2):  
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(dist_2points(10, 5, 15, 5))


# strings

s = 'hello world'
print(s, type(s))

# conditionals

a = 2
b = 2
if a == b:
	print('a equals b')

def is_even(x):
	if x % 2 == 0: return True
	return False

print(is_even(2))
print(is_even(3))

# boolean

c = a == b
print(c)
print(type(c))

# if-elif-else

if a < b: print('a < b')
elif a > b:print('a > b')
else:	print('a == b')

# chaining

if a < b or a > b:
	 print('all things being equal, a and b are not')
if a < b and a > b:
	 print('you are living in a strange world')
if not False: 	
	print(True)

# Floating Point Warning

a = 0.3
b = 0.1 * 3
if a < b: print('a < b')
elif a > b: print('a > b')
else:	print('a == b')

print(abs(a - b))
if abs(a - b) < 1e-9: print('close enough')

if math.isclose(a, b): print('close enough')


# string comparison

s1 = 'A'
s2 = 'B'
s3 = 'a'
if s1 < s2: print('A < B')
if s2 < s3: print('B < a')

# none type

def silly(m, x, b):
	y = m * x + b

print(silly(2, 3, 4))


# more practice

def is_integer(x):
	if x == x // 1: return True
	return False

print(is_integer(1))
print(is_integer(1.5))

def is_probability(x):
	if 0 <= x <= 1: return True
	return False

print(is_probability(0.5))
print(is_probability(2))

def is_nucleotide(x):
	if x == 'A' or x == 'T' or x == 'C' or x == 'G' : return True
	return False

print(is_nucleotide('A'))
print(is_nucleotide('B'))

def DNAmw(x):
	if x == 'A': return 313.21
	elif x == 'T': return 304.2
	elif x == 'C': return 289.18
	elif x == 'G': return 329.21
	else: return 'none'

print (DNAmw('A'))
print (DNAmw('B'))

def DNA_complement(x):
	if x == 'A': return 'T'
	elif x == 'T': return 'A'
	elif x == 'C': return 'G'
	elif x == 'G': return 'C'
	else: return 'none'

print (DNA_complement('A'))
print (DNA_complement('B'))

# Even More Practice

def large_in_charge(a, b, c):
	if a > b and a > c: return a
	elif b > a and b > c: return b
	else: return c

print (large_in_charge(1, 2, 3))

def sensitivity(TP, FN): return TP / (TP + FN)

print(sensitivity(0.9, 0.7))

def specificity(TN, FP): return TN / (TN + FP)

print(specificity(0.7, 0.9))

def F1_score(TP, FP, FN): return (2 * TP) / (2 * TP + (FP + FN))

print(F1_score(0.7, 0.2, 0.3))

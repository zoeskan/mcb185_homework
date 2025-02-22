# tuples

t = 1,2 
print(t)
print(type(t))

person = 'Steve', 21, 57891.50
print(person)

def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) /2
	return x, y


print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)

print(m[0], m[1])

# iteration

i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break

i = 0
while i < 10:
	print(i)
	i = i +3
print('final value of i is', i)

# for i in range()

for i in range(1, 10, 3):
	print(i)

for i in range(0, 5):
	print(i)

for i in range(2, 10, 2):
	print(i)

for i in range(5):
	print(i)
 
# all 3 of these do the same thing...
for i in range(5): print(i)
for i in range(0, 5): print(i)
for i in range(0, 5, 1): print(i)

# for item in container

basket = 'milk', 'eggs', 'bread'
for thing in basket:
	print(thing)

for i in range(len(basket)):
	print(basket[i])


# nesting!

for i in range(7):
	if i % 2 == 0: print(i, 'is even')
	else:	       print(i, 'is odd')

# Write a function that calculates the triangular number. This is the sum of numbers from 1 to n.

def triangular(n):
	tri = 0
	for i in range(n + 1):
		tri = tri + i
		return tri

print(triangular(1))
print(triangular(2))
print(triangular(3))
print(triangular(4))
print(triangular(5))

# Write a function that calculates the factorial of a number.

def factorial(n):
	if n == 0: return 1
	fac = 1
	for  i in range (1, n + 1):
		fac = fac * i
	return fac

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))

# Write a function that computes the Poisson probability of k events occurring with an expectation of n: n^k e^-n / k!

def poisson(n, k):
	return n**k * math.e**-n / factorial(k)

# Write a function that solves "n choose k": n! / k!(n - k)!

def nchoosek(n, k):
	return factorial(n) / (factorial(k) * factorial(n - k))
	

# Write a function that estimates Euler's number: e (2.71828...). This can be computed as the infinite sum of 1/n!. Choose a finite number of iterations.

def eulerr(limit):
	e = 0
	for n in range (limit):
		e = e + 1 / factorial(n)
	return e

# Write a function to determine if a number is prime.

def is_prime(n):
	for den in range(2, n // 2 +1):
		if n % den == 0: return False
	return True
	
print(is_prime(0))
print(is_prime(1))
print(is_prime(2))
print(is_prime(12))
	
# Write a function that estimates Pi (3.14159...) using the Nilakantha series. Again, choose a finite limit. Pi = 3 + 4/(2x3x4) - 4/(4x5x6) + 4/(6x7x8) - 4/(8x9x10) ...

def nilakantha(limit):
	pi = 3.14
	for i in range(1, limit+1):
		n = 2 * i
	d = n* (n+1) * (n*2)
	if i % 2 == 0: pi = pi - 4 / d
	else:	pi = pi + 4 / d
	return pi

# Random Numbers

import random

for i in range(5):
	print(random.random())
	
for i in range(3):
	print(random.randint(1, 6))
	
random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())


# More Practice

# monty pi-thon

total = 0
inside = 0

while True:
	x = random.random()
	y = random.random()
	if math.sqrt(x**2 + y**2) <= 1: 
		inside += 1
	total += 1
	print((inside / total) * 4)
	
# D&D Stats

# 3D6
normaltot = 0
r1tot = 0
x2tot = 0
d1tot = 0
trials = 10000
for i in range(trials):
	total = 0
	for i in range(3):
		total += (random.randint(1, 6))
	normaltot += total
	
	
	# 3D6r1
	
	total = 0
	for i in range(3):
		roll = random.randint(1, 6)
		if roll == 1:
			roll = random.randint(1, 6)
		total += roll
	r1tot += total
	
	
	# 3D6x2
	
	total = 0
	for i in range(3):
		roll1 = random.randint(1, 6)
		roll2 = random.randint(1, 6)
		if roll1 > roll2: total += roll1
		else: total += roll2
	x2tot += total
	
	# 4D6d1
	
	total = 0
	lowest = 6
	for i in range(4):
		roll = random.randint(1, 6)
		total += roll
		if roll < lowest:
			lowest = roll
	total -= lowest
	d1tot += total
print('normaltot average:', normaltot / trials)
print('r1tot average:', r1tot / trials)
print('x2tot average:', x2tot / trials)
print('d1tot average:', d1tot / trials)

	
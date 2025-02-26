# Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# Fn = F(n-1) + F(n-2), where n > 1
# each number is the sum of the two preceding numbers, starting with 0 and 1


def fibonacci(Fn):
	F0 = 0
	F1 = 1
	print(F0)
	print(F1)
	for i in range(2, Fn):
		Fn = F0 + F1
		print(Fn)
		F0 = F1
		F1 = Fn
	
fibonacci(10)
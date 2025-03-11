import sys
import math

# the number of values
vals = []
for arg in sys.argv[1:]:
	vals.append(int(arg))
vals.sort()	

print(f'number of values: {len(vals)}')

# the minimum and maximum values

mini = vals[0]
maxi = vals[0]
for val in vals:
	if val < mini: mini = val
	if val > maxi: maxi = val

print(f'maximum: {maxi}, minimum: {mini}')

# the mean and standard deviation

meantot = 0
for val in vals:
	meantot += val
mean = meantot / len(vals)
print(f'mean: {mean}')


var = 0
for val in vals:
	var += (mean - val) ** 2 / len(vals)
sd = math.sqrt(var)
	
print(f'standard deviation: {sd}')

# the median value

med = 0

if len(vals) % 2 == 1:
	mid = len(vals) // 2
	med = vals[mid]
else: 
	mid1 = len(vals) // 2
	mid2 = mid1 - 1
	med = (vals[mid1] + vals[mid2]) / 2

print(f'median: {med}')



	 
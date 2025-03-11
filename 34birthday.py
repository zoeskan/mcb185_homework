import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
redupe = 0

for i in range(trials):
	calendar = [0] * days
	for j in range(people):
		bday = random.randint(0, days - 1)
		calendar[bday] += 1
		if calendar[bday] > 1:
			redupe += 1
			break
	
prob = redupe / trials
print(f'prob of repeat dupe: {prob:.2f}')

# alternative
# for i in range(days):
	#calendar.append(0)
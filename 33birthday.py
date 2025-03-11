import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
dupe = 0

for i in range(trials):
	bdays = []
	for j in range(people):
		bday = random.randint(0, days)
		if bday in bdays:
			dupe += 1
			break
		bdays.append(bday)

prob = dupe / trials
print(f'prob dupe bday: {prob:.2f}')



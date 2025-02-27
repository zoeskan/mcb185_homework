# death saves
# 0 = death
# if < 10 = failure
# if > 10 = success
# if 3 failures = die
# if 3 successes = stable
# if 1 = 2 failures
# if 20 = revived
# probability of death, stabilizes, or revives?

import math
import random

trials = 10
death = 0
stable = 0
revive = 0

for i in range(trials):
	# what happens to my character?
	succ = 0
	fail = 0
	revi = False
	while succ < 3 and fail < 3 and revi == False:
		roll = random.randint(1, 20)
		if roll == 20: revi = True
		elif roll == 1: fail += 2
		elif roll < 10: fail += 1
		else: succ += 1
		
	# record what happened	
	if fail >= 3: death += 1
	if succ >= 3: stable += 1
	if revi == True: revive += 1
	
	# overall results
print('prob.death:', death / trials)
print('prob.stable:', stable / trials)
print('prob.revive:', revive / trials)
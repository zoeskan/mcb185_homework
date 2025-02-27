# death save
# 2 rolls
# dc = 5, roll > 5 for success
# dc = 15, roll > 15 for success
# advantage = roll 2 dice and take larger value
# disadvantage = roll 2 dice and take lower value


import math
import random

trials = 1000
# loops dcs
for dc in range(5, 16, 5):
	nor = 0
	adv = 0
	dis = 0
	
	for i in range(trials):
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		if r1 >= dc: nor += 1
		if r1 >= dc or r2 >= dc: adv += 1
		if r1 >= dc and r2 >= dc: dis += 1
		
		#record what happens
	print('dc:', dc, 'nor:', nor / trials, 'adv:', adv / trials, 'dis:', dis / trials)
		
		
















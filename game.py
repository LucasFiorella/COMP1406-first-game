import random, os, sys, time

def timed_raw_input():
	timeout = 5
	start = time.time()
	s = raw_input()
	stop = time.time()
	if stop-start > timeout:
		print "TIMEOUT!"
		print "Score: %d. Level: %d.\n" % (score,level)
		print "Game Over!\n\n"
		os._exit(1)
	return s

def add():
	global lives, score, level, total
	a = random.randint(0,total)
	b = random.randint(0,total)	
	print a, " + ", b, " = ",
	c = int(timed_raw_input())
	if a + b == c:
		score += 100
		total += 1
		print "Correct!"
	elif lives > 0:
		lives -= 1
		print "Wrong! The correct answer was %d!" % (a+b)
	else:
		print "Wrong! The correct answer was %d!" % (a+b)
		print "Score: %d. Level: %d.\n" % (score,level)
		print "Game Over!\n\n"
		os._exit(1)
	print "Score: %d. Level: %d. Lives: %d.\n" % (score,level,lives)

def sub():
	global lives, score, level, total

	a = random.randint(0,total)
	b = random.randint(0,total)
	print a, " - ", b, " = ",
	c = int(timed_raw_input())
	if a - b == c:
		score += 100
		total += 1
		print "Correct!"
	elif lives > 0:
		lives -= 1
		print "Wrong! The correct answer was %d!" % (a+b)
	else:
		print "Wrong! The correct answer was %d!" % (a+b)
		print "Score: %d. Level: %d.\n" % (score,level)
		print "Game Over!\n\n"
		os._exit(1)
	print "Score: %d. Level: %d. Lives: %d.\n" % (score,level,lives)

def mul():
	global lives, score, level, total
	a = random.randint(0,total)
	b = random.randint(0,total)
	print a, " x ", b, " = ",
	c = int(timed_raw_input())
	if a * b == c:
		score += 100
		total += 1
		print "Correct!"
	elif lives > 0:
		lives -= 1
		print "Wrong! The correct answer was %d!" % (a+b)
	else:
		print "Wrong! The correct answer was %d!" % (a+b)
		print "Score: %d. Level: %d.\n" % (score,level)
		print "Game Over!\n\n"
		os._exit(1)
	print "Score: %d. Level: %d. Lives: %d.\n" % (score,level,lives)

def div():
	global lives, score, level, total
	while a % b != 0:	
		a = random.randint(0,total)
		b = random.randint(0,total)
	print a, " / ", b, " = ",
	c = int(timed_raw_input())
	if a // b == c:
		score += 100
		total += 1
		print "Correct!"
	elif lives > 0:
		lives -= 1
		print "Wrong! The correct answer was %d!" % (a+b)
	else:
		print "Wrong! The correct answer was %d!" % (a+b)
		print "Score: %d. Level: %d.\n" % (score,level)
		print "Game Over!\n\n"
		os._exit(1)
	print "Score: %d. Level: %d. Lives: %d.\n" % (score,level,lives)

###############################################################################

print "Welcome to math race!"
print "The goal is to answer math question, you have 5 seconds per question.\n"
print "Press <ENTER> to start..."
lives = 3
score = 0
level = 1
total = 2
raw_input()
while lives > 0:
	if level == 1:
		while total <= 10:
			add()
	elif level == 2:
		while total <= 10:
			sub()
	elif level == 3:
		while total <= 10:
			mul()
	elif level == 4:
		while total <= 10:
			div()
	total = 2
	level += 1
	if level == 5:
		print "You win!"
		print "Score: %d. Lives: %d.\n" % (score,lives)

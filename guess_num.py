import random
answer = random.randint(1, 100)
count = 0
while True:
	value = input('input number:')
	value = int(value)
	count += 1
	print('You guessed ', count, 'times')
	if answer ==  value:
		print('correct!')
		break
	elif value < answer:
		print('more then ', value)
	elif value > answer:
		print('under ', value)
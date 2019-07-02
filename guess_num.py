import random
answer = random.randint(1, 100)

while True:
	value = input('input number:')
	value = int(value)
	if answer ==  value:
		print('correct!')
		break
	elif value < answer:
		print('more then ', value)
	elif value > answer:
		print('under ', value)
import random
start = input('Enter the start num of random: ')
end = input('Enter the end num of ramdom: ')
start = int(start)
end = int(end)
answer = random.randint(start, end)
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
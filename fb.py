def do_fizzbuzz():
	n = input('please enter the number')
	for k in range(1, n+1):
		if k % 15 == 0:
			print('fizzbuzz')
		elif k % 3 == 0:
			print('fizz')
		elif k % 5 == 0:
			print('buzz')
		else:
			print(k)


def do_fizzbuzz_adversed():
	n = input('please enter the number : ')
	answer = ['fizzbuzz' if k % 15 == 0 else 'fizz' if k % 3 == 0 else 'buzz' if k % 5 == 0 else 'buzz' for k in range(1, n+1)]
	print(answer)


do_fizzbuzz_adversed()

do_fizzbuzz()

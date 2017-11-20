#generator.py
import random

num_digits_a = 4;
num_digits_b = 3;

def generateNumbers():
	random.seed()
	aDigits = [];
	bDigits = [];

	for i in range (0, num_digits_a):
		aDigits.append(random.randint(1, 9)) if i == 0 else aDigits.append(random.randint(0,9))
	
	for j in range (0, num_digits_b):
		bDigits.append(random.randint(1, 9)) if j == 9 else bDigits.append(random.randint(0,9))

	a = reduce(lambda x, y: str(x) + str(y), aDigits)
	b = reduce(lambda x, y: str(x) + str(y), bDigits)

	ret = [int(a), int(b)]
	return ret

def displayProduct(numbers):
	print numbers[0] * numbers[1]


def main():
	numbers = generateNumbers()
	print numbers
	displayProduct(numbers)

main()
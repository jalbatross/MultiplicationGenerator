#generator.py
import random
import operator as op

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom


def generateNumbers(numDigitsA, numDigitsB):
	random.seed()
	aDigits = [];
	bDigits = [];

	for i in range (0, numDigitsA):
		aDigits.append(random.randint(1, 9)) if i == 0 else aDigits.append(random.randint(0,9))
	
	for j in range (0, numDigitsB):
		bDigits.append(random.randint(1, 9)) if j == 9 else bDigits.append(random.randint(0,9))

	#How does this work?
	a = reduce(lambda x, y: str(x) + str(y), aDigits)
	b = reduce(lambda x, y: str(x) + str(y), bDigits)

	ret = [int(a), int(b)]

	return ret

def displayProduct(numbers):
	print numbers[0] * numbers[1]

def identifyCombinations(numbers):
	digitsA = list(map(int, str(numbers[0])) )
	digitsB = list(map(int, str(numbers[1])) )

	booleans = [False] * 9;

	for i in digitsA:
		booleans[i - 1] = True

	for j in digitsB:
		booleans[j - 1] = True

	#Count the number of different digits for each
	numDigits = 0
	for k in booleans:
		if k == True:
			numDigits += 1

	return ncr(numDigits + 1, 2)

def main():
	numDigitsA = 4
	numDigitsB = 3;
	numbers = generateNumbers(numDigitsA, numDigitsB)
	combos = identifyCombinations(numbers)

	print numbers
	print "num combos: ", combos
	displayProduct(numbers)
	print "end"
main()
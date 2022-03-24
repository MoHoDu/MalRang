def printNumTo100(num):
		if num <= 100:
				print(num)
				printNumTo100(num + 1)

printNumTo100(1)
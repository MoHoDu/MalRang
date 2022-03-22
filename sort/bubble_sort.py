numbers = [7, 3, 2, 9, 4]
for ibf in range(0, len(numbers) - 1) :
	for ib in range(ibf + 1, len(numbers)) :
		if numbers[ibf] > numbers[ib] :		
			temp = numbers[ibf]
			numbers[ibf] = numbers[ib]
			numbers[ib] = temp
	
		print(numbers)
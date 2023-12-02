import re

f = open("input.txt", "r")
lines = f.readlines()

pattern = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'

sum = 0

trad = {
		'one': '1',
		'two': '2',
		'three': '3',
		'four': '4',
		'five': '5',
		'six': '6',
		'seven': '7',
		'eight': '8',
		'nine': '9'
		}

for line in lines:
	numbers = re.findall(pattern, line)
	if numbers[0] in trad:
		num1 = trad[numbers[0]]
	else:
		num1 = numbers[0]
	if numbers[-1] in trad:
		num2 = trad[numbers[-1]]
	else:
		num2 = numbers[-1]
	number = int(num1+num2)
	sum += number

print(sum)

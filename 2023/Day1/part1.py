import re

f = open("input.txt", "r")
lines = f.readlines()

pattern = r'\d'

sum = 0

for line in lines:
	numbers = re.findall(pattern, line)
	number = int(numbers[0] +(numbers[-1]))
	sum += number

print(sum)

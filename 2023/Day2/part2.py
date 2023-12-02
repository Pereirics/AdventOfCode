import re

f = open("input.txt", "r")
lines = f.readlines()

pattern_set = r'\d+ (?:red|blue|green)(?:, \d+ (?:red|blue|green))*(?=;?)'
pattern_color = r'(\d+) (red|blue|green)'

val = {'red': 0,
	   'green': 0,
	   'blue': 0
	  }

sum = 0

for line in lines:
	m = re.findall(pattern_set, line)
	for match in m:
		color = re.findall(pattern_color, match)
		for col in color:
			if val[col[1]] < int(col[0]):
				val[col[1]] = int(col[0])
	sum_val = 1
	for k,v in val.items():
		sum_val *= v
		val[k] = 0
	sum += sum_val

print(sum)

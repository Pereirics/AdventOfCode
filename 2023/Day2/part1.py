import re

# 12 red 13 green 14 blue

f = open("input.txt", "r")
lines = f.readlines()

pattern_id = r'Game (\d+)'
pattern_set = r'\d+ (?:red|blue|green)(?:, \d+ (?:red|blue|green))*(?=;?)'
pattern_color = r'(\d+) (red|blue|green)'

val = {'red': 12,
	   'green': 13,
	   'blue': 14
	  }

sum = 0

for line in lines:
	m = re.match(pattern_id, line)
	id_num = int(m.group(1))
	m = re.findall(pattern_set, line)
	flag = 1
	for match in m:
		color = re.findall(pattern_color, match)
		for col in color:
			if val[col[1]] < int(col[0]):
				flag = 0
				break
	if flag:
		sum += id_num

print(sum)

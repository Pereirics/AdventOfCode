import re

f = open("input.txt", "r")
lines = f.readlines()

pattern = r'\d+'

sum = 0

for i in range(len(lines)):
	match =	re.finditer(pattern, lines[i])
	for m in match:
		start, end = m.span()
		#print(f"Match: {m.group(0)}, Coords: {start}, {end}")
		if start > 0 and lines[i][start-1] != '.' and not(lines[i][start-1].isdigit()) :
			sum += int(m.group(0))
		elif end < len(lines[i])-1 and lines[i][end] != '.' and not(lines[i][end].isdigit()):
			sum += int(m.group(0))
		else:
			for j in range(start-1, end+1):
				if i > 0 and j >= 0 and j < len(lines[i]) and lines[i-1][j] != '.' and not(lines[i-1][j].isdigit()):
					sum += int(m.group(0))
					break
				elif i < len(lines)-1 and j >= 0 and j < len(lines[i]) and lines[i+1][j] != '.' and not(lines[i+1][j].isdigit()):
					sum += int(m.group(0))
					break
print(sum)

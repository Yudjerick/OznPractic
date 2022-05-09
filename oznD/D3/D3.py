import re

s = input()

def replacer(match):
	return str(int(match.group())**3)

print(re.sub(r'\d+', replacer ,s))

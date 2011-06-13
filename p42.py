# Project Euler problem 42
# How many triangle words...?

triang = []

def val(word):
	val = 0
	for i in range(0, len(word)):
		val += ord(word[i])-ord('A')+1
	return val   

def build():
	for i in range(1,21):
		triang.append(i*(i+1)/2)
		
def solve():
	file = open("words.txt", "r")

	line_w = []
	for line in file: # just 1 line
		line_w = line.split(',') 
	
	list_w = []
	for el in line_w:
		list_w.append(el.strip('"'));

	count = 0	
	for word in list_w:
		if val(word) in triang:
			count += 1
	print count

if __name__=="__main__":
	build()
	solve()

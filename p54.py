# Project Euler problem 54

# How many hands does Player 1 win?

import time

values = ['A','2','3','4','5','6','7','8','9','T','J','Q','K','A']
suites = ['H', 'D', 'C', 'S']
res=["Royal Flush", "Straight Flush", "Four of a Kind", "Full House", "Flush",
	"Straight", "Three of a Kind", "Two Pairs", 
	"One PairA", "One PairK", "One PairQ", "One PairJ", "One PairT", 
	"One Pair9", "One Pair8", "One Pair7", "One Pair6", "One Pair5", 
	"One Pair4", "One Pair3", "One Pair2",
	"A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def eval_hand(h):
	# is royal flush?
	v = [el[0] for el in h]
	s = [el[1] for el in h]	

	v.sort()	
	if ((v == ['A', 'J', 'K', 'Q', 'T']) and (s[0] == s[1]) and 
		(s[1]==s[2]) and (s[2]==s[3]) and (s[3]==s[4])):
		return "Royal Flush"
	
	# is straight flush?
	for i in range(0,10):
		cnt = 0
		for el in values[i:i+5]:
			if el in v:
				cnt += 1
		if cnt==5:
			if ((s[0] == s[1]) and (s[1]==s[2]) and (s[2]==s[3]) and (s[3]==s[4])):
				return "Straight Flush"
	
	# is four of a kind?
	if (((v[0]==v[1]) and (v[1]==v[2]) and (v[2]==v[3])) or
		((v[1]==v[2]) and (v[2]==v[3]) and (v[3]==v[4]))):
		return "Four of a Kind"
	
	# is full house?
	if (((v[0]==v[1]) and (v[1]==v[2]) and (v[3]==v[4])) or 
		((v[0]==v[1]) and (v[2]==v[3]) and (v[3]==v[4]))):
		return "Full House"

	# is flush?
	if ((s[0] == s[1]) and (s[1]==s[2]) and (s[2]==s[3]) and (s[3]==s[4])):
		return "Flush"
	
	# is straight?
	for i in range(0,10):
		cnt = 0
		for el in values[i:i+5]:
			if el in v:
				cnt += 1
		if cnt==5:
			return "Straight"

	# is three of a kind?
	if (((v[0]==v[1]) and (v[1]==v[2])) or
		((v[1]==v[2]) and (v[2]==v[3])) or
		((v[2]==v[3]) and (v[3]==v[4]))) :
		return "Three of a Kind"
	# is two pairs?
	if(( (v[0]==v[1]) and (v[2]==v[3]) ) or 
		( (v[0]==v[1]) and (v[3]==v[4]) ) or 
		( (v[1]==v[2]) and (v[3]==v[4]) )):
		return "Two Pairs"

	# is one pair?
	if (v[0]==v[1]) or (v[1]==v[2]):
		return "One Pair"+str(v[1])
	
	if (v[2]==v[3]) or (v[3]==v[4]):
		return "One Pair"+str(v[3])

	# is high card
	for i in xrange(13,0,-1):
		if values[i] in v:
			return str(values[i])

	return "none"

def solve():
	file = open("poker.txt", "r")
	
	p1_win_cnt = 0
	p2_win_cnt = 0

	for line in file: 
		p1 = line.split()[:5]
		p2 = line.split()[5:]
		
		r1 = eval_hand(p1)
		r2 = eval_hand(p2)
		if (res.index(r1) < res.index(r2)):
			p1_win_cnt +=1
		if (res.index(r1) > res.index(r2)):
			p2_win_cnt +=1
		if (res.index(r1) == res.index(r2)):
			print p1, r1, "--", p2, r2

	print "p1 win: ", p1_win_cnt
	print "p2 win: ", p2_win_cnt

if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"

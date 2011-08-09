# Project Euler problem 61

# Find the sum of the only ordered set of six cyclic 4-digit numbers for which
# each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal,
# and octagonal, is represented by a different number in the set.

import time

def solve():
	l_tr = [i*(i+1)/2 for i in range(1,141)]
	l_sq = [i*i for i in range(1,99)]
	l_pt = [i*(3*i-1)/2 for i in range(1,82)]
	l_hx = [i*(2*i-1) for i in range(1,71)]
	l_hp = [i*(5*i-3)/2 for i in range(1,64)]
	l_oc = [i*(3*i-2) for i in range(1,59)]

	l_nr = []
	l_nr.extend(l_tr)
	l_nr.extend(l_sq)
	l_nr.extend(l_pt)
	l_nr.extend(l_hx)
	l_nr.extend(l_hp)
	l_nr.extend(l_oc)

	l_nr.sort()

	# remove elems <1000
	del l_nr[:160]

	# remove elems with 3rd digit 0
	while 1:
		found = 0
		for el in l_nr:
			if (el%100)<10:
				l_nr.remove(el)
				found = 1
		if found == 0:
			break	

	# how many next elems
	i = 0
	next_d = {}
	while i<len(l_nr):
		next_d[l_nr[i]] = []

		for j in range(0, len(l_nr)):
			if i == j:
				continue
			if l_nr[j]/100 == l_nr[i]%100:
				next_d[l_nr[i]].append(l_nr[j])
		i += 1
	
	comb = []
	for el1 in l_nr:
		if len(next_d[el1]) == 0 :
			continue
		for el2 in next_d[el1]:
			if len(next_d[el2]) == 0 :
				continue
			for el3 in next_d[el2]:
				if len(next_d[el3]) == 0 :
					continue
				for el4 in next_d[el3]:
					if len(next_d[el4]) == 0 :
						continue
					for el5 in next_d[el4]:
						if len(next_d[el5])==0:
							continue
						for el6 in next_d[el5]:
							comb.append([el1,el2,el3,el4,el5,el6])
	
	def check(cm):
		l_subl = []
		for el in cm:
			e = []
			if el in l_tr:
				e.append("tr")
			if el in l_sq:
				e.append("sq")
			if el in l_pt:
				e.append("pt")
			if el in l_hx:
				e.append("hx")
			if el in l_hp:
				e.append("hp")
			if el in l_oc:
				e.append("oc")

			l_subl.append(e)
		
		map_s = {"tr":2**0, "sq":2**1, "pt":2**2, "hx":2**3, "hp":2**4, "oc":2**5}

		ok = 0
		ss = []
		for s0 in l_subl[0]:
			for s1 in l_subl[1]:
				for s2 in l_subl[2]:
					for s3 in l_subl[3]:
						for s4 in l_subl[4]:
							for s5 in l_subl[5]:
								s = 0			
								s |= map_s[s0]
								s |= map_s[s1]
								s |= map_s[s2]
								s |= map_s[s3]
								s |= map_s[s4]
								s |= map_s[s5]

								if s == 63:
									ok = 1
									ss = [s0, s1, s2, s3, s4, s5]
		return (ok, ss)

	for c in comb:
		c6 = (c[4]%100)*100 + (c[0]/100) 
		if (c6 == c[5]) and check(c)[0] == 1:
			print c, sum(c), check(c)[1]
		
if __name__=="__main__":
	start = time.time()
	solve()
	print "Elapsed Time:", (time.time() - start), "sec"

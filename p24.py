# Project Euler problem 24
# What is the millionth lexicographic permutation of the digits 
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import itertools

if __name__ == "__main__":
    perm = itertools.permutations([0,1,2,3,4,5,6,7,8,9])
    print (list(perm))[1000000-1]
    
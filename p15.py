# Project Euler problem 15

# Any path has lengh 2n, and has n DOWN and n RIGHT instructions
# Number of all possible combinations: (2n!)/(n! * n!)

def factorial(n):
    f = 1
    while (n > 0):
        f = f * n
        n = n - 1
    return f

if __name__ == "__main__":
    rez = factorial(40)/(factorial(20)**2)

    print rez

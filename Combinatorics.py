import numpy


def comb(n ,r):
    if r is 0:
        return 1
    elif r is 1:
        return n
    elif n >= r:
        return (n*comb(n-1,r-1))/r
    elif n <= r:
        return 0


def perm(n, r):
    if r is 0:
        return 1
    elif r is 1:
        return n
    else:
        return fact(r)*comb(n, r)


def fact(n):
    if n is 1:
        return 1
    elif n is 0:
        return 1
    else:
        return n*fact(n-1)


what = str(input("Enter a character   "))
if what is "c":
    n = int(input("Enter n   "))
    print('\n')
    r = int(input('Enter r   '))
    print (int(comb(n , r))
if what is "p":
    n = int(input("Enter n   "))
    r = int(input("\nEnter r   "))
    print(perm(n , r))

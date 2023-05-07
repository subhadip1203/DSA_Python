
from re import X


def printNtoOne(n):

    # do something
    print(n)

    # break recursion
    if n>1:
        printNtoOne(n-1)

num = 5
printNtoOne(num)
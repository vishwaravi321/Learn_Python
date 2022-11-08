'''
Task:
Given an integer,n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird'''


n = int(input().strip())

def ttf():
    for i in range(2, 6):
        if n != i :
            pass
        else:
            print("Not Weird")

def stt():
    for i in range(6,21):
        if n != i:
            pass
        else:
            print("Weird")


def condi():
    if n < 5 :
        ttf()
    else:
        stt()

if n % 2 == 1 :
    print("Weird")
else:
    if n > 20 :
        print("Not Weird")
    else:
        condi()

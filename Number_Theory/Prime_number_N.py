from math import sqrt

def isPrime(N):
    for i in range(2, int(sqrt(N))):
        if N % i == 0:
            return False
    return True

if __name__ == "__main__":

    n = int(input())
    ans = isPrime(n)

    if ans :
        print("Prime Numer")
    else:
        print("Non Prime Number")
# Print all Divisors of a given Number
# Time Complexity O(sqrt(n))

def printDivisors(n):
    print("The Divisors of ",n,"are")
    for i in range(1, int(n**0.5)+1):
        if n % i ==0:
            print(i, end=" ")
            if i != n/i:
                print(int(n/i), end=" ")
    print()

if __name__=="__main__":
    n = int(input())
    printDivisors(n)

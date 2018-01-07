# Find factorial of the number
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

n=int(input("Enter a number : "))
print("Factorial of number is",fact(n))


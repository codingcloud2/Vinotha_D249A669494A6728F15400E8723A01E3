def findFact(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f

print("Enter a Number: ", end="")
try:
    num = int(input())
    fact = findFact(num)
    print("\nFactorial of", num, "=", fact)
except ValueError:
    print("\nInvalid Input!")

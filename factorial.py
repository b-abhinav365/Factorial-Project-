import sys

if len(sys.argv) > 1:
    num = int(sys.argv[1])
else:
    num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
    sys.exit(1)

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial of", num, "is", fact)

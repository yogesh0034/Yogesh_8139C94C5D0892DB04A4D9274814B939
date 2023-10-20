# 1. Implement a recursive function to calculate the factorial of a given number.


def fact(m):
  if m <= 1:
    return 1
  else:
    return m * fact(m - 1)


n = int(input("Enter the value of n:"))
print("The factorial of", n, "is", fact(n))

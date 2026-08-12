# A function calling itself to solve a problem 
def factorial(n):
    if(n == 0 or n == 1):
        return n
    return factorial(n-2) + factorial(n-1)
print(factorial(6))
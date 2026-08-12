# Function help in reusability and modularity in python
def average(a,b,c):
    d = (a + b + c)/3.0
    print(d)
average(3,5,1)

def greet(name):
    return f"Hello, {name}"
print(greet("Alece"))   # output: Hello Alice!


def add(a,b):
    d = (a + b)
    return d
print(f" This is the sum of :  {add(10,21)}")
def add(a, b):  # this is positional argumanets 
    return a + b 
c = add(3,5)   # arguments 
print(c)

# default arguments 
def add(a, b , plus = 0):
    return a + b + plus
c = add(3,5,2)  # output: 10 decause it overight the default value 
print(c)


## what are key word agrements 
def add(a, b, plus=0):
    x = a + b + plus
    return x 

c = add(3,5,4)
print(c)

c1 = add(a=3, b=5)
print(c1)
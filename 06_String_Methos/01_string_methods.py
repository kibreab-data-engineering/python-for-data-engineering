s = "hello world"
a = len(s)
print(a)
print(s.upper())
print(s.lower())
print(s.capitalize())  # Capitalize the first letter 
print(s.title())
print("-------------------------------------------------")
#Removing WhiteSpace
text = "   hello world    "
print(text)      # orgona; as is
print(text.strip())  # removing all the spaces 
print(text.lstrip()) # removinf left spaces 
print(text.rstrip())  # remoing right spaces 


# Finding and Replacing 
text = "python is fun"
print(text.find("is"))  # output: 7 
print(text.replace("fun", "awesome"))  # Output is awesome

# splitting and joining 
text = "apple,banana,orange"
fruit = text.split(",")
print(fruit)   # output: ['apple', 'banana', 'orange']


# 
text = "Python1233"
print(text.isalpha())  # is all the character is alphabet
print(text.isdigit())  # is digit 
print(text.isalnum())  # is all number  number and alphanet
print(text.isspace())  # is space


# Test 
# Modify the variables below to match the expected output

greeting = "Hi"
language = "Java"
status = "bad"

print(F"{greeting.replace("Hi","Hello")}, Python Learner")
print(f'I am "{status.replace("bad","good")}"')

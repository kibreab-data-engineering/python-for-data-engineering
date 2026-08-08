# create a string variable name with your full name The first charactor, last charactor and length of the string. 
name = "John"
print(name[0])
print(name[3])
print(len(name))

# concteniate two string "Hello" and "world" with a space in between:
a = "Hello"
b = "World"
print(f"{a} {b}")

# String slicing and indexing 
text = "Python programming"
print(text[0:6])  # first six charactor
print(text[-6:])  # last six character

# Reverse the entire text 
text = "Python Programing"
print(text[::-1])  # this will revers the string 

# String Methods and Functions
text = "      I Love Python programing   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())
print(text.count("o"))

# Checked string "123abc"
text = "123abc"
print(text.isalpha())  
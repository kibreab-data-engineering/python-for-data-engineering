name = "Harry"

# name = "H  a  r  r  y"
#         0  1  2  3  4
#        -5 -4 -3 -2 -1
print(name[4]) # is a last charactor
print(name[-1]) # is a last charactor

# Get one item 
fruit = ["apple", "banana", "orange", "mango","grape"]
print(fruit[-3])

# first and Last 
numbers = [10,20,30,40,50]
print(f"First {numbers[0]}")
print(f"Last {numbers[4]}")

# Get a charactor 
name = "python"
print(name[0])
print(name[5])
print(name[2])

# change an item
cities = ["New York", "Boston","Chicago", "Dallas"]
cities[1]="Miami"
print(cities)

# Mini Challenge
numbers = [5,10,15,20,25,30]
print(f"First  number: {numbers[0]}")
print(f"Third  number: {numbers[2]}")
print(f"Last   number: {numbers[5]}")
print(f"Second from number: {numbers[-2]}")

# For loop Manually access each items 
a = [10,20,30,40]
for number in a :  #   number --> takes each item one at a time
    print(number)

# You can also add in a loop 
cities = ["New York", "Boston", "Chicago","Dallas"]
for i in range(len(cities)):
    print(cities[i])

# For even number example 
numbers = [4,10,13,18,21]
for number in numbers:
    if number % 2 == 0:
        print(number)

# Combine for + of + Counter

numbers = [4,10,13,18,21]
count= 0 
for number in numbers:
    if number % 2 == 0:
        count += 1
print(f"There are {count} even numbers")

# Combine for + of + Counter

numbers = [4,10,13,18,21]
count= 0 
for number in numbers:
    if number % 2 != 0:
        count += 1
print(f"There are {count} odd numbers")


# Print every nummber, even, count the even number 
numbers = [5,8,12,7,15,20,22]
for number in numbers:
    print(number)
print("---------------------------------------")
numbers = [5,8,12,7,15,20,22]
for number in numbers:
    if number % 2 == 0:
        print(number)
print("---------------------------------------")
numbers = [5,8,12,7,15,20,22]
count = 0
count_odd=0
for number in numbers:
    if number % 2 == 0:
        count += 1
print(f" There are {count} even numbers in the list")
print("------------------------------------------")
for number in numbers:
    if number % 2 != 0:
        count_odd += 1 
print(f"There are {count_odd} odd numbers in the list")

# # for i in range(1, 6): # range function goes from 1 to (6-1) ie 5 in this case
# #     print(i)

# for i in range(1, 11):
#     print("5 X", i, "=",  5*i)

# #Practice Employee salary 
# salaries = [4200,5100,3900,6000,4700]
# for i in range(len(salaries)):
#     print(f"Employee {i + 1} : ${salaries[i]}")

# #practice Study grade analyzer 
# grades = [88,92,76,64,99,81]
# for i in range(len(grades)):
#     print(f"Student {i + 1}r : ${grades[i]}")

#Practice prind student name:
# students = ["John", "Mary", "David", "Sara","Mike"]
# for i in range(len(students)):
#     print(f"Student  {i + 1} : $ {students[i]}" )

# #pratice items 
# prices = [15,30,45,60,75]
# for i in range(len(prices)):
#     print(f"Itmes {i+1} : $ {prices[i]}")

# Shopping Receipt
# items = ["Apple","Milk","Bread"]
# prices = [2,4,3]
# for i in range(len(items)):
#     print(f"{items[i]} - $ {prices[i]}")

# print only even number
# for i in range(1,21):
#    if i % 2 == 0:
#     print(i)

# the same as above 
# for i in range(2,21,2):
#     print(i)
# print("------------------------------")
# # Count Down
# for number in range(10,0,-1):
#     print(number)

# Sum numbers 
# total = 0 
# for number in range(1,101):
#     total += number
#     print(total)

# multiplication 

# number = int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{number} X {i} = {number * i}")

# Bonas challenge 

# numbers = [12, 7, 25, 18, 9]

# Using a for loop:

# Print each number.
# Print whether it is Even or Odd.
# Count how many even numbers there are.
# Print the total at the end.
# print("--- Below is for even number --- ")
# numbers = [12, 7, 25, 18, 9]
# for numbers in numbers:
#     if numbers % 2 == 0:
#         print(f" {numbers} is even") 
# print("---below is for odd number ---- ")
# numbers = [12, 7, 25, 18, 9]
# for numbers in numbers:
#     if numbers % 2 != 0:
#         print(f"{numbers} is odd ") 

# find number greater than 20 
# numbers = [12, 25, 8, 41, 19, 30]
# for numbers in numbers:
#     if numbers >= 20:
#         print(f" number bove 20 : {numbers}")

# count even number 
numbers = [4, 10, 13, 18, 21]
even_count = 0
odd_count = 0
for number in numbers:
    if number % 2 == 0:   
        even_count += 1
    else:
        odd_count +=1
print(f"There are {even_count} even numbers.")
print(f"There are {odd_count} odd numbers.")



# Create a program that checks if a person is eligible to vote (age >=18)
'''
from datetime import date
today = date.today().year
year = int(input(" What year were you born: "))
age = today- year
if age > 18:
    print(f"You are eligible to vote since you are {age} your old")
elif age < 17:
    print(f"You have to be over 18 to vote you are {age} your old")
elif  age < 10:
    print("You are a very young perhaphs child: ")
elif age > 60:
    print("You can't vote: ")
'''
# wite a program that ask the user for a nmber from the user print "Even" if it is even otherwise odd 
'''
a = int(input("Enter a Number: "))
if a % 2 == 0:
    print(f"{a} : is an even number: ")
if a % 2 != 0:
    print(f"{a} is an odd number: ")
elif a <= 0:
    print(f"Please enter a whole number: ")
    '''

# Ask a user to enter a dat number (1-7) and print the corresponding dat of the week using match case 
'''
num = int(input("Enter a number: "))
match num:
    case 1:
        print(f"{num} is Monday")
    case 2:
        print(f"{num} is tuesday:")
    case 3:
        print(f"{num} is Wednesday: ")
    case 4: 
        print(f"{num} is Thurday: ")
    case 5:
        print(f"{num} is Friday: ")
    case 6:
        print(f"{num} is Saturrday: ")
    case 7: 
        print(f"{num} is Sunday")
    case _:
        print("Please add number between 1-7 : ")
'''
'''
# Write a program using match case that simulates a simple calculator 
# ask the user for two number and an operation (+,-,*,/)
num1 = int(input("Please enter fist number: "))
num2 = int(input("Please enter second number: "))
operation = input("Please enter an oprations: ")
match operation:
    case "+":
        print(f"{num1} + {num2 } = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2 } = {num1 - num2}")
    case "*":
        print(f"{num1} X {num2 } = {num1 * num2}")
    case "/":
        print(f"{num1} / {num2 } = {num1 / num2}")
    case _:
        print(f"Please enter a valid operator: ")
'''
'''
# Print numbers from 1 to 10 using a for loop.
for i in range (1,11):
    print(i)
'''
'''
# Print the multiplication table of a number ( entered by user)
a = int(input("Please enter a number to be multiplied: "))
for i in range (1,10):
    print(f"{a} x {i} = {i * a}")
'''
'''
# Calculate the sum of all numbers from 1 to 100 using a for loop.
a = int(input("Please enter a number: "))
for i in range (1,101):
    print(f"{a} X {i} = {a + i} ")
'''
'''
# Print numbers from 1 to 10 using a while loop.
sum = 0 
i = 1
while i<5:
    print(i)
    sum +=i
'''
'''
password = "Y2k123"
entered_pass = input("Enter Password:  ")
while (entered_pass != password):
    entered_pass = input("Wrong Password! Try again and enter Password: ")
    print("Success! You are logged in  ")
'''

# Use a for loop to print numbers from 1 to 10 but stop the loop if the number is 7 (use break)
'''
for i in range(1,10):
    if(i == 7):
        break
    print(i)

'''

# print numbers from 1 to 10, skipping the number 5 ( use continue)
for i in range(1,10):
        if(i == 5):
             continue
        print(i)

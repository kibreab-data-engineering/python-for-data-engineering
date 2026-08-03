# Personal information 
name = input("Fist Name\n")
last_name = input( "Last Name\n")
age = 35
city = "Asmara"

print(f'----------- Profite------------------\n{'Name' : <10}: {name} {last_name}\n{'Age' :<10}: {age}\n{'City' : <10}: {city}\n{'-------------------------------------'}')

# Increase salary by 10%
name = input("Employee Name\n")
current = float(input("Enter current salary\n"))
new_salary = current * 1.10
raises = new_salary - current

# print(f"{'Employee' :15}: {name}\n{'Current Salary' :15}: ${current}\n{'New Salary' :<15} : ${new_salary}\
#       \n{'Raise (10%)' :15} : {raises}")


# Ask use for shopping total 
# product = input("Enter Product Name : \n")
# price = float(input("Enter full price : \n"))
# quantity = int(input ("Enter a quantity : \n"))
# print(f"{'Product':<15}: {product}\n{'Qty' :<15} : {quantity}\n{'Total':<15}: ${price * quantity}")

#Average Score 
# math = float(input("Math Score\n"))
# science = float(input("Science Score\n"))
# english = float(input("English Score\n"))
# average = (math + science + english )/ 3

# # print(f"{'Math' :<15}:{math}\n{'Science' :<15}:{science}\n{'English' :<15}:{english}\n{'Average ':<15}:{average:.sf}")
# print(
#     f"{'Math':<15}:{math:.2f}\n"
#     f"{'Science':<15}:{science:.2f}\n"
#     f"{'English':<15}:{english:.2f}\n"
#     f"{'Average':<15}:{average:.2f}"
# )

# name = input( "What is your name\n")
# age = int(input("What you were you born\n"))
# currnt = int(input("What is your current year\n"))

# print(f"{'Hello '}{name}{'You are'} {currnt-age} {"and you are young"}")

# BMI Calculator 
# weight = float(input("What is you weight in (Kg)\n"))
# height = float(input("What is your height(meets)\n"))
# bmi = weight/(height ** 2)
# print(f"{'Weight':<15}:{weight}\n{'Height':<15}:{height}\n{'Your BMI is':<15}:{bmi:.2f}")

#operators
# number = int(input("Enter a number\n"))
# print(f"{'The square root of ':<15}{number}{' Is '}{number ** 2}\
#       \n{'The Cube root of ':<15}{number}{' is '}{number ** 3}")

# total_seconds = 7384

# hours = total_seconds // 3600
# minutes = (total_seconds % 3600) // 60
# seconds = total_seconds % 60

# print(f"{hours} hours")
# print(f"{minutes} minutes")
# print(f"{seconds} seconds")

# # Tip calculator 
# # bill = float(input("How much is total bill\n"))
# # tip = float(input("How do you want 10%, 20% tip\n"))
# # print(f"{'Bill':<15}:{bill}\n{'Tip':<15}:{bill * tip:.2f}\n{'Total':<15}:{(bill * tip)+bill}")

# # Discount Calculation 
# price = float(input("Total price: "))
# discount = float(input("How much is current discount (%): "))

# discount_amount = price * (discount / 100)
# final_price = price - discount_amount

# print(
#     f"{'Price':<15}: ${price:.2f}\n"
#     f"{'Discount':<15}: ${discount_amount:.2f} ({discount:.0f}%)\n"
#     f"{'Final Price':<15}: ${final_price:.2f}"
#     )


#a = input("enter a number ")
#print(a + " is the number you entered")

#b = input("enter your name ")
#print("Hello " + b + "!")

### 
# a = input("enter first number ")
# b = input("enter second number ")
# print("The sum of " + a + " and " + b + " is " + str(int(a) + int(b)))
# a = int(input("Enter a number between 1 and 10: "))

# match a:
#     case 1:
#         print("You won a charger")
#     case 3:
#         print("You won $3")
#     case 6:
#         print("You won a camera")
#     case _:
#         print("Better luck nect time")

# a = int(input("Enter a number between 1-7: "))

# match a:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Enter a valid number between 1 and 7")


#calculator
# a = int(input("Enter first number: "))
# operation = input("Enter operation: ")
# b = int(input("Enter second number: "))
# match operation:
#     case "+":
#         print(f"Result: {a + b}")
#     case "-":
#         print(f"Result: {a - b}")
#     case "*":
#         print(f"Result: {a * b}")
#     case "/":
#         if b == 0:
#             print("You cannot divide by zero")
#         else:
#             print(f"Result: {a/b}")
#     case _:
#         print("Invalid operator")

# grade
# a = input("Enter your letter grade: ")
# match a:
#     case "A":
#         print("Excellent: ")
#     case "B":
#         print("Good: ")
#     case "C":
#         print("Average: ")
#     case "D":
#         print("Need Improvment: ")
#     case "F":
#         print("Failed: ")
#     case _:
#         print("Invalid Entry: ")

# # Traffic Light 
# a = input("Traffic light: ")
# match a:
#     case "Red":
#         print(f"{a} --> Stop")
#     case "Yellow":
#         print(f"{a} --> Slow Down")
#     case "Green":
#         print(f"{a} --> Go")
#     case _:
#         print("Unknown signal")

# Simple menu
a = int(input("Enter menu: "))
match a:
    case 1:
        print(f"{a} --> Opening profile....")
    case 2:
        print(f"{a} --> Openong Settings...")
    case 3:
        print(f"{a} --> Logginh out     ...")
    case _:
        print("Invalid choice")
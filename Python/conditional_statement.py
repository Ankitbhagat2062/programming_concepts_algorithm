#  1. Write a program to check whether the given number is in between 1 and 100 or not.
number=50
if number>1 and number<100:
    print("The number is between 1 and 100.")
else:
    print("The number is not between 1 and 100.")


#      2. Check whether the user input number is even or odd and 
#       display it to user.
user_input = int(input("Enter a number: "))
if user_input % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#     3. Write a program that asks the user for a number 
#           in the range of 1 to 12. 
#        The program should display the corresponding month, where 
#        1=january, 2=february,3=march,4=april,5=may,6=june,7=july, 
#        8=august,9=september,10=october,11=november,12=december. The program should display an error 
#        message if the user enters a number that is outside the range of 1 to 12.
user_number = int(input("Enter a number between 1 and 12: "))
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
print(f'Your month is {months.get(user_number, "Error: Number is outside the range of 1 to 12.")}')



#        4. A school has following rules for grading system:
#         a. Below 25 - F
#         b. 25 to 45 - E
#         c. 45 to 50 - D
#         d. 50 to 60 - C
#         e. 60 to 80 - B
#         f. Above 80 - A
#         Ask user to enter marks and print the corresponding grade.
user_marks = int(input("Enter your marks: "))
if user_marks < 25:
    print("Grade: F")
elif 25 <= user_marks < 45:
    print("Grade: E")
elif 45 <= user_marks < 50:
    print("Grade: D")
elif 50 <= user_marks < 60:
    print("Grade: C")
elif 60 <= user_marks < 80:
    print("Grade: B")
else:
    print("Grade: A")


#         5. Write a program to check whether a number is divisible by 
#         7 or not.
number_to_check = int(input("Enter a number: "))
if number_to_check % 7 == 0:
    print(f"{number_to_check} is divisible by 7.")
else:
    print(f"{number_to_check} is not divisible by 7.")



#         6. Write a program to accept two numbers and mathematical operators and 
#         perform operation accordingly.
#             Like:
#             Enter First Number: 7
#             Enter Second Number : 9
#             Enter operator : +
#             Your Answer is : 16
first_number = float(input("Enter First Number: "))
second_number = float(input("Enter Second Number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    result = first_number / second_number

print(f"Your Answer is : {result}")


#          7. Write a Python program to check car loan eligibility:
#             Salary >= 50,000 and Credit Score >= 700: "Eligible"
#             Otherwise: "Not Eligible"
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))
if salary >= 50000 and credit_score >= 700:
    print("Eligible for car loan.")
else:
    print("Not eligible for car loan.")

#         8. Write a Python program that takes an integer input n n. 
#         From given number, 
#         check if it is divisible by both 3 and 5, and print "FizzBuzz" 
#         if true. 
#         If the number is divisible only by 5, print "Buzz." If it is 
#         divisible only by 3, print "Fizz." 
#         Finally, if the number is not divisible by either 3 or 5, 
#         print the number itself.
num1 = int(input("Enter an integer: "))
if num1 % 3 == 0 and num1 % 5 == 0:
    print("FizzBuzz")
elif num1 % 5 == 0:
    print("Buzz")
elif num1 % 3 == 0:
    print("Fizz")
else:
    print(num1)


# 9. Write a Python program that takes a character input and 
# checks whether it is a vowel or consonant.
char = input("Enter a character: ").lower()
if char in 'aeiou':
    print(f"{char} is a vowel.")    
else:
    print(f"{char} is a consonant.")


# 10. Write a Python program to input marks and determine the grade based on the following conditions:
# 90-100: A
# 80-89: B
# 70-79: C
# Below 70: Fail
marks = int(input("Enter your marks: "))
if 90 <= marks <= 100:  
    print("Grade: A")
elif 80 <= marks < 90:
    print("Grade: B")
elif 70 <= marks < 80:
    print("Grade: C")
else:
    print("Fail")



# 11. Write a Python program to categorize a person’s age:
# Age < 13: Child
# 13 <= Age <= 19: Teenager
# Age > 19: Adult
age = int(input("Enter your age: "))
if age < 13:
    print("You are a Child.")
elif 13 <= age <= 19:
    print("You are a Teenager.")
else:
    print("You are an Adult.")


# 12.Write a Python program to check if a given character is uppercase, lowercase, or a digit.
given_char=input("Enter a character: ")
if given_char.isupper():
    print(f"{given_char} is an uppercase letter.")
elif given_char.islower():
    print(f"{given_char} is a lowercase letter.")
elif given_char.isdigit():
    print(f"{given_char} is a digit.")



# 13. Write a Python program that takes a color as input ("Red", "Yellow", "Green") and 
# outputs the corresponding action ("Stop", "Get Ready", "Go").
color=input("Enter a traffic light color (Red, Yellow, Green): ").lower()
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get Ready")
elif color == "green":
    print("Go")


# 14. Write a Python program to check eligibility for a job based on age and experience:
# Age > 18 and Experience >= 2 years: Eligible
# Otherwise: Not Eligible
your_age = int(input("Enter your age: "))
your_experience = int(input("Enter your years of experience: "))
if your_age > 18 and your_experience >= 2:
    print("You are eligible for the job.")
else:
    print("You are not eligible for the job.")



# 15. Write a Python program to give advice based on the temperature:
# Temperature > 30°C: "It's hot, stay hydrated!"
# Temperature between 15-30°C: "Enjoy the weather!"
# Temperature < 15°C: "It's cold, wear warm clothes!"
temperature = float(input("Enter the temperature in °C: "))
if temperature > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temperature <= 30:
    print("Enjoy the weather!")
else:
    print("It's cold, wear warm clothes!")



# 16. Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:
# Pizza: $10
# Burger: $7
# Pasta: $8

menu_option = input("Enter a menu option (Pizza, Burger, Pasta): ").lower()
if menu_option == "pizza":
    print("Price: $10")
elif menu_option == "burger":
    print("Price: $7")
elif menu_option == "pasta":
    print("Price: $8")
else:
    print("Invalid menu option.")


# 17. Write a Python program to select players based on height:
# Height >= 6 feet: Selected
# Height < 6 feet: Not Selected
height = float(input("Enter your height in feet: "))
if height >= 6:
    print("You are selected.")
else:
    print("You are not selected.")



# 18. Write a Python program to check if a person is eligible to watch a movie based on their age:
# Age >= 18: Allowed
# Age < 18: Not Allowed
age_crit = int(input("Enter your age: "))
if age_crit >= 18:
    print("You are allowed to watch the movie.")
else:
    print("You are not allowed to watch the movie.")


# 19. Write a Python program to check login credentials:
# Username: "admin", Password: "password123"
# If correct, print "Access Granted"; otherwise, print "Access Denied."
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password123":
    print("Access Granted")
else:
    print("Access Denied")


# 20. Write a Python program that takes a month number (1–12) and outputs the corresponding season:
# 12, 1, 2: "Winter"
# 3, 4, 5: "Spring"
# 6, 7, 8: "Summer"
# 9, 10, 11: "Autumn"

month = int(input("Enter a month number (1-12): "))
if month in [12, 1, 2]:
    print("Season: Winter")
elif month in [3, 4, 5]:
    print("Season: Spring")
elif month in [6, 7, 8]:
    print("Season: Summer")
elif month in [9, 10, 11]:
    print("Season: Autumn")
else:
    print("Invalid month number.")

# Create an signup form . First and lastname must be in alphabet and cannot . Email must contain @ and . . Force user to enter email again . Password msut be greater than 8 character.

first_name=input('Enter Your first name')
last_name=input('Enter Your first name')
form_email=input('Enter your email')
remail=input('Enter email again')
form_password = input('Enter your password')
if not first_name.isalpha() and first_name == '':
    print('You must enter your name in alphabet')
elif not last_name.isalpha() and not last_name != '':
    print('You must enter your name in alphabet')
elif not '@' in form_email and not '.' in form_email:
    print('Invalid email')
elif not remail== form_email:
    print('Email must match with email')
elif len(form_password) < 8:
    print('Pass word must be atleast 8 character')
else:
    print(f'Welcome ${first_name} ${last_name} . Your email is ${form_email}')

# Q1. A theme park has these rules. You can ride the roller coaster if you are at least 12 years old AND at least 140 cm tall.
#  Write the if-else code for this
if age >= 12 and height >= 140:
    print("You can ride the roller coaster.")
else:
    print("You do not meet the requirements.")


# Q2. Design a Traffic Light System. Given a variable light that can be "red", "yellow", or "green", print the correct 
# instruction. Also handle an invalid color with an error message
light = "green"  # Example input

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Slow down")
elif light == "green":
    print("Go")
else:
    print("Error: Invalid color")

# Q3. Write a match statement that takes a number 1-4 and prints the corresponding season: 1=spring, 2=summer, 3-autumn, 
# 4-winter. Default "unknown"
month_num = 2  # Example input

match month_num:
    case 1: print("spring")
    case 2: print("summer")
    case 3: print("autumn")
    case 4: print("winter")
    case _: print("unknown")

# Q4 Write a login system using nested if Check
# If username equals "admin"
# Inside that, if password equals "pass123"
# Print appropriate messages for valid login, wrong password, wrong username
username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "pass123":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# Q5 Design a Bank Loan Approval System. Approve a loan only if ALL three conditions are met
# Age is between 21 and 60 (inclusive)
# Monthly income is at least 30,000
# Credit score is at least 700
# If not approved, print which condition failed. If multiple fail, pick the most important one to report
income = float(input("Enter your monthly income: "))
age = int(input("Enter your age: "))
credit_score = int(input("Enter your credit score: "))
if not (21 <= age <= 60):
    print("Loan Denied: Age must be between 21 and 60.")
elif income < 30000:
    print("Loan Denied: Monthly income too low.")
elif credit_score < 700:
    print("Loan Denied: Credit score too low.")
else:
    print("Loan Approved!")

# Q6. You are developing a simple ticket booking system for a movie theatre. The ticket price depends on the age of the person 
# and whether they have a membership card. If the person is under 12 the ticket is free. If the person is between 12 and 60: 
# If they have a membership card, the ticket costs $150. If they do not have a membership card, the ticket costs $200. 
# If the person is over 60, the ticket costs $100 regardless of membership as senior citizenship discount. Write the nested if-else 
# code to determine the ticket price based on user input for age and membership status.
age = int(input("Enter your age: "))
has_membership = input("Do you have a membership? (yes/no): ").lower()
if age < 12:
    price = 0
elif 12 <= age <= 60:
    if has_membership:
        price = 150  # Example discounted price
    else:
        price = 200  # Example standard price
else:
    price = 100  # Example senior price
print(f"The ticket price is ${price}.")

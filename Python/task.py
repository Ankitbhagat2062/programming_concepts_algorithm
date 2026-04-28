
# a='Expression'
# print(a[::2]) # Epeso
# print(a[:]); # Expression
# print(a[-2:3:-1]) # oisse
# print(a[-3:4]) # 
# print(a[-3:-4:-1]) # i
# print(a[-3:7:-2]) # 
# print(a[1:-8]) # x
# print(a[9::-10]) # n
# print(a[9:-10:-1]) # noisserpx
# print(a[11::-6]) # nr
# print(a[2:-15:-1]) #pxEii9k
# print(a[-15::-2])# 
# print(a[7:-1]) # io
# print(a[-1:0:]) # 
# print(a[:-1:]) # Expressio
# print(a[::-1]) # noisserpxE
# print(a[-1:7]) # 
# print(a[:-3:]) # Express
# print(a[-1:0]) #

# programming_language = 'python programming'
# print(programming_language[6])
# print(programming_language[-12])
# print(programming_language[0])
# print(programming_language[-1])
# print(programming_language[9])
# print(programming_language[::1])
# print(programming_language[::-1])
# print(programming_language[7:])
# print(programming_language[:6])
# print(programming_language[-11:])
# print(programming_language[0:18:2])
# print(programming_language[1:18:3])
# print(programming_language[-18::4])
# print(programming_language[::5])
# print(programming_language[::-3])
# print(programming_language[2:15])
# print(programming_language[-16:-3])
# print(programming_language[7:18])
# print(programming_language[:10:-1])
# print(programming_language[-1:-10:-2])
# print(programming_language[::2])
# print(programming_language[1::2])
# print(programming_language[3:18:4])
# print(programming_language[-15:18:3])
# print(programming_language[-1::-1])
# print(programming_language[0:6])
# print(programming_language[7:18])
# print(programming_language[-18:-12])
# print(programming_language[-11:])
# print(programming_language[6:7])
# print(programming_language[:])
# print(programming_language[::])
# print(programming_language[0:18:1])
# print(programming_language[-18:18])
# print(programming_language[5:-5])
# print(programming_language[-10:-1])
# print(programming_language[-1:-19:-1])
# print(programming_language[17::-1])
# print(programming_language[:0:-1])
# print(programming_language[10:0:-2])
# print(programming_language[0:18:3])
# print(programming_language[1:18:4])
# print(programming_language[-17:-1:2])
# print(programming_language[-18:0:2])
# print(programming_language[::7])

# data="program"

# print(data.append('m'))
# default step = 1
# default start = 0
# default end = len(string)

phone_num = '+9779+84+5821'

final_phone_num = ''
seen_plus = False
for ch in phone_num:
    if ch == '+':
        if not seen_plus:
            final_phone_num += ch
            seen_plus = True
    else:
        final_phone_num += ch

# print('Final phone number:', final_phone_num)

# price = '$123.45'
# print(price.replace('$', ''))  # '123.45'

# pl='python'
# print(pl.replace('p', 'P').replace('n', 'N'))  # 'PythoN'

# maketrans and translate
# new_pl = pl.maketrans('pn', 'PN')
# print(pl.translate(new_pl))  # 'PythoN'
# print(new_pl)  # {112: 80, 110: 78}

# ord and chr
# print(ord('a'))  # 97
# print(chr(97))   # 'a'

# id="STUDENT ID CARD"
# name="STUDENT NAME"
# s_name=input('Enter your name: ')
# age_var='AGE'
# age=int(input('Enter your age: '))
# coll_var='COLLEGE NAME'
# coll_name=input('Enter your college name: ')
# blood_group_var='BLOOD GROUP'
# blood_group=input('Enter your blood group: ')
# print(id.center(60))
# print(f'{name.center(30)}: {s_name}')
# print(f'{age_var.center(22, " ")}{" "*8}: {str(age)}')
# print(f'{coll_var.center(30)}: {coll_name}')
# print(f'{blood_group_var.center(30)}: {blood_group}')

# find and index and rfind and rindex
text = "programming. python"
# print(text.find('p'))  # 3
# print(text.index('p'))  # 3
# print(text.rfind('p'))  # 3
# print(text.rindex('p'))  # 3

# print(text.find('p') - len(text))  # negative index of p

number = '\t123 456'
# print(number.isdigit())  # True
# print(number.isalpha())  # False
# print(number.isalnum())  # True
# print(number.isdecimal())  # True
# print(number.isnumeric())  # True
# print(number.isprintable())  # True
# print(number.isspace())  # False
a=10
b=20
# print(f'{10*b}')
# print('{}{c}{}'.format(b,c=10,a))// error
# print('{0} {1} {c}'.format(b,a,c=10))
# print('{}{}'.format('Hello ', 'World'))

# name=input('Enter your name: ')
# print(f'{name.replace(' ','_')}')
# s_name=name.split()
# print(('_').join(s_name))

# f_name='Ram'
# m_name='Bahadur'
# l_name='KC'
# print(f_name,m_name,l_name,sep='_')

# title capitalize
# full_name='ram bahadur kc'
# print(full_name.title())
# print(full_name.capitalize())

# Bitwise NOT (~) operation:
# a = -19
# In binary (two's complement 32-bit): -19 = 11111111111111111111111111101101
# Bitwise NOT flips all bits:         ~-19 = 00000000000000000000000000010010
# Result in decimal: 18
# Formula: ~a = -(a + 1)
# Calculation: ~(-19) = -(-19 + 1) = -(-18) = 18

# A customer buys 3 items at Rs 111.33 each .The store offers 10% discount on total purchase .
#  Write a Python program that calulates and displays the subtotal discount and find totalt price after the discount
#  is applied . Format all amounts in 2 decimal places .
# item=111.33
# discount_percent =10
# Total_SP=item*3
# discount=discount_percent/100*Total_SP
# Total_Price=Total_SP-discount

# print(f'Discount of {discount:.2f} is applied on Total Price of {Total_Price:.2f}')

# A hotel charges Rs1200.08 per night and a traveller stays for 7 nights and gets an 18% discount on the total day .
# Write a python program that calculates and displays the totalstay cost , discount amount , and final amount to be paid after
#  discount .Format all amounts in 2 decimal places .

one_night_charge=1200.08
totaldays=7
discount_percent=18

Total_Stay_Cost=one_night_charge*totaldays

discount_amount=discount_percent/100*Total_Stay_Cost
final_amount=Total_Stay_Cost-discount_amount 
# print(2 and 3 or 2 and 4)  # (2 & 3) = 2 (binary 10 & 11 = 10), (2 & 4) = 0 (10 & 100 = 000), 2 or 0 = 2

# 1. Check if a username is not empty and the age is greater than or equal to 18.
# username="ankitbhagat"
# age = int(input("Enter your age: "))
# if username and age >= 18:
#     print("Valid")
# else:
#     print("Invalid")


# 2. Check if the password is at least 8 characters long and does not contain spaces.
# password="ankit@123"
# if len(password) >= 8 and ' ' not in password:
#     print("Password is valid")
# else:
#     print("Password is invalid")

# 3. Check if a user email contains ‘@’ and ends with ‘.com’.
# email="example@gmail.com"
# if '@' in email and email.endswith('.com'):
#     print('email is valid')
# else:
#     print("email must contain @ and must end with .com")

# 4. Check is a username is a string and is longer than 8 characters. 
# username="ankitbhagat"
# if type(username) and len(username) > 8:
#     print("Username is valid")
# else:
#     print("username must be string and longer that 8 character")

# 5. Check if a username contains only allowed special characters ‘_’ and ‘.’ and does not contain spaces
# username="ankit_123.bhagat"
# if '_' in username and '.' in username and ' ' not in username:
#     print("Username is valid")
# else:
#     print("Username must contain special charcter like _ and . It must not contain spaces")
# Bitwise NOT (~) of 1:
# Python uses two's complement representation for integers (32-bit or 64-bit)
# 
# Step 1: Convert 1 to binary (32-bit two's complement)
#         1 = 00000000000000000000000000000001
#
# Step 2: Apply Bitwise NOT - flip ALL bits (0→1, 1→0)
#         ~1 = 11111111111111111111111111111110
#
# Step 3: Interpret the result as two's complement signed integer
#         Since the leftmost bit is 1, this is a NEGATIVE number
#         To find the negative value:
#         - Flip all bits back: 11111111111111111111111111111110 → 00000000000000000000000000000001
#         - Add 1: 00000000000000000000000000000001 + 1 = 00000000000000000000000000000010 (which is 2)
#         - Result is -(2) = -2
#
# Formula: ~a = -(a + 1)
# Calculation: ~1 = -(1 + 1) = -2

# In Python, a string is a sequence of characters enclosed within either single quotes (''), double quotes ("") or triple quotes ('''''' or """). Strings are immutable, meaning once they are created, their content cannot be changed. Strings can contain letters, numbers, symbols, and whitespace characters.


name = "python"

# access a string
# print(name)

# indexing(+/-)
# print(name[2])
# print(name[-2])

# slicing(+/-)
# print(name[2:5])
# print(name[-2:-5:-1][::-1])

# name = "TopS TeCHnoLOgy Pvt. LTd.".lower()

# print(name.count('t'))
# print(name.count('T'.lower()))

# print(name.find('t'))

# print(name)
# print(name.center(50, '-'))

# print(len(name))

# print(name.strip())
# print(name.lstrip())
# print(name.rstrip())


    

# print(name.lower())
# print(name.upper())
# print(name.title())
# print(name.capitalize())
# print(name.swapcase())

# password = "Test@"

# upper_case = False
# lower_case = False
# digit = False
# special_ch = False

# if len(password) < 8:
#     print("Password len at least 8 digits")
# else:
#     for ch in password:
#         if ch.isupper():
#             upper_case = True
#         if ch.islower():
#             lower_case = True
#         if ch.isdigit():
#             digit = True
#         if not ch.isalnum():
#             special_ch = True

# if (upper_case and lower_case and digit and special_ch):
#     print("password is correct")
# else:
#     print("Password in-correct")


# print(dir(name))

# code  = "python"

# print(code.startswith('z'))
# print(code.startswith('p'))
# print(code.startswith('P'))
# print(code.endswith('on'))


# account_number = "5234 4763 3573 8436"
# # print(account_number.replace(" ", '-'))
# print(account_number.replace("4", '-'))

import random
fname = "brijesh"
lname = "gondaliya"
otp = int(random.randint(111111,999999))
# message = f"Hello, {fname} {lname}\nYour OTP is: {otp}"
# print("Hello, {} {}\nYour OTP is: {}".format(fname,lname,otp))
# print("Hello, {0} {1}\nYour OTP is: {2}".format(fname,lname,otp))
# print("Hello, %s %s\nYour OTP is: %d"%(fname,lname,otp))


# fullname = fname + ' ' + lname
# print(fullname*3)

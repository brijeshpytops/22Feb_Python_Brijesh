"""
In Python, a function is a block of reusable code that performs a specific task. Functions allow you to break down your program into smaller, more manageable pieces, making your code easier to understand, reuse, and maintain.

syntax :

def function_name([para1, para2,....paran]):
    # code block

function_name(value1, value2, ...., valuen)


Here are some key points about functions in Python:

Definition: Functions in Python are defined using the def keyword followed by the function name and a pair of parentheses containing zero or more parameters. The function body is then indented below the definition.

Parameters: Parameters are variables that are passed into the function when it is called. They provide a way to pass data to the function. Functions can accept any number of parameters, including none.

Return Value: Functions can optionally return a value using the return statement. This allows functions to compute results and pass them back to the caller for further processing or use.

Function Call: To execute a function, you need to call it by using its name followed by parentheses containing any arguments you want to pass into the function. If the function returns a value, you can store it in a variable or use it directly.
"""

# num1 = 10
# num2  = 20

# print()

# num3 = 30
# num4 = 40

# print(num3+num4)

# def sum(num1, num2):
#     return num1+num2

# sum(10, 20)


# sum(30, 40)
# number = sum(30, 40)
# print(number)

# types of function para in python
# postional para/args
# def add(a, b, c):
#     print(a + b + c)

# add(10,20,30)

# default para/args
# def genrate_bill(tomato=50):
#     print(tomato)

# genrate_bill(tomato=70)

# keyword para/args
# def genrate_bill(store_name, tomato=50, potato=18) :
#     print(store_name)
#     print(f"Total amount: {tomato+potato}")

# genrate_bill("JIO-MART", tomato=110)

# variable length para/args
# *args/**kwargs

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     print(total)
#     # print(sum(nums))
#     # print(type(nums))

# add(10,20,30,40,50,60,70,80,90,100,1000)


# def genrate_bill(store_name, **products):
#     # print(type(products))
#     total = 0
#     print(f"Store name: {store_name}")
#     print("Products | price")
#     for name, price in products.items():
#         total += price
#         print(name, price)
#     print("-"*20)
#     print(f"Total amount: {total}")

# genrate_bill("JIO-MART", book=20, pen=2, butter_milk=175, milk=33, lemon=20, ice_cream=100)

# sum = lambda num1, num2:num1+num2
# print(sum(10,20))

# nums = [1,2,3,4,5]
# print(list(map(lambda num:num**3, nums)))


# x  = 10

# def test():
#     global x
#     x =  20
#     print(x, "---")

# test()
# print(x)
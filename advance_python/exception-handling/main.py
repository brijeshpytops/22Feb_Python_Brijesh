"""
Exception handling in Python refers to the process of dealing with errors that occur during the execution of a program. When a Python program encounters an error (also known as an exception), it raises an exception. If these exceptions are not handled properly, they can cause the program to terminate abruptly, resulting in an undesirable user experience.

keywords - try, except, else, finally, raise, assert

"""

# print("start")
# print(a)
# print("end")

import datetime

print("start")
try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = (a/b) + c + "hello"
except ZeroDivisionError:
    print("You can not devide by 0")
# except TypeError:
#     print("You can not concate float with str")
except Exception as e:
    current_time = datetime.datetime.now().strftime('%d-%m-%Y, %I:%M:%S %p')
    print(f"{current_time} - {e}") 
else:
    print(result)
finally:
    print("I will execute anyway") 
print("end")

# bal = 10000
# withdrow = 2000
# if withdrow > bal:
#     raise ValueError("Insuficent balance")
# else:
#     bal -= withdrow
#     print("Remaning balance : ", bal)
#     print("You can withdrow")

# bal = 10000
# withdrow = 2000
# assert (withdrow > bal), "Insuficent balance"


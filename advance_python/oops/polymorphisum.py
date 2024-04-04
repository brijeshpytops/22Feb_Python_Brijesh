# class math_:
#     def sum(self, a, b):
#         print(a+b)
# 
#     def sum(self, a, b, c):
#         print(a + b + c)
# 
# obj = math_()
# # print(dir(obj))
# obj.sum(10, 20)


# class math_:
#     def sum(self, a=None, b=None, c=None):
#         if (a!=None and b!=None and c!=None):
#             print(a+b+c)
#         elif(a!=None and b!=None):
#             print(a+b)
# 
# obj = math_()
# obj.sum(10, 20, 30)


class parent:
    def details(self):
        print("I am a person of parent class")

class child(parent):
    def __init__(self):
        super().details()

    def details(self):
        print("I am a person of Child class")

obj = child()
# obj.details()
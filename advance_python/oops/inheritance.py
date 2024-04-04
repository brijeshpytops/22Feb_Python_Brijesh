# Single inheritance
# class A:
#     def a(self):
#         print("I am from class A")
# 
# 
# class B(A):
#     def b(self):
#         print("I am from class B")
# 
# obj = B()
# print(dir(obj))
# obj.a()
# obj.b()


# multilevel inh.
# class A:
#     def a(self):
#         print("I am from class A")
# 
# 
# class B(A):
#     def b(self):
#         print("I am from class B")
# 
# 
# class C(B):
#     def c(self):
#         print("I am from class C")
# 
# obj = C()
# print(dir(obj))
# obj.a()
# obj.b()
# obj.c()


# multiple inh.
# class A:
#     def a(self):
#         print("I am from class A")
# 
# 
# class B:
#     def b(self):
#         print("I am from class B")
# 
# 
# class C(A,B):
#     def c(self):
#         print("I am from class C")
# 
# obj = C()
# print(dir(obj))
# obj.a()
# obj.b()
# obj.c()

# class master:
#     def m(self):
#         return "m"
#     
# class ML(master):
#     def ml(self):
#         return "ml"
# 
# class MLL(ML):
#     def mll(self):
#         return "mll"
# class MLR(ML):
#     def mlr(self):
#         return "mlr"
#     
# class MR:
#     def mr(self):
#         return "mr"
    
# obj = MLR()
# print(MLR.__mro__)
# print(MLR.mro())
# print(dir(obj))
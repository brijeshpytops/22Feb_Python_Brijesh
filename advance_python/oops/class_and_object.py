# # class class_name:
# #     pass

# class auth: # define class
#     # data members
#     username = "tops@07"
#     email = "top@gmail.com"
#     password = "1234qwer"
#     confirm_password = "1234qwer"

#     # member funtions
#     def register(yoyo):
#         return "this is a registerfunction"

#     def login(yoyo):
#         return "this is a login function"

#     def forgot(yoyo):
#         return "this is a forgot function"

# obj = auth() # create obj

# print(obj.username)
# print(obj.email)
# print(obj.password)
# print(obj.register())
# print(obj.login())
# print(obj.forgot())
# print(obj.)

# print(dir(obj))

# x = 10
# print(x)

# def hello():
#     return "helo"

# hello()

# name = "python"
# name = str()
# items = []
# items = list()
# items.append()


# class animal:
#     class dog:
#         def speak(self):
#             return "Bho Bho"

#     class cat:
#         def speak(self):
#             return "meow meow"
        
# obj1 = animal().dog()
# obj2 = animal().cat()
# # print(dir(obj1))
# print(obj1.speak(),obj2.speak())

# class animal:
#     def speak(self, voice):
#         return voice
    
# dog = animal()
# print(dog.speak("Bho bho"))
# cat = animal()
# print(cat.speak("meow meow"))

import pandas as pd

class animal:
    def animal_property(self, name, voice):
        return f"Name: {name},\nVoice:{voice}"

animal_data = []
flag = True
while(flag):
    name = input("Enter a animal name: ") 
    voice = input("Enter animal voice: ")
    print(animal().animal_property(name, voice))
    animal_data.append((name, voice))
    yesNo = input("You want to contine? [y/n]: ").lower()
    if yesNo == 'y':
        flag = True
    else:
        flag = False

# Creating a DataFrame
df = pd.DataFrame(animal_data, columns=['animal_name', 'animal_voice'])

# Writing DataFrame to an Excel file
excel_filename = 'animal_sounds.xlsx'
df.to_excel(excel_filename, index=False)

print(f"Data has been written to {excel_filename} successfully.")
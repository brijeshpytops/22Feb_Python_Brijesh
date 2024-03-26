file = open('example.txt', 'w')

print(file.tell())
file.seek(6)
print(file.tell())
file.write("-------")

# # open('example.txt', 'x')

# file = open('example.txt', 'w')
# # str_ = input("Enter something...: ")
# # file.write(str_)
# lines = ['This is a line - 1\n', 'This is a line - 2\n', 'This is a line - 3\n', 'This is a line - 4\n', 'This is a line - 5\n', 'This is a line - 6\n', 'This is a line - 7\n', 'This is a line - 8\n', 'This is a line - 9\n', 'This is a line - 10']
# file.writelines(lines)
# file.close()

# a_file = open('example.txt', 'a')
# new_line = '\nThis is a line - 11\n'
# a_file.write(new_line)
# a_file.close()

# print(file.read())
# print(file.read(8))

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readlines())


# file_path = r'C:\brijesh-py\new_example.txt'
# # print(open(file_path, 'r').read())
# open(file_path, 'x')

# print(r"brijesh go\ndaliya")

# import os

# os.system('py app.py')
# os.system('type nul > new_sample.py')
# os.remove('new_sample.py')
# os.system('mkdir test')

# old_file_path = r'C:\brijesh-py\new_example.txt'
# new_file_path = r'C:\brijesh-py\sample.txt'
# os.rename(old_file_path, new_file_path)

# print(os.listdir(r'C:\brijesh-py'))
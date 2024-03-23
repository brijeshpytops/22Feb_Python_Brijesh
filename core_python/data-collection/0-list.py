"""
List - mutable, ordered, duplicate values are allowed, indexing, slicing

In Python, a list is a data structure used to store a collection of items, such as integers, strings, or other objects. Lists are mutable, which means they can be modified after creation. Lists are ordered, meaning the items in a list maintain their position and can be accessed by their index. Lists are defined using square brackets [], with commas separating the individual items.

syntax:

list_name = []
list_name = list()
"""

# mix = [1,2,3,"python", 45.34, 'dfdffdf']

# print(len(mix))
# print(type(mix))

# access elements of list
# print(mix)

# indexing (+/-)
# nums = [1,2,3,4,5,6,7,8,9,10]

# print(nums[4])
# print(nums[8])

# print(nums[-1])
# print(nums[-5])

# slicing (+/-)
# array_name[start:stop+1:setp+1]
# print(nums[3:8])
# print(nums[:8])
# print(nums[3:])
# print(nums[::2])
# print(nums[::-1])
# print(nums[-4:-8:-1])

# nums = [1,1,1,1,2,3,4,5]
# print(nums)

mummy_list = ['tomato', 'potato', 'onion']
n_aunty_list = ['milk', 'butter-milk']
my_list = ['drink','chocolate']


mix_list = mummy_list + n_aunty_list + my_list

# for item in mix_list:
#     print(item.title())

# for index in range(len(mix_list)):
#     print(mix_list[index])

# mix_list[-1] = 'ice-cream'
# print(mix_list)
# print(dir(mix_list))

# add - append, extend, insert
sister_list = ['chocolate', 'lipstik']
# mix_list.append(sister_list)
# mix_list.extend(sister_list)
# mix_list.insert(0, sister_list)


# update
# mix_list[2] = sister_list
# print(mix_list)

# delete - clear, pop, remove
# mix_list.clear()
# mix_list.pop()
# mix_list.remove('drink')

# del mix_list[-1]
# print(mix_list)
# mix - copy, count, index, reverse,sort

# mix_list.append('tomato')
# print(mix_list.count('tomato'))
# print(mix_list.index('tomato', 1))
# mix_list.reverse()
# mix_list.sort()
# print(mix_list)

# int_nums = [1,2,3,4,5]
# print(id(int_nums))
# float_list = int_nums.copy()
# print(id(float_list))

# x = 10
# y = 10

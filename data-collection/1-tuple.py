"""
Tuple - immutable, ordered, indexing, slicing, duplicat a value are allowed

In Python, a tuple is another type of data structure similar to a list, but with one key difference: tuples are immutable, meaning they cannot be changed after creation. Once a tuple is created, its elements cannot be modified, added, or removed.

Tuples are defined using parentheses (), with commas separating the individual items. Optionally, you can include a comma after the last item, although it's not necessary unless you're defining a tuple with a single element.

syntax:

tuple_name = ()
tuple_name = tuple()
comma_tuple_name = 1,
"""

nums = (1, 1,2,3,4,5)
# print(len(nums))
# print(type(nums))

# print(nums[2])
# print(nums[-1])
# print(nums[:2])
# print(nums[::-1])
# nums[0] = 111 # TypeError: 'tuple' object does not support item assignment
# print(nums)

# 'count', 'index'
# print(dir(nums))
# print(nums.count(2))
# print(nums.index(3))
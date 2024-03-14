"""
In Python, a dictionary is a built-in data type that stores key-value pairs. It is also known as a hashmap or associative array in other programming languages. Dictionaries are mutable, meaning they can be modified after creation.

Here's a brief overview of how dictionaries work in Python:

Key-Value Pairs: Each entry in a dictionary consists of a key and its corresponding value. Keys must be unique within a dictionary, but values can be duplicated.

Syntax: Dictionaries are defined using curly braces {}. Each key-value pair is separated by a colon :. Keys and values can be of any data type, but keys are commonly strings or numbers.

syntax:
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

"""

contacts = {
    "A":[
        {
            'aman':{
                'email':['aman@gmail.com', 'aman07@gmail.com'],
                'mobile':643765746578
            },
            'ajay':{
                'email':'ajay@gmail.com',
                'mobile':['63247657623', '872677367534']
            }
        }
    ],
    "B":[
        {
            'bubban':{
                'email':'bubban@gmail.com',
                'mobile':['63247234657623', '872675445367534']
            },
            'bunty':{
                'email':'bunty@gmail.com',
                'mobile':['63111114657623', '87267522227534']
            }
        }
    ]
}

new_contacts = {
    'C':[
        {
            "chaman":{
                'email':'chaman@gmail.com',
                'mobile':['63333114657623', '77777227534']
            }
        }
    ],
    'D':[
        {
            "dhiru":{
                'email':'dhiru@gmail.com',
                'mobile':['44443114657623', '888888227534']
            }
        }
    ]
}

# contacts.update(new_contacts)

# print(contacts)
# print(contacts['B'][0]['bubban']['mobile'][-1])


employee = {
    'name':"brijesh gondaliya",
    'salary':5
}

# employee.pop('name')
# employee.popitem()
print(employee)

# print(employee.get('name'))
# print(employee.keys())
# print(employee.values())
# print(employee.items())

# for key in employee.keys():
#     print(key)
# for value in employee.values():
#     print(value)
# for key,value in employee.items():
#     print(key, value)

# print(dir(employee))
#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# items = ['tomato', 'potato', 'onion']
# price = 20

# products = dict()
# print(products.fromkeys(items, price))


car = {
    'name':"BMW",
    'price':20,
    # 'color':'red'
}
car.setdefault('color', 'black')
print(car)
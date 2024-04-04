import re

# print("brijesh go\\ndaliya")

# print(r'brijesh go\\ndaliya')

data = "map mood moon mat map mm m mmmm mmm chand"
pattern = r"\bm\w\w\w\b"
# result = re.search(pattern, data)
result = re.findall(pattern, data)
print(result.group())
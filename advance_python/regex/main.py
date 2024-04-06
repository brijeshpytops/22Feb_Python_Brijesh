import re

# print("brijesh go\\ndaliya")

# print(r'brijesh go\\ndaliya')
# 
# data = "map mood moon mat map mm m mmmm mmm chand"
# pattern = r"\bm\w\w\w\b"
# # result = re.search(pattern, data)
# result = re.findall(pattern, data)
# print(result.group())


data = "m ,fgmh xcmngxns xmhgmis mndbgj 23-12-1996 hgcuy mhg x 1-1-1997 mnhf ndhgvju  v mcvbnbgnf, mat map this is a python codfgfh"

# pattern = r"\b\d{1,2}-\d{1,2}-\d{4}\b"
# pattern = r"\bm\w*\b"
# pattern
# 
# reasult = re.findall(pattern, data)
# 
# print(reasult)

# print(data.count('is'))


# import re
# 
# def validate_email(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     return re.match(pattern, email) is not None
# 
# def test_emails(emails):
#     valid_emails = []
#     invalid_emails = []
#     
#     for email in emails:
#         if validate_email(email):
#             valid_emails.append(email)
#         else:
#             invalid_emails.append(email)
#     
#     return valid_emails, invalid_emails
# 
# # Example list of emails
# email_list = [
#     "example@email.com",
#     "invalid.email@",
#     "another_example123@email.co.uk",
#     "no_symbol_email.com"
# ]
# 
# valid_emails, invalid_emails = test_emails(email_list)
# 
# print("Valid emails:")
# for email in valid_emails:
#     print(email)
# 
# print("\nInvalid emails:")
# for email in invalid_emails:
#     print(email)


# import re
# 
# def validate_mobile(phone):
#     pattern = r'^\d{10}$'  # Assumes a 10-digit phone number format
#     return re.match(pattern, phone) is not None
# 
# def test_mobiles(phone_numbers):
#     valid_numbers = []
#     invalid_numbers = []
#     
#     for phone in phone_numbers:
#         if validate_mobile(phone):
#             valid_numbers.append(phone)
#         else:
#             invalid_numbers.append(phone)
#     
#     return valid_numbers, invalid_numbers
# 
# # Example list of phone numbers
# phone_list = [
#     "1234567890",
#     "987654321",  # Less than 10 digits
#     "99999999999"  # More than 10 digits
# ]
# 
# valid_numbers, invalid_numbers = test_mobiles(phone_list)
# 
# print("Valid phone numbers:")
# for phone in valid_numbers:
#     print(phone)
# 
# print("\nInvalid phone numbers:")
# for phone in invalid_numbers:
#     print(phone)


# data = "This is a php code"
# res = re.match("php", data)
# print(res)
# 
# import re

# data = "it is a php scripting language"
# res = re.match("php", data)
# print(res)


# data = "This is a php code"
# res = re.search(r"php", data)
# print(res)

# print(re.sub('php', 'Python', data))
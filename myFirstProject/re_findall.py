import re
em = 'john@gmail.com, angie123@outlook.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', em)
for email in emails:
     print(email)

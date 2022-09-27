import re
phone_number = '(210)-345-0987'
pattern = '\D'
outcome = re.sub(pattern, '', phone_number)
print(outcome)

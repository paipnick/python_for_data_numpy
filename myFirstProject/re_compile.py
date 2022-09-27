import re
birthdate = "John's birthday is on 18/12/94"
string_pattern = r"\d{2}"
regex_pattern = re.compile(string_pattern)
outcome = regex_pattern.findall(birthdate)
print(outcome)

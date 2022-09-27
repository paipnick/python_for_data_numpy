import re
patterns = ['Learning Python', 'workearly']
text = 'Learning Python now'
for pattern in patterns:
     print('Looking for "%s" in "%s" --> ' %(pattern, text), end = '')
     if re.search(pattern, text):
          print('Found a match')
     else:
          print('No match found!')

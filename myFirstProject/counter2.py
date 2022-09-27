from collections import Counter

mylist = ['a', 'b', 'c', 'a', 'a', 'a', 'b', 'c']
count = Counter(mylist)
print(Counter(mylist))

count.update(['a', 'b', 'b', 'c'])
print("Updated", count)

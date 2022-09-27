from os import path
if path.exists('workearly.txt'):
      src = path.realpath('workearly.txt')
head, tail = path.split(src)
print('head: ', head)
print('tail: ', tail)

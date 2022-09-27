import shutil
from os import path
import datetime
import time
if path.exists('workearly.txt'):
      src = path.realpath('workearly.txt')
head, tail = path.split(src)
print('head: ', head)
print('tail: ', tail)
dst = src + '.bak'
shutil.copy(src, dst)
shutil.copystat(src, dst)
t = time.ctime(path.getmtime('workearly.txt.bak'))
print(t)
print(datetime.datetime.fromtimestamp(path.getmtime('workearly.txt.bak')))

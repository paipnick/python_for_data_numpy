file1 = open('workearly.txt', 'w+')
for i in range(10):
      file1.write("The line is %d\r\n" % (i+1))
file1.close()

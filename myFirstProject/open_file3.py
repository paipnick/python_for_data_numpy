file1 = open('workearly.txt', 'r')
if file1.mode == 'r':
      contents = file1.read()
      print(contents)

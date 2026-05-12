'''Write a program that reads a text file and overwrites its content to UPPERCASE. For
testing it, create a local text file with a few sentences in it. '''
f = open('example.txt', 'a')
f.write('My first text file:\n\n')
f.write('third line, \n')
f.write('fourth line \n fifth line ')
f.write('end of the file')
f.close()
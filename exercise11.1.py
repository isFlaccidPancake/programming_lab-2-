'''Write a program that reads a text file and overwrites its content to UPPERCASE. For
testing it, create a local text file with a few sentences in it. '''
f = open('example.txt', 'r')
lines= f.readlines()#lista
print(lines)
f.close
f=open('example.txt', 'w')
for line in lines:
    nline=line.upper()
    f.write(nline)
f.close()
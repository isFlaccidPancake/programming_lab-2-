def copy(file1,file2):
    f1=open(file1,'r')
    f2=open(file2,'w')
    for line in f1:
        f2.write(line)
    f1.close()
    f2.close()
copy('example.txt', 'copia.txt')
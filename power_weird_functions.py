A=int(input('based '))
B=int(input('power of '))
lista= [*(A for i in range(0,B))] 
print(lista) 
def add(integer,integer_2):
    addition=0
    for i in range(integer_2):
        addition+=integer
    return addition

def mult(lista):
    sum= add(lista[0],lista[1])
    lista.pop(0)
    lista.pop(0)
    lista.insert(0,sum)
    return lista
for i in range(0,len(lista)-1):
    mult(lista)
    print(lista)
print(lista[0])


'''Write a program that stores student grades in a tuple and shows a menu of
choices to the user:
1) insert a new grade in the tuple
2) view the marks stored in the tuple
3) print the average of the grades stored in the tuple,
0) exit the program
and performs the actions related to the choice, repeatedly, until the user enters 0.
• Tip: for 3, use the function defined in exercise 7.3.'''
tuples=tuple()
def f_1():
    global tuples
    x= (int(input('new grade:  ')),)
    tuples+= x

def f_2():
    global tuples
    print(tuples)
def f_3():
    global tuples
    tot=0
    for i in tuples:
        tot+=int(i)
        result=tot/len(tuples)
    print(result)

def f_0():
    global boolean
    boolean=False

boolean= True
while boolean:
    n=int(input('command:  '))
    if n==1:
        f_1()
    elif n==2:
        f_2()
    elif n==3:
        f_3()
    elif n==0:
        f_0()
        
    
    
    
    
    
    
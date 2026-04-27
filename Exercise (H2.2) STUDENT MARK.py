'''Exercise (H2.2)
Given a string showing student marks, write a program that prints the students with
the best and worst marks. The string is formed as a sequence of “s:X m:Y;”, where X is
the student ID and Y is the mark.
E.g., given A = “s:213 m:28;s:78 m:16;s:765 m:19;” the program prints:
Best student -> ID: 213 Mark: 28
Worst student -> ID: 78 Mark: 16'''

stringa= input('insert data')
best=0
best_=''
worst=30
worst_=''
check_1=0


score=''
new=''
for i in range(len(stringa)-1):
    if stringa[i]==';':
        new= stringa[check_1:i]
        
        for j in range(len(new)-1,0,-1):
            if new[j]!=':':
                score+= new[j]
            else:
                score= int(score[::-1])
                break 
        if score> best:
            best_= new
            best=score
        elif score< worst:
            worst_= new
            worst=score
                
        score=''        
        check_1=i+1
        
print(best_)
print(worst_)

    

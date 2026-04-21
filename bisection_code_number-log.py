n=float(input('log n of x, specify n: '))
x = float(input('log n of x, specify x: '))
low, high= 0 , x
small= 0.0001
tr=0
guess= (high+low)/2
if x<0 or n<=0:
    print('MATH ERROR')
else:
    while abs(n**guess - x )>= small: 		#abs() because we look at he magnitude of our error
        tr+=1
        if n**guess> x:
            high= guess
        else:
            low= guess
        guess= (high+low)/2
print(guess, tr)
    
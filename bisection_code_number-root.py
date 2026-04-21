x=float(input('number you want the root n of:   '))
n=int(input('root n, specify n:  '))
approximation= 0.00001			#this can vary
high, low= x , 0
if x<0:			#cases where number is 0.5---> root is 0.707
    high-=1				
else:
    high+=1
if high<low:			#make sure the range is properly disposed
    b=low
    low=high
    high=b
guess= (high + low)/2				#bisection method
while abs((guess**n-x)) > approximation:#abs() because we look at he magnitude of our error
    print('guessing')
    if guess**n< x:					#updating the range, each time halving it
        low= guess
    else:
        high= guess
    guess= (high + low)/2
print(guess)
print(guess**n)
        
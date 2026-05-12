#naive check for prime number

x = int(input("insert a number: "))

d = 2

while d < x/2:
    if x % d == 0: #not prime: d is a divisor
        print(f"{x} is not prime, can be divided by {d}")
        break
    else:
        d = d + 1

if  d >= x/2 :
    print(f"{x} is prime")
              
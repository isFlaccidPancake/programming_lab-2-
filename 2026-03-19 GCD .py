#find the GCD of two numbersx = int(input("insert a number: "))
x = int(input("insert a number: "))
y = int(input("insert a number: "))

if x > y:
    d = y
else:
    d = x

while (x % d != 0) or (y % d != 0):
    d = d - 1
print(f"GCD between {x} and {y} is {d}")
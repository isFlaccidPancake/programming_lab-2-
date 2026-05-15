'''Exercise 12.3
• Write a recursive function that given a positive integer n, returns the sum of the first n
odd integers. Do not use for or while.
E.g., given n = 5, the function returns the sum of 1, 3, 5, 7, and 9.'''
def sum_off_odd(n):
    if n==1:
        return 1
    return (n*2)-1+sum_off_odd(n-1)

print(sum_off_odd(int(input())))

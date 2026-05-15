#H12.1
def reverse(stringa):
    if len(stringa)==1:
        return stringa
    return reverse(stringa[1:])+stringa[:1]
print(reverse(input()))
    
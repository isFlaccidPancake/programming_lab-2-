#score conversion form Numbers to letters

v = int(input("insert the numerical score: "))

if v < 18:
    print("score is F")
else:
    if v < 22:
        print("score is D" )
    else:
        if v < 25:
            print("score is C" )
        else:
            if v < 28:
                print("score is B")
            else:
                print("score is A")
    

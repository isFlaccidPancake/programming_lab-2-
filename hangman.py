import random
def find_locations(c,s):
    return tuple(i for i in range(len(s)) if s[i]==c)#tuple compresion


#part 2
f_v=open('vocabulary.txt','a')
list_w= input('insert a new word separated by ";"	')
words= list_w.split(';')
for w in words:
    w=w.strip()
    if (w.isalpha()):
        f_v.write(w.upper()+'\n')#one word in each line
        
#part 3
user=input('your name	')
score=100
f_v=open('vocabulary.txt','r')
words=f_v.readlines()
print(words)
f_v.close
word= random.choice(words).strip()
mask= '_'*len(word)
mask_=[i for i in mask]


#part 4
    
while (score>0 and mask!=word):
    print('current guess:	'+mask)
    c= input('guess the word letter by letter	').upper()
    if c in mask:
        print('already guessed')
    elif c in word:
        for i in range(len(word)):
            if word[i]==c:
                mask_[i]=c
        mask=''
        for j in mask_:
            mask+=j
        print(mask)       
    else:
        score-=random.choice([10]*5+[0])
    print(score)
if score<0:
    print('you lost')
else:
    print('you won, the word was	',word)
    #open score file
    win_line= str(score) +' '+user
    f_w= open('scorex.txt','a+')
    f_w.seek(0)
    score_list=[]
    for line in f_w:
        score_list.append(int(line.split()[0]))
    if score_list== [] or score > min(score_list):
        f_w.write(str(score)+" "+user+'\n')
        
    f_w.close()
    
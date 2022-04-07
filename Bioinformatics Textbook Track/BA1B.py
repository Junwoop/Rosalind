import re
with open('rosalind_ba1b.txt','r') as t:
    t=t.read().strip().splitlines()
    text,k=t[0],int(t[1])
    maxcount=[]
    maxes=[]
    for i in range(len(text)-k):
        cnt=text.count(text[i:i+k])
        maxcount.append(cnt)
    for i in range(len(maxcount)):
        if maxcount[i]==max(maxcount):
            maxes.append(text[i:i+k])
    print(' '.join(list(dict.fromkeys(maxes))))















































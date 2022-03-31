t=open('rosalind_mrna.txt','r').read().strip().splitlines()
t=''.join(t)
dic={'F':2,'L':6,'I':3,'M':1,'V':4,'S':6,'P':4,'T':4,'A':4,'Y':2,'H':2,'Q':2,'N':2,
     'K':2,'D':2,'E':2,'C':2,'W':1,'G':4,'R':6}
prob=3
for prot in t:
    prob*=dic[prot]
print(prob%1000000)


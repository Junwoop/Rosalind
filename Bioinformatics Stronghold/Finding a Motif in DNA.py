with open('rosalind_subs.txt','r') as t:
    a=t.read().split('\n')
    string,mot=a[0],a[1]
    start=0
    pos=[]
    for start in range(0,len(string)):
        try :i=string.index(mot,start,len(string))+1
        except ValueError:
            pass
        pos.append(i)
    x=list(dict.fromkeys(pos))
    y=list(map(str,x))
    #print(' '.join(y))

#solution by Leandro Lima
File = open('rosalind_subs.txt').read().split('\n')
s1,s2=File[0],File[1]
for i in range(len(s1)):
    if s1[i:].startswith(s2): #[i:]start from i, no limit.
        print(i+1,)

#solution by romz34
r = 0
while r != -1 :
        r = s1.find(s2,r+1) #last element coordinate in find = -1
        print(r+1) 








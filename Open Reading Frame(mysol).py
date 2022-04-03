import re
#reverse strand => complementary and 5'3' reverse
t= open('rosalind_orf.txt','r').read().strip().splitlines()
t=''.join(t[1:])
u=open('codon.txt','r').read().splitlines()
seq,cod=u[0].split(',') , u[1].split(',')
dic=dict(zip(seq,cod))
reverse={'A':'T','T':'A','G':'C','C':'G'}
ret=''.join([reverse[i] for i in t])[::-1]
pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAG|TGA|TAA))')
m=re.findall(pattern,t)
n=re.findall(pattern,ret)

def orf(seq):
    tri=re.findall('\w{3}',seq)
    listt=[]
    for j in tri:
        if dic[j]=='STOP':
            break
        listt.append(dic[j])
    return ''.join(listt)

result=[]
for i in m:
    result.append(orf(i))
for i in n:
    result.append(orf(i))
result=list(dict.fromkeys(result))
print('\n'.join(result))














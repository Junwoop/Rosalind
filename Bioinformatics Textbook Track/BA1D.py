import re
with open('rosalind_ba1d.txt','r') as t:
    t=t.read().strip().splitlines()
    motif=t[0]
    text=''.join(t[1:])
    pos=[g.start() for g in re.finditer(r'(?=%s)'%motif,text)]
    print(' '.join(map(str,pos)))

# Solution by wenruihuang
# for i in range(len(seq)-len(kmer)+1):
#     if seq[i: i+len(kmer)] == kmer:
#         print i,










































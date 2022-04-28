import itertools
with open('rosalind_lexf.txt','r') as t:
    t=t.read().splitlines()
    alphabet,n=''.join(t[0].split()),int(t[1])
    for p in itertools.product(alphabet,repeat=n): #p as a tuple for each product
        print(''.join(p))





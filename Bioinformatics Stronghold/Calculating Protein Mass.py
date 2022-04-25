p=open('protein_mass.txt','r').read()
x,y=p.split()[::2],list(map(float,(p.split()[1::2])))#float, not intergers
mass_table=dict(zip(x,y))
with open('rosalind_prtm.txt','r') as t:
    t=t.read().strip()
    sum=0
    for i in t:
        sum+=mass_table[i]
    print(sum)
#in normal situations, add mass of water '18.01528'






























































































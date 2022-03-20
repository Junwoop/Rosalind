t=open('rosalind_prot.txt','r')
a=t.read().strip('\n')
cod=[]
for i in range(0,len(a),3): #range from start to end of list a, but by 3
    cod.append(a[i:i+3]) #append '0,1,2','3,4,5'...

p=open('protein.txt','r')
b=p.read().split() #make list by split()
pro={}
for i in range(0,len(b),2): #list trace but by 2(codon, protein, codon, protein...)
    pro[b[i]]=b[i+1] #Key=codon, value=protein(i+1)
trans=[]
for i in cod:
    trans.append(pro[i]) #append values
trans.remove('Stop') #remove stop codon at the end
print(''.join(trans))


#Answer by Ben Usman
coded = t.read().strip('\n') #raw RNA string
decoded = ''

traL = p.read().split() #['codon','protein'...]
traDict = dict(zip(traL[0::2], traL[1::2])) #"dict" creates a dictionary, "zip" creates (a,b) type joint
#[0::2] =start from 0, by 2 / [1::2]=start from 1, by 2
for i in range(0, len(coded)-3, 3): #len(coded)-3 = omits stop codon
    decoded += traDict[coded[i:i+3]] #dictionary input: RNA string by 3.

print(decoded)
























from Transprot import Transprot #From 'Library' import 'Function'
#String Slicing
with open('rosalind_splc.txt','r') as t:
    t=''.join(t.read().strip().split())
    t=t.split('>') #split by FASTA indicator
    t.remove('')
    string=[]
    for i in t:
        string.append(i[13:]) #slicing Rosalind_XXXX
    DNA = string[0]

#sorting exon sequences by its order(by index in mainstring)
    order=sorted(string[1:],key=lambda x:DNA.index(x))

#1.slice DNA from start to start(firt exon)
#2. next DNA string=end(first exon) to end
#3. fragments are appended to spliced[]
    exons = []
    for i in order:
        exons.append(DNA[0:DNA.index(i)])
        DNA=DNA[DNA.index(i)+len(i):]
    exons.append(DNA)
    spliced=''.join(exons)

#Transprot=Homebrew package translates DNA->protein
    print(Transprot.Translate(spliced))







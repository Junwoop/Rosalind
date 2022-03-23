with open('rosalind_grph.txt','r') as t:
    t=t.read().split('\n')
    t=''.join(t).split('>')
    t.remove('')
    name,first,last=[],[],[]
    #Return overlapping reads if overlap>3
    for i in t:
        name.append(i[:13]) #name = Rosalind_####
        first.append(i[13:16]) #first 3 bases
        last.append(i[-3:]) #last 3 bases
    for i in range(len(last)): #got this idea from "https://52387118.tistory.com/46"
        for j in range(len(first)):
            if i!=j: #compute for every other reads (first vs last)
                if last[i]==first[j]:
                    print(name[i],name[j])

























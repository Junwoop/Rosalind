with open('rosalind_hamm.txt','r') as t:
    t=(t.read().split('\n')) #split by \n, making 2 strings as elements
    a,b=list(t[0]),list(t[1]) #making each string into list ==> a=['A','G','C'....]
    count=0 #predefining count
    for i in range(0,len(a)): #under a condition that a,b is in equal length.
        if a[i] != b[i]: #comparing each nth element
            count +=1
    print(count)

#solution by Ben Usman
with open('rosalind_hamm.txt','r') as t:
    t = (t.read().split('\n'))
    a,b=t[0],t[1]
    print(sum([x!=y for x,y in zip(a,b)]))
    #zip makes list or tuple by grouping 2 iterable.
    #note= [] or {} on line using zip.
    #ex> {x:y for x,y in zip(a,b)} = dictionary. a,b could be list, range...






















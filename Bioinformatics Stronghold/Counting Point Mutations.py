with open('rosalind_hamm.txt','r') as t:
    t=(t.read().split('\n')) #split by \n, making 2 strings as elements
    a,b=list(t[0]),list(t[1]) #making each string into list ==> a=['A','G','C'....]
    count=0 #predefining count
    for i in range(0,len(a)): #under a condition that a,b is in equal length.
        if a[i] != b[i]: #comparing each nth element
            count +=1
    print(count)
























with open('rosalind_iev.txt','r') as t:
    t=t.read().split()
    t=list(map(int,t))
    print(t[0]*2+t[1]*2+t[2]*2+t[3]*1.5+t[4]*1)

    #solution by sharno
    sum([a * int(b) for a, b in zip([2, 2, 2, 1.5, 1, 0], t.read().split())])
    # calculation(a+b) for a,b in zip(list,list)
    #computes by element, 1 outcome for each element position.
    

























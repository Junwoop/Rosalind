with open('rosalind_fib.txt','r') as t:
    a=list(map(int,t.read().split()))
    n,k=a[0],a[1]
    previous1,previous2=1,1
    for i in range(2,n):
        current=previous1+k*previous2 #fertile + newborn
        previous2=previous1 #next newborn = current*k
        previous1=current #for next step, our current will be previous1.
    print(current)

















with open('rosalind_fibd.txt','r') as t:
    t=t.read().split()
    n,m=int(t[0]),int(t[1]) #n=after n month, m=rabbit lifespan
    #solution by abeliangrape
    def fib(n, k=1): #k=1, the initial value of function, since rabbits live at least 1
        ages = [1] + [0] * (k - 1)#each element represents rabbits with x months old
        #if k(lifespan)=5, there will be 5 elements
        #at start, ages=[1,0,0,0,0]
        for i in range(n - 1):
            ages = [sum(ages[1:])] + ages[:-1]
        #first element=newborns, can't reproduce so sum(ages[1:])
        #[sum(ages[1:])]=sums second to last element = shows newborn babies = will be the first element of next
        #ages[:-1] = [1,0,0,0] until right before the last element. since rabbits age, it shifts population one element to right
        return sum(ages)
    print(fib(n,m))















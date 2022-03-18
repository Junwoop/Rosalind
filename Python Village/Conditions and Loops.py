with open('rosalind_ini4.txt','r') as t:
    x=t.read().split()
    y=list(map(int,x))
    sum=0
    for i in range(y[0]|1,y[1]+1,2): #a|1 = | is bitwise OR, need to study more on this. returns odd value always
        sum+=i # a+=i means add each i value into a
    print(sum)







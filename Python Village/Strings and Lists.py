with open('rosalind_ini3.txt','r') as t:
    str=t.readlines()#created list with string[1], positions[2]
    pos=str[1].split()#making separate list with positions[2]. split by blank
    pos=list(map(int,pos))#convert to integer(don't forget 'list')
    string=str[0]
    print(string[pos[0]:pos[1]+1], string[pos[2]:pos[3]+1])#print [a:b+1], [c:d+1]






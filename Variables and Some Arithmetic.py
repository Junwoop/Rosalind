with open('rosalind_ini2.txt','r') as t:
    a=(t.read().strip('\n')).split(' ') #list with string generated
    b=list((map(int, a))) #convert string into integers
                        # map(function, list) => apply function to each element in list
    print(b[0]**2+b[1]**2)









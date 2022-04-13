with open('rosalind_ba1g.txt','r') as t:
    t=t.read().strip().splitlines()
    str1,str2=t[0],t[1]
    Ham_dis=0
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            Ham_dis+=1
    print(Ham_dis)

    #solution by James Ashmore
    distance = sum(1 for i, j in zip(str1, str2) if i != j)
    #counting 1 for each (str1 != str2) pairs, sum for the result
    print(distance)




























































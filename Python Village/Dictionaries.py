with open('rosalind_ini6.txt','r') as t:
    str=t.read().split()
    from collections import Counter #Counter counts elements #Counter('Hello World') #Counter({'l':3,'o':2...})
    d=dict(Counter(str)) #dict(counter results) #d=['we':3,'did':2....]
    for i in d:
        print(i,d[i]) #dictionary value = d[key]











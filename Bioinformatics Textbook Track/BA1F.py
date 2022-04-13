with open('rosalind_ba1f.txt','r') as t:
    string=''.join(t.read().strip().splitlines())
    skew=0
    skew_trend=[]
    for i in string:
        if i=='C':
            skew-=1
        elif i=='G':
            skew+=1
        else:
            pass
        skew_trend.append(skew)
    res = []
    n = 0
    while True:
        try:
            indexing=skew_trend.index(min(skew_trend),n)
            result=indexing+1
            n = result
            res.append(str(result))
        except ValueError: #try couples with except. breaking when error
            break #don't display ValueError
    print(' '.join(res))

    # def minimumSkews(sequence):
    #     skews = [0] # initial value
    #     values = {'A': 0, 'T': 0, 'C': -1, 'G': 1, }
    #     for base in sequence:
    #         skews.append(skews[-1] + values[base]) #append(last value+dic value)
    #     minimum = min(skews)
    #     indices = [str(i) for i, v in enumerate(skews) if v == minimum]
    #     #Enumerate= assigns index to each element in index
            #get value if v==minimum
    #     return ' '.join(indices)
    # print(minimumSkews(string))
























































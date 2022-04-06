import re
with open('rosalind_ba1a.txt','r') as t:
    t=t.read().strip().splitlines()
    text,motif=t[0],t[1]
    # case=start=0
    # while True:
    #     start = text.find(motif, start) + 1
    #     if start>0: #start returns value if motif exists. -1 when theres no more motif
    #         case+=1
    #     else:
    #         break
    # print(case)
    print(len(re.findall('(?=%s)'%motif,text)))







































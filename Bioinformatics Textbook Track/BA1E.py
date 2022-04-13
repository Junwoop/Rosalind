with open('rosalind_ba1e.txt','r') as t:
    t=t.read().strip().splitlines()
    seq,num=t[0],t[1].split()
    k,L,T= int(num[0]),int(num[1]),int(num[2])
    def freqtable(window, k):
        occur = {} #the position of this dic is most important
        # if positioned outside of function, it accumulates
        for i in range(len(window)-k+1):
            motif = window[i:i + k]
            if motif not in occur:
                occur[motif]=1
            else:
                occur[motif]+=1
        return occur
    def findclumps(seq,k,L,T):
        patterns=set()
        for i in range(len(seq)-L+1):
            window=seq[i:i+L]
            result=freqtable(window,k)
            for s in result:
                if result[s]>=T:
                    patterns.add(s)
            #for temporary funciton results; only add bigger than T
            #then go back to next result with empty batch
        return(' '.join(patterns))
    print(findclumps(seq,k,L,T))














































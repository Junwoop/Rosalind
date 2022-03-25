with open('input.txt','r') as t:
    s=t.read().split('>')[1:]
    #[1:] since s[0]=''
    #''+'>'+'Rosalind...' splitted
    #s=['Rosalind_1\nGATTACA\n',.....]
    for i in range(len(s)):
        s[i] = s[i].replace("\n", '') #strip '\n'
        while s[i][0] not in "ACGT": #s[i][0]='R','O','S'...
            # '' in '' = True/False
            s[i] = s[i][1:]
    # 1st: s[i][0] ='R', S[i]becomes s[i][1:], which is Osalind_2 AT...
    #repeats until it reaches 'ACGT'
    ##result: s=['GATTACA', 'TAGACCA', 'ATACA']

    # Get shortest of DNA strings
    index = s.index(min(s, key=len)) #getting min(by length)
    motif = 'A' #need initial value for comparison
    shortest = s[index] #=ATACA(ex)

    # cycle over the DNA string letters
    for i in range(len(shortest)):
        n = 0
        present = True
        while present: #defalt for present is True, so it goes on
            # cycle inside over all other DNA strings and if it's present in there considered a motif and length gets increased by 1
            for each in s: #each= each FASTQ
                if shortest[i:i + n] not in each or n>1000:
                    #begins with shortest str[0:0] = 1 Base.
                    #for each shortest[i:i+n], it compares it to each 'each'
                    #substring to s[0],s[1],s[2]
                    #when present=True, n goes on...until 1000
                    #n>1000 limits the loop. it takes forever without limit
                    present = False
                    #only pass when all elements has it. pass True to next step
                    break #'break' to get out of 'while' loop
            if present: #=if True
                motif = max(shortest[i:i + n], motif, key=len)
                #in max or min, key= provides metric for min/max
                #this max(compares between shortest[1:1+n] and motif)
                #motif = value replaced if shortest[1:1+n]is bigger(key=len)
            n += 1 #n+=1 until the present is true
    #for shortest string => apply while(n+=1) for start-end.
    print(motif)







































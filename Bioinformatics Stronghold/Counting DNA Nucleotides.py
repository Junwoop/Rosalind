with open('rosalind_dna.txt','r') as t:
    a=t.read()
    from collections import Counter
    d=dict(Counter(a)) #again, counter arrages counts in a dictionary form.
    print(d['A'],d['C'],d['G'],d['T'])

    print(*map(a.count,'ACGT'))
    #solution by "arekolek"
    #'map(function,iterable)
    #applying a.count to 'ACGT' each on 'A''C''G''T' so 4 outputs
    #'map'is not printable as it only applies function *makes printable












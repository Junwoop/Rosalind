#solution by hascool

from re import finditer
from urllib.request import urlopen

uniprot = "http://www.uniprot.org/uniprot/%s.fasta" # %s A space for string.
#%d = interger / %f = real number

for protein in open('rosalind_mprt.txt', 'r').read().strip().splitlines(): #for each element in text

    # Fetch the protein's fasta file and get rid of newlines.'
    f = urlopen(uniprot % protein).read().decode('utf-8')
    f = ''.join(f.splitlines()[1:])

    # Find all the positions of the N-glycosylation motif.
    locs = [g.start()+1 for g in re.finditer(r'(?=N[^P][ST][^P])', f)]
    #without '?', it will miss overlaps. Regular regex does not overlap!
    # ?=means {0,1} =repeats 0 or 1 times.
    # [^P]=not P. [ST]= either S or T is fine.

    # Print them out, if any.
    if locs != []:
        print(protein)
        print(' '.join(map(str, locs)))

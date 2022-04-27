with open('rosalind_revp.txt','r') as t:
    text=t.read().strip().split()
    text=''.join(text[1:])

    def rev_comp(text):
        rev = text.translate(text.maketrans('ATCG','TAGC'))
        return rev[::-1]

    for j in range(4,13,2): #range(4,12) creates 4~11, beware. palindrome is even, so jump by 2
        for i in range(len(text)-j+1):
            palindrome = text[i:i+j]
            if palindrome == rev_comp(palindrome):
                print(i+1, len(palindrome))

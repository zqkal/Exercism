codons = {'AUG':'Methionine',
          'UUU':'Phenylalanine', 'UUC':'Phenylalanine', 
          'UUA':'Leucine', 'UUG':'Leucine', 
          'UCU':'Serine', 'UCC':'Serine', 'UCA':'Serine','UCG':'Serine',
          'UAU':'Tyrosine', 'UAC':'Tyrosine',
          'UGU':'Cysteine', 'UGC':'Cysteine',
          'UGG':'Tryptophan',
          'UAA':'STOP', 'UAG':'STOP','UGA':'STOP'}

def proteins(codon):

    for k, v in codons.items():
        if k == codon and v != 'STOP':
            return ''.join("{}".format(codons[k]))
            break


val = ['AUG', 'UUU', 'UAA']
for i in val:
    print(proteins(i))

#proteins('UGG')


__author__ = 'rodrigo'

import re

expressions = [
    'in summary',
    'in conclusion',
    'our investigation',
    'the paper describes',
    'the most important',
    'according to the study',
    'significantly',
    'important',
    'in particular',
    'hardly',
    'impossible'
]

# CP = Cue-phrase score,
# CPS = Number of cue-phrases in the sentence,
# CPD = Total number of cue-phrases in the document

file = open('documents/9150')
sentences = file.readlines()
#print(sentences)

x = 'Meu nome é rodrigo bastos. Eu sou louco por computação. Meu nome Rodrigo Bastos'

exactMatch = re.compile('rodrigo bastos', flags=re.IGNORECASE)
print(exactMatch.findall(x))

# for sentence in sentences:
#     for expression in expressions:
#         exactMatch = re.compile(expression, flags=re.IGNORECASE)
#         print(exactMatch.search(sentence))

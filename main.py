__author__ = 'rodrigo'

import re

cue_phrases = [
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
    'impossible',
    'The purpose',
    'information'
]

# CP = Cue-phrase score,
# CPS = Number of cue-phrases in the sentence,
# CPD = Total number of cue-phrases in the document

file = open('documents/8514')
sentences = file.readlines()
#print(sentences)

# x = 'Meu nome é rodrigo bastos. Eu sou louco por computação. Meu nome Rodrigo Bastos'
#
# exactMatch = re.compile('rodrigo bastos', flags=re.IGNORECASE)
# print(exactMatch.findall(x))

for sentence in sentences:
    for cue_phrase in cue_phrases:
        exactMatch = re.compile(cue_phrase, flags=re.IGNORECASE)
        match = exactMatch.findall(sentence)

        if len(match) > 0:
            print(match)



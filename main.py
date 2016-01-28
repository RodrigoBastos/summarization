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
    'The information'
]

# CP = Cue-phrase score,
# CPS = Number of cue-phrases in the sentence,
# CPD = Total number of cue-phrases in the document

file = open('documents/9136')
sentences = file.readlines()

# x = 'Meu nome é rodrigo bastos. Eu sou louco por computação. Meu nome Rodrigo Bastos'
#
# exactMatch = re.compile('rodrigo bastos', flags=re.IGNORECASE)
# print(exactMatch.findall(x))

count_cue_phrases = 0
count_cue_phrases_document = {}
for sentence in sentences:
    n_cue_phrases = 0
    for cue_phrase in cue_phrases:
        exactMatch = re.compile(cue_phrase, flags=re.IGNORECASE)
        match = exactMatch.findall(sentence)
        n_cue_phrases += len(match)
        count_cue_phrases += len(match)
    if n_cue_phrases > 0:
        count_cue_phrases_document[sentence] = n_cue_phrases
#print(count_cue_phrases_document)

for item in count_cue_phrases_document:
    print(item, count_cue_phrases_document[item])


__author__ = 'rodrigo'

import re
from os import listdir
from os.path import isfile, join

onlyfiles = [f for f in listdir('documents') if isfile(join('documents', f))]

#incidentally, for example, anyway, by the way, furthermore, first, second, then, now, thus, moreover, therefore, hence, lastly, finally, in summary, and on the other hand."
cue_phrases = [
    'incidentally',
    'for example',
    'anyway',
    'by the way',
    'furthermore',
    'first',
    'second',
    'moreover',
    'therefore',
    'and on the other hand',
    'in summary',
    'in conclusion',
    'our investigation',
    'the paper describes',
    'the most important',
    'according to the study',
    'significantly',
    'in particular',
    'hardly',
    'impossible',
    'The purpose',
    'The information'
]

# CP = Cue-phrase score,
# CPS = Number of cue-phrases in the sentence,
# CPD = Total number of cue-phrases in the document
files = []
for name_file in onlyfiles:
    file = open('documents/'+name_file)
    files.append(file.readlines())

count = 0
for sentences in files:
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
    count += count_cue_phrases
    for item in count_cue_phrases_document:
        print(item, count_cue_phrases_document[item])


print(count)




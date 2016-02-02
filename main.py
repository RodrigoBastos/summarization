__author__ = 'rodrigo'

import re
from os import listdir
from os.path import isfile, join
from nltk.tokenize import sent_tokenize
from operator import itemgetter

# users = [{'name': 'Zoe', 'age': 10}, {'name': 'Homer', 'age': 39}]
# newlist = sorted(users, key=lambda k: k['name'])
# print(newlist)


# text = 'Meu nome é Rodrigo. Sou aluno da ufal. Faço mestrado de informática'
# sent_tokenize_list = sent_tokenize(text)
# print(sent_tokenize_list)

onlyfiles = [f for f in listdir('documents') if isfile(join('documents', f))]

# incidentally, for example, anyway, by the way, furthermore, first, second, then, now, thus, moreover, therefore, hence, lastly, finally, in summary, and on the other hand."
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

conj_adverb = [
    'above all',
    'accordingly',
    'actually',
    'admittedly',
    'after all',
    'after that',
    'afterwards',
    'again',
    'all in all',
    'all the same',
    'also',
    'alternatively',
    'another time',
    'anyway',
    'as a consequence',
    'as a corollary',
    'as a result',
    'as it happened',
    'as it is',
    'as it turned out',
    'as luck would have it',
    'as well',
    'at any rate',
    'at first',
    'at first blush',
    'at first sight',
    'at first view',
    'at least',
    'at once',
    'at that',
    'at the outset',
    'at the same time',
    'before',
    'before long',
    'besides',
    'by all means',
    'by and by',
    'by comparison',
    'by contrast',
    'by the same token',
    'by the way',
    'certainly',
    'clearly',
    'come to think of it',
    'consequently',
    'conversely',
    'correspondingly',
    'despite this',
    'earlier',
    'either',
    'equally',
    'essentially, then',
    'even',
    'even so',
    'even then',
    'eventually',
    'ever since',
    'except',
    'failing that',
    'finally',
    'first',
    'first of all',
    'firstly',
    'following this',
    'for a start',
    'for another thing',
    'for example',
    'for instance',
    'for one thing',
    'for that matter',
    'for this reason',
    'fortunately',
    'further',
    'furthermore',
    'having said that',
    'hence',
    'however',
    'if not',
    'if so',
    'in a different vein',
    'in actual fact',
    'in addition',
    'in any case',
    'in conclusion',
    'in contrast',
    'in fact',
    'in other words',
    'in particular',
    'in short',
    'in spite that',
    'in sum',
    'in that case',
    'in the beginning',
    'in the case of',
    'in the end',
    'in the event',
    'in the first place',
    'in the hope that',
    'in the meantime',
    'in this way',
    'in truth',
    'in turn',
    'in which case',
    'incidentally',
    'indeed',
    'initially',
    'instantly',
    'instead',
    'just',
    'just then',
    'last',
    'lastly',
    'later',
    'likewise',
    'luckily',
    'mainly because',
    'meanwhile',
    'merely',
    'mind you',
    'moreover',
    'much later',
    'much sooner',
    'naturally',
    'nevertheless',
    'next',
    'no doubt',
    'nonetheless',
    'not because',
    'not only',
    'not that',
    'notably',
    'on the contrary',
    'on the one hand',
    'on the one side',
    'on the other hand',
    'on the other side',
    'on top of this',
    'once again',
    'once more',
    'originally',
    'otherwise',
    'overall',
    'plainly',
    'presently',
    'previously',
    'put another way',
    'rather',
    'reciprocally',
    'regardless of that',
    'second',
    'secondly',
    'similarly',
    'simultaneously',
    'soon',
    'specifically',
    'still',
    'subsequently',
    'suddenly',
    'summarising',
    'summing up',
    'sure enough',
    'surely',
    'that is',
    'that is to say',
    'then again',
    'thereafter',
    'thereby',
    'therefore',
    'third',
    'thirdly',
    'this time',
    'though',
    'thus',
    'to be sure',
    'to begin with',
    'to conclude',
    'to make matters worse',
    'to start with',
    'to sum up',
    'to summarise',
    'to take an example',
    'too',
    'true',
    'ultimately',
    'undoubtedly',
    'unfortunately',
    'well',
    'what is more',
    'whereas',
    'whereupon'
]

# def sentences_tokenize (document) :



# CP = Cue-phrase score,
# CPS = Number of cue-phrases in the sentence,
# CPD = Total number of cue-phrases in the document

# Lendo todos os arquivos
files = []
for name_file in onlyfiles:
    file = open('documents/' + name_file)
    files.append({'document': [line.rstrip("\n").strip() for line in file.readlines()], 'doc_id': name_file})

print(len(files))
#files = [files[0]]
dict_document = []
cue_phrases_document = 0

for file in files:
    # Current Document
    # Tokenize Line
    dict_sentences = {}
    document = file['document']
    doc_id = file['doc_id']
    good_sentences = []
    for line in document:
        cue_phrases_sentence = 0
        sentences = sent_tokenize(line)
        for sentence in sentences:
            for cue_phrase in conj_adverb:
                # MATCH
                exactMacth = re.compile(cue_phrase, flags=re.IGNORECASE)
                match = exactMacth.findall(sentence)
                cue_phrases_sentence += len(match)

            if cue_phrases_sentence > 0:
                dict_sentences[sentence] = cue_phrases_sentence
        cue_phrases_document += cue_phrases_sentence

    # Calcule Cue Phrase Score
    if len(dict_sentences) > 0:
        for sentence in dict_sentences:
            cps = dict_sentences[sentence]

            cp = cps / cue_phrases_document
            good_sentences.append({'sentence': sentence, 'cp': cp})

        # Get the best sentences in document
        newlist = sorted(good_sentences, key=lambda k: k['cp'], reverse=True)[:4]
        dict_document.append({'sentences': newlist, 'doc': doc_id})
    else:
        dict_document.append({'sentences': 'NOT CUEPHRASE', 'doc': doc_id})


print(sorted(dict_document, key=lambda k: k['doc']))


# Preciso adicionar as 4 melhores sentenças do Documento

# for sentence in file['document']:

#         for cue_phrase in conj_adverb:
#             # Match
#             exactMatch = re.compile(cue_phrase, flags=re.IGNORECASE)
#             match = exactMatch.findall(sentence)
#
#             # Cue Phrases in Document
#             cue_phrases_document += len(match)
#
#             # Cue Phrases In Sentence
#             cue_phrases_sentence += len(match)
#
#         if cue_phrases_sentence > 0:
#             dict_sentences[sentence] = cue_phrases_sentence
#
#     max_cp = -99999
#     for sentence in dict_sentences:
#         cps = dict_sentences[sentence]
#         cp = cps / cue_phrases_document
#         if max_cp < cp:
#             max_cp = cp
#             dict_document.append({'sentence': sentence, 'cp': cp})
#
# print(dict_document)

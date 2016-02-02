__author__ = 'rodrigo'

import re
from os import listdir
from operator import itemgetter
from os.path import isfile, join
from nltk.tokenize import sent_tokenize
from utils import cue_phrases

def read_all_files():
    files = []
    onlyfiles = [f for f in listdir('documents') if isfile(join('documents', f))]
    for name_file in onlyfiles:
        file = open('documents/' + name_file)
        files.append({'document': [line.rstrip("\n").strip() for line in file.readlines()], 'doc_id': name_file})

    return files

# Lendo todos os arquivos
files = read_all_files()

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
            for cue_phrase in cue_phrases:
                # MATCH
                exactMacth = re.compile(cue_phrase, flags=re.IGNORECASE)
                match = exactMacth.findall(sentence)
                cue_phrases_sentence += len(match)

            if cue_phrases_sentence > 0:
                dict_sentences[sentence] = cue_phrases_sentence
        cue_phrases_document += cue_phrases_sentence

    # Calcule Cue Phrase Score
    # CP = Cue-phrase score,
    # CPS = Number of cue-phrases in the sentence,
    # CPD = Total number of cue-phrases in the document
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

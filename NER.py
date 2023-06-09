#using NER

import spacy

nlp = spacy.load('en_core_web_sm')
tokens2 = nlp(sent2)

print([token.text for token in tokens2])

from nltk.tokenize import sent_tokenize
print(sent_tokenize(sent))
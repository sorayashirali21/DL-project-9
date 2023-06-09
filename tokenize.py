#tokenize
from nltk.tokenize import sent_tokenize
print(sent_tokenize(sent))

import nltk
tokens = word_tokenize(sent)
print(nltk.pos_tag(tokens))
nltk.help.upenn_tagset('PRP')
nltk.help.upenn_tagset('VBP')

print([(token.text, token.pos_) for token in tokens2])

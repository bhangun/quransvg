import nltk

#nltk.download()

import codecs
#f = codecs.open('/Users/bhangun/workalmustanir/quransvg/raw_surah/q001.txt', 'r', 'utf-8-sig')
f = codecs.open('/Users/bhangun/workalmustanir/quransvg/raw_surah/q002.txt', 'r', 'utf-8-sig')
text = f.read()
a = nltk.word_tokenize(text)
f = nltk.FreqDist(a)
print(f.most_common(500))
import nltk
from nltk.corpus import gutenberg
import codecs

f1 = '/Users/bhangun/workalmustanir/quransvg/raw_surah/q001.txt'
f = codecs.open(f1, 'r', 'utf-8-sig')
#f = codecs.open('/Users/bhangun/workalmustanir/quransvg/raw_surah/q002.txt', 'r', 'utf-8-sig')
#f = codecs.open('/Users/bhangun/workalmustanir/quransvg/quran_text/quran-uthmani.txt', 'r', 'utf-8-sig')
#f = codecs.open('/Users/bhangun/workalmustanir/quransvg/quran_text/quran-simple-clean.txt', 'r', 'utf-8-sig')
text = f.read()

#nltk.download('gutenberg')

#raw = gutenberg.raw(text)
#ff = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
#ww = ff.keys()
#print(ww)


import unicodedata
lines = codecs.open(f1, encoding='utf8').readlines()
line = lines[2]
print(line.encode('unicode_escape'))

#a = nltk.word_tokenize(f)
#print(text.find('ٱللَّهِ'))
#print(a[1:5].count)
#f = nltk.FreqDist(a)
#print(f)
#o=f.most_common(100000)
#print(o)
#out = open("quran-index-clean.txt", "a")
#for x in o:
#   out.write("%s\n" %(x,))
#out.close()

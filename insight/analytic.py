import nltk

#nltk.download('punckt')
#nltk.download('stopwords')

import codecs
#f = codecs.open('/Users/bhangun/workalmustanir/quransvg/raw_surah/q001.txt', 'r', 'utf-8-sig')
#f = codecs.open('/Users/bhangun/workalmustanir/quransvg/raw_surah/q002.txt', 'r', 'utf-8-sig')
f = codecs.open('/Users/bhangun/workalmustanir/quransvg/quran_text/quran-uthmani-clean.txt', 'r', 'utf-8-sig')
#f = codecs.open('/Users/bhangun/workalmustanir/quransvg/quran_text/quran-simple-clean.txt', 'r', 'utf-8-sig')

text = f.read()

a = nltk.word_tokenize(text)
print(a)
#print(text.find('هُوَ'))
#print(a[1:5].count)

f = nltk.FreqDist(a)
#print(f)

o=f.most_common(100000)
#print(o)
print(len(o))

#text = nltk.Text(a)
#text.collocations()
#print(text)

#out = open("quran-text.txt", "a")
#for x in o:
#   out.write("%s\n" %(x,))
#out.write(str(text))
#out.close()



#tagger = nltk.pos_tag(text)
#nltk.corpus.treebank.tagged_words(tagset='universal')
#print(tagger)


# Total char in each words
#for word in f:
#    print(word, '(' + str(len(word)) + '),')

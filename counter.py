import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from nltk.probability import FreqDist
from collections import Counter
text = open("results.txt").read()
tokenized = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered = [w for w in tokenized if not w in stop_words]
final = [word for word in filtered if word.isalnum()]
#fdist  = FreqDist(final)
#print(type(fdist))
#print(fdist.most_common(50))
fin = Counter(final)
print(fin)
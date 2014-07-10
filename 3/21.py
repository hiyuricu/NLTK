import re
import nltk
from urllib import urlopen
cor = nltk.corpus.words.words()
def unknown(url):
    f = open("answer21.txt","w")
    html = urlopen(url).read()
    raw = nltk.clean_html(html)
    l2 = sorted(set([w.lower() for w in re.findall('\w+', raw)]))
    answer = [w for w in l2 if w not in cor]
    for w in answer:
        f.write(w)
        f.write("\n")
    f.close()

if __name__ == "__main__":
	import sys
	unknown(sys.argv[1])
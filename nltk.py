import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
sample_text = state_union.raw("1.txt")
tokenized = PunktSentenceTokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words = nltk.tokenize(i)
            tagged=nltk.pos_tag(words)

            print(tagged)

    except Exception  as e:
        print(str(e))


process_content()

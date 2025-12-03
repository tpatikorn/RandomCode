import re
from nltk.stem import SnowballStemmer
from bow_constants import text_eat, stop_words, split_re

stemmer = SnowballStemmer("english")

def get_count(text, minimum=2):
    words = re.split(split_re, text.lower())
    words = list(map(lambda w: stemmer.stem(w), words))
    word_count = set(
        filter(lambda p: (p[0] not in stop_words and p[1] >= minimum),
               map(lambda w: (w, words.count(w)), words)))
    return sorted(word_count, key=lambda f: f[1], reverse=True)

print(get_count(text_eat))

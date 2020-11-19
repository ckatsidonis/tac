"""Filter out stopwords for word cloud"""

import sys
import nltk
try:
    from nltk.corpus import stopwords
except LookupError:
    nltk.download('stopwords')
    from nltk.corpus import stopwords

sw = stopwords.words("french")
sw += ["les", "plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout",
       "ils", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous",
       "celle", "entre", "encore", "toutes", "pendant", "moins", "dire", "cela", "non",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres",
       "van", "het", "autre", "jusqu", "oktober", "klein", "décembre", "ville",
       "bruxelles", "conseil communal","mesdames", "messieurs", "bourgmestre", 
       "commune","communal", "franc", "question", "belge","commission", "très",
       "rue","francs","ceux","pourrait","belgique", "conseil","collège",
       "année","assistance","demande","service","cour","proposition","article",
       "septembre","favorable","grand","concerne","total","personnel","moment",
       "toute","certain","août","leurs", "peuvent","relative","peu",
       "également","voir","elles","grande","nombre","celui",
       "cours","laquelle","née","mar","divers"]
sw = set(sw)


def filtering(year, folder=None):
    if folder is None:
        input_path = f"{year}.txt"
        output_path = f"{year}_keywords.txt"
    else:
        input_path = f"{folder}/{year}.txt"
        output_path = f"{folder}/{year}_keywords.txt"
    output = open(output_path, "w", encoding='utf-8')
    with open(input_path, encoding='utf-8') as f:
        text = f.read()
        words = nltk.wordpunct_tokenize(text)
        kept = [w.lower() for w in words if len(
            w) > 2 and w.isalpha() and w.lower() not in sw]
        kept_string = " ".join(kept)
        output.write(kept_string)
    return f'Output has been written in {output_path}!'


if __name__ == '__main__':
    data_path = sys.argv[1]
    chosen_year = sys.argv[2]
    filtering(data_path, chosen_year)

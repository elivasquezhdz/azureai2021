from summa.summarizer import summarize
import nltk
import sys

uuid = sys.argv[1]

with open("results/{}/text.txt".format(uuid)) as f:
    text = f.read()

text = text.replace("\n","")
summary = summarize(text, language='english')

with open("results/{}/summary.txt".format(uuid)) as f:
    f.write(summary)
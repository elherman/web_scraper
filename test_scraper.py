#!usr/bin/env python3
# Author: Emma Herman

import bs4
import console
import requests
import urllib
import nltk
from bs4 import BeautifulSoup
#import word_cloud

page = urllib.request.Request( 'https://newrepublic.com/article/122745/drunk-confessions-women-and-cliches-literary-drunkard')
article = urllib.request.urlopen(page)
soup = BeautifulSoup(article, 'html.parser')

body = soup.find("div",{"class":"content-body"}).get_text(strip=True)
paragraph = body.split()
wordfreq =  [paragraph.count(w) for w in paragraph]

print("String\n" + body +"\n")
print("List\n" + str(paragraph) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\"n" + str(list(zip(paragraph, wordfreq))))

with open('google10k.txt','r') as f:
    dta = f.read()
cw10k = dta.split('\n')

#remove punctuation from paragraph

list(set(paragraph) - set(cw10k))

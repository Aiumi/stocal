from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
from shf import algo
import sys

#sys.stdout = open('output.txt', 'w')

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts) 
    return u" ".join(t.strip() for t in visible_texts)

'''html = urllib.request.urlopen('https://www.nbcnews.com/business/business-news/what-boycott-nike-sales-are-31-percent-kaepernick-campaign-n908251').read()
print(text_from_html(html))
phraseFreq(text_from_html(html))'''



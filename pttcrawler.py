
# coding: utf-8

# In[17]:


import requests
from bs4 import BeautifulSoup
import re


# In[18]:



#print (plaintext)


# In[52]:


def pttcrawler(min_pages):
    page = 4042
    while page > min_pages:
        url = 'https://www.ptt.cc/bbs/Stock/index'+str(page)+'.html'
        source = requests.get(url)
        plaintext = source.text
        soup = BeautifulSoup(plaintext,"lxml")
        for link in soup.findAll("div",{"class":"title"}): 
            if link.findAll('a'):
                res = link.findAll('a')[0]
            else:
                continue
            title = res.string
            href = "https://www.ptt.cc" +res.get('href')
            #print (title,href)
            get_article_text(href)

        page -=1

def get_article_text(url):
    source = requests.get(url)
    plaintext = source.text
    soup = BeautifulSoup(plaintext,"lxml")   
    for link in soup.findAll("div",{"id":"main-content"}):
        res = link.findAll('div',{"class":"article-metaline"})[0]
        author = res.findAll('span',{"class":'article-meta-value'})[0]
        print (author.string)
pttcrawler(4041)


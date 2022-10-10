#Arjun Venkat - asv180003
#Arjun Balasubramanian - axb200075

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('stopwords')
nltk.download('punkt')

import re
import os

def crawl(base_url, levels = 1):
    global urls ## get the set of urls
    baseparse = urllib.parse.urlparse(base_url) ## get the parsed url
    try:
        basepage = urllib.request.urlopen(base_url) ## open the basepage
    except Exception as e:
        return ## exit if the open doesn't work
    soup = BeautifulSoup(basepage) ## get the soup
    
    for link in soup.find_all("a", href=True): ## find all the links
        parsed_url = urllib.parse.urlparse(link['href']) ## get the parts of the link
        if parsed_url.scheme == '' and parsed_url.netloc == '': ## check if local link or link to another page
            url = ''.join([baseparse.scheme, '://', baseparse.netloc, parsed_url.path]) ## join the parts of the url
            if(url not in urls) and levels != 0: ## make sure we havent seen this url and check the level
                crawl(url, levels - 1) ## some recursion if we want to go deeper (we can keep going until and getting more links)
            urls.add(url) ## add the url to the set
        elif isValid(link['href']): ## check if url is valid
            if(link['href'] not in urls) and (levels != 0): ## make sure the url isnt in the set
                crawl(url, levels - 1) ## recursion
            urls.add(link['href']) ## add to the set

def isValid(url):
    sketchUrl = urllib.parse.urlparse(url) ## break the url into parts
    if sketchUrl.scheme and sketchUrl.netloc: ## check if the scheme and netloc are empty
        return True
    else:
        return False

def scrape(urls):
  current_directory = os.getcwd()
  final_directory = os.path.join(current_directory, r'pagedata')
  if not os.path.exists(final_directory):
    os.makedirs(final_directory)
    for url in urls:
        try:
            page = urllib.request.urlopen(url)
        except Exception as e:
            print("Couldn't access the page : " + url)
            continue
        soup = BeautifulSoup(page)
        page_text = ''
        for tag in soup.find_all('p'):
            page_text = page_text + ' ' + tag.get_text()
        fname = re.sub('[<>:"\/|?*]',"",url)
        if(len(fname) > 100):
            fname = fname[:100]
        fname = 'pagedata/' + fname + '.txt'
        try:
            f = open(fname, "w+")
            f.write(page_text)
            f.close()
        except Exception as E:
            print("Couldn't write : " + url)

## CLEAN UP THE TEXT
def cleanText(text):
    text = text.replace('\n', '') ## remove newline
    text = text.replace('\t', '') ## remove tabs
    text = text.lower() ## lowercase letters
    return text

def cleanFiles(path):
    for file in os.listdir(path): ## go through the files
        fname = os.path.join(path,file) ## get the filepath
        f = open(fname, 'r') ## open to read
        text = f.read() ## read the file
        text = cleanText(text) ## clean the text
        sent_tokens = sent_tokenize(text) ## tokenize the text
        f.close() ## close the file
        #for token in sent_tokens:
          #print(type(sent_tokens))

def get_top_terms(path):
  
  #get all the tokens from all files
  tokens = []
  for file in os.listdir(path):
    fname = os.path.join(path,file)
    with open(fname, 'r') as f:
      text = f.read()
      tokens.extend(word_tokenize(text))
      

  #clean up tokens and find frequencies of words
  tokens = [t for t in tokens if t.isalpha() and t not in stopwords.words('english')]
  frequency_dict = {t:tokens.count(t) for t in set(tokens)}
  frequency_dict = {k: v for k, v in sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)}
  top_25_freq = {k: frequency_dict[k] for k in list(frequency_dict)[:25]}
  return top_25_freq

#main code
urls = set()
starting_url = 'https://www.usatoday.com/story/tech/2022/10/05/apple-universal-charger-after-eu-votes-new-rule/8188187001/'
urls.add(starting_url)
crawl(starting_url, levels = 0)
scrape(urls)
cleanFiles('pagedata')
file_word_freq_dict = get_top_terms('pagedata')

#the top 25 most frequent words
print(file_word_freq_dict)

#knowledge base
knowledge_base = {}

knowledge_base['computer'] = 'A ccomputer an electronic device for storing and processing data, typically in binary form, according to instructions given to it in a variable program.'
knowledge_base['version'] = 'An operating system can have different versions with updates to improve performance.'
knowledge_base['story'] = 'A story is an account of imaginary or real people and events told for entertainment.'
knowledge_base['professor'] = 'A professor is a teacher of the highest rank in a college or university.'
knowledge_base['news'] = 'The news covered the election that happened today."
knowledge_base['USA'] = 'The current president of the USA is Joe Biden.'
knowledge_base['assistant'] = 'The managing director and his assistant oversaw the project'
knowledge_base['media'] = 'The news is covered on various forms of media, including print and television.'
knowledge_base['engineering'] = 'Engineering is the branch of science and technology concerned with the design, building, and use of engines, machines, and structures.'
knowledge_base['electrical'] = 'Electrical engineers often have to design circuits and wiring.'

import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import pickle

## 1.a
def getDicts(filename): ## create the function, takes in the training filename
    
    ## 1.b
    f = open(filename, "r", encoding='utf-8') ## open the file
    text = f.read() ## read the entire contents of the file
    f.close() ## close the file
    text.replace('\n', '') ## remove the newlines
    
    ## 1.c
    tokens = word_tokenize(text) ## tokenize the words
    
    ## 1.d
    bigrams = list(ngrams(tokens, 2)) ## create the list of bigrams
    
    ## 1.e
    unigrams = tokens ## create the list of unigrams (basically just the tokens)
    
    ## 1.f
    bigram_dict = {b: bigrams.count(b) for b in set(bigrams)} ## create the count dict for bigrams
    
    ## 1.g
    unigram_dict = {t: unigrams.count(t) for t in set(unigrams)} ## create the count dict for unigrams
    
    ## 1.h
    return unigram_dict, bigram_dict ## return the bigram and unigram dict


if __name__ == '__main__':
    ## i
    uni_eng, bi_eng = getDicts('ngram_files/LangId.train.English') ## create the english dicts
    #print("English Completed")
    uni_fr, bi_fr = getDicts('ngram_files/LangId.train.French') ## create the french dicts
    #print("French Completed")
    uni_it, bi_it = getDicts('ngram_files/LangId.train.Italian') ## create the italian dicts
    #print("Italian Completed")
    
    ## pickle all the created dictionaries
    pickle.dump(uni_eng, open("uni_eng.p","wb"))
    pickle.dump(bi_eng, open("bi_eng.p","wb"))
    pickle.dump(uni_fr, open("uni_fr.p","wb"))
    pickle.dump(bi_fr, open("bi_fr.p","wb"))
    pickle.dump(uni_it, open("uni_it.p","wb"))
    pickle.dump(bi_it, open("bi_it.p","wb"))
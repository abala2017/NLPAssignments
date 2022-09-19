## Arjun Balasubramanian
## axb200075


import nltk
import sys
#nltk.download('stopwords')
from nltk.tokenize import word_tokenize ## import the tokenizer
from nltk.corpus import stopwords ## import the stopwords
from nltk.stem import WordNetLemmatizer ## import the lemmatizer
from random import seed ## import the seeds for the random
from random import randint ## import the random
seed(42) ## set the seed

#1
if( len(sys.argv) != 2): ## check if system arguement is given
    print("Error: No file given") ## gives an error
    exit() ## exit the program
f = open(sys.argv[1], "r") ## open the corpus file

# 2

raw_text = f.read() ## read the corpus in
tokens = word_tokenize(raw_text) ## tokenize the corpus
unique_tokens = set(tokens) ## get the unique tokens
lexical_diversity = len(unique_tokens) / len(tokens) ## get the lexical diveristy by dividing unique / total
print("The lexical diversity is %.2f" % (lexical_diversity)) ## print out results

# 3
def process_raw_text(raw_text):
    # a
    lower_text = raw_text.lower() ## lower the text
    tokens = word_tokenize(lower_text) ## tokenize the text
    tokens = [word for word in tokens if word.isalpha()] ## take out non-alphabetical tokens
    stop_words = set(stopwords.words('english')) ## set the stopwords
    tokens = [word for word in tokens if word not in stop_words] ## remove the stopwords from the token
    tokens = [word for word in tokens if len(word) > 5] ## remove the words shorter than 5 letters
    
    # b
    lemmatizer = WordNetLemmatizer() ## create the lemmatizer object
    lemmas = [lemmatizer.lemmatize(word) for word in tokens] ## lemmatize the tokens
    uniq_lemmas = set(lemmas) ## get the unique tokens
    
    # c
    tags = nltk.pos_tag(uniq_lemmas) ## tag the parts of speech
    print("The first 20 tagged items :") ## print out the first 20 tags
    print(tags[:20])
    print("\n")
    
    #d
    nouns = [tag[0] for tag in tags if tag[1][:2] == "NN"] ## take out all the non-nouns

    #e
    print("The number of tokens is " + str(len(tokens))) ## print the number of tokens
    print("The number of nouns is " + str(len(nouns))) ## print the number of nouns
    
    #f
    return tokens,nouns ## return tokens and nouns


tokens, nouns = process_raw_text(raw_text) ## call the function


# 4
noun_count = {nouns[i] : tokens.count(nouns[i]) for i in range(len(nouns))} ## get the count of each noun
sorted_count = sorted(noun_count.items(), key=lambda x:x[1], reverse = True) ## sort them by most common
most_common = sorted_count[:50] ## get the first 50 common nouns
print("The most common words and their count : ") ## print them out
print(most_common)
word_bank = [word[0] for word in most_common] ## get the words from the list of tuples



#5
def guessing_game(word_bank):
    print("Let's play a word guessing game!") ## print the starting dialouge
    points = 5 ## set the points
    lose = win = False ## set the win/lose conditions
    word = word_bank[randint(0,49)] ## pick the word
    guessed = [] ## letters guessed by user
    while((not lose) and (not win)): ## make sure the user has not won or lost
        print("".join([letter if letter in guessed else "-" for letter in word])) ## print out the dashes
        guess = input("Guess a letter: ") ## print the prompt and get the next letter
        if(len(guess) != 1): ## validate the input
            print("invalid input ಠ_ಠ") ## complain if its not correct
            continue ## restart the loop
        if(guess in guessed): ## check if they guessed the letter already
            print("already guessed (ง •̀_•́)ง") ## complain
            continue ## restart loop
        guessed += guess ## add guess to the guessed letters
        if(guess in word): ## check if the guessed letter is in the goal word
            points = points + 1 ## if it is increase points
            print("Right! Score is " + str(points) + " ヘ( ^o^)ノ＼(^_^ )") ## congratulate
        else:
            points = points - 1 ## if not, decrease points
            print("Sorry, wrong guess. Score is " + str(points) + " ¯\_(ツ)_/¯") ## print score and miss
        win = set(word).issubset(set(guessed)) ## win condition met if all the letters have been guessed
        if(points == 0): ## check if we reached 0 points
            lose = True ## lose condition met if points = 0
    if(win): ## if the player wins
        print("You solved it!") ## congratulate
        print("Final Score: " + str(points)) ## print final score
        print("( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)") ## the crowd goes wild
    else: ## if the player loses
        print("Maybe next time o(╥﹏╥)o") ## help them deal with the loss


guessing_game(word_bank) ## play the game

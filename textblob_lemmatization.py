from textblob import Word

# Lemmatization: reduce word to root form as found in a dictionary
def tlemmatize(word, posc=''):
    # allow for part of speech parameter optional parameter
    tword = Word(word)
    if posc != '':
        print(word,":",tword.lemmatize(posc))
    else:
        print(word,":",tword.lemmatize())


# part of speech components
# ADJ, ADJ_SAT, ADV, NOUN, VERB = 'a', 's', 'r', 'n', 'v'  


tlemmatize("apples")
tlemmatize("media")
tlemmatize("greater", "a") # adjective
tlemmatize("feet")
from textblob import TextBlob

text = "I love to watch football, but I have never played it"  
text_blob_object = TextBlob(text)

print(text)
for nlength in [2,3,4]:
    print('ngrams of length = ', nlength)
    for ngram in text_blob_object.ngrams(nlength):  
        print(ngram)
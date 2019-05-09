from textblob import TextBlob

text = "I love to watchf footbal, but I have never played itt"  
text_blob_object = TextBlob(text)

print('original:')
print(text)
print('corrected:')
print(text_blob_object.correct())
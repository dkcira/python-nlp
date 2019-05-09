from textblob import TextBlob

text = "I love to watch football, but I have never played it"  

text_blob_object = TextBlob(text)
text2 = text_blob_object.upper()
text3 = text_blob_object.lower()

print(text)
print(text2)
print(text3)
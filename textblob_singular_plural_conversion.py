from textblob import TextBlob  

text = ("Football is a good game. It has many health benefit")  

text_blob_object = TextBlob(text)

print('text')
print(text)
print('pluralize')
print(text_blob_object.words.pluralize())
print('singularize')
print(text_blob_object.words.singularize())
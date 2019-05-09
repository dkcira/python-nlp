from textblob import TextBlob  

# translation using the google translate API
# https://cloud.google.com/translate/docs/

print('translate')

text_blob_object_french = TextBlob(u'Salut comment allez-vous?')  
print('french:', text_blob_object_french)
print('english:',text_blob_object_french.translate(to='en'))  

text_blob_object_arabic = TextBlob(u'مرحبا كيف حالك؟') 
print('arabic:', text_blob_object_arabic)
print('english:', text_blob_object_arabic.translate(to='en'))

print('\ndetect language')
text_blob_object = TextBlob(u'Hola como estas?')
print(text_blob_object)
print(text_blob_object.detect_language())
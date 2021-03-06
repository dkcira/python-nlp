from textblob import TextBlob  

# Tokenization

# wikipedia first paragraph on AI
document = ('In computer science, artificial intelligence (AI), '\
    'sometimes called machine intelligence, is intelligence '\
    'demonstrated by machines, in contrast to the natural intelligence '\
    'displayed by humans and animals. Computer science defines AI '\
    'research as the study of \"intelligent agents\": any device that '\
    'perceives its environment and takes actions that maximize its '\
    'chance of successfully achieving its goals.[1] Colloquially, '\
    'the term \"artificial intelligence\" is used to describe machines '\
    'that mimic \"cognitive\" functions that humans associate with other '\
    'human minds, such as \"learning\" and \"problem solving\".[2]')

# create a textblob object with the TextBlob class
text_blob_object = TextBlob(document)

# tokenize sentences using the attribute
document_sentences = text_blob_object.sentences
print('tokenized sentences')
print(document_sentences)
print(len(document_sentences))

# tokenize words
document_words = text_blob_object.words
print('tokenized words')
print(document_words)
print(len(document_words))

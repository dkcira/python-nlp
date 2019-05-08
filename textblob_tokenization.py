from textblob import TextBlob  

# Tokenization

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

text_blob_object = TextBlob(document)

document_sentences = text_blob_object.sentences

print(document_sentences)
print(len(document_sentences))
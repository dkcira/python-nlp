from textblob import TextBlob  
from textblob.classifiers import NaiveBayesClassifier  

# dummy moview review data

# train data with sentiment
train_data = [  
    ('This is an excellent movie', 'pos'),
    ('The move was fantastic I like it', 'pos'),
    ('You should watch it, it is brilliant', 'pos'),
    ('Exceptionally good', 'pos'),
    ("Wonderfully directed and executed. I like it", 'pos'),
    ('It was very boring', 'neg'),
    ('I did not like the movie', 'neg'),
    ("The movie was horrible", 'neg'),
    ('I will not recommend', 'neg'),
    ('The acting is pathetic', 'neg')
]

# test data with sentiment
test_data = [  
    ('Its a fantastic series', 'pos'),
    ('Never watched such a brillent movie', 'pos'),
    ("horrible acting", 'neg'),
    ("It is a Wonderful movie", 'pos'),
    ('waste of money', 'neg'),
    ("pathetic picture", 'neg')
]

classifier = NaiveBayesClassifier(train_data)

first_text = 'It is very boring'
print('\ntext:', first_text)
print('classifier:',classifier.classify(first_text))

second_text = 'Its a fantastic series'
print('\ntext:', second_text)
print('classifier:',classifier.classify(second_text))

sentence = TextBlob(second_text, classifier=classifier)
print('as a sentence:', sentence.classify())

print('\ntest data:', test_data)
print('accuracy:', classifier.accuracy(test_data))
print('\n')
classifier.show_informative_features(3)  

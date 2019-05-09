import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib
#%matplotlib inline # for notebooks
from textblob import TextBlob


# data from here: https://www.kaggle.com/snap/amazon-fine-food-reviews/
reviews_datasets = pd.read_csv(r'/Users/dorian/Downloads/Reviews.csv')
reviews_datasets = reviews_datasets.head(20000) # get just the first 20K
reviews_datasets.dropna() # drop not-a-number

# show the first lines
print('first lines of reviews dataset')
print(reviews_datasets.head())

sns_plot = sns.distplot(reviews_datasets['Score'])
sns_plot.get_figure().savefig('sentiment_analysis_score.png')

sns_plot = sns.countplot(x='Score', data=reviews_datasets)
sns_plot.get_figure().savefig('sentiment_analysis_score2.png')

# let's get a review and find its polarity using TextBlob
print(reviews_datasets['Text'][350])
text_blob_object = TextBlob(reviews_datasets['Text'][350])
print(text_blob_object.sentiment)

# function fo adding column of sentiment polarity to the dataset
def find_pol(review):
    return TextBlob(review).sentiment.polarity

# add column to dataset
reviews_datasets['Sentiment_Polarity'] = reviews_datasets['Text'].apply(find_pol)
print('reviews dataset with sentiment polarity, just two columns')
print(reviews_datasets[['Summary','Sentiment_Polarity']].head())

# plot distribution of sentiment polarity
sns_plot = sns.distplot(reviews_datasets['Sentiment_Polarity'])
sns_plot.get_figure().savefig('sentiment_analysis_polarity.png')

# plot average polarity for each score rating
sns_plot = sns.barplot(x = 'Score', y = 'Sentiment_Polarity', data = reviews_datasets)
sns_plot.get_figure().savefig('sentiment_analysis_polarityscore.png')

# most negative reviews, where polarity value = -1
most_negative = reviews_datasets[reviews_datasets.Sentiment_Polarity == -1].Text.head()
print('most negative reviews')
print(most_negative)
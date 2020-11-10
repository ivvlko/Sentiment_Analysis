import re
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('wordnet')


def custom_clean_transformer(text):
    
    def clean_text(text):
        text = text.lower()
        text = re.sub(r"what's", "what is ", text)
        text = re.sub(r"\'s", " ", text)
        text = re.sub(r"\'ve", " have ", text)
        text = re.sub(r"can't", "can not ", text)
        text = re.sub(r"n't", " not ", text)
        text = re.sub(r"i'm", "i am ", text)
        text = re.sub(r"\'re", " are ", text)
        text = re.sub(r"\'d", " would ", text)
        text = re.sub(r"\'ll", " will ", text)
        text = re.sub('\W', ' ', text)
        text = re.sub('\s+', ' ', text)
        text = re.sub(r'\d', '', text)
        text = text.strip(' ')
        return text
    cleaned_data = [clean_text(x) for x in text]
    text=cleaned_data
    return text

    
def custom_stem_transformer(text):
    stemmer = SnowballStemmer(language='english', ignore_stopwords=True)
    brand_new_list = []
    for row in text:
        new_row = ''
        tokenized_row = word_tokenize(row)
        for word in tokenized_row:
            new_row += stemmer.stem(word) + ' '
        brand_new_list.append(new_row)
    text = brand_new_list
    return text




def clean_text(text):
    text = text.lower()
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"can't", "can not ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub('\W', ' ', text)
    text = re.sub('\s+', ' ', text)
    text = re.sub(r'\d', '', text)
    text = text.strip(' ')
    return text
    
    
def stem_series(series):
    """
    We use word_tokenizer from NLTK
    for each comment which splits by
    word, then we apply stemming to each
    word and add it to 'new_row', then append
    the stemmed row to the new list and
    at the end we return it
    """
    stemmer = SnowballStemmer(language='english', ignore_stopwords=True)
    brand_new_list = []
    for row in series:
        new_row = ''
        tokenized_row = word_tokenize(row)
        for word in tokenized_row:
            new_row += stemmer.stem(word) + ' '
        brand_new_list.append(new_row)
    return brand_new_list


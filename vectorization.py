import nltk
import string
from nltk.stem import WordNetLemmatizer

#nltk.download('wordnet')
#nltk.download('punkt_tab')

sentences = ["Hattile padyo pwa.",
            "Musale padyo phush phush."]
lemmatizer = WordNetLemmatizer()

def normalize(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    lemmas = [lemmatizer.lemmatize(t) for t in tokens]
    clean = [w for w in lemmas if w not in string.punctuation]
    return clean


normal = [normalize(s) for s in sentences]


all_words = []
for s in normal:
    all_words.extend(s)

vocab = sorted(set(all_words))
print("Vocabulary:", vocab)

def bag_of_words(sentence,vocab):
    sentence_words = normalize(sentence)
    
    # Create vector: 1 if word exists, 0 otherwise
    vector = []
    for word in vocab:
     if word in sentence_words:
        vector.append(1)
     else:
        vector.append(0)
    
    return vector

sentences = ["Hattile padyo pwa.", "Musale padyo phush phush."]
vectors = [bag_of_words(s, vocab) for s in sentences]
print(vectors)

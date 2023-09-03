# importing part-of-speech function for lemmatization
from part_of_speech import get_part_of_speech

# importing a passage from Through the Looking Glass
from looking_glass import looking_glass_text

# importing Counter to get word counts for bag of words
from collections import Counter

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import re
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Change text to another string:
text = looking_glass_text

cleaned = re.sub('\W+', ' ', text).lower()
tokenized = word_tokenize(cleaned)

stopwords_list = stopwords.words('english')
filtered = [word for word in tokenized if word not in stopwords_list]

normalizer = WordNetLemmatizer()
normalized = [normalizer.lemmatize(
    token, get_part_of_speech(token)) for token in filtered]

# Comment out the print statement below
# print(normalized)

# Defining bag_of_looking_glass_words & print:
bag_of_looking_glass_words = Counter(normalized)
print(bag_of_looking_glass_words)

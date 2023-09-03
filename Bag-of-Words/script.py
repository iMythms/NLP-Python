# importing regex and nltk
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# importing Counter to get word counts for bag of words
from collections import Counter

# importing a passage from Through the Looking Glass
from looking_glass import looking_glass_text

# importing part-of-speech function for lemmatization
from part_of_speech import get_part_of_speech

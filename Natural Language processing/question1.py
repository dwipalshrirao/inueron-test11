import tensorflow as tf
import tensorflow_text as text
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
import spacy
from autocorrect import Speller

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")








def preprocess_text(text):
    # Emoji Removal

    text = re.sub(r'[\U00010000-\U0010ffff]', '', text)
    print()

    text = nlp(text)

    # Lemmatization
    words = [word.lemma_ for word in text]
    print(words)

    # Grammar Correction
    words = [author_correct_word(word) for word in words]

    # Http Links Removal
    text = [re.sub(r'http\S+', '',word ) for word in words] 

    # Stop Words Removal
    stop_words = set(stopwords.words('english'))
    words = [word.numpy().decode('utf-8') for word in words.numpy() if word.numpy().decode('utf-8') not in stop_words]
    
    # Lowercasing
    words = [word.lower() for word in words]

    # Remove white spaces
    words =  [word.strip() for word in words if word.strip()]

    # text normalization
    text = ' '.join(words)
    print(text)





    # Part of speech tagging using SpaCy
    pos_tags = [(token.text, token.pos_) for token in nlp(text.numpy().decode('utf-8'))]
    

# Example usage
input_text = "Adds word-relevant emojis to text with sometimes hilarious 😂 results 😏. Read more about its history 📚 and how it works"

# preprocessed_data = preprocess_text(input_text)

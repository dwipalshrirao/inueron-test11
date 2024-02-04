import spacy
import spellchecker
import re

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")


def author_correct_word(misspelled_word):
    # Create a spell checker object
  spellcheckerobj = spellchecker.SpellChecker()
  if misspelled_word:
    # Check the spelling of a word
    corrected_word = spellcheckerobj.correction(misspelled_word)

    # Print the corrected word
    print(corrected_word)
    return corrected_word
  return ""





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
    words = [re.sub(r'http\S+', '',word ) for word in words] 

    # Stop Words Removal
    words = [word for word in words if nlp(word).is_stop]
    
    # Lowercasing
    words = [word.lower() for word in words]

    # Remove white spaces
    words =  [word.strip() for word in words if word.strip()]

    # text normalization
    text = ' '.join(words)
    return text


# Example usage
input_text = "Adds word-relevant emojis to text with sometimes hilarious 😂 results 😏. Read more about its history 📚 and how it works"

preprocessed_data = preprocess_text(input_text)
print(preprocessed_data)
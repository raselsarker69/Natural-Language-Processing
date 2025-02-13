import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download NLTK data
nltk.download('punkt')  
nltk.download('stopwords')  
nltk.download('wordnet')  
nltk.download('averaged_perceptron_tagger')  

# Read Text File
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

file_path = 'bangla.txt'
input_text = read_file(file_path)


# Text Cleaning
def clean_text(text):
    words_to_remove = ['১', '১১৮', 'ক', '১', 'খ', '১', 'গ', '১৮', '২০১৮', '৩', '১', 'মার্চ', 'শ্রেণি', 'ঘ', '১১১', '০', '০']
    # Create a regex pattern to match whole words
    pattern = r'\b(?:' + '|'.join(map(re.escape, words_to_remove)) + r')\b'
    
    text = re.sub(r'[,:.» ঃ()\[\]*৳$₹/£%_;“”॥।€|!\'-]', '', text)  
    
    text = re.sub(r'\d+', '', text)  
    text = re.sub(r'\n\s*\n', '\n', text)  # Replace multiple newlines with a single newline
    noise_pattern = r'[^\s]*প্র.*প্র[^\s]*'  
    text = re.sub(r'\bpage\b', '', text, flags=re.IGNORECASE)  # Remove standalone 'page' (case-insensitive)
    text = re.sub(noise_pattern, '', text)
    # Remove specific keywords if they are noise
    text = re.sub(r'\b(Proper Noun|Other|Adjective|Noun|Conjunction)\b', '', text, flags=re.IGNORECASE)
    text = text.strip().lower()  
    return text

cleaned_text = clean_text(input_text)


# Tokenization
def tokenize_text(text):
    return word_tokenize(text)

tokens = tokenize_text(cleaned_text)


# Remove Stopwords
def remove_stopwords(tokens, language='bengali'):
    stop_words = set(stopwords.words(language))
    return [word for word in tokens if word not in stop_words]

filtered_tokens = remove_stopwords(tokens)


# Stemming
def stem_tokens(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(word) for word in tokens]

stemmed_tokens = stem_tokens(filtered_tokens)


# Lemmatization
def lemmatize_tokens(tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in tokens]

lemmatized_tokens = lemmatize_tokens(filtered_tokens)

from bnlp import NLTKTokenizer, POS

# Initialize tokenizer and POS tagger
tokenizer = NLTKTokenizer()
bnlp_pos = POS()

# Custom POS Tagging
POS_TAG_MAP_BANGLA = {
    'NOUN': 'Noun',
    'ADJ': 'Adjective',
    'VERB': 'Verb',
    'PRON': 'Pronoun',
    'ADV': 'Adverb',
    'CONJ': 'Conjunction',
    'PREP': 'Preposition',
    'DET': 'Determiner',
    'INT': 'Interjection',
    'CARD': 'Cardinal Number',
    'FOREIGN': 'Foreign Word'
}

def custom_pos_tagging(tokens):
    standard_pos_tags = nltk.pos_tag(tokens)
    custom_tags = [(word, POS_TAG_MAP_BANGLA.get(tag, 'Other')) for word, tag in standard_pos_tags]
    return custom_tags

custom_pos_tags = custom_pos_tagging(filtered_tokens)
    


# Save Outputs with Beautiful Printing for custom_pos_tags
def save_to_file(data, file_name, beautiful=False):
    with open(file_name, 'w', encoding='utf-8') as f:
        if beautiful and all(isinstance(i, tuple) for i in data):  # Beautiful formatting for custom_pos_tags
            f.write(f"{'Word':<20}{'POS Tag':<20}\n")  # Header
            f.write("=" * 40 + "\n")  # Divider
            for word, tag in data:
                f.write(f"{word:<20}{tag:<20}\n")
        elif isinstance(data, list):
            if all(isinstance(i, tuple) for i in data):  # For POS tags (normal)
                for tag in data:
                    f.write(f"{tag[0]}: {tag[1]}\n")
            else:  # For tokens, lemmatized tokens, etc.
                f.write("\n".join(data))
        elif isinstance(data, str):  # For plain text
            f.write(data)

# Save results to respective files
save_to_file(cleaned_text, 'cleaned_text.txt')               
save_to_file(tokens, 'tokens.txt')                          
save_to_file(lemmatized_tokens, 'lemmatized_tokens.txt')    
save_to_file(custom_pos_tags, 'custom_pos_tags.txt', beautiful=True)  

print("Outputs saved to respective text files.")
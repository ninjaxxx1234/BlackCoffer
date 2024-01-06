import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import re
from nltk.tokenize import RegexpTokenizer, sent_tokenize



path = 'data/blackcoffer2.html'
url1 = 'https://insights.blackcoffer.com/oil-prices-by-the-year-2040-and-how-it-will-impact-the-world-economy/'
url2 = 'https://insights.blackcoffer.com/internet-demands-evolution-communication-impact-and-2035s-alternative-pathways/'

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, 'w') as f:
        f.write(r.text)
fetchAndSaveToFile(url2, path)
fetchAndSaveToFile(url1, 'data/blackcoffer.html')
with open("data/blackcoffer.html", "r") as f:
    html_doc = f.read()
def clean_tokens(tokens):
    cleaned_tokens = []
    for token in tokens:
        # Remove special characters
        clean_token = re.sub(r'[^a-zA-Z0-9\s]', '', token)
        # Remove hyperlinks
        clean_token = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '',
                             clean_token)

        # Check if the token is not empty after cleaning
        if clean_token == token:
            cleaned_tokens.append(clean_token.upper())

    return cleaned_tokens
soup = BeautifulSoup(html_doc, 'html.parser')
entry_title_h1 = soup.find('h1', class_='entry-title')
post_content_div = soup.find('div', class_='td-post-content tagdiv-type')
# Extract text from the h1 tag
if entry_title_h1:
    entry_title_text = entry_title_h1.get_text(strip=True)
    title = entry_title_text
    print("Title:", entry_title_text)

# Find the div with class="td-post-content tagdiv-type"
if post_content_div:
    # Get text from <p> tags that don't have links and are not in any strong tag
    text_from_p_tags = [p.get_text(strip=True) for p in post_content_div.find_all('p') if
                        'href' not in p.attrs and not p.find_parents('strong')]
    print(text_from_p_tags)
    article = ' '.join(text_from_p_tags)
else:
    print("Div not found.")
text_from_p_tags = [p.get_text(strip=True) for p in post_content_div.find_all('p') if 'href' not in p.attrs]
print(text_from_p_tags)

article = ' '.join(text_from_p_tags)
print(article)
article_array = nltk.word_tokenize(article)
sentence_list = sent_tokenize(article)
print(sentence_list)
text_tokens = clean_tokens(article_array)
print(clean_tokens(article_array))


def average_sentence_length(text):
    sentence_list = sent_tokenize(text)
    tokens = nltk.word_tokenize(text)
    totalWordCount = len(tokens)
    totalSentences = len(sentence_list)
    average_sent = 0
    if totalSentences != 0:
        average_sent = totalWordCount / totalSentences

    average_sent_length = average_sent

    return round(average_sent_length)


def complex_word_count(text_tokens):
    complexWord = 0

    for word in text_tokens:
        vowels = 0
        if word.endswith(('es', 'ed')):
            pass
        else:
            for w in word:
                if (w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u'):
                    vowels += 1
            if (vowels > 2):
                complexWord += 1
    return complexWord

def count_syllables(word):
    """
    Count the number of syllables in a word.
    """
    vowels = "AEIOUaeiou"
    count = 0
    prev_char = ''

    for char in word:
        if char in vowels and prev_char not in vowels:
            count += 1
        prev_char = char

    # Handle special cases
    if word.endswith(("es", "ed")):
        count -= 1

    return max(count, 1)  # Ensure at least one syllable

def count_complex_words(text_tokens):
    """
    Count the number of complex words in a list of tokens.
    """
    complex_word_count = 0

    for token in text_tokens:
        syllable_count = count_syllables(token)
        if syllable_count > 2:
            complex_word_count += 1

    return complex_word_count
def percentage_complex_word(text_tokens):
    complexWord = count_complex_words(text_tokens)
    complex_word_percentage = 0
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in text_tokens if word.lower() not in stop_words]

    if len(text_tokens) != 0:
        complex_word_percentage = complexWord / len(filtered_tokens)
        complex_word_percentage*=100
    return complex_word_percentage
def fog_index(averageSentenceLength, percentageComplexWord):
    fogIndex = 0.4 * (averageSentenceLength + percentageComplexWord)
    return fogIndex
def average_words_per_sentence(text):
    # Tokenize the text into sentences
    sentences = nltk.sent_tokenize(text)

    # Tokenize each sentence into words
    words_per_sentence = [len(nltk.word_tokenize(sentence)) for sentence in sentences]

    # Calculate the average number of words per sentence
    if len(words_per_sentence) > 0:
        average = sum(words_per_sentence) / len(words_per_sentence)
        return average
    else:
        return 0
def syllable_per_word(text_tokens):
    syllables = 0
    words = 0
    for token in text_tokens:
        syllables += count_syllables(token)
        words += 1
    syllable_per_word = syllables / words if words > 0 else 0
    return syllable_per_word
def count_personal_pronouns(text):
    # Define the list of personal pronouns
    personal_pronouns = ["I", "we", "my", "ours", "us"]

    # Define the regex pattern to match the personal pronouns
    pronoun_pattern = r'\b(?:' + '|'.join(re.escape(pronoun) for pronoun in personal_pronouns) + r')\b'

    # Count occurrences of personal pronouns in the text
    total_count = sum(len(re.findall(pronoun_pattern, text, re.IGNORECASE)) for pronoun in personal_pronouns)

    # Exclude occurrences related to the country name "US"
    total_count -= len(re.findall(r'\b(?:US)\b', text, re.IGNORECASE))

    return total_count
def average_word_length(text_tokens):

    # Calculate the total number of characters in each word
    total_characters = sum(len(word) for word in text_tokens)

    # Calculate the total number of words
    total_words = len(text_tokens)

    # Calculate the average word length
    if total_words > 0:
        average_length = total_characters / total_words
        return average_length
    else:
        # Handle the case where there are no words to avoid division by zero
        return 0

averageSentenceLength = average_sentence_length(article)
print("AVERAGE SENTANCE LENGTH: ", average_sentence_length(article))
print("COMPLEX WORD COUNT: ", count_complex_words(text_tokens))

stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in text_tokens if word.lower() not in stop_words]
print(filtered_tokens)
print("WORD COUNT: ", len(filtered_tokens))
complexWordPercentage = percentage_complex_word(text_tokens)
print("COMPLEX WORD PERCENTAGE: ", complexWordPercentage)
fog_index = fog_index(averageSentenceLength, complexWordPercentage)
print("FOG INDEX: ", fog_index)
average_words_per_sentence = average_words_per_sentence(article)
print("AVERAGE WORDS PER SENTENCE: ", average_words_per_sentence)
syllable_per_word = syllable_per_word(text_tokens)
print("SYLLABLE PER WORD: ", syllable_per_word)
personal_pronoun_count = count_personal_pronouns(article)
print("PERSONAL PRONOUN COUNT: ", personal_pronoun_count)
avgWordLength = average_word_length(text_tokens)
print("AVERAGE WORD LENGTH: ", avgWordLength)


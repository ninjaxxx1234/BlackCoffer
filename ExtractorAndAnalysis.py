import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# Function to calculate subjectivity score
def subjectivity_score(positiveScore, negativeScore, cleanedTokens):
    sub_score = (positiveScore + negativeScore) / ((len(cleanedTokens)) + 0.000001)
    return sub_score

# Function to calculate average word length
def average_word_length(text_tokens):
    total_characters = sum(len(word) for word in text_tokens)
    total_words = len(text_tokens)
    average_length = total_characters / total_words if total_words > 0 else 0
    return average_length

# Function to count personal pronouns
def count_personal_pronouns(text):
    personal_pronouns = ["I", "we", "my", "ours", "us"]
    pronoun_pattern = r'\b(?:' + '|'.join(re.escape(pronoun) for pronoun in personal_pronouns) + r')\b'
    total_count = sum(len(re.findall(pronoun_pattern, text, re.IGNORECASE)) for pronoun in personal_pronouns)
    total_count -= len(re.findall(r'\b(?:US)\b', text, re.IGNORECASE))  # Exclude occurrences related to "US"
    return total_count

# Function to count syllables per word
def syllable_per_word(text_tokens):
    syllables = sum(count_syllables(token) for token in text_tokens)
    words = len(text_tokens)
    syllable_per_word = syllables / words if words > 0 else 0
    return syllable_per_word

# Function to calculate average words per sentence
def average_words_per_sentence(text):
    sentences = nltk.sent_tokenize(text)
    words_per_sentence = [len(nltk.word_tokenize(sentence)) for sentence in sentences]
    average = sum(words_per_sentence) / len(words_per_sentence) if len(words_per_sentence) > 0 else 0
    return average

# Function to calculate average sentence length
def average_sentence_length(text):
    sentence_list = sent_tokenize(text)
    tokens = nltk.word_tokenize(text)
    totalWordCount = len(tokens)
    totalSentences = len(sentence_list)
    average_sent_length = totalWordCount / totalSentences if totalSentences != 0 else 0
    return round(average_sent_length)

# Function to clean tokens by removing stop words
def textCleaner(text_tokens):
    cleaned_tokens = [token for token in text_tokens if token not in stopWordsList]
    return cleaned_tokens

# Function to calculate positive score
def positive_score(text_tokens):
    return sum(1 for word in text_tokens if word in positiveWordList)

# Function to calculate negative score
def negative_score(text_tokens):
    return -sum(1 for word in text_tokens if word in negativeWordList)

# Function to calculate polarity score
def polarity_score(positiveScore, negativeScore):
    return (positiveScore - negativeScore) / ((positiveScore + negativeScore) + 0.000001)

# Function to count syllables in a word
def count_syllables(word):
    vowels = "AEIOUaeiou"
    count = 0
    prev_char = ''
    for char in word:
        if char in vowels and prev_char not in vowels:
            count += 1
        prev_char = char
    if word.endswith(("es", "ed")):
        count -= 1
    return max(count, 1)  # Ensure at least one syllable

# Function to count complex words
def count_complex_words(text_tokens):
    return sum(1 for token in text_tokens if count_syllables(token) > 2)

# Function to calculate percentage of complex words
def percentage_complex_word(text_tokens):
    complexWord = count_complex_words(text_tokens)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in text_tokens if word.lower() not in stop_words]
    return (complexWord / len(filtered_tokens)) * 100 if len(filtered_tokens) != 0 else 0

# Function to calculate fog index
def fog_index_calculator(averageSentenceLength, percentageComplexWord):
    return 0.4 * (averageSentenceLength + percentageComplexWord)

# Function to read text files from a directory
def read_text_files(directory_path):
    text_list = []
    if os.path.isdir(directory_path):
        for filename in os.listdir(directory_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(directory_path, filename)
                with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                    try:
                        text_content = file.read()
                        text_list.append(text_content)
                    except UnicodeDecodeError as e:
                        pass
    return text_list

# Function to clean tokens by removing special characters and hyperlinks
def clean_tokens(tokens):
    cleaned_tokens = []
    for token in tokens:
        clean_token = re.sub(r'[^a-zA-Z0-9\s]', '', token)  # Remove special characters
        clean_token = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '',
                             clean_token)  # Remove hyperlinks
        if clean_token == token:
            cleaned_tokens.append(clean_token.upper())
    return cleaned_tokens

# Fetch HTML content from a URL and save it to a file
def fetchAndSaveToFile(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        with open(output_file, 'w', encoding='utf-8') as f:
            try:
                f.write(str(soup))
                print(f"HTML content scraped successfully and saved to {output_file}")
            except UnicodeEncodeError as e:
                print(f"UnicodeEncodeError: {e}")
                print("Replacing problematic characters with '-' and continuing.")
                fixed_content = str(soup).encode('utf-8', 'replace').decode('utf-8')
                f.write(fixed_content)
    except requests.RequestException as e:
        print(f"Error fetching content from {url}: {e}")

# Read stop words from text files
directory_path = 'StopWords'
result_text_list = read_text_files(directory_path)
stopWordsList = [token.upper() for text_content in result_text_list for token in nltk.word_tokenize(text_content)]

# Read positive and negative words from text files
positiveWordsFile = 'positive-words.txt'
negativeWordsFile = 'negative-words.txt'
positiveWordList = nltk.word_tokenize(open(positiveWordsFile, 'r').read())
positiveWordList = clean_tokens(positiveWordList)

negativeWordList = nltk.word_tokenize(open(negativeWordsFile, 'r').read())
negativeWordList = clean_tokens(negativeWordList)

# Output directory for HTML files
output_directory = 'Output'

# Input CSV file path
input_csv_path = "Input.xlsx - Sheet1.csv"

# Output CSV file path
output_csv_path = "Output/Output Data Structure.xlsx - Sheet1.csv"

# Read input data from CSV
df = pd.read_csv(input_csv_path, header=0)

# Initialize output DataFrame
output_df = pd.DataFrame()

# Dictionary to store article data
article_db = dict()
count = 0
# Loop through each row in the input CSV
for _, row in df.iterrows():
    url = row['URL']
    url_id = row['URL_ID']

    # Generate a unique filename based on the URL
    filename = os.path.join(output_directory, url_id + ".html")

    # Fetch and save content to the unique file
    fetchAndSaveToFile(url, filename)

    # Read the HTML content from the file
    try:
        with open(filename, "r", encoding='utf-8', errors='replace') as f:
            html_doc = f.read()
        print("File read successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        print("Replacing problematic characters with '-' and continuing.")
        html_doc = f.read().encode('utf-8', 'replace').decode('utf-8', 'replace')

    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')

    # Extract title from h1 tag
    entry_title_h1 = soup.find('h1', class_='entry-title')
    if entry_title_h1:
        entry_title_text = entry_title_h1.get_text(strip=True)
        title = entry_title_text
        print("Title:", entry_title_text)

    # Find post content div
    post_content_div = soup.find('div', class_='td-post-content tagdiv-type')

    # Extract text from all <p> tags within the specified div
    article = ''
    if post_content_div:
        text_from_p_tags = [p.get_text(strip=True) for p in post_content_div.find_all('p') if 'href' not in p.attrs and '</strong>' not in str(p)]
        print(text_from_p_tags)
        article = ' '.join(text_from_p_tags)
    else:
        # If div is not found, get all <p> tags without links and without strong
        all_p_tags = soup.find_all('p')
        text_from_p_tags = [p.get_text(strip=True) for p in all_p_tags if 'href' not in p.attrs and '</strong>' not in str(p)]
        print(text_from_p_tags)
        article = ' '.join(text_from_p_tags)
        print("Div not found.")

    # Tokenize and clean text
    article_array = nltk.word_tokenize(article)
    sentence_list = sent_tokenize(article)
    text_tokens = clean_tokens(article_array)

    # Store article data in dictionary
    article_db[url_id] = [url, title, article, text_tokens, sentence_list]

    # Calculate various metrics
    averageSentenceLength = average_sentence_length(article)
    positiveScore = positive_score(text_tokens)
    negativeScore = negative_score(text_tokens)
    polarityScore = polarity_score(positiveScore, negativeScore)
    complex_word_count = count_complex_words(text_tokens)
    percentageComplexWord = percentage_complex_word(text_tokens)
    fog_index = fog_index_calculator(averageSentenceLength, percentageComplexWord)
    averagewordspersentence = average_words_per_sentence(article)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in text_tokens if word.lower() not in stop_words]
    word_count = len(filtered_tokens)
    syllablePerWord = syllable_per_word(text_tokens)
    personal_pronoun_count = count_personal_pronouns(article)
    avgWordLength = average_word_length(text_tokens)
    subjectivityScore = subjectivity_score(positiveScore, negativeScore, text_tokens)

    # Print and save metrics to dictionary
    print("POSITIVE SCORE: ", positiveScore)
    print("NEGATIVE SCORE: ", negativeScore)
    print("POLARITY SCORE: ", polarityScore)
    print("SUBJECTIVITY SCORE: ", subjectivityScore)
    print("AVERAGE SENTENCE LENGTH: ", averageSentenceLength)
    print("COMPLEX WORD PERCENTAGE: ", percentageComplexWord)
    print("FOG INDEX: ", fog_index)
    print("AVERAGE WORDS PER SENTENCE: ", averagewordspersentence)
    print("COMPLEX WORD COUNT: ", complex_word_count)
    print("WORD COUNT: ", word_count)
    print("SYLLABLE PER WORD: ", syllablePerWord)
    print("PERSONAL PRONOUN COUNT: ", personal_pronoun_count)
    print("AVERAGE WORD LENGTH: ", avgWordLength)

    # Prepare data for DataFrame
    data = {
        'url_id': url_id,
        'url': url,
        'positive_score': positiveScore,
        'negative_score': negativeScore,
        'subjectivity_score': subjectivityScore,
        'poalrity_score': polarityScore,
        'average_sentence_length': average_sentence_length(article),
        'percentage_complex_word': percentageComplexWord,
        'fog_index': fog_index,
        'average_words_per_sentence': averagewordspersentence,
        'complex_word_count': count_complex_words(text_tokens),
        'word_count': len(filtered_tokens),
        'syllable_per_word': syllablePerWord,
        'personal_pronoun_count': personal_pronoun_count,
        'average_word_length': avgWordLength
    }

    # Replace 'output.csv' with your desired output CSV file path
    output_df = output_df._append(data, ignore_index=True)
    print(output_df)
    count += 1
output_df.to_csv(output_csv_path, index=False)
print(f"Data written to {output_csv_path}")


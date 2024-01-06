import nltk
import os
from nltk.tokenize import RegexpTokenizer, sent_tokenize
text_tokens = ['WE', 'ARE', 'IN', 'ANINTERCONNECTED', 'WORLD', 'ANY', 'CHANGE', 'IN', 'ONE', 'PART', 'OF', 'THE', 'WORLD', 'WILL', 'ALWAYS', 'LEAD', 'TO', 'SOME', 'CHANGES', 'IN', 'OTHER', 'PARTS', 'OF', 'THE', 'WORLD', 'AS', 'WELL', 'MAYBE', 'A', 'BIT', 'LATER', 'BUT', 'SURELY', 'THERE', 'WILL', 'BE', 'SOME', 'CHANGE', 'AND', 'THAT', 'IS', 'WHAT', 'WE', 'ARE', 'SEEING', 'IN', 'TODAY', 'S', 'VEHICLESARE', 'THE', 'CHANGE', 'THAT', 'WE', 'ARE', 'SEEING', 'IN', 'TODAY', 'S', 'WORLD', 'WITH', 'SO', 'MANY', 'ADVANCEMENTS', 'IN', 'TECHNOLOGY', 'ECONOMIES', 'ARE', 'GETTING', 'BIGGER', 'CHINA', 'MIGHT', 'SURPASS', 'THE', 'US', 'AND', 'BECOME', 'A', 'SUPERPOWER', 'WE', 'WILL', 'HAVE', 'INDIA', 'INCHING', 'TOWARDS', 'A', '15', 'TRILLION', 'ECONOMY', 'BY', '2040', 'AND', 'THERE', 'WILL', 'BE', 'COMPETITION', 'AMONG', 'THEMSELVES', 'TO', 'OUTSHINE', 'THE', 'OTHER', 'WE', 'ARE', 'ALSO', 'SEEING', 'APARADIGM', 'SHIFTTOWARD', 'A', 'MOREMULTIPOLAR', 'WORLDFROM', 'A', 'UNIPOLAR', 'WORLD', 'WHERE', 'POWERS', 'ARE', 'MOVING', 'TOWARDS', 'CERTAIN', 'CLUSTERS', 'OF', 'THE', 'WORLD', 'AND', 'EVERYONE', 'WANTS', 'TO', 'BE', 'A', 'PART', 'OF', 'THESE', 'CLUSTERS', 'BUT', 'IN', 'ALL', 'THESE', 'REARRANGEMENTS', 'TAKING', 'PLACE', 'WE', 'ARE', 'IN', 'A', 'WAY', 'CREATING', 'A', 'BETTER', 'AND', 'MORESUSTAINABLELIFE', 'FOR', 'OUR', 'PRESENT', 'AS', 'WELL', 'AS', 'OUR', 'FUTURE', 'GENERATIONS', 'WE', 'HAVE', 'WITNESSED', 'THE', 'COP26', 'WHERE', 'WE', 'SAW', 'LEADERS', 'OF', 'TOP', 'COUNTRIES', 'TAKING', 'PLEDGES', 'TO', 'CREATE', 'A', 'MORE', 'SUSTAINABLE', 'FUTURE', 'AND', 'THE', 'ANSWER', 'LIES', 'IN', 'A', 'SAFER', 'AND', 'GREENER', 'PLANET', 'AND', 'ELECTRIC', 'VEHICLES', 'OCCUPY', 'A', 'HUGE', 'CHUNK', 'OF', 'IT', 'INTERNAL', 'COMBUSTION', 'ENGINES', 'HAVE', 'ALREADY', 'PEAKED', 'AND', 'ELECTRIC', 'VEHICLES', 'ARE', 'GETTING', 'CHEAPER', 'AND', 'CHEAPER', 'ASGOVERNMENTSOF', 'EVERY', 'COUNTRY', 'ARE', 'ACTIVELY', 'PUSHING', 'FOR', 'ELECTRIC', 'VEHICLES', 'AS', 'WE', 'HAVE', 'SEEN', 'THE', 'JOINT', 'STATEMENT', 'IN', 'COP', '26', 'THAT', 'AS', 'BUSINESS', 'FLEET', 'OWNERS', 'AND', 'OPERATORS', 'OR', 'SHARED', 'MOBILITY', 'PLATFORMS', 'WE', 'WILL', 'WORK', 'TOWARDS', '100', 'OF', 'OUR', 'CAR', 'AND', 'VAN', 'FLEETS', 'BEING', 'ZERO', 'EMISSION', 'VEHICLES', 'BY', '2030', 'OR', 'EARLIER', 'THIS', 'IS', 'A', 'STEP', 'TOWARDS', 'THE', 'FUTURE', 'INDIA', 'WHICH', 'IS', 'HOME', 'TO', 'A', 'LARGE', 'NUMBER', 'OF', 'AND', 'CONSTITUTES', 'MORE', 'THAN', '70', 'OF', 'GLOBAL', 'SALES', 'AND', 'MORE', 'THAN', '80', 'IN', 'INDIA', 'IS', 'ALSO', 'A', 'SIGNATORY', 'TO', 'THIS', 'STATEMENT', 'AND', 'IF', 'WE', 'ANALYZE', 'IT', 'CRUDE', 'OIL', 'COAL', 'AND', 'GAS', 'ARE', 'THE', 'MOST', 'DEMANDED', 'NATURAL', 'RESOURCE', 'STILL', 'IN', 'THE', 'WORLD', 'BUT', 'IT', 'S', 'NOT', 'FREE', 'AND', 'WITH', 'THE', 'LATEST', 'SCENARIOS', 'IN', 'AND', 'AROUND', 'THE', 'WORLD', 'IT', 'S', 'BETTER', 'TO', 'SWITCH', 'TO', 'A', 'MORE', 'SAFE', 'EFFICIENT', 'ANDAFFORDABLEELECTRIC', 'VEHICLE', 'IF', 'WE', 'LOOK', 'AT', 'THEECONOMIC', 'ASPECTSOF', 'ELECTRIC', 'VEHICLES', 'IT', 'WILL', 'SURELY', 'IMPROVE', 'THE', 'LIVELIHOOD', 'OF', 'SOCIETY', 'AND', 'IN', 'TURN', 'THE', 'WORLD', 'EVS', 'ARE', 'ON', 'TRACK', 'TO', 'RISE', 'TO', '20', 'OF', 'CHINA', 'S', 'TOTAL', 'MARKET', 'BY', '2025', 'UP', 'FROM', '6', 'IN', '2020', 'AND', 'TO', '37', 'IN', 'THE', 'EU', 'FROM', '11', 'LAST', 'YEAR', 'IN', 'THE', 'THEY', 'ARE', 'FORECAST', 'TO', 'REACH', '10', 'BY', '2025', 'INDIA', 'IS', 'ALSO', 'NOT', 'LAGGING', 'INDIA', 'S', 'EV', 'MARKET', 'IS', 'STILL', 'NASCENT', 'AND', 'IS', 'FORECAST', 'TO', 'RECORD', 'A', 'CAGR', 'FROM', '2020', 'TO', '2025', 'ELECTRIFICATION', 'IS', 'EXPECTED', 'TO', 'PENETRATE', 'CARS', 'AND', 'CONNECTIVITY', 'MODES', 'LIKE', 'IN', 'INDIA', 'BY', '2030', 'IT', 'IS', 'EXPECTED', 'ABOUT', '70', 'OF', 'FLEETS', 'AND', '30', 'OF', 'PRIVATE', 'TO', 'BE', 'ELECTRIC', 'BY', '2030', 'FOR', 'PASSENGER', 'VEHICLES', '40', 'OF', 'FLEETS', 'AND', '15', 'OF', 'PRIVATE', 'CARS', 'WILL', 'BE', 'ELECTRIC', 'BY', 'THAT', 'TIME', 'THERE', 'ARE', 'ALSO', 'DIFFERENT', 'STEPS', 'TAKEN', 'BY', 'THE', 'GOVERNMENT', 'LIKE', 'TAX', 'EXEMPTIONS', 'SCHEMES', 'LIKE', 'PLI', 'FAME', 'AND', 'BATTERY', 'SWAPPING', 'POLICY', 'WE', 'MUST', 'ALSO', 'NOTE', 'THAT', 'IT', 'IS', 'ESTIMATED', 'THAT', 'AROUND', '10', 'MILLION', 'DIRECT', 'JOBS', 'WILL', 'BE', 'CREATED', 'AND', 'INDIRECTLY', 'ALMOST', '50', 'MILLION', 'JOBS', 'WILL', 'BE', 'CREATED', 'AROUND', 'THIS', 'SECTOR', 'IF', 'WE', 'LOOK', 'AT', 'THE', 'GLOBAL', 'PICTURE', 'WE', 'ARE', 'ALSO', 'SEEING', 'THAT', 'THERE', 'IS', 'APRICE', 'PARITYBETWEEN', 'BATTERY', 'VEHICLES', 'AND', 'ICE', 'VEHICLES', 'AND', 'WITH', 'SO', 'MANY', 'ADVANCEMENTS', 'IN', 'TECHNOLOGY', 'WE', 'ARE', 'SEEING', 'THE', 'PRICES', 'OF', 'BATTERIES', 'COMING', 'DOWN', 'WITH', 'MORE', 'PLAYERS', 'GETTING', 'INVOLVED', 'IN', 'IT', 'WITH', 'PRICES', 'ESTIMATED', 'TO', 'BE', 'FURTHER', 'DOWN', 'AS', 'A', 'WORLD', 'LEADER', 'COUNTRIES', 'LIKE', 'CHINA', 'AND', 'THE', 'USA', 'ARE', 'IN', 'A', 'RACE', 'TO', 'BUILD', 'MORE', 'BATTERIES', 'SO', 'THAT', 'THEY', 'HAVE', 'THE', 'CAPABILITIES', 'TO', 'FURTHER', 'RISE', 'TO', 'THE', 'OCCASION', 'OF', 'BEING', 'A', 'MAJOR', 'EXPORTERS', 'IN', 'THE', 'WORLD', 'THE', 'EUROPEAN', 'UNION', 'IS', 'ALSO', 'NOT', 'LAGGING', 'AS', 'THEY', 'ARE', 'ALSO', 'TRYING', 'TO', 'CATCH', 'UP', 'BY', 'PRODUCING', 'ENOUGH', 'BATTERIES', 'TO', 'BE', 'BY', '2025', 'CRUDE', 'OILS', 'ARE', 'INCREASING', 'DAY', 'BY', 'DAY', 'WE', 'HAVE', 'SEEN', 'A', 'SHORTAGE', 'OF', 'GAS', 'IN', 'EUROPEAN', 'COUNTRIES', 'MAINLY', 'DUE', 'TO', 'THE', 'UKRAINE', 'WAR', 'AND', 'EVERYBODY', 'IS', 'TRYING', 'TO', 'FIND', 'AN', 'ALTERNATIVE', 'TO', 'GAS', 'AND', 'CRUDE', 'OIL', 'AS', 'IT', 'IS', 'HARMFUL', 'AND', 'IT', 'S', 'ONE', 'OF', 'THE', 'MAIN', 'REASONS', 'WHYPOLLUTIONIS', 'SUCH', 'A', 'HAVOC', 'IN', 'THE', 'WORLD', 'ONE', 'OF', 'THE', 'MAJOR', 'PROBLEMS', 'OF', 'CRUDE', 'OILS', 'IS', 'OIL', 'SPILLING', 'WHICH', 'IS', 'ENDANGERING', 'MARINE', 'SPECIES', 'AIR', 'POLLUTION', 'CAUSED', 'DUE', 'TO', 'PETROL', 'AND', 'DIESEL', 'VEHICLES', 'IS', 'ALSO', 'AFFECTING', 'OUR', 'PLANET', 'AND', 'IF', 'THERE', 'IS', 'LESS', 'OIL', 'THEN', 'THERE', 'IS', 'LESS', 'POLLUTION', 'AS', 'ALTERNATIVE', 'DRIVETRAINS', 'FUEL', 'ECONOMY', 'AND', 'SHARED', 'MOBILITY', 'WILL', 'IMPACT', 'OIL', 'DEMAND', 'HOWEVER', 'NATIONS', 'STILL', 'WON', 'T', 'REACH', 'BY', '2050', 'WITHOUT', 'DOING', 'MORE', 'COAL', 'IS', 'ALSO', 'A', 'GREAT', 'CONTRIBUTOR', 'TO', 'THIS', 'POLLUTIONENVIRONMENTAL', 'IMPACTSASSOCIATED', 'WITH', 'USING', 'COAL', 'AS', 'AN', 'ENERGY', 'SOURCE', 'ARE', 'PARTICULATE', 'EMISSION', 'OZONE', 'SMOG', 'AND', 'ACID', 'RAIN', 'COAL', 'AND', 'FUEL', 'OIL', 'COMBUSTION', 'EMIT', 'FLY', 'ASH', 'PARTICLES', 'INTO', 'THE', 'ATMOSPHERE', 'WHICH', 'CONTRIBUTE', 'TO', 'AIR', 'POLLUTION', 'PROBLEMS', 'THOUGH', 'IT', 'IS', 'SAID', 'THAT', 'PRICES', 'OF', 'CRUDE', 'OIL', 'HAVEN', 'T', 'PEAKED', 'YET', 'THEY', 'WILL', 'SURELY', 'PEAK', 'BY', '2040', 'SO', 'WE', 'NEED', 'TO', 'FORESEE', 'THE', 'FUTURE', 'TO', 'HAVE', 'AN', 'ALTERNATIVE', 'IN', 'SOCIETY', 'THOUGH', 'WE', 'STILL', 'CAN', 'T', 'REACH', 'A', 'COMPLETE', 'OUTWASH', 'OF', 'OIL', 'IN', '2050', 'WE', 'CAN', 'MAKE', 'SURE', 'THAT', 'OTHER', 'ALTERNATIVES', 'ARE', 'READY', 'AND', 'WELL', 'JOB', 'OPPORTUNITIESARE', 'ALSO', 'A', 'MAJOR', 'REASON', 'WHY', 'WE', 'SHOULD', 'CONSIDER', 'EVS', 'AS', 'OUR', 'FUTURE', 'WE', 'REALIZE', 'THAT', 'THE', 'MAX', 'RANGE', 'OF', 'AN', 'ELECTRIC', 'VEHICLE', 'WILL', 'BE', 'AROUND', 'KM', 'SO', 'PEOPLE', 'NEED', 'TO', 'STOP', 'SOMEWHERE', 'TO', 'RECHARGE', 'THEIR', 'BATTERIES', 'FOR', 'AT', 'LEAST', 'MINUTES', 'WHICH', 'CAN', 'PROVIDE', 'A', 'TIME', 'FRAME', 'IN', 'WHICH', 'PEOPLE', 'CAN', 'AVAIL', 'RESTAURANTS', 'EXPLORE', 'SHOPPING', 'COMPLEXES', 'AND', 'WHAT', 'NOT', 'THIS', 'WILL', 'HELP', 'IN', 'GENERATING', 'EMPLOYMENT', 'OPPORTUNITIES', 'IN', 'HUBS', 'LIKE', 'THESE', 'THERE', 'IS', 'ALSO', 'A', 'RUSH', 'IN', 'COUNTRIES', 'LIKE', 'CHINA', 'THE', 'USA', 'AND', 'THE', 'EUROPEAN', 'UNION', 'TO', 'BUILD', 'CHARGING', 'STATIONS', 'LIKE', 'THIS', 'WHICH', 'WILL', 'ACCELERATE', 'THE', 'PROCESS', 'OF', 'EV', 'VEHICLES', 'IN', 'THIS', 'FAST', 'PACED', 'WORLD', 'ALMOST', 'EVERY', 'ALTERNATIVE', 'FAMILY', 'IS', 'HAVING', 'A', 'CAR', 'BUT', 'IF', 'PUBLIC', 'VEHICLES', 'LIKE', 'BUSES', 'AND', 'TRAINS', 'CAN', 'BE', 'CHANGED', 'INTO', 'ELECTRIC', 'VEHICLES', 'THIS', 'CAN', 'BOOST', 'THE', 'ECONOMY', 'AS', 'A', 'WHOLE', 'BY', 'CREATING', 'GREATER', 'NEEDS', 'WITH', 'MORE', 'OPPORTUNITIES', 'IN', 'THESE', 'SECTORS', 'SUCH', 'AS', 'TRANSPORTATION', 'AND', 'COMMUNICATION', 'ARE', 'VERY', 'MUCH', 'A', 'BUILDING', 'BLOCK', 'OF', 'TODAY', 'S', 'PROCESS', 'HOWEVER', 'IF', 'WE', 'ARE', 'TALKING', 'ABOUT', 'A', 'WORLD', 'THAT', 'IS', 'GREENER', 'AND', 'FITTER', 'WE', 'MUST', 'REALIZE', 'AND', 'UNDERSTAND', 'THAT', 'ELECTRIC', 'VEHICLES', 'DO', 'HAVE', 'ACOSTTO', 'THIS', 'PLANET', 'THERE', 'IS', 'A', 'HUGE', 'AMOUNT', 'OF', 'ELECTRIC', 'WASTE', 'WHICH', 'IS', 'NOT', 'SO', 'CONCERNING', 'IN', 'TODAY', 'S', 'WORLD', 'IT', 'MIGHT', 'BE', 'A', 'CONCERN', 'IN', 'THE', 'WORLD', 'WE', 'ARE', 'ALL', 'PLANNING', 'TO', 'LIVE', 'IN', 'ELECTRIC', 'VEHICLES', 'AND', 'BATTERIES', 'NEED', 'RARE', 'MATERIALS', 'WHICH', 'ARE', 'NOT', 'EASY', 'TO', 'FIND', 'ELECTRONIC', 'WASTE', 'ALSO', 'KNOWN', 'IS', 'ANY', 'ELECTRONIC', 'PRODUCT', 'OR', 'PRODUCT', 'CONTAINING', 'ELECTRONIC', 'COMPONENTS', 'THAT', 'HAS', 'REACHED', 'THE', 'END', 'OF', 'ITS', 'USABLE', 'LIFE', 'CYCLE', 'UNBEKNOWNST', 'TO', 'MANY', 'CONSUMERS', 'ELECTRONICS', 'CONTAIN', 'TOXIC', 'SUBSTANCES', 'THEREFORE', 'THEY', 'MUST', 'BE', 'HANDLED', 'WITH', 'CARE', 'WHEN', 'NO', 'LONGER', 'WANTED', 'OR', 'NEEDED', 'THERE', 'ARE', 'ALSO', 'NEGATIVE', 'EFFECTS', 'ON', 'SOIL', 'WHEN', 'THE', 'IMPROPER', 'DISPOSAL', 'OF', 'IN', 'REGULAR', 'LANDFILLS', 'OR', 'IN', 'PLACES', 'WHERE', 'IT', 'IS', 'DUMPED', 'ILLEGALLY', 'BOTH', 'HEAVY', 'METALS', 'AND', 'FLAME', 'RETARDANTS', 'CAN', 'SEEP', 'DIRECTLY', 'FROM', 'THE', 'INTO', 'THE', 'SOIL', 'CAUSING', 'CONTAMINATION', 'OF', 'UNDERLYING', 'GROUNDWATER', 'OR', 'CONTAMINATION', 'OF', 'CROPS', 'THAT', 'MAY', 'BE', 'PLANTED', 'NEARBY', 'OR', 'IN', 'THE', 'AREA', 'IN', 'THE', 'FUTURE', 'THEREFORE', 'WE', 'MUST', 'ALSO', 'NOT', 'ONLY', 'FOCUS', 'ON', 'SOLELY', 'ELECTRIC', 'VEHICLES', 'BUT', 'ALSO', 'ON', 'OTHER', 'KINDS', 'OF', 'FUELS', 'LIKE', 'GREEN', 'HYDROGEN', 'FUELS', 'LIKE', 'ETHANOL', 'WHICH', 'CAN', 'BE', 'GENERATED', 'FROM', 'AGRICULTURAL', 'WASTE', 'COMPANIES', 'PLAY', 'AN', 'IMPORTANT', 'PART', 'IN', 'THIS', 'CHANGE', 'RATHER', 'THAN', 'MAKING', 'IT', 'ONLY', 'ELECTRIC', 'THEY', 'SHOULD', 'TRY', 'TO', 'MAKE', 'VEHICLES', 'THAT', 'ARE', 'HYBRID', 'IN', 'NATURE', 'THEY', 'CAN', 'SWITCH', 'ENGINES', 'SO', 'THAT', 'THEY', 'ARE', 'READY', 'TO', 'SWITCH', 'FROM', 'PETROL', 'OR', 'DIESEL', 'TO', 'GREEN', 'HYDROGEN', 'AND', 'ETHANOL', 'AND', 'ALSO', 'TO', 'ELECTRIC', 'FUTURE', 'IS', 'S', 'TIME', 'TO', 'ACT']


def average_sentence_length(text):
    sentence_list = sent_tokenize(text)
    totalWordCount = len(tokens)
    totalSentences = len(sentence_list)
    average_sent = 0
    if totalSentences != 0:
        average_sent = totalWordCount / totalSentences

    average_sent_length = average_sent

    return round(average_sent_length)
def subjectivity_score(positiveScore, negativieScore, cleanedTokens):
    sub_score = (positiveScore + negativeScore) / ((len(cleanedTokens)) + 0.000001)
    return sub_score


def textCleaner(text_tokens):
    cleaned_tokens = []
    for token in text_tokens:
        if token not in stopWordsList:
            cleaned_tokens.append(token)
        else:
            continue
    cleanedTokenList = cleaned_tokens
    return cleanedTokenList
def positive_score(text):
    numPosWords = 0
    for word in text_tokens:
        if word in positiveWordList:
            numPosWords += 1

    sumPos = numPosWords
    return sumPos
def negative_word(text):
    numNegWords=0
    for word in text_tokens:
        if word in negativeWordList:
            numNegWords -=1
    sumNeg = numNegWords
    sumNeg = sumNeg * -1
    return sumNeg
def polarity_score(positiveScore, negativeScore):
    pol_score = (positiveScore - negativeScore) / ((positiveScore + negativeScore) + 0.000001)
    return pol_score
def read_text_files(directory_path):
    text_list = []

    # Check if the specified path is a directory
    if os.path.isdir(directory_path):
        # Loop through all files in the directory
        for filename in os.listdir(directory_path):
            # Check if the file is a text file (you can adjust the condition based on your file extensions)
            if filename.endswith(".txt"):
                file_path = os.path.join(directory_path, filename)

                # Read the content of the text file and append it to the list
                with open(file_path, 'r') as file:
                    text_content = file.read()
                    text_list.append(text_content)

    return text_list


import re
from nltk.tokenize import word_tokenize




# Function to remove special characters and hyperlinks
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




# Specify the directory path containing text files
directory_path = 'StopWords'

# Call the function to read text files and store content in a list
result_text_list = read_text_files(directory_path)

# Print the content of the list
stopWordsList = []
for i, text_content in enumerate(result_text_list, start=1):
    tokenized_text_content = nltk.word_tokenize(text_content)
    tokens = word_tokenize(" ".join(tokenized_text_content))
    cleaned_tokens = clean_tokens(tokens)
    stopWordsList.extend(cleaned_tokens)
print(stopWordsList)
print(len(stopWordsList))
positiveWordsFile = 'positive-words.txt'
negativeWordsFile = 'negative-words.txt'
positiveWordList = []
negativeWordList = []
with open(positiveWordsFile, 'r') as file:
    text_content = file.read()
    positiveWordList = nltk.word_tokenize(text_content)

tokens = word_tokenize(" ".join(positiveWordList))
positiveWordList = clean_tokens(tokens)
print(positiveWordList)
with open(negativeWordsFile, 'r') as file:
    text_content = file.read()
    negativeWordList = nltk.word_tokenize(text_content)

tokens = word_tokenize(" ".join(negativeWordList))
negativeWordList = clean_tokens(tokens)
print(negativeWordList)
positiveScore = positive_score(text_tokens)
negativeScore = negative_word(text_tokens)
print("POSITIVE SCORE: ", positive_score(text_tokens))
print("NEGATIVE SCORE: ", negative_word(text_tokens))

polarityScore = polarity_score(positiveScore, negativeScore)
print("POLARITY SCORE: ", polarityScore)
cleanedTokens = textCleaner(text_tokens)
print(len(text_tokens), len(cleanedTokens))
print(cleanedTokens)
subjectivityScore = subjectivity_score(positiveScore, negativeScore, cleanedTokens)
print("SUBJECTIVITY SCORE: ", subjectivityScore)
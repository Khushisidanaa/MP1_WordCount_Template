import random 
import os
import string
import sys
import re

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

delimiters = " \t,;.?!-:@[](){}_*/"

def get_titles():
    titles = []
    for line in sys.stdin:
        titles.append(line.strip())
    return titles

def process_title(title, delimiters):
    delimeter_pattern= "[" + re.escape(delimiters) + "]"
    words = re.split(delimeter_pattern, title)
    processed_words=[word.lower().strip() for word in words if word.lower().strip() not in stopWordsList]
    return  processed_words


    



def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def process(userID):
    indexes = getIndexes(userID)
    word_freq = {}
   
    
    titles = get_titles()
    for index in indexes:
        title = titles[index]
        processed_words = process_title(title, delimiters)

        # Count word frequencies
        for word in processed_words:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    # Sort words by frequency in descending order and select top 20
    top_20_words = sorted(word_freq.items(), key=lambda x: (-x[1], x[0]))[1:21]

    # Print or return the top 20 words and their frequencies
    for word, freq in top_20_words:
        print(f"{word}")

process(sys.argv[1])

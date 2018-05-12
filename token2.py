import re
import json
import operator 
import json
from collections import Counter
from nltk import bigrams 
from nltk.corpus import stopwords
import string

with open('stream_csk.json', 'r') as f:
    line = f.readline() 
    tweet = json.loads(line)
    print(json.dumps(tweet, indent=4)) 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', 
    r'(?:[\w_]+)',r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', r'(?:@[\w_]+)',
    r"(?:[a-z][a-z'\-_]+[a-z])", r'<[^>]+>', 
    
    r'(?:\S)' 
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 
tweet = ' http://google.com #NLP'
print(preprocess(tweet))

with open('stream_csk.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)
        tokens = preprocess(tweet['text'])
        #do_something_else(tokens)




 
fname = 'stream_ipl.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_all = [term for term in preprocess(tweet['text'])]
        # Update the counter
        count_all.update(terms_all)
    # Print the first 250 most frequent words
    print(count_all.most_common(250))


 
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]

# Count terms only once, equivalent to Document Frequency
terms_single = set(terms_all)
# Count hashtags only
terms_hash = [term for term in preprocess(tweet['text']) 
              if term.startswith('#')]
# Count terms only (no hashtags, no mentions)
terms_only = [term for term in preprocess(tweet['text']) 
              if term not in stop and
              not term.startswith(('#', '@'))] 
             

 
terms_bigram = bigrams(terms_stop)
print (terms_bigram)






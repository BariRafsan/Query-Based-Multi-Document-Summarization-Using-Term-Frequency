#!/usr/bin/env python
# coding: utf-8
import os
from heapq import nlargest 
#python -m spacy download en_core_web_sm

#pip install -U spacy
#get_ipython().system('python -m spacy download en_core_web_sm')
import spacy
nlp = spacy.load('en_core_web_sm') 
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
stopwords = list(STOP_WORDS)
def get_summary(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]

    punctuation1 = punctuation + '\n' +'\n\n'

    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation1:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] +=1
                
    max_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word]/max_frequency

    sentence_tokens = [sent for sent in doc.sents]

    sentence_score = {}
    for sent in sentence_tokens: #create a dictionary for sen tokens
        for word in doc:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_score.keys():
                    sentence_score[sent]= word_frequencies[word.text.lower()]
                else:
                    sentence_score[sent] += word_frequencies[word.text.lower()]

    select_length = int(len(sentence_tokens)*0.05)
    summary  = nlargest(select_length, sentence_score,key= sentence_score.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    #print(summary)
    return summary




data_set = r'D:\University\University 4,2\CSE475 Machine Learning\Query Based Summarization\DataSet'

list_of_files = {} # dictionary

docsfile = {}

for (dirpath, dirnames, filenames) in os.walk(data_set): # oswalk itarate all posilbile paths#print(dirpath,dirnames, filenames)
    for filename in filenames:
        if not filename.endswith('.DS_Store'):
            file_p = os.sep.join([dirpath, filename]) # slashjoint
            list_of_files[filename] = file_p

para = []
df_list = []
for key, topic_dict in list_of_files.items():
    
            s = ''
            with open(topic_dict, 'r') as f:
                data = f.read()
                s += data
                s= s.replace('\n',' ')
                s= s.replace('[','')
                s= s.replace(']','')
                df_list.append(key)
                    #h_sum_list.append(key)
                para.append(s)
                
for key, value in zip(df_list, para):
    print(key)
    print('##############################################################################################')
    with open (key, 'w') as fp:
        fp.write(get_summary(str(value)))








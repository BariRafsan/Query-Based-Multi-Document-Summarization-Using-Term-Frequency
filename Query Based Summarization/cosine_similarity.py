# Program to measure the similarity between 
# two sentences using cosine similarity.
#from summery import *
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


######################################Cosine Similarity############################################################
def cosine_similarity(key,X,Y):
    global max
    global max_key
# tokenization

    X_list = word_tokenize(X) 
    Y_list = word_tokenize(Y)
    
    # sw contains the list of stopwords
    sw = stopwords.words('english') 
    l1 =[];l2 =[]
    
    # remove stop words from the string
    X_set = {w for w in X_list if not w in sw} 
    Y_set = {w for w in Y_list if not w in sw}
    
    # form a set containing keywords of both strings 
    rvector = X_set.union(Y_set) 
    for w in rvector:
        if w in X_set: l1.append(1) # create a vector
        else: l1.append(0)
        if w in Y_set: l2.append(1)
        else: l2.append(0)
    c = 0
    
    # cosine formula 
    for i in range(len(rvector)):
            c+= l1[i]*l2[i]
    
    cosine = c / float((sum(l1)*sum(l2))**0.5)
    if cosine > max:
        max=cosine
        max_key=key
    print("similarity with "+key+"  :", cosine)
    
            





Y=input("Enter the Question: ")
#Y ="steps toward introduction of the Euro"
######################################
################Value OF X ####################
data_set = r'D:\University\University 4,2\CSE475 Machine Learning\PROJECT\Summary'

list_of_files = {} # dictionary

docsfile = {}

for (dirpath, dirnames, filenames) in os.walk(data_set): # oswalk itarate all posilbile paths#print(dirpath,dirnames, filenames)
    for filename in filenames:
        if not filename.endswith('.DS_Store'):
            file_p = os.sep.join([dirpath, filename]) # slashjoint
            list_of_files[filename] = file_p

para = []
df_list = []
max =-999
max_key=''
for key, topic_dict in list_of_files.items():
    
            s = ''
            with open(topic_dict, 'r') as f:
                data = f.read()
                s += data
                s= s.replace('\n',' ')
                s= s.replace('[','')
                s= s.replace(']','')
                df_list.append(key)
                
                para.append(s)
            cosine_similarity(key,str(para),Y)  
print(max)
print(max_key)





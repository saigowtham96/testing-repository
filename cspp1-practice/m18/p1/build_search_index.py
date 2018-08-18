'''  Tiny Search Engine - Part 1 - Build a search index

    In this programming assingment you are given with some text documents as input.
    Complete the program below to build a search index. Don't worry, it is explained below.
    A search index is a python dictionary.
    The keys of this dictionary are words contained in ALL the input text documents.
    The values are a list of documents such that the key/word appears in each document atleast once.
    The document in the list is represented as a tuple.
    The tuple has 2 items. The first item is the document ID.
    Document ID is represented by the list index.
    For example: the document ID of the third document in the list is 2
    The second item of the tuple is the frequency of the word occuring in the document.

    Here is the sample format of the dictionary.
    {
        word1: [(doc_id, frequency),(doc_id, frequency),...],
        word2: [(doc_id, frequency),(doc_id, frequency),...],
        .
        .
    }
'''
import re
import  math

def clean_up(data):
    '''
    removing special characters
    '''
    data = data.lower()
    data_list = data.split(" ")
    count = 0
    while count < len(data_list):
        data_list[count] = re.sub("[^a-z]","",data_list[count])
        count += 1

    return data_list

def remove_stop_words(word_list):
    '''
    removing stop words
    '''
    stop_words = load_stopwords("stopwords.txt")

    temp_word_list = word_list[:]

    for each_word in temp_word_list:
        if each_word in stop_words:
            word_list.remove(each_word)

    return word_list
def get_frequency(wordlist):
    freq_dict={}
    for each_word in word_1:
        if word not in freq_dict:
            frequency[each_word]+=[0,1]
        else:
            frequency[each_word] = 1 
    
    for each_word in word_2:
        if word not in freq_dict:
            freqency[each_word]+=[1,0]
         else:
             frequency[each_word] = 1
    return freq_dict       
    
# helper function to load the stop words from a file
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as f_stopwords:
        for line in f_stopwords:
            stopwords[line.strip()] = 0
    return stopwords


            

def build_search_index(docs):
    '''
        Process the docs step by step as given below
    '''

    # initialize a search index (an empty dictionary)

    # iterate through all the docs
    # keep track of doc_id which is the list index corresponding the document
    # hint: use enumerate to obtain the list index in the for loop

        # clean up doc and tokenize to words list

        # add or update the words of the doc to the search index

    # return search index
    pass
    d ={}
    d1 = cleanup(d1)
    d2 = cleanup(d2)
    list_1=[]
    list_2=[]
    dict_1 = remove_stop_words(d1)
    dict_2 = remove_stop_words(d2)
    count=0
    for i in enumerate(len(dict_1)):
        list_1.index(dict_1)
        count=count+1
    if count == len(dict_1)
    print(dict_1)
    return dict_1
        
        
        
        
        
        
                       
                       
                       
                       
                       
            
        
                       
                       
                       
            
                       
    

# helper function to print the search index
# use this to verify how the search index looks
def print_search_index(index):
    '''
        print the search index
    '''
    keys = sorted(index.keys())
    for key in keys:
        print(key, " - ", index[key])

# main function that loads the docs from files
def main():
    '''
        main function
    '''
    # empty document list
    documents = []
    # iterate for n times
    lines = int(input())
    # iterate through N times and add documents to the list
    for i in range(lines):
        documents.append(input())
        i += 1

    # call print to display the search index
    print_search_index(build_search_index(documents))

if __name__ == '__main__':
    main()

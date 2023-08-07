#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from collections import defaultdict
from functools import reduce

#This function helps me to load the CSV file into a DataFrame so its easier to be read
data = pd.read_csv('injury.csv')

# This function helps me remove the NaN values from the 'Team' variable
data = data.dropna(subset=['Team'])

#Implements the MapReduce Word Count Algorithm
def map_reduce(data):
    def mapper(word):
        return [(word, 1)]

    #Implements Reducer which Sums the counts for each word
    def reducer(word_counts_dict, word_count):
        word_counts_dict[word_count[0]] += word_count[1]
        return word_counts_dict

    # Mapping phase
    mapped_data = data['Team'].apply(mapper).explode()

    # Reducer phase
    reduced_data_dict = reduce(reducer, mapped_data, defaultdict(int))

    # Sorts the word counts by value in descending order for easier visualization
    sorted_word_counts = dict(sorted(reduced_data_dict.items(), key=lambda x: x[1], reverse=True))

    return sorted_word_counts

# Execute the MapReduce function on the 'Team' column of the DataFrame
word_counts = map_reduce(data)

# Display the word counts sorted from highest to lowest since it is sorted in a descending format
print(word_counts)


# In[ ]:





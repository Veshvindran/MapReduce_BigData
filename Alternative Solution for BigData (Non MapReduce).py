#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

# Replace 'injury.csv' with the correct path to your dataset file if it's not in the current working directory
df = pd.read_csv(r'C:\Users\vesh\Desktop\injury.csv')


# In[19]:


team_column = df['Team']

# Converts all the rows into string type in order to handle NaN values
team_column = team_column.astype(str)

# Split each entry in the "Team" column into individual words and stacks them into a Series
word_series = team_column.str.split(expand=True).stack()

#Counts the appeareance of the word
word_counts = word_series.value_counts()

# Prints the word count summary from highest to lowest
# Easier than map reduce way easier xD
print(word_counts)


# In[ ]:





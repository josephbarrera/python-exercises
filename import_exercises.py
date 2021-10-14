#!/usr/bin/env python
# coding: utf-8

# 1. Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
# 
# Run an interactive python session and import the module. Call the is_vowel function using the . syntax.
# 
# 

# In[1]:


import function_exercises
function_exercises.is_vowel('b')


# Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.

# In[ ]:


from function_exercises import calculate_tip
calculate_tip(20, 50)


# Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. Test this function in your notebook.

# In[ ]:


from function_exercises import get_letter_grade as glg
glg(47)


# 2. Read about and use the itertools module from the python standard library to help you solve the following problems:
# 
# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# In[2]:


import itertools as it

list(it.combinations('abc123', 2))


# How many different combinations are there of 2 letters from "abcd"?

# In[3]:


import itertools as it

list(it.combinations('abcd', 2))


# How many different permutations are there of 2 letters from "abcd"?

# In[4]:


list(it.permutations('abcd', 2))


# 3. Save this file as profiles.json inside of your exercises directory (right click -> save file as...).
# 
# Use the load function from the json module to open this file.
# 
# import json
# 
# json.load(open('profiles.json'))
# 
# Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
# 

# In[6]:


import json
json.load(open('profiles.json'))


# - Total number of users

# In[8]:


profiles = json.load(open('profiles.json'))
len(profiles)


# - Number of active users

# In[10]:


profiles[0]['isActive']


# In[11]:


type(profiles[0]['isActive'])


# In[12]:


active_users = [profile for profile in profiles if profile['isActive']]
len(active_users)


# - Number of inactive users

# In[14]:


inactive_users = [profile for profile in profiles if(not profile['isActive'])]
len(inactive_users)


# - Grand total of balances for all users

# In[17]:


total_balance = 0

for profile in profiles:
    total_balance += profile['balance']
    
print(total_balance)


# - Average balance per user

# In[ ]:





# - User with the lowest balance

# In[19]:


user_lowest_balance = min(profiles, key=lambda x: x["balance"])
user_lowest_balance


# - User with the highest balance

# In[20]:


user_highest_balance = max(profiles, key=lambda x: x["balance"])
user_highest_balance


# - Most common favorite fruit

# In[22]:


fruits = []
for profile in profiles:
    fruits.append(profile["favoriteFruit"])
    
fruits


# In[23]:


set(fruits)


# In[25]:


max(fruits, key=fruits.count)


# - Least most common favorite fruit

# In[26]:


min(fruits, key=fruits.count)


# - Total number of unread messages for all users

# In[29]:


greeting = 'Hello, Hebert Estes! You have 423414 unread messages.'


# In[33]:


count_unread = ''

for character in greeting:
    if character.isdigit():
        count_unread += character
int(count_unread)


# In[34]:


total_num_unread = 0

for profile in profiles:
    count = count_unread(profile['greeting'])
    total_num_unread += count

print(total_num_unread)


# In[ ]:





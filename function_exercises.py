#!/usr/bin/env python
# coding: utf-8

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[40]:


import keyword
two = 2 or "2"


def is_two(x):
    if x == two:
        return True
    return False


is_two(3)


# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[62]:


vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
string = ['']


def is_vowel(string):
    for letter in string:
        if letter in vowels:
            return True
    return False


is_vowel("au")


# In[64]:


def is_vowel(string):
    ''' return if input string is a consonant. '''

    return string.lower() in ['a', 'e', 'i', 'o', 'u']


is_vowel('au')


# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[43]:


def is_consonant(string):
    for letter in string:
        if letter in vowels:
            return False
    return True


is_consonant("a")


# In[65]:


def is_consonant(string):
    ''' return if input string is a consonant.'''

    return not is_vowel(string)


is_consonant('u')


# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[56]:


def capitalize_first_consonant_letter(string):
    first_letter = string[0]
    for letter in string:
        if first_letter not in vowels:
            return first_letter.upper()


capitalize_first_consonant_letter("hotdog")


# In[68]:


def capitalize_consonant(string):

    if is_consonant(string[0]) == True:
        string = string.capitalize()

    return string


capitalize_consonant('hand')


# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[ ]:


# In[70]:


def calculate_tip(tip_percentage, total_bill):

    return total_bill * (tip_percentage/100)


calculate_tip(10, 100)


# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[ ]:


# In[71]:


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[ ]:


# In[73]:


def handle_commas(string):
    number = ''
    for char in string:
        if char not in ',':
            number += char
    return int(number)


handle_commas(',,6,,2,4,,,5,,4545,,,,')


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[ ]:


# In[76]:


def get_letter_grade(number):
    if number >= 90:
        return 'A'
    elif number >= 80:
        return 'B'
    elif number >= 70:
        return 'C'
    else:
        return 'F'


get_letter_grade(68)


# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[ ]:


# In[80]:


def remove_vowels(string):
    new_string = ''
    for char in string:
        if char.lower() not in "aeiou":
            new_string += char
    return new_string


remove_vowels('Asjfjsgljasjdsnavsowerjf')


# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# - for example:
#   - Name will become name
#   - First Name will become first_name
#   - % Completed will become completed

# In[ ]:


def normalize_name(string):

    # In[ ]:

    # 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
    # - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    # - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

    # In[ ]:

    # In[ ]:

    # Additional Exercise
    #
    # Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.

    # In[ ]:

    # In[ ]:

    # Bonus
    #
    # 1. Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

    # In[ ]:

    # In[ ]:

    # 2. Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
    # - col_index('A') returns 1
    # - col_index('B') returns 2
    # - col_index('AA') returns 27
    print

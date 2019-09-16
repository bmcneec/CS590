#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Addition - # same as R -- DYNaMIC TyPiNg
15 + 32


# In[2]:


# Exponents IS Different from R
3**7


# In[3]:


# Use Equal sign ( = ) to assign variables
my_dogs = 2


# In[5]:


my_dogs


# In[7]:


my_dogs = ['Billie', 'Birdie']


# In[13]:


# Variables name = expresion
variable = 50
variable

variable = variable + 10
variable

variable +=10     ### shorthand for variable = variable + 10
variable


# In[89]:


## type is like class in R ##
type(variable)
type(2.3)

fl = 2.4
type(fl)

s = 'text'
type(s)

Booleans = True or False # In R (TRUE or FALSE)
t = True
f = False
type(t)

# Strings - Single or Double Quotes 
'hello'
"hello"

## Python uses len()  where R uses nchar() in strings
len('Hello World')

# print()  is the same

# in R, sprintf() --## DIFFERENCE ##

print('The class {} begins at {}'.format('CS590', '1:30PM'))

print('The class %s begins at %s' %('CS590', '1:30PM'))

# List - variable = []
my_list = [1,2,3]
type(my_list)

my_list = ['String', 15, 100.23, 'Text']
my_list

len(my_list)

# Indexing and Slicing in Python

## DIFFERENCE --- In R, indexing begins at 1
## DIFFERENCE --- In Python, Indexing begins at 0

my_list[0]
my_list[1]
my_list[1:]
my_list[:-1] # want everything up to the last number
my_list[-1]

my_list[::2] # grab everything and get every other one
my_list[::-1] # start from the end
my_list += ['new item']
my_list


## Methods in Python are like Functions in R ### DIFFERENCE ###
# method .format() using print function
list1 = [1,2,3]
list1.append('Append me!')
list1
list1.pop(0) # removes 
list1

new_list = ['a','x','c','z','b']
new_list
new_list.sort()
new_list
new_list.reverse()
new_list

# nesting in python # Nested Lists
ls1 = [1,2,3]
ls2 = [4,5,6]
ls3 = [7,8,9]

matrix = [ls1, ls2, ls3]
matrix
matrix[0]
matrix[0][2]


### Dictionaries ### Similar to a List in R ---
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
my_dict

my_dict['key3']

my_dict



# KEYS
my_dict.keys()
# Values
my_dict.values()

# TUPLE - cannot be changed 
t = (1,2,3)
type(t)

# cannot change values already present in a string, but can append

# upper case 
s.upper()
#lower case
s.lower()
# split - removes a value (like a w in world)
s.split()

x = {1}
x = set()
x.add(2)
x.add(1)
x


# In[ ]:





# In[ ]:





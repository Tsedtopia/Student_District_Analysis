#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
import pandas as pd


# In[2]:


# File to load
schools_data_to_load = r"C:\Users\films\Resources\School_District_Analysis\schools_complete.csv"
students_data_to_load = r"C:\Users\films\Resources\School_District_Analysis\students_complete.csv"


# In[3]:


df = pd.read_csv


# In[4]:


# Read the student data file and store into a Pandas DataFrame
school_data_df = pd.read_csv(schools_data_to_load)
student_data_df = pd.read_csv(students_data_to_load)

#Cleaning Student Names and Replacing Substrings in a Pythong String

# Add each prefix and suffix to remove to a list
prefixes_suffixes = ["Dr.", "Mr.", "Ms.", "Mrs.", "Miss", "MD", "DDS", "DVM", "PHD"]

# Iterate through the words in the "prefixes_suffixes" List and replace them with an empty space,
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"grade")
    
# Check names.
student_data_df.head(10)


# ## Replace the 9th grade reading and math scores at Thomas High School with NaN. 

# In[5]:


# Install numpy using conda install numpy or pip install numpy. 
# Step 1. Import numpy as np.
import numpy as np


# In[6]:


import pandas as pd


# In[7]:


# Step 2. Use the loc method on the student_data_df to select all the reading scores from the 9th grade at Thomas High School and replace them with NaN.
student_data_df.loc[(student_data_df["school_name"] == "Thomas High School") & (student_data_df["grade"] == "9th"),
                    ("reading_scores")] = float("NaN")


# In[8]:


# Step 3. Refactor the code in Step 2 to replace the math scores with NaN
student_data_df.loc[(student_data_df["school_name"] == "Thomas High School") & (student_data_df["grade"] == "9th"),
                                    ("reading_scores")]= float("NaN")


# In[9]:


#  Step 4. Check the student data for NaN's. 
print (student_data_df.loc[(student_data_df["school_name"] == "Thomas High School") & (student_data_df["grade"] == "9th")])


# In[11]:


student_data_df.to_csv("schools_complete_output.csv", index=False)


# In[ ]:


# Read the school data file and store it in a Pandas DataFrame
school_data_df = pd.read_csv(school_data_to_load)
school


#!/usr/bin/env python
# coding: utf-8

# In[63]:


# Dependencies and Setup
import pandas as pd


# In[64]:


# File to load
schools_data_to_load = r"C:\Users\films\Resources\School_District_Analysis\schools_complete.csv"
students_data_to_load = r"C:\Users\films\Resources\School_District_Analysis\students_complete.csv"


# In[65]:


df = pd.read_csv


# In[66]:


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


# In[67]:


# Install numpy using conda install numpy or pip install numpy. 
# Step 1. Import numpy as np.
import numpy as np


# In[68]:


import pandas as pd


# In[69]:


# Determiine if there are any missing values in the school data
school_data_df.count()


# In[70]:


# Determine if there any missing values in the student data.
student_data_df.count()


# In[71]:


# Determine if there are any missing values in the school data
school_data_df.isnull()


# In[72]:


# Determine if there are any missing values in the student data.
student_data_df.isnull().sum()


# In[73]:


# Add the Pandas dependency
import pandas as pd


# In[74]:


# Files to load
file_to_load = r"C:\Users\films\Resources\School_District_Analysis\missing_grades.csv"


# In[75]:


# Read the CSV into a DataFrame
missing_grade_df = pd.read_csv(file_to_load)
missing_grade_df


# In[76]:


# Determine data types for the school Data Frame
school_data_df.dtypes


# In[77]:


# Determine data type of the budget column in the school DataFrame
school_data_df["budget"].dtype


# In[78]:


# Determine data type for the student DataFrame
student_data_df.dtypes


# In[93]:


# Combine the data into a single dataset
school_data_complete_df = pd.merge(student_data_df, school_data_df, on = ["school_name", "school_name"])
school_data_complete_df.head()


# In[99]:


# Get the total number of students
student_count = school_data_complete_df.count()
student_count


# In[108]:


# Calculate the Total Budget.
total_budget = school_data_df["budget"].sum()
total_budget


# In[109]:


# Calculate the average reading score
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score


# In[110]:


# Calculate the average math score
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score


# In[112]:


district_summary_df["Total Budget"]


# In[111]:


# Format the columns
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)

district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)

district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)

district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:0f}".format)

district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)


# In[11]:


student_data_df.to_csv("schools_complete_output.csv", index=False)


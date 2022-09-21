#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os


# In[2]:


student_data = os.path.join("C:/Users/avnit/Desktop/new_full_student_data.csv")
student_df = pd.read_csv(student_data)
student_df


# In[3]:


student_df.head()


# In[4]:


# Check the Nulls
student_df.isnull().sum()


# In[5]:


# Remove the Nulls
student_df = student_df.dropna()
student_df


# In[6]:


student_df.isnull().sum()


# In[7]:


# Check Duplicated Values
student_df.duplicated().sum()


# In[8]:


student_df = student_df.drop_duplicates()
student_df


# In[9]:


student_df.duplicated().sum()


# In[10]:


# Checking the Data types
student_df.dtypes


# In[18]:


# Removing'th' suffix
student_df['grade'] = student_df['grade'].str.replace('th', '')
student_df['grade']


# In[19]:


# Changing the data type
student_df['grade'] = student_df['grade'].astype(int)
student_df.dtypes


# In[20]:


# Summarize the data
student_df.describe()


# In[21]:


# Display mean math score
student_math = student_df["math_score"].mean()
student_math


# In[22]:


#Store the minimum reading score
min_reading_score = student_df["reading_score"].min()
min_reading_score


# In[23]:


# Display the grade column by using loc
student_grade_loc=student_df.loc[:,"grade"]
student_grade_loc


# In[24]:


# Display the first three rows of Columns 3,4,5
student_columns_iloc=student_df.iloc[0:3,[3,4,5]]
student_columns_iloc


# In[25]:


# Select the rows for Grade 9, and display their summary statistics
filter= student_df['grade'] == 9
student_df.loc[filter].describe()


# In[26]:


#  Store the row with minimum overall reading score
min_reading_score=student_df["reading_score"].min()
min_reading_score = student_df.loc[student_df["reading_score"]==min_reading_score]
min_reading_score


# In[27]:


#Select all the reading scores from the 10th graders at Dixon High School

student_Dixon_School=student_df[["reading_score","school_name"]].loc[(student_df["grade"] == 10) & (student_df["school_name"] == "Dixon High School")]
student_Dixon_School


# In[28]:


#Find the mean reading score for all the students in Grades 11 and 12 combined

student_df["math_score"].loc[(student_df["grade"] == 11) | (student_df["grade"] == 12)].mean()


# In[29]:


#Display the average budget for each school type

item_group = student_df.groupby(by = "school_type").mean()
item_group.loc[:,["school_budget"]]


# In[30]:


#Find the total number of students
school_group=student_df.groupby(by="school_name").count()
school_group.loc[:,["student_id"]].sort_values("student_id",ascending = False)


# In[31]:


#Find the average math score by grade for each school type
math_score_group= student_df.groupby(by=["school_type","grade"]).mean()
math_score_group.loc[:,["math_score"]]


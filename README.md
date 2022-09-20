# School_District_Analysis
## Overview:
  PyCity School Analysis focuses on preparing all standardized test data for analysis,reporting,and presentation to provide insights about performance trends and patterns.These insights are used to inform discussions and strategic decisions at the school and district level.
  
## Task:
- To analyze data on student funding and student's standardized test scores.
- To aggregate the data and showcase trends in school performance.

## Summary

 ### Analysis of the data are followed in steps:
 
  1. Collecting of data
    Imported the data from new_full_student_data.csv file into Dataframe named student_df by using Pandas read_csv and the os module.
    
  2. Preparing Data
  
    - Checking Missing values: There were total 1968 null values in reading_score and 982 in math_score.
    - Checking Duplicate values: There were total 1836 total duplicates values.
    - Checking the Data types : Changed the datatypes of grade from float to int
  3. Summarize the Data


    - Generated the statistic summary of student_df by using describe function
    - Summary statistics of Grade 9 is as below:
      Count : 4132
      Mean : 9
      min : 9.0
      Max : 9
    - Minimum reading_score: Mathew Thomas, student of grade 10 from Dixon High School has minimum reading_score.
    - Average Budget by school_type :
      Charter : 872625.65
      Public : 911195.55
    - Total number of students by school_name : Montgomery High School has highest student(2038).
    - Average Math score by grade and school_type:
      Grade 9 from Charter school type has average of 70.00 
      Grade 9 from Public school typer has average of 64.00

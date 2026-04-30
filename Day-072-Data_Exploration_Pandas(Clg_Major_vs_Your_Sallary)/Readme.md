# Day 72 – Data Exploration with Pandas (College Majors vs Your Salary)

## Overview

This is a data analysis overview where I used Pandas (a Python library) to explore a dataset about college majors and their salaries. The dataset contains information about 51 different undergraduate majors, their starting salaries, mid-career salaries, salary ranges, and which category they belong to (STEM, Business, or HASS - Humanities/Arts/Social Sciences). I learned how to load data, clean it, find missing values, access specific columns and rows, sort data, find highest and lowest values, calculate salary spreads (difference between top 90% and bottom 10% earners), and group data by category. This taught me the essential first steps of any data science project - exploring and understanding your data before doing any complex analysis.

## What I Have Learned

* **How to Explore a Pandas DataFrame**: The first step in any data science project is to explore your data. I learned to use df.head() to see the first 5 rows of my dataframe, which gives me a quick preview of what the data looks like - column names, types of values, and whether the data is clean or messy.

* **How to Detect NaN Values & Clean Your Data**: NaN stands for "Not a Number", these are missing or bad values in your dataset. I used df.isna() to find where NaN values exist (returns True for empty cells). Then I used df.dropna() to remove rows with missing values, creating a clean dataframe. Without cleaning, NaN values can break your calculations and give wrong results

* **How to Sort Your Data**: Used df.sort_values('column_name') to sort the dataframe by any column. You can also add ascending=False to sort from highest to lowest instead of lowest to highest. This helps find which majors have the highest salaries or smallest salary ranges.

* **How to Group Data by Category**: Used df.groupby('Group').count() to count how many majors belong to each category (STEM, Business, HASS). Then used df.groupby('Group').mean() to calculate the average salary for each category. Grouping lets you compare different categories against each other.

* **df.shape**: This gives you a tuple showing (number of rows, number of columns). For my dataset, it showed (51, 6) meaning 51 different majors and 6 columns of information

* **df.columns**: This prints out all the column names in your dataframe. My columns were: 'Undergraduate Major', 'Starting Median Salary', 'Mid-Career Median Salary', 'Mid-Career 10th Percentile Salary', 'Mid-Career 90th Percentile Salary', and 'Group'.

* **df.isna()**: Returns a dataframe of True/False values, True where data is missing (NaN). I saw that row 50 had NaN values in all salary columns because it was a source attribution row, not actual data

* **df.tail()**: Shows the last 5 rows of the dataframe. This helped me spot that the last row was not real data, It said "Source: PayScale Inc." with empty salary values.

* **df['column_name']**: Square bracket notation lets you access a single column. For example, df['Starting Median Salary'] gives you all the starting salary values.

* **df['column'].max()**: Finds the maximum value in a column.

* **df['column'].idxmax()**: Finds the index (row number) where the maximum value is located. The highest starting salary was at index 43 (Physician Assistant).

* **df.loc[43]**: Gets the entire row at index 43. This showed me all information about Physician Assistant major like starting salary, mid carrer salary and group.

* **df.insert(1, 'Spread', spread_col)**: Used to add a new column at a specific position. I created a "Spread" column that calculates the difference between 90th percentile salary and 10th percentile salary. This shows which majors have the widest salary range (high risk/high reward) vs narrowest range (low risk).

* **df['column1'].subtract(df['column2'])**: Pandas lets you do arithmetic with entire columns. I used this to calculate spread: Mid-Career 90th Percentile Salary - Mid-Career 10th Percentile Salary. No loops needed,Pandas does it for all rows at once.

* **df.sort_values('Spread')**: Sorts the dataframe from smallest spread to largest spread. 

* **df.groupby('Group').count()**: Counts how many majors in each group. Business had 12 majors, HASS had 22 majors, STEM had 16 majors.

## How It Works

### Data Exploration and Cleaning

* **Loading and First Look**: I imported pandas and loaded the CSV file using pd.read_csv(). Then I used df.head() to see the first 5 rows. This showed me the column names and what kind of data I'm working with like undergraduate major names, salary numbers, and group categories.

* **Checking Data Size**: df.shape told me the dataset has 51 rows and 6 columns. This is a small dataset, but the same methods work on millions of rows.

* **Finding Missing Data**: df.isna() revealed that row 50 had NaN (empty) values in every column except Undergraduate Major. df.tail() confirmed the last row was not real data, it just said "Source: PayScale Inc." with no salary numbers.

* **Cleaning the Data**: I used df.dropna() to create a new cleaned dataframe called clean_df. This removed the bad row. Now I had 49 rows of real data.

### Accessing and Analyzing Data

* **Finding Highest Starting Salary**: clean_df['Starting Median Salary'].max() returned 74300.0. To find which major had highest starting salary, I used clean_df['Starting Median Salary'].idxmax() which returned row index 43 number of starting highest salary. Then clean_df.loc[43] showed me it was Physician Assistant major subject name.

* **Finding Lowest Starting Salary**: clean_df['Starting Median Salary'].min() returned 34000.0. Using clean_df['Starting Median Salary'].idxmin() and clean_df.loc showed me Spanish had the lowest starting salary.

* **Finding Highest Mid-Career Salary**: clean_df['Mid-Career Median Salary'].max() returned 107000.0. The index was 8, which was Chemical Engineering.

* **Finding Lowest Mid-Career Salary**: clean_df['Mid-Career Median Salary'].min() returned 52000.0. The index was 18, which was Education.

### Calculating Salary Spread

* **Creating Spread Column**: I calculated the spread by subtracting the 10th percentile salary from the 90th percentile salary. This shows the range between what the bottom 10% earn and the top 10% earn. A wider spread means higher risk but also higher potential. I used clean_df.insert(1, 'Spread', spread_col) to add this new column right after Undergraduate Major.

* **Lowest Risk Majors (Smallest Spread)**: I sorted the dataframe by Spread using clean_df.sort_values('Spread'). The smallest spreads were Nursing (50,700), PhysicianAssistant(57,600), Nutrition(65,300), Spanish(65,400) & Health Care Administration(66,400), These major have more pridictable salaries.

* **Highest Potential (Top 90th Percentile)**:  I sorted by 'Mid-Career 90th Percentile Salary' in descending order using ascending=False. The top earners at the 90th percentile were Economics(210,000), Finance(195,000), Chemical Engineering(194,000), Math(194,000) and Physics(178,000).

* **Highest Risk Majors (Largest Spread)**: Sorting by Spread in descending order showed Economics had the largest spread at $159,400, meaning Economics graduates can earn anywhere from very little to very high amounts.

### Grouping and Comparing Categories

* **Counting by Group**: clean_df.groupby('Group').count() showed me how many majors belong to each category. HASS had the most (22 majors), then STEM (16 majors), then Business (12 majors).

* **Averages by Group**: clean_df.groupby('Group').mean() calculated that on average STEM has the highest starting(53,862) and mid carrier(90,812) salaries, Business has middle range starting(44,633) and mid carrier(75,083) salaries & HASS has the lowest starting(37,186) & mid carrier(62,968) salaries.

## Highlights

* **Data Exploration**: Learned to use .head(), .shape, .columns, .tail() as first steps to understand any dataset.
* **Detecting NaN Values**: Used .isna() to find missing data and .dropna() to clean it.
* **Finding Min/Max Values**: Used .max(), .min(), .idxmax(), .idxmin() to find highest and lowest values and their positions.
* **Sorting Data**: Used .sort_values() to organize data from lowest to highest or highest to lowest.
* **Adding New Columns**:  Used .insert() to add calculated columns like Spread (salary range).
* **Sorting Data**: Used .sort_values() to organize data from lowest to highest or highest to lowest.
* **Arithmetic on Columns**: Learned that Pandas lets you do math on entire columns at once without loops.
* **Grouping Data**: Used .groupby().count() and .groupby().mean() to compare different categories.




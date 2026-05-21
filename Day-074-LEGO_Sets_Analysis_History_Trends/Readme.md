# Day 74 – LEGO Sets Analysis of History & Trends(with Pandas & Matplotlib)

## Overview

This is a data analysis and visualisation project where I used Pandas and Matplotlib to explore LEGO datasets containing information about LEGO sets, themes, colors, and release years. The project focused on analysing trends in LEGO products over time, understanding relationships between datasets, and creating charts to visualise the data clearly.

In this project, I learned how to combine and manipulate datasets, work with relational database concepts like primary and foreign keys, aggregate data using groupby functions, and create different types of charts such as line charts, scatter plots, and bar charts. I also learned how to use HTML Markdown inside Jupyter Notebooks to organise and present my work more professionally.

## What I Have Learned

* **How to Use HTML Markdown in Jupyter Notebooks**: Learned how to create section headings using # and embed images using the `<img>` tag inside notebooks to make projects more organised and visually appealing.

* **How to Combine groupby() and count() Functions**: Learned how to group data and count values together to analyse how many entries belong to specific categories.

* **How to Use .value_counts()**: Used .value_counts() to count how many times each unique value appears in a column. This is useful for quickly analysing frequencies in datasets.

* **How to Slice DataFrames**: Learned how to use dataframe slicing like df[:-2] and df[:10] to select specific rows from the dataset.

* **How to Use .agg()**: Learned how to use .agg() together with .groupby() to perform operations on specific columns, like counting unique LEGO themes released each year and calculating the average number of parts per LEGO set.

* **How to Rename Columns**: Learned how to rename dataframe columns using .rename() to make column names clearer and easier to understand.

* **How to Create Line Charts with Two Axes**: Learned how to use two separate y-axes on the same chart, where one axis showed the number of LEGO sets released and the other showed the number of LEGO themes over time, making both trends easier to compare despite their different value ranges.

* **How to Create Scatter Plots in Matplotlib**: Learned how to create scatter plots to visualise relationships between two variables. Scatter plots helped identify patterns between LEGO sets and the average number of parts over time.

* **How Relational Databases Work**:Learned how primary keys uniquely identify rows in a table and how foreign keys connect different tables together. Understanding these relationships made it easier to work with connected LEGO datasets.

* **How to Merge DataFrames**: Learned how to combine multiple dataframes together using .merge() based on a common column. This allowed me to connect LEGO set data with theme information for better analysis.

* **How to Create Bar Charts with Matplotlib**: Learned how to use bar charts to compare values between different categories visually. Bar charts made it easier to compare the popularity of LEGO themes and sets.

* **plt.bar()**: Used plt.bar() to create bar charts for comparing categories visually. Bar charts made comparisons between LEGO themes and sets easier to understand.


## How It Works

### Loading and Understanding the Dataset

* **Loading the LEGO Datasets**: First, I imported Pandas and Matplotlib libraries and loaded multiple LEGO datasets using pd.read_csv(). The datasets contained information about LEGO sets, themes, release years, and number of parts.

* **Using Markdown in Notebook**: I used Markdown headings and images inside the notebook to organise different sections of the project and make the notebook easier to understand.

### Grouping and Analysing Data

* **Counting LEGO Sets by Year**: Used .groupby() together with .count() to analyse how many LEGO sets were released each year. This helped visualise how LEGO production increased over time.

* **Finding Popular LEGO Themes**: Used .value_counts() to identify which LEGO themes appeared the most in the dataset. This made it easier to compare popular categories.

* **Using Aggregation Functions**: Used .agg() together with .groupby() to count unique LEGO themes released each year and calculate the average number of parts per LEGO set.

* **Merging DataFrames**: Used .merge() to connect LEGO sets data with themes data using common columns. This allowed theme names and set information to be analysed together.


### Creating Charts with Matplotlib

* **Creating Line Charts**: Used plt.plot() to visualise how the number of LEGO sets and themes changed over time.

* **Using Dual Axis Charts**: Created charts with two separate y-axes where one axis represented the number of LEGO sets released and the other represented the number of LEGO themes over time.

* **Creating Scatter Plots**: Used plt.scatter() to analyse the relationship between release years and the average number of parts per LEGO set.

* **Creating Bar Charts**: Used plt.bar() to compare LEGO themes and categories visually also dded titles, labels, and legends using plt.title(), plt.xlabel(), plt.ylabel(), and plt.legend() to make charts easier to understand and more visually appealing.

### Analysing Trends and Insights

* **LEGO Growth Over Time**: The charts showed that the number of LEGO sets and themes increased significantly over the years as LEGO expanded its product range.

* **Increasing LEGO Complexity**: Scatter plots showed that the average number of parts per LEGO set generally increased over time, meaning LEGO sets became more detailed and complex.

* **Comparing LEGO Categories**: Bar charts made it easier to compare LEGO themes and identify which categories appeared most frequently in the dataset.


## Highlights

* **Data Visualisation**: Learned how to create line charts, scatter plots, and bar charts using Matplotlib.
* **Grouping Data**: Used .groupby() and .count() to analyse LEGO trends.
* **DataFrame Slicing**: Learned how to inspect specific portions of a dataframe using slicing.
* **Aggregation Functions**: Used .agg() to summarise yearly LEGO data
* **Relational Database Concepts**: Learned about primary keys and foreign keys.
* **Merging DataFrames**: Combined LEGO datasets together using .merge().
* **Dual Axis Charts**: Compared LEGO sets and themes using two y-axes.
* **Trend Analysis**: Analysed how LEGO sets and themes evolved over time.

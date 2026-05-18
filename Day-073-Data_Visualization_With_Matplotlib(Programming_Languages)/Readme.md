# Day 73 – Data Visualisation with Matplotlib (Programming Languages Popularity Analysis)

## Overview

This is a data analysis and visualisation project where I used Pandas and Matplotlib to explore how different programming languages changed in popularity over time. The dataset contains the number of posts on Stack Overflow related to programming languages such as Python, Java, JavaScript, C++, and many others from different years.

In this project, I learned how to clean and reshape data, work with timestamps and time-series data, create pivot tables, handle missing values, and build line charts using Matplotlib. I also learned how to customise charts by changing figure sizes, labels, legends, font sizes, line widths, and axis limits. This project taught me how data visualisation helps identify trends and patterns in real-world datasets.

## What I Have Learned

* **How to Visualise Your Data with Matplotlib**: Learned how to use Matplotlib to create line charts that show how programming languages changed in popularity over time. Data visualisation makes trends and patterns easier to understand.

* **How to Pivot, Group and Manipulate Your Data with Pandas**:  Learned how to restructure raw datasets into the format needed for analysis and plotting using methods like .groupby() and .pivot().

* **How to Work with Timestamps and Time-Series Data**: Learned how to convert date strings into datetime objects using pd.to_datetime(). Time-series data is data collected over time, and working with timestamps is very important in data science and analytics.

* **How to Style and Customise a Line Chart**: Learned how to customise charts by changing figure size, labels, legends, line widths, tick sizes, and axis limits to make charts more readable and visually appealing.

* **df.groupby('TAG').sum()**: Groups the dataframe by programming language tags and calculates the total number of posts for each language.

* **df.groupby('TAG').count()**: Counts how many rows belong to each programming language tag.

* **.idxmax()**: Finds the index label where the maximum value exists. I used this to find which programming language had the highest number of Stack Overflow posts.

* **.idxmin()**: Finds the index label where the minimum value exists.

* **pd.to_datetime()**: Converts date strings into datetime objects so that Pandas and Matplotlib can properly work with dates.

* **df.pivot()**: Learned how to use .pivot() method to Reshapes the dataframe into a pivot table where dates become rows, programming languages become columns, and the number of posts become values.

* **reshaped_df.fillna(0)**: Replaces all missing NaN values with 0

* **reshaped_df.isna().values.any()**: Checks whether the dataframe still contains any NaN values and return boolean value as per that.

* **Chart Customisation with Matplotlib**: Learned how to customise line charts using plt.figure(figsize=(16,10)) to increase chart size, plt.xlabel() and plt.ylabel() to add axis labels, plt.xticks() and plt.yticks() to change tick font sizes, plt.ylim() to control the y-axis range, plt.plot() to create line charts, linewidth=3 to make lines thicker and easier to read, and plt.legend() to identify which line belongs to each programming language.

* **Rolling Averages with Pandas**: Learned how to smooth noisy time-series data using rolling averages like rolling(window=3).mean(), rolling(window=6).mean(), and rolling(window=12).mean(). Smaller windows helped analyse short-term trends while larger windows made long-term trends easier to understand.


## How It Works

### Data Exploration and Understanding

* **Loading the Dataset**: First, I imported Pandas and Matplotlib libraries and loaded the CSV file using pd.read_csv(). The dataset contained dates, programming language tags, and the number of posts for each language.

* **Checking the Dataset**:  I used df.head() to view the first 5 rows of the dataframe. This helped me understand the structure of the dataset and what kind of information it contains.

* **Checking Dataset Size**: Using df.shape showed how many rows and columns are present in the dataframe.

* **Viewing Column Names**: df.columns displayed all column names like DATE, TAG, and POSTS.

* **Counting Values**: Used df.count() to check how many non-empty values exist in each column.

### Grouping and Analysing Data

* **Grouping Programming Languages**: I used df.groupby('TAG').sum() to calculate the total number of posts for each programming language.

* **Finding Most Post Languages**: Using .idxmax() and .max() helped me identify which programming language had the highest number of Stack Overflow posts

* **Finding Least Post Languages**: Using .idxmin() and .min() showed which language had the lowest number of posts

### Working with Time-Series Data

* **Checking Date Format**: Initially, the DATE column was stored as a string.

* **Converting Dates**: I used pd.to_datetime() to convert the DATE column into datetime objects.

* **Why Datetime Matters**: Datetime objects allow Pandas and Matplotlib to understand dates properly and plot charts in chronological order.

### Reshaping the Data

* **Creating a Pivot Table**: I used df.pivot(index='DATE', columns='TAG', values='POSTS') to reshape the dataframe.

* **How Pivot Works**: After pivoting, every programming language became its own column, dates became rows, and post counts became values. This format is much better for creating charts.

* **Handling Missing Values**: Some programming languages did not have posts in certain months, so NaN values appeared. I used .fillna(0) to replace missing values with zero

* **Checking for NaN Values**: reshaped_df.isna().values.any() confirmed whether any missing values still existed.

### Creating Charts with Matplotlib

* **Creating a Basic Line Chart**: Used plt.plot() to visualise how the number of posts changed over time.

* **Customising Charts with Matplotlib**: After pivoting, every programming language became its own column, dates became rows, and post counts became values. This format is much better for creating charts.

### Smoothing the Data with Rolling Averages

* **Why Rolling Average is Useful**: Real-world data often contains sudden spikes and noise. Rolling averages smooth the data and make overall trends easier to understand.

* **Using Different Rolling Windows**: Used rolling(window=3).mean(), rolling(window=6).mean(), and rolling(window=12).mean() to smooth the data. Smaller rolling windows showed short-term changes while larger windows helped analyse long-term popularity trends more clearly which help me understand by the end of 2020 python is the most popular programming language.

* **Comparing Trends**: Rolling averages helped me better compare the rise and decline of programming languages over time.

## Highlights

* **Data Visualisation**: Learned how to create line charts using Matplotlib
* **Datetime Conversion**: Used pd.to_datetime() to convert date strings into datetime objects.
* **Grouping Data**: Used .groupby() to analyse programming language popularity.
* **Pivot Tables**: Used .pivot() to restructure data for plotting.
* **Handling Missing Data**: Used .fillna(0) to replace NaN values.
* **Chart Customisation**: Styled charts using labels, legends, line widths, axis limits, and font sizes.
* **Looping Through Columns**: Used loops to plot multiple programming language trends dynamically.
* **Rolling Averages**: Used rolling windows to smooth noisy data.
* **Trend Analysis**: Compared how programming languages changed in popularity over time.
* **Real-World Data Skills**: Learned important data analysis and visualisation concepts used in real-world projects.
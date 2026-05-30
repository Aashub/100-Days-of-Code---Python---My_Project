# Day 75 – Google Trends and Data Visualisation(Tesla, Bitcoin, Unemployment Analysis)

## Overview

This is a data analysis and visualisation project where I used Pandas and Matplotlib to explore the relationship between Google search trends and real-world data such as Tesla stock prices, Bitcoin prices, and U.S. unemployment rates.

The project focused on cleaning and preparing time-series datasets, analysing search popularity trends, comparing multiple datasets with different time intervals, and creating professional visualisations to identify patterns and relationships. Through this project, I learned how search behaviour can often reflect public interest and, in some cases, even act as an early indicator of economic and market events.
 
## What I Have Learned

* **How to Use .describe()**: Learned how to quickly generate descriptive statistics such as count, mean, minimum, maximum, and standard deviation for numerical columns using .describe() method This provides a quick summary of the dataset without needing multiple calculations.

* **How to Find Missing Values Using .isna()**: Revised how to identify missing values in datasets and count the total number of missing entries using .isna().values.sum() This is useful when cleaning datasets before analysis..

* **How to Convert Strings into Datetime Objects**: Revised and used how to convert date columns from string format into Pandas datetime objects for time-series analysis.

* **How to Use .resample()**: Learned how to change the frequency of time-series data to make datasets comparable df.resample('M', on='DATE').last() For example, Bitcoin price data was daily while Google Trends data was monthly. Resampling allowed both datasets to be compared on the same timeline..

* **How to Create Dual-Axis Charts Using.twinx()**: Learned how to display two different datasets with separate y-axes on the same chart ax2 = ax1.twinx() This is useful when the two datasets have very different value ranges..

* **How to Increase Chart Resolution Using DPI**: Learned how to create sharper and higher-quality visualisations plt.figure(figsize=(14,8), dpi=120) Higher DPI improves chart clarity..

* **How to Work with matplotlib.dates Locators**: Learned how to improve date formatting and timeline readability on charts by controlling how dates appear on the x-axis. This makes long time-series charts easier to interpret.

* **How to Create Dashed and Dotted Lines**: Learned how to use different line styles to distinguish multiple datasets on the same chart, linestyle='--', linestyle='.' Dashed and dotted lines improve chart readability..

* **How to Use Different Markers on Charts**:Learned how to highlight data points using markers marker='o' Markers help identify individual observations more clearly..

* **How to Use .grid() in Matplotlib**: Learned how to add grid lines to charts for easier trend analysis plt.grid(True, linestyle='--') Grid lines make seasonality and patterns easier to spot.

* **How to Analyse Time-Series Data**: Learned how to compare datasets across time and identify relationships between public search behaviour and real-world events.


## How It Works

### Loading and Understanding the Data

* **Loading Multiple Datasets**: Imported Pandas and Matplotlib and loaded datasets containing Google search trends, Tesla stock prices, Bitcoin prices, and unemployment statistics.

* **Exploring Dataset Structure**: Used methods such as .shape, .columns, .head(), and .describe() to understand the structure and contents of each dataset.

* **Inspecting Time-Series Data**: Analysed the frequency of data collection to determine whether data was daily or monthly.

### Data Cleaning and Preparation

* **Checking for Missing Values**: Used .isna() and .sum() to identify missing values in the datasets.

* **Removing Missing Data**: Cleaned incomplete records before performing analysis.

* **Converting Dates**: Converted string-based date columns into Pandas datetime objects.

* **Resampling Bitcoin Data**: Converted daily Bitcoin price data into monthly data using .resample() so it could be compared directly with Google Trends search data.

### Creating Visualisations

#### Tesla Search Trends vs Stock Price
* Created dual-axis line charts comparing Tesla search popularity and Tesla stock prices.
* Styled charts using custom colours, thicker lines, larger figure sizes, and higher DPI.
* Added proper labels, titles, and date formatting.

#### Bitcoin Search Trends vs Bitcoin Price
* Compared Bitcoin search interest against Bitcoin market prices.
* Used dashed lines and markers to improve readability.
* Analysed how public interest changed during major Bitcoin price movements.

#### Unemployment Benefits Search vs Unemployment Rate
* Compared Google searches for "Unemployment Benefits" against official U.S. unemployment data.
* Added grid lines to make seasonality easier to observe.
* Used rolling averages to smooth search trends and compare them more effectively with unemployment rates.

### Key Insights Found

#### Tesla Insights
* Tesla search popularity generally increased alongside major increases in Tesla's stock price.
* A significant spike in search interest occurred around March 2016 when the Tesla Model 3 was unveiled.
* The largest search spikes occurred during periods when Tesla's stock price experienced rapid growth.
* Public interest and stock performance appeared to be strongly connected.

#### Bitcoin Insights
* Massive increases in Bitcoin prices during late 2017 and early 2018 were accompanied by record-high Google search volumes.
* Public interest surged as Bitcoin became a mainstream topic.
* During later Bitcoin price increases, search volume grew less dramatically because people were already familiar with Bitcoin.
* Search popularity reflected market excitement and investor attention.

#### Unemployment Insights
* Searches for "Unemployment Benefits" showed clear seasonality, with many spikes occurring near the end of each year.
* The 2007–2008 Financial Crisis caused a major increase in unemployment and unemployment-related searches.
* It took roughly a decade for unemployment rates to recover to pre-crisis levels.
* The large search spike in late 2013 was not accompanied by a similar increase in unemployment, suggesting other factors influenced public interest.

#### COVID-19 Impact Insight
* When 2020 data was included, unemployment reached levels far higher than those observed during the 2008 Financial Crisis.
* The COVID-19 pandemic created an unprecedented spike in both unemployment rates and unemployment-related searches.
* The charts clearly demonstrated the economic impact of the pandemic.

## Highlights

* **Time-Series Analysis**: Worked with monthly and daily datasets.
* **Datetime Conversion**: Converted string dates into datetime objects.
* **Descriptive Statistics**: Used .describe() to quickly analyse datasets.
* **Resampling Data**: Used .resample() to align datasets with different frequencies.
* **Dual-Axis Charts**: Compared search trends and real-world metrics on the same visualisation.
* **Chart Styling**: Improved charts using colours, markers, line styles, DPI, labels, and limits.
* **Rolling Averages**: Smoothed noisy data to identify long-term trends.
* **Grid and Date Formatting**: Enhanced chart readability using grids and date locators.
* **Trend Discovery**: Identified relationships between Google search behaviour, stock prices, cryptocurrency markets, and unemployment rates.

# Day 76 – Google Play Store App Analytics with Pandas & Plotly

## Overview

This is a data analysis and visualisation project where I used Pandas and Plotly to explore thousands of Android applications from the Google Play Store. The dataset contains information about app categories, ratings, installs, reviews, prices, content ratings, genres, and more.

The project focused on cleaning and preparing large datasets, analysing app popularity and competition, estimating app revenue, exploring pricing strategies, and creating interactive visualisations. Through this project, I learned how businesses can use data to understand market competition, identify profitable opportunities, evaluate pricing decisions, and analyse app performance across different categories.

In this module, I compared thousands of Google Play Store apps to gain insights into how competitive different app categories are, which categories offer the best opportunities based on popularity, how downloads are affected when an app is paid instead of free, how much developers can reasonably charge for paid apps, which paid apps generated the highest revenues, and whether paid apps can realistically recover their development costs through sales.
 
## What I Have Learned

* **How to Pull a Random Sample from a DataFrame Using .sample()**: Learned how to select random rows from a dataset using .sample(). This is useful when inspecting large datasets because it provides a quick and unbiased look at the data.

* **How to Find and Remove Duplicate Entries**: Learned how to identify duplicate records using .duplicated() and remove them using .drop_duplicates(). Removing duplicates ensures that analysis is based on unique and accurate data.

* **How to Convert Strings into Numeric Values**: Learned how to remove unwanted symbols and convert text-based columns into numeric data using .astype(). This made it possible to perform calculations and visualise app installs, prices, and revenues.

* **How to Use .value_counts()**: Used .value_counts() to count how frequently unique values appear in a column. This helped analyse content ratings, app categories, and genres across the Play Store.

* **How to Use .sort_values()**: Learned how to sort data from highest to lowest values. This made it easier to identify the highest-rated apps, apps with the most installs, and apps generating the most estimated revenue.

* **How to Use .groupby() and .agg()**: Used .groupby() together with .agg() to calculate category-level statistics such as app counts and total installs. This helped compare competition and popularity across categories.

* **How to Work with Nested Data**: Learned how to split and reshape columns containing multiple genres into individual values. This made genre analysis more accurate and meaningful.

* **How to Create Pie and Donut Charts with Plotly**: Learned how to visualise categorical data using interactive pie and donut charts. These charts helped analyse the distribution of content ratings across applications.

* **How to Create Vertical and Horizontal Bar Charts with Plotly**:Used Plotly bar charts to compare app categories based on installs, competition, and popularity. Bar charts made category comparisons easier to understand.

* **How to Create Grouped Bar Charts**: Learned how to compare free and paid apps across categories using grouped bar charts. This helped identify which categories contained relatively more paid applications.

* **How to Create Scatter Plots with Plotly**: Used scatter plots to analyse the relationship between app popularity and competition. Scatter plots helped reveal categories that attracted large numbers of downloads despite having fewer apps.

* **How to Use Colour Scales in Scatter Plots**: Learned how to use colour scales to represent additional information within a scatter plot. Colour coding made patterns and category differences easier to identify.

* **How to Create Box Plots**: Learned how to use box plots to compare app installs, pricing, and revenue distributions. Box plots helped identify medians, outliers, and the overall spread of the data.


## How It Works

### Loading and Understanding the Data

* **Loading the Dataset**: Imported Pandas and Plotly libraries and loaded the Google Play Store dataset containing information about thousands of Android applications.

* **Exploring the Dataset**: Used methods such as .sample(), .shape, and .columns to understand the dataset structure and inspect different app records.

* **Understanding App Information**: Analysed columns containing app ratings, installs, reviews, prices, content ratings, categories, and genres to understand what information was available for analysis.

### Data Cleaning and Preparation

* **Checking for Missing Values**: Used .isna() and .sum() to identify missing values in the datasets.

* **Removing Missing Data**: Removed incomplete records using .dropna() to ensure cleaner analysis.

* **Removing Duplicate Apps**: Used .duplicated() and .drop_duplicates() to eliminate duplicate entries and keep only unique applications.

* **Converting Data Types**: Converted installs and price columns from text format into numeric values using .astype() and string cleaning methods.

* **Creating Revenue Estimates**: Calculated estimated revenue by combining app prices with installation counts to evaluate the earning potential of paid apps.

* **Preparing Genre Data**: Split nested genre information into individual genres to perform more detailed analysis.


### Creating Visualisations

#### Content Ratings Analysis
* Created pie and donut charts to analyse the distribution of content ratings across apps.
* Compared how many apps were designed for Everyone, Teen, Mature audiences, and other age groups
* Visualised category proportions more effectively using interactive Plotly charts.

#### App Category Analysis
* Created vertical and horizontal bar charts to compare app categories.
* Analysed which categories contained the most apps and which categories attracted the largest number of downloads.
* Compared competition levels across categories.

#### Competition vs Popularity Analysis
* Created scatter plots to compare app competition and popularity.
* Used colour scales to visualise additional information such as category size and installs.
* Identified categories that offered strong download potential despite lower competition.

#### Free vs Paid Apps Analysis
* Created grouped bar charts to compare the number of free and paid apps across categories.
* Analysed how app pricing affected download opportunities.
* Compared categories where paid apps were more common.

#### Revenue and Pricing Analysis
* Created box plots to compare app prices, installs, and estimated revenues.
* Analysed revenue distributions and identified high-performing paid applications.
* Investigated whether paid apps generated enough revenue to justify development costs.

### Key Insights Found

#### App Category Insights
* The FAMILY category contained the largest number of apps (around 18% of all apps in the dataset), making it the most competitive category on the Play Store.
* The category with the most apps was not necessarily the most popular. For example, GAME apps generated significantly more installs than many categories that contained more applications.
* Categories such as GAME, COMMUNICATION, and TOOLS attracted billions of installs despite facing intense competition from thousands of existing apps.
* Categories such as EVENTS and BEAUTY contained relatively few apps and comparatively lower install counts, indicating smaller market sizes.

#### Paid vs Free App Insights
* apps overwhelmingly dominated the Play Store and achieved far higher install counts than paid apps.
* The median number of installs for free apps was substantially higher than for paid apps, showing that users are generally more willing to download free applications.
* Categories such as PERSONALIZATION, MEDICAL, and FAMILY contained a relatively larger proportion of paid apps compared to categories such as COMMUNICATION and SOCIAL.
* Developers choosing a paid model often traded download volume for direct revenue generation.

#### Revenue Insights
* A small number of paid apps generated exceptionally high estimated revenues. Examples from the analysis included apps such as: Minecraft, Hitman Sniper, Facetune, Sleep as Android Unlock, Other premium apps with both high prices and millions of installs 
* Some of these apps generated estimated revenues in the tens of millions of dollars when calculated using: Estimated Revenue = Price × Number of Installs
* Most paid apps earned significantly less revenue than the top-performing apps, creating a highly skewed revenue distribution.
* The box plot analysis showed numerous revenue outliers, indicating that only a small percentage of paid apps achieved exceptional commercial success.
* The majority of paid apps clustered around much lower revenue levels, suggesting that earning substantial revenue from paid downloads alone is difficult.

#### Competition Insights
* Categories such as GAME and FAMILY were highly competitive because they contained thousands of apps, yet they also attracted enormous numbers of downloads.
* Categories such as COMMUNICATION achieved extremely high average installs despite having fewer apps than categories like FAMILY, making them particularly attractive from a popularity-versus-competition perspective.
* The scatter plot revealed that some categories combined strong popularity with moderate competition, representing potentially profitable opportunities for developers.
* Highly saturated categories required developers to compete against thousands of existing apps, making visibility and user acquisition more challenging.
* Analysing both total installs and app counts together provided a more realistic picture of market opportunities than looking at either metric alone.

## Highlights

* **Random Sampling**: Used .sample() to inspect large datasets efficiently.
* **Numeric Conversion**: Converted text-based data into numeric format using .as_type().
* **Grouping Data**: Used .groupby() and .agg() to analyse app categories.
* **Nested Data Wrangling**: Processed genre information stored within single columns.
* **Plotly Visualisations**: Created interactive pie, donut, bar, scatter, and box plots.
* **Competition Analysis**: Compared app popularity against category competition.
* **Pricing Strategy Analysis**: Investigated the impact of free vs paid app models.

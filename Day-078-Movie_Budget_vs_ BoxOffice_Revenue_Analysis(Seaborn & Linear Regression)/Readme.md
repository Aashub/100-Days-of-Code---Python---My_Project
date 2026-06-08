# Day 78 – Movie Budget vs Box Office Revenue Analysis (Seaborn & Linear Regression)

## Overview

This is a data analysis and visualisation project where I used Pandas, Seaborn, Matplotlib, and Scikit-Learn to explore the relationship between movie production budgets and box office revenue.

The project focused on cleaning and preparing movie financial datasets, analysing revenue performance, identifying loss-making films, comparing older and modern movies, creating scatter and bubble charts, and building linear regression models to understand how production budgets influence worldwide revenue.

Through this project, I learned how data visualisation can reveal relationships within data and how linear regression can be used to measure and predict trends. I also explored how movie budgets have changed over time and how strongly production budgets are related to box office success.

## Notebook Link
https://drive.google.com/file/d/1wMZi_ysEbf6Vksab4ELL4Z2eCKhjBnRU/view?usp=drive_link


## What I Have Learned

* **Seaborn Data Visualisation**: Learned how to use the Seaborn library to create attractive and informative visualisations. Seaborn made it easy to build scatter plots, bubble charts, and regression plots while providing built-in styling options.

* **Linear Regression with Scikit-Learn**: Learned how to build and interpret linear regression models using Scikit-Learn. I calculated regression coefficients, intercepts, and R-squared values to evaluate how well a model explains the relationship between movie budgets and revenue.

* **Regression Scatter Plots**: Learned how to visualise relationships between variables using scatter plots and regression lines. These charts helped identify whether larger production budgets generally lead to higher box office revenue.

* **Bubble Charts with Seaborn**: Learned how to add a third dimension to a scatter plot using the `size` and `hue` parameters. Bubble charts helped visualise multiple variables simultaneously within a single chart.

* **Converting Financial Data into Numeric Format**: Used .replace() with regular expressions to remove currency symbols and commas from movie budget and revenue columns. After cleaning the values, converted them into integers using .astype() so the data could be analysed mathematically.

* **Filtering Data with Multiple Conditions**: Learned how to filter DataFrames using both .loc[] and .query() with multiple conditions. This made it possible to identify specific groups of movies such as international releases and unreleased films.

* **Floor Division for Decade Analysis**: Used floor division (//) to convert release years into decades. This made it easier to compare older and newer films and analyse long-term trends in movie budgets and revenue.

* **Seaborn Chart Styling**: Learned how to customise Seaborn charts using built-in styles such as darkgrid and whitegrid, along with Matplotlib parameters for figure size and resolution.

* **Descriptive Statistics with Pandas**: Used .describe() to quickly generate summary statistics such as averages, minimums, maximums, and percentiles for movie budgets and revenues.

## How It Works

### Loading and Understanding the Data

* **Loading the Dataset**: Imported Pandas, Seaborn, Matplotlib, and Scikit-Learn libraries and loaded a movie dataset containing production budgets, domestic revenue, worldwide revenue, and release dates.

* **Exploring the Dataset**: Used methods such as .shape, .info(), .head(), and .describe() to understand the structure of the dataset and analyse movie financial information.

* **Inspecting Data Quality**: Checked for missing values, duplicate records, and incorrect data types before beginning the analysis.

### Data Cleaning and Preparation

* **Converting Financial Data**: Removed $ symbols and commas from budget and revenue columns before converting them into numeric values. This allowed movie budgets, domestic revenue, and worldwide revenue to be compared mathematically and used for statistical analysis.

* **Working with Datetime Data**: Converted release dates into datetime objects so movie releases could be analysed chronologically. This made it possible to study how budgets and revenue patterns changed across different decades of filmmaking.

* **Filtering Special Cases**: Used .loc[] and .query() to identify unusual records in the dataset. The analysis found 512 movies with no domestic revenue, 357 movies with no worldwide revenue, 1 movie that earned revenue internationally despite having no domestic revenue, and 7 unreleased movies that required further investigation.

* **Removing Unreleased Movies**: Excluded the 7 unreleased movies from the dataset because their box office performance was incomplete. This ensured that all revenue calculations and visualisations were based only on films that had already been released.


### Revenue and Financial Analysis

* **Analysing Movie Performance**: Used descriptive statistics to examine budgets and worldwide revenue across thousands of films. The average movie cost approximately $31 million to produce and generated around $89 million in worldwide revenue, showing that successful films can earn several times their production budget.

* **Identifying Loss-Making Films**: Compared production budgets against worldwide revenue to determine whether movies recovered their costs. The analysis revealed that a surprisingly large number of films failed to break even despite reaching cinemas worldwide.

* **Calculating Financial Outcomes**: Found that approximately 37.2% of movies earned less than their production budget, demonstrating that movie production remains a high-risk business where financial success is far from guaranteed.

### Creating Visualisations

* **Budget vs Revenue Analysis**: Created scatter plots to compare production budgets with worldwide revenue. The charts showed a general upward trend, indicating that higher-budget movies often earned more money, although there were many exceptions.

* **Bubble Chart Analysis**: Used Seaborn bubble charts to visualise budget, revenue, and release date in a single chart. This made it easier to identify blockbuster films, outliers, and clusters of movies with similar financial performance.

* **Movie Releases Over Time**: Plotted movie budgets against release dates to observe long-term industry trends. The visualisation clearly showed budgets increasing over time, especially after the 1970s as large-scale blockbuster productions became more common.

### Decade-Based Analysis

* **Creating Decades**: Used floor division (//) to convert release years into decade groups. This allowed movies released in the same era to be analysed together rather than individually.

* **Comparing Old and New Films**: Split the dataset into films released before 1970 and after 1970. This made it possible to compare how movie financing and box office performance evolved over time.

* **Analysing Budget Trends**: The comparison showed that modern films generally operate with much larger budgets than older films, reflecting rising production costs and the growth of blockbuster filmmaking.

### Linear Regression Analysis

#### Regression for Modern Films
* Used Seaborn's .regplot() and Scikit-Learn's Linear Regression model to analyse the relationship between production budgets and worldwide revenue for movies released after 1970.
* The model achieved an R² value of approximately 0.56, meaning that production budget alone explained about 56% of the variation in worldwide revenue. This indicated a reasonably strong relationship between spending and earnings.

#### Regression for Older Films
* Built a separate regression model for movies released before 1970 to see whether the same relationship existed in earlier decades.
* Although a positive relationship was still present, the model produced a much lower R² value, showing that production budget was a far weaker predictor of revenue for older films.

### Revenue Prediction

#### Predicting Box Office Revenue
* Used the fitted regression equation to estimate the worldwide revenue of a hypothetical movie with a $350 million production budget the revenue prediction of that movie is $600 million. This demonstrated how historical data can be used to make future revenue predictions using machine learning models.

### Key Insights Found

#### Movie Revenue Insights
* The average movie in the dataset cost approximately $31 million to produce and generated around $89 million in worldwide revenue.
* While many films were highly profitable, the distribution of revenue was extremely uneven, with a small number of blockbuster movies generating exceptionally large returns.

#### Loss-Making Film Insights
* Approximately 37.2% of movies failed to recover their production budgets, showing that financial success in the film industry is far less predictable than many people assume.

#### Budget Growth Insights
* Production budgets increased dramatically over time, particularly after the 1970s.
* The charts showed a clear transition from relatively modest film budgets to modern blockbuster productions costing hundreds of millions of dollars.

#### Regression Insights for Modern Films
* Modern movies displayed a clear positive relationship between budget and revenue.
* With an R² value of around 56%, production budget proved to be one of the strongest indicators of a movie's potential box office performance.

#### Regression Insights for Older Films
* Older movies showed a weaker connection between spending and earnings.
* he lower R² value suggested that factors other than production budget played a much larger role in determining commercial success before 1970.

## Highlights

* **Data Cleaning**: Removed unwanted symbols and converted financial data into numeric format.
* **Conditional Filtering**: Used .loc[] and .query() to compare multiple conditional statements.
* **Descriptive Statistics**: Used .describe() to summarise movie financial data.
* **Bubble Charts**: Created multi-dimensional visualisations using Seaborn.
* **Scatter Plots**: Analysed the relationship between production budgets and revenue.
* **Decade Analysis**: Used floor division to group movies by decade.
* **Regression Visualisation**: Used Seaborn's .regplot() to display regression lines.
* **Linear Regression**: Built predictive models using Scikit-Learn.
* **Model Evaluation**: Calculated slope, intercept, and R-squared values to assess model quality.
* **Revenue Prediction**: Estimated future movie revenue using regression equations.

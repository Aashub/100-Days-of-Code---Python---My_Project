# Day 80 – Dr. Semmelweis Handwashing Discovery Analysis

## Overview

This is a data analysis and visualisation project where I used Pandas, NumPy, Plotly, Seaborn, Matplotlib, and SciPy to investigate one of the most important discoveries in medical history: Dr. Ignaz Semmelweis' introduction of mandatory handwashing at Vienna General Hospital.

The project focused on cleaning and preparing historical childbirth datasets, comparing maternal death rates across hospital clinics, analysing how death rates changed before and after the introduction of handwashing, visualising distributions using histograms and Kernel Density Estimates (KDEs), and applying statistical hypothesis testing to determine whether the observed reduction in deaths was statistically significant.

Through this project, I learned how data can be used to support a compelling real-world argument. By combining descriptive statistics, visualisations, rolling averages, distribution analysis, and hypothesis testing, I was able to demonstrate the dramatic impact that handwashing had on reducing maternal mortality.

## Notebook Link
https://drive.google.com/file/d/1C1U31Sp-b5WyiqISYUOO8qttZTUTYMhA/view?usp=drive_link


## What I Have Learned

* **Histograms for Distribution Analysis**: Learned how to use histograms to visualise the distribution of monthly death rates. Histograms helped compare how death-rate patterns changed before and after the introduction of handwashing.

* **Overlapping Histograms**: Learned how to superimpose multiple histograms on the same chart even when the datasets contained different numbers of observations. Using histnorm='percent' made both distributions directly comparable

* **Sunburst Charts**: Learned how to visualise hierarchical data using Sunburst charts. This made it possible to explore Nobel Prize-winning organisations by country, city, and institution within a single visualisation.

* **Kernel Density Estimates (KDEs)**: Learned how to use Seaborn's .kdeplot() to create smooth estimates of data distributions. KDEs provided a clearer view of how monthly death rates were distributed before and after handwashing.

* **Statistical Significance Testing with SciPy**: Learned how to use SciPy's stats.ttest_ind() to compare two distributions and determine whether differences in their means were statistically significant.

* **Interpreting p-values**: Learned how p-values can be used to evaluate evidence against a null hypothesis. A very small p-value indicated that the reduction in death rates after handwashing was highly unlikely to have occurred by chance.

* **Time-Series Visualisation and Legends in Matplotlib**: Learned how to visually separate pre-handwashing and post-handwashing periods within the same chart using different styles and colours, while configuring legends to clearly distinguish multiple datasets and time periods.

* **Conditional Processing with NumPy**: Used np.where() to classify observations as occurring before or after the introduction of handwashing. This allowed comparisons between the two periods throughout the analysis.

* **Rolling Average Analysis**: Used .rolling(window=6).mean() to smooth monthly death-rate fluctuations and reveal underlying trends that were difficult to see in raw monthly data.

* **Twin-Axis Visualisations**: Used Matplotlib's .twinx() method to compare births and deaths on the same timeline while maintaining separate scales for each variable.


## How It Works

### Loading and Understanding the Data

* **Loading the Datasets**: Imported Pandas, NumPy, Plotly, Seaborn, Matplotlib, and SciPy libraries and loaded annual and monthly childbirth datasets containing birth and death records from Vienna General Hospital.

* **Exploring the Dataset Structure**: Used methods such as .shape, .columns, .head(), and .describe() to understand the structure of both datasets and examine birth and death statistics.

* **Inspecting Data Quality**: Checked for missing values and duplicate records using .isna() and .duplicated(). The analysis showed that both datasets contained no missing values and no duplicate records.

### Data Cleaning and Preparation

* **Working with Datetime Data**: Loaded monthly records with parsed datetime values, making it possible to perform time-series analysis and date-based filtering.

* **Calculating Death Rate Percentages**: Created percentage-based death-rate columns by dividing deaths by births and multiplying by 100. This allowed mortality rates to be compared fairly across different clinics and time periods.

* **Creating Time-Based Categories**: Used np.where() to classify observations as occurring before or after the introduction of mandatory handwashing in the form of handwash status column `yes` or `no`.

### Hospital and Clinic Analysis

* **Comparing Hospital Clinics**: Analysed annual childbirth and death records for Clinic 1 and Clinic 2 separately. Clinic 1 consistently recorded more births and more maternal deaths than Clinic 2.

* **Calculating Clinic Death Rates**: Compared maternal mortality rates between the two clinics using percentage-based analysis rather than raw death counts.

* **Investigating Historical Mortality**: Calculated the overall maternal mortality rate across the dataset and compared it with modern childbirth mortality statistics.

### Time-Series Analysis

* **Births and Deaths Over Time**: Created dual-axis time-series charts showing monthly births and deaths. The visualisation revealed a sharp decline in deaths after 1847 despite births remaining high.

* **Yearly Death Rate Trends**: Calculated yearly mortality percentages for both clinics and visualised how death rates changed across the 1840s.

* **Rolling Average Analysis**: Applied a 6-month moving average to smooth short-term fluctuations and reveal long-term trends in maternal mortality.

* **Highlighting Historical Events**: Created charts that visually separated the periods before and after handwashing, making the impact of the intervention easier to observe.

### Handwashing Impact Analysis

#### Before and After Comparison
* **Creating Pre-Handwashing and Post-Handwashing Groups**: Split the monthly dataset into two periods based on June 1847, when handwashing became mandatory.
* **Calculating Mortality Changes**: Compared average maternal death rates before and after handwashing to measure the impact of the new policy.
* **Evaluating Improvement Magnitude**: Calculated both percentage-point reductions and relative improvements in maternal mortality rates.

### Distribution Analysis

#### Histogram Analysis
* **Comparing Distributions**: Created overlapping histograms to compare monthly death-rate distributions before and after handwashing.
* **Normalising Histogram Data**: Used percentage-based histogram scaling to ensure fair comparisons despite different sample sizes.
* **Adding Distribution Summaries**: Combined histograms with box plots to visualise spread, central tendency, and outliers simultaneously.

#### Kernel Density Estimation (KDE)
* **Creating Smoothed Distributions**: Used Seaborn's .kdeplot() to estimate the underlying distribution of monthly death rates.
* **Comparing Distribution Shapes**: Analysed how the entire distribution shifted toward lower death rates after handwashing rather than focusing only on averages.

### Statistical Analysis

#### Hypothesis Testing
* **Performing a T-Test**: Used SciPy's stats.ttest_ind() to compare monthly death-rate distributions before and after handwashing.
* **Calculating Statistical Significance**: Measured the probability that the observed reduction in death rates occurred purely by chance.
* **Evaluating the Evidence**: Used the p-value and t-statistic to determine whether handwashing had a statistically significant effect on maternal mortality.

### Key Insights Found

#### Maternal Mortality Insights
* The overall maternal mortality rate across the Vienna hospital dataset was approximately 7.08%, highlighting how dangerous childbirth was during the 1840s.
* This mortality rate was dramatically higher than modern maternal mortality levels, demonstrating the severe medical challenges faced during the period.

#### Hospital Clinic Comparison Insights
* Clinic 1 consistently recorded both more births and more maternal deaths than Clinic 2 throughout the dataset.
* Clinic 1 recorded an average maternal death rate of 9.92%, while Clinic 2 recorded an average death rate of only 3.88%.
* Women giving birth in Clinic 1 faced a mortality risk that was more than twice that of women in Clinic 2.
* The consistently higher mortality rate in Clinic 1 became the key observation that motivated Dr. Semmelweis' investigation.

#### Yearly Mortality Insights
* Yearly mortality percentages showed that the mortality gap between the two clinics remained visible throughout the 1840s.
* In 1842, approximately 16% of women died in Clinic 1 compared with approximately 7.6% in Clinic 2, highlighting one of the most severe mortality differences observed during the analysis.
* The yearly trend analysis reinforced the conclusion that Clinic 1 consistently experienced substantially worse outcomes than Clinic 2.

#### Time-Series Insights
* Dual-axis charts showed that births remained relatively high over time while maternal deaths dropped sharply after 1847 after introducing hand wash.
* Visualising births and deaths together helped demonstrate that the reduction in mortality was not caused by a decline in the number of births.
* Separating the pre-handwashing and post-handwashing periods made the timing and impact of the intervention immediately visible.

#### Handwashing Impact Insights
* Before handwashing became mandatory, the average maternal death rate was approximately 10.5%.
* After handwashing was introduced, the average maternal death rate fell to approximately 2.11%.
* The intervention reduced the average monthly death rate by approximately 8.4 percentage points.
* The risk of death during childbirth became approximately 5 times lower after handwashing was introduced.
* The reduction was so large that it became clearly visible in every major visualisation used throughout the project.

#### Distribution Insights
* The histogram analysis showed that high monthly death-rate outcomes were far more common before handwashing than afterwards.
* Percentage-based histogram normalisation allowed fair comparisons between the pre-handwashing and post-handwashing periods despite different sample sizes.
* After handwashing, the entire death-rate distribution shifted toward substantially lower mortality values rather than improving only a few isolated months.
* KDE analysis confirmed that the overall distribution moved toward lower death rates after the intervention.
* The box plot analysis showed reductions not only in the average death rate but also in the overall spread and variability of monthly mortality outcomes.

#### Statistical Significance Insights
* The independent t-test produced a t-statistic of approximately 5.51 and a p-value of approximately 0.000000299.
* The age distribution histogram showed that most Nobel laureates received their prizes between the ages of 50 and 70, with relatively few winners receiving awards at very young ages.

#### Category Age Trend Insights
* Nobel laureates became progressively older across most categories as time progressed, indicating an increasing delay between discoveries and Nobel Prize recognition.
* The p-value was far below the 1% significance threshold. This provided extremely strong statistical evidence that the reduction in maternal mortality was not caused by random variation.
* The analysis strongly supported the conclusion that mandatory handwashing played a decisive role in reducing deaths.

## Highlights

* **NumPy Processing**: Used NumPy's np.where() to separate the data into pre-handwashing and post-handwashing periods and compare the impact of Semmelweis' intervention.
* **Time-Series Visualisation**: Visualised mortality trends over time and highlighted the introduction of handwashing practices on the chart.
* **Rolling Average Analysis**: Applied a 6-month moving average to smooth short-term fluctuations and reveal the long-term decline in maternal deaths after handwashing was implemented.
* **Histogram Visualisation**: Compared the distribution of monthly mortality rates before and after handwashing.
* **KDE Visualisation**: Created smooth distribution curves using Kernel Density Estimation (KDE) to better visualise how mortality rates shifted after the intervention.
* **Statistical Testing:**: Used SciPy to test whether the reduction in mortality rates after handwashing was statistically significant rather than the result of random chance.
* **P-Value Interpretation:**: Interpreted p-values to determine whether the observed differences were likely due to chance.
* **Chart Annotation & Legends**: Added legends and highlighted important historical periods to improve chart readability and storytelling.
* **Evidence-Based Conclusions**: Used statistical analysis and visualisations to support the argument that handwashing significantly reduced maternal mortality.
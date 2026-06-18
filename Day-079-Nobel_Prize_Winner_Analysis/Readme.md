# Day 79 – Nobel Prize Data Analysis & Visualisation (Plotly, Seaborn & Pandas)

## Overview

This is a data analysis and visualisation project where I used Pandas, Plotly, Seaborn, and Matplotlib to explore more than a century of Nobel Prize data.

The project focused on cleaning and preparing Nobel Prize datasets, analysing prize distributions across genders, countries, categories, institutions, and cities, creating interactive visualisations such as donut charts, choropleth maps, bar charts, and sunburst charts, and analysing how Nobel Prize trends have changed over time.

Through this project, I learned how different visualisation techniques can reveal completely different insights from the same dataset. I also explored global Nobel Prize distribution patterns, institutional research dominance, prize-sharing trends, and how the age of Nobel Prize winners has evolved over time.

## Notebook Link
https://drive.google.com/file/d/10MytzGd17huIetxf3iLjqFqE2GmVtLeX/view?usp=drive_link


## What I Have Learned

* **Plotly Interactive Visualisations**: Learned how to create interactive charts using Plotly. I built donut charts, bar charts, choropleth maps, line charts, and sunburst charts to explore Nobel Prize data from multiple perspectives.

* **Choropleth Maps**: Learned how to create world maps using Plotly's Choropleth visualisation. By combining Nobel Prize counts with ISO country codes, I visualised how Nobel Prizes are distributed across different countries.

* **Sunburst Charts**: Learned how to visualise hierarchical data using Sunburst charts. This made it possible to explore Nobel Prize-winning organisations by country, city, and institution within a single visualisation.

* **Seaborn Regression Analysis**: Learned how to use Seaborn's regression plots with the lowess=True parameter to visualise non-linear trends. This helped analyse how Nobel Prize winners' ages have changed over time.

* **Histograms and Data Distribution**: Used Seaborn's .histplot() to visualise the distribution of Nobel Prize winners' ages. Histograms helped reveal common age ranges and identify unusual values within the dataset.

* **Rolling Averages for Trend Analysis**: Used .rolling(window=5).mean() to smooth yearly Nobel Prize counts and prize-sharing trends. Rolling averages made long-term patterns easier to identify.

* **Grouping and Aggregating Data**: Used .groupby(), .agg(), .value_counts(), .merge(), and .sort_values() to summarise Nobel Prize data by category, gender, country, city, and organisation.

* **Donut and Bar Charts with Plotly**: Created donut charts to compare gender distributions and bar charts to compare Nobel Prize counts across categories, countries, institutions, and cities.

* **Working with Multiple Visualisation Perspectives**: Learned how different charts such as line plots, box plots, histograms, and regression plots can reveal different aspects of the same dataset.


## How It Works

### Loading and Understanding the Data

* **Loading the Dataset**: Imported Pandas, NumPy, Plotly, Seaborn, and Matplotlib libraries and loaded a Nobel Prize dataset containing information about laureates, prize categories, organisations, countries, and award years.

* **Exploring the Dataset**: Used methods such as .shape, .info(), .head(), and .describe() to understand the structure of the dataset and examine Nobel Prize records.

* **Inspecting Data Quality**: Checked for duplicate records and missing values before performing analysis. The investigation showed missing information primarily in birth dates and organisation-related columns.

### Data Cleaning and Preparation

* **Investigating Missing Values**: Used .isna() and filtering operations to identify rows containing missing birth dates and organisation information. This helped determine whether missing values belonged to individuals or institutions.

* **Converting Datetime Data**: Converted the birth_date column into datetime format using pd.to_datetime(). This enabled age calculations and time-series analysis.

* **Creating Prize Share Percentages**: Converted Nobel Prize share fractions into percentage values. For example, a prize share of 1/2 became 50%, making prize-sharing analysis easier.

### Gender and Category Analysis

* **Analysing Gender Distribution**: Used .value_counts() and a Plotly donut chart to compare male and female Nobel Prize winners. The visualisation showed that male laureates significantly outnumber female laureates throughout Nobel Prize history.

* **Identifying Early Female Laureates**: Filtered the dataset to identify the first female Nobel Prize winners and examine their achievements.

* **Finding Repeat Winners**: Used .value_counts() to identify individuals and institutions that won Nobel Prizes multiple times. The analysis revealed that 4 individuals and 2 organisations won Nobel Prizes more than once.

* **Analysing Nobel Prize Categories**: Used .value_counts() to compare Nobel Prize categories. The analysis showed that Medicine had the highest number of awards with 222 prizes, while Economics had the lowest with 86 prizes.

* **Investigating Economics Prizes**: Found that the first Economics Nobel Prize was awarded in 1969 under the title "The Sveriges Riksbank Prize in Economic Sciences."

* **Comparing Men and Women Across Categories**: Used .groupby() and grouped Plotly bar charts to compare Nobel Prize distributions across categories by gender.

### Time-Series Analysis

* **Analysing Prizes Awarded Per Year**: Used .groupby() to count Nobel Prizes awarded each year and visualised the results using scatter plots.

* **Creating Rolling Averages**: Applied a 5-year rolling average using .rolling(window=5).mean() to smooth yearly fluctuations and reveal long-term trends in Nobel Prize awards.

* **Analysing Prize Sharing Trends**: Calculated the yearly average prize share percentage and compared it with Nobel Prize counts using dual-axis charts.

* **Comparing Prize Counts and Prize Sharing**: The visualisation revealed that as the number of Nobel Prize winners increased over time, individual prize shares generally became smaller due to more prizes being shared among multiple recipients.

### Country-Level Analysis

* **Top Nobel Prize Countries**: Grouped Nobel Prize data by birth country and calculated total prize counts. The analysis showed that the United States dominated Nobel Prize awards, followed by several European nations.

* **Creating a Choropleth Map**: Merged Nobel Prize counts with ISO country codes and created a world map showing the geographical distribution of Nobel Prize winners.

* **Country Category Analysis**: Compared Nobel Prize categories across the top 20 countries using grouped horizontal bar charts. This revealed how different countries specialise in different research areas.

* **Tracking Nobel Prize Growth by Country**: Calculated cumulative Nobel Prize totals for each country over time and visualised how countries built their Nobel Prize records throughout history.

### Organisation and Research Analysis

* **Top Research Institutions**: Grouped Nobel Prize winners by organisation and identified the top 20 institutions with the highest number of Nobel Prize winners.

* **Research Cities Analysis**: Analysed organisation cities and identified the top research hubs responsible for producing Nobel Prize-winning work.

* **Birth City Analysis**: Compared the top 20 birth cities of Nobel Prize laureates using Plotly bar charts.

* **Sunburst Chart Analysis**: Created a hierarchical Sunburst chart showing Nobel Prize-winning organisations grouped by country, city, and institution. This provided a detailed view of where Nobel Prize-winning discoveries were made.

### Age Analysis of Nobel Laureates

#### Calculating Winning Age
* **Creating Winning Age Data**: Calculated the age of each laureate at the time they received the Nobel Prize by subtracting birth year from award year.
* **Youngest and Oldest Winners**: The analysis found the youngest Nobel Prize winner and the oldest Nobel Prize winner in the dataset, highlighting the wide age range of Nobel laureates.
* **Average Winning Age**: Found that the average Nobel Prize winner received their award at approximately 59 years of age.

#### Visualising Age Distribution
* **Histogram Analysis**: Used Seaborn's .histplot() to visualise the distribution of Nobel Prize-winning ages. The histogram showed that most laureates received their awards between their 50s and 70s.
* **Regression Trend Analysis**: Used Seaborn's .regplot() with lowess=True to analyse how winning age changed over time. The trend suggested that Nobel Prize winners have generally become older over the years.
* **Category-Based Age Analysis**: Created box plots to compare winning ages across Nobel Prize categories and identify differences between fields.

### Key Insights Found

#### Nobel Prize Category Insights
* Medicine received the highest number of Nobel Prizes with 222 awards, making it the most awarded category in the dataset.
* Economics received the fewest Nobel Prizes with 86 awards, largely because the category was introduced much later in 1969.
* The category analysis showed that scientific fields have consistently dominated Nobel Prize awards throughout history.

#### Gender Representation Insights
* Nobel Prize awards have historically been dominated by male laureates, with women representing only a small percentage of total winners.
* The gender distribution charts highlighted a significant gender gap across Nobel Prize history.
* Marie Curie became one of the most influential early female laureates and remains one of the few individuals to receive multiple Nobel Prizes.
* The gender imbalance was most pronounced in Physics, Chemistry, and Economics, where male laureates overwhelmingly dominated the awards. In contrast, Literature, Peace, and Medicine showed comparatively higher female representation, although women still remained a minority across all Nobel Prize categories.

#### Repeat Winner Insights
* Only 4 individuals won the Nobel Prize more than once. Marie Curie became the only laureate to win Nobel Prizes in two different scientific fields (Physics and Chemistry), Linus Pauling became the only laureate to win Nobel Prizes in two completely different categories (Chemistry and Peace), John Bardeen became the only person to receive two Nobel Prizes in Physics, and Frederick Sanger became the only person to receive two Nobel Prizes in Chemistry.
* Only 2 organisations received multiple Nobel Prizes. The International Committee of the Red Cross (ICRC) won the Nobel Peace Prize three times & the United Nations High Commissioner for Refugees (UNHCR) received the Nobel Peace Prize twice.

#### Prize Sharing Insights
* Nobel Prizes have increasingly been shared among multiple recipients over time.
* The rolling average analysis showed that the average prize share awarded to each laureate gradually decreased as collaborative research became more common.
* The introduction of Economics in 1969 also contributed to the rise in the total number of awards distributed each year.

#### Country Insights & Historical Country Trends
* The United States emerged as the most successful country in Nobel Prize history, winning substantially more prizes than any other nation.
* The United Kingdom and Germany ranked second and third respectively.
* European countries dominated Nobel Prize achievements during the early decades of the awards.
* Before World War II, Nobel Prize winners were heavily concentrated in Europe.
* Following World War II, the United States rapidly overtook European nations and became the dominant Nobel Prize-winning country.
* The geographic distribution of Nobel-winning research shifted significantly during the twentieth century.

#### Research Institution Insights
* Harvard University, University of California, Massachusetts Institute of Technology, Stanford University, and University of Cambridge appeared among the institutions with the highest numbers of Nobel Prize-winning affiliations.
* Nobel Prize-winning research was highly concentrated among a relatively small group of elite universities and research organisations rather than being evenly distributed across institutions worldwide.
* The analysis showed that major research hubs in the United States and Europe have played a dominant role in producing Nobel Prize-winning discoveries over the past century.

#### Research City and Sunburst Insights
* Cambridge, Massachusetts and New York recorded the highest numbers of Nobel Prize-winning research affiliations, making them the two most influential research hubs
* The Sunburst chart revealed that France's Nobel Prize-winning research was heavily concentrated in Paris, showing a strong centralisation of scientific achievement within a single city.
* In contrast, Germany's Nobel Prize-winning discoveries were distributed across multiple cities and research institutions, indicating a more geographically diverse research ecosystem.
* The United Kingdom showed a strong concentration of Nobel Prize-winning research around Cambridge and the University of Cambridge, highlighting the city's long-standing importance in scientific research and innovation.

#### Laureate Age Insights
* The average Nobel Prize winner received their award at approximately 59 years of age, indicating that major scientific and academic recognition typically occurs later in a researcher's career.
* The age distribution histogram showed that most Nobel laureates received their prizes between the ages of 50 and 70, with relatively few winners receiving awards at very young ages.

#### Category Age Trend Insights
* Nobel laureates became progressively older across most categories as time progressed, indicating an increasing delay between discoveries and Nobel Prize recognition.
* Physics showed the strongest ageing trend, with the average winning age rising from below 50 years in the early Nobel era to more than 70 years in recent decades.
* Chemistry and Medicine followed a similar pattern, with average winning ages steadily increasing throughout the twentieth and twenty-first centuries.
* Economics displayed the most stable age pattern, showing much smaller changes over time compared with Physics, Chemistry, and Medicine.

## Highlights

* **Data Cleaning**: Investigated missing values, converted string data into numeric format, and worked with datetime objects for time-based analysis.
* **Pandas Analysis**: Used .value_counts(), .groupby(), .agg(), .sort_values(), and .merge() to analyse Nobel Prize categories, countries, organisations, and laureates.
* **Rolling Average Analysis**: Learned & Applied rolling averages to smooth Nobel Prize sharing trends and reveal long-term changes in collaborative researc
* **Plotly Visualisations**: Created interactive donut charts, bar charts, Choropleth maps, and Sunburst charts to explore Nobel Prize distributions across genders, countries, cities, and research institutions.
* **Seaborn Analysis**: Used histograms, box plots, and .lmplot() with LOWESS regression lines to analyse age distributions and long-term Nobel Prize trends.
* **Gender Analysis**: Found that Nobel Prizes have historically been dominated by male laureates, although female representation has gradually increased over time.
* **Category Analysis**: Identified Medicine as the most awarded Nobel Prize category, while Economics had the fewest awards due to its introduction in 1969.
* **Country Analysis**: Confirmed that the United States became the dominant Nobel Prize-winning nation after World War II, surpassing all European countries.
* **Research Institution**: Identified institutions such as Harvard University, MIT, Stanford University, the University of California system, and the University of Cambridge among the most successful Nobel Prize-affiliated organisations.
* **Prize Sharing Trends**: Observed that Nobel Prizes have increasingly been shared among multiple recipients, reflecting the growing importance of collaborative scientific research.
* **Age Trend Analysis**: Found that the average Nobel laureate received their award at approximately 59 years old and that winning ages have increased across most categories over time.
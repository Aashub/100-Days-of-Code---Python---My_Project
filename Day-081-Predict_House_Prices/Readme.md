# Day 81 – Boston House Price Prediction using Multivariable Regression

## Overview

This is a data analysis and machine learning project where I used Pandas, NumPy, Seaborn, Matplotlib, Plotly, and Scikit-Learn to analyse housing data from Boston and build a property valuation model using Multivariable Linear Regression.

The project focused on exploring relationships between housing features and property prices, preparing data for machine learning, splitting data into training and testing sets, building regression models, evaluating model performance using R² scores and residual analysis, applying logarithmic transformations to improve model accuracy, and using the final model to estimate property values.

Through this project, I learned how multiple variables can be combined to predict house prices, how to evaluate the quality of a regression model, and how data transformations can significantly improve predictive performance.

## Notebook Link

https://drive.google.com/file/d/1kLgRaoqn2b9Twe8rRqx4G3lmP1-65iqC/view?usp=drive_link

## What I Have Learned

* **Training and Testing Data Splits**: Learned how to divide data into training and testing sets using train_test_split(). This allowed the model to be trained on one portion of the data and evaluated on completely unseen data.

* **Multivariable Linear Regression**: Learned how to build regression models using multiple independent variables instead of relying on a single predictor. This allowed house prices to be estimated using many property characteristics simultaneously.

* **Evaluating Regression Performance**: Learned how to use R² scores to measure how much variation in house prices can be explained by the model. Higher R² values indicated better predictive performance.

* **Interpreting Regression Coefficients**: Learned how regression coefficients reveal the influence of each feature on property values. Positive coefficients increased predicted prices, while negative coefficients reduced them.

* **Residual Analysis**: Learned how to analyse residuals (prediction errors) to determine whether a model fits the data well. Residual distributions helped identify skewness and areas where the model could be improved.

* **Data Transformation with Logarithms**: Used np.log() to transform house prices into log prices. This reduced skewness in the target variable and improved overall model performance.

* **Comparing Multiple Models**: Learned how to compare different regression models using training and testing R² scores. This made it possible to determine whether data transformations improved predictive accuracy.

* **Relationship Visualisation with Seaborn**: Used pair plots, joint plots, histograms, and distribution plots to explore relationships between housing variables before building predictive models.
## How It Works 

### Loading and Understanding the Data

* **Loading the Dataset**: Imported Pandas, NumPy, Seaborn, Plotly, Matplotlib, and Scikit-Learn libraries and loaded the Boston Housing dataset containing 506 housing records and 14 variables.

* **Exploring the Dataset**: Used methods such as .shape, .columns, .head(), .info(), and .describe() to understand the structure of the dataset and examine property-related information.

* **Inspecting Data Quality**: Checked for missing values and duplicate records using .isna() and .duplicated(). The analysis confirmed that the dataset contained no missing values and no duplicate records

### Descriptive Statistics

* **Analysing Housing Features**: Used descriptive statistics to examine crime rates, room counts, pollution levels, tax rates, school quality indicators, and housing prices.

* **Student-Teacher Ratio Analysis**: Calculated the average number of students per teacher and found that Boston schools averaged approximately 18.46 students per teacher.

* **Average House Price Analysis**: Calculated the average property price and found that the average Boston home in the dataset was worth approximately $22,530.

* **Room Count Analysis**: Found that properties contained between 3.56 rooms and 8.78 rooms on average per dwelling.

* **Charles River Analysis**: Investigated the CHAS feature and confirmed that it identifies whether a property borders the Charles River (1) or not (0).


### Exploratory Data Analysis

* **Price Distribution Analysis**: Used Seaborn histograms and KDE plots to examine the distribution of Boston housing prices.

* **Distance Analysis**: Visualised commuting distances to employment centres using distribution plots and explored how location influenced housing characteristics.

* **Room Distribution Analysis**: Examined the distribution of average room counts across Boston neighbourhoods.

* **River Access Analysis**: Used Plotly bar charts to compare the number of properties located near the Charles River versus those located elsewhere.

### Relationship Analysis

* **Pair Plot Analysis**: Used Seaborn's .pairplot() to visualise relationships between every feature in the dataset and identify potential correlations.

* **Distance vs Pollution Analysis**: Used .jointplot() to compare employment distance (DIS) and pollution levels (NOX). The visualisation showed that pollution generally decreased as distance from employment centres increased.

* **Industry vs Pollution Analysis**: Compared industrial land usage (INDUS) and pollution levels (NOX). Areas with higher industrial activity generally experienced higher pollution levels.

* **Income vs Rooms Analysis**: Compared lower-income population percentages (LSTAT) with average room counts (RM). Neighbourhoods with higher proportions of lower-income residents generally contained fewer rooms per dwelling.

* **Income vs House Price Analysis**: Examined the relationship between lower-income population percentages and housing prices. Higher values of LSTAT were associated with lower property values.

* **Rooms vs House Price Analysis**: Analysed the relationship between room counts and property prices. Houses with more rooms generally commanded significantly higher market values.

### Building the Regression Model

#### Splitting the Data

* **Training and Testing Sets**: Split the dataset into training and testing subsets using an approximately 80/20 split.
* **Training Data**: Approximately 79.8% of the dataset was used for training.
* **Testing Data**: Approximately 20.2% of the dataset was reserved for model evaluation.

#### Running Multivariable Regression

* **Training the Model**: Built a Multivariable Linear Regression model using Scikit-Learn's LinearRegression().
* **Evaluating Initial Performance**: The initial model achieved a training R² score of approximately 0.75, meaning that the model explained around 75% of the variation in Boston housing prices.

#### Coefficient Analysis

* **Evaluating Feature Importance**: Analysed regression coefficients to understand how different housing characteristics influenced property values.
* **Room Premium Analysis**: The model estimated that each additional room increased property value by approximately $3,108.
* **Positive Influences on Price**: Features such as room count (RM) and proximity to the Charles River (CHAS) positively influenced predicted property values.
* **Negative Influences on Price**: Features such as pollution (NOX), student-teacher ratio (PTRATIO), crime rate (CRIM), and lower-income population percentage (LSTAT) negatively impacted property values.

### Residual Analysis

#### Evaluating Model Errors

* **Predicted vs Actual Prices**: Compared actual housing prices against predicted prices to assess model accuracy.
* **Residual Distribution Analysis**: Examined the distribution of residuals to determine whether prediction errors appeared random.
* **Residual Skewness**: The original model produced residuals with a skewness of approximately 1.46, indicating that prediction errors were not perfectly symmetrical.

### Improving the Model with Data Transformation

#### Log Transformation

* **Transforming House Prices**: Applied np.log() to housing prices before retraining the model.
* **Reducing Skewness**: The log transformation reduced skewness in the target variable and improved the suitability of the data for linear regression.
* **Building a New Regression Model**: Trained a second regression model using log-transformed house prices.

#### Evaluating the Improved Model

* **Improved Training Performance**: The log-transformed model achieved a training R² score of approximately 0.79, improving upon the original model's score of 0.75.
* **Improved Residual Distribution**: Residual skewness dropped dramatically from 1.46 to approximately 0.09, indicating a much more balanced error distribution.

### Out-of-Sample Testing

#### Comparing Model Performance

* **Original Model Performance**: The original regression model achieved a test-set R² score of approximately 0.67.
* **Log Model Performance**: The log-transformed model achieved a test-set R² score of approximately 0.74.
* **Model Comparison**: The transformed model performed substantially better on unseen data, demonstrating that the logarithmic transformation improved generalisation performance.

### Property Valuation

#### Predicting an Average Property

* **Average Property Valuation**: Using average values for all housing features, the model estimated a property value of approximately $20,703.

### Predicting a Custom Property

* **Custom Property Characteristics**: Valued a custom property containing 8 rooms, a student-teacher ratio of 20, a distance of 5 from employment centres, near to the Charles River.
* **Estimated Property Value**: The model predicted a property value of approximately $25,792.

### Key Insights Found

#### Housing Market Insights
* The average home in the Boston dataset was valued at approximately $22,530, while the model's estimated value for an average property was approximately $20,703, indicating that the regression model captured overall market pricing reasonably well.
* Boston properties varied substantially in size, ranging from approximately 3.56 rooms to 8.78 rooms per dwelling, highlighting the diversity of housing within the dataset.

#### Housing Feature Insights
* The strongest positive relationship with house prices came from the average number of rooms (RM). The model estimated that every additional room increased property value by approximately $3,108.
* Properties located near the Charles River (CHAS) generally received a positive price premium, suggesting that waterfront proximity increased housing demand.
* Higher levels of pollution (NOX), larger student-teacher ratios (PTRATIO), higher crime rates (CRIM), and larger lower-income populations (LSTAT) were all associated with lower property values.

#### Relationship Analysis Insights
* The distance-versus-pollution analysis showed that pollution levels generally decreased as properties became farther away from major employment centres.
* Neighbourhoods with higher proportions of lower-income residents typically had fewer rooms per dwelling and significantly lower housing prices.
* The room count analysis demonstrated a clear positive relationship between property size and market value, making room count one of the most influential predictors in the model.

#### Regression Model Insights
* The initial Multivariable Regression model achieved a training R² score of approximately 0.75, meaning that around 75% of housing-price variation could be explained by the available housing features.
* The test-set R² score of approximately 0.67 confirmed that the model retained a substantial amount of predictive power when evaluated on unseen data.

#### Data Transformation Insights
* Applying a logarithmic transformation improved training performance from 0.75 to 0.79 and testing performance from 0.67 to 0.74.
* Residual skewness decreased dramatically from 1.46 to 0.09, indicating that prediction errors became much more normally distributed after transformation.
* The log-transformed model provided both better predictive accuracy and more reliable statistical assumptions than the original model.

#### Property Valuation Insights
* A property with average Boston housing characteristics was estimated to be worth approximately $20,703.
* Increasing the number of rooms to 8, maintaining river access, and using the specified custom property characteristics increased the estimated value to approximately $25,792.

## Highlights

* **Relationship Visualisation**: Used pair plots and joint plots to investigate how housing features interact with one another.
* **Train-Test Splitting**: Divided the dataset into training and testing sets to evaluate model performance on unseen data.
* **Multivariable Regression**: Built a housing valuation model using multiple housing characteristics simultaneously.
* **Coefficient Interpretation**: Identified room count as one of the strongest positive drivers of house prices.
* **Residual Analysis**: Evaluated prediction errors using residual plots and distribution analysis.
* **Log Transformation**: Improved model performance by transforming housing prices with np.log().
* **Data Transformation**: Applied transformations to improve model performance.
* **Model Comparison**: Compared original and transformed models using training and testing R² scores.
* **Property Valuation**: Estimated the market value of both average and customised Boston properties using the final regression model.

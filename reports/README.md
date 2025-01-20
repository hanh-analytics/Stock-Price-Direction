# Reports: Insights and Explanations

This folder contains detailed reports, insights, and explanations for the stock price analysis project. The project aims to analyze historical stock price data, derive actionable insights, and predict the price direction of Amazon.com, Inc. (AMZN) stock using various analytical techniques and models. Below are the key components included in this folder:


## 1. **Hypothesis Testing**  
   - **Objective**: Evaluate whether the proportion of days where the closing price is higher than the opening price significantly deviates from 0.50.  
   - **Methodology**:  
     - Use a binomial test to compare the observed proportion of "higher close" days against the expected proportion of 0.50.  
     - Perform the test at a specified significance level (`alpha= 0.05`).  
   - **Outcome**: Statistical insight into whether the daily stock price movement is random or influenced by other factors.  

## 2. **Dashboard**
   - **Objective**: Provide an interactive visualization of stock trends and patterns.
   - **Features**:
     - Historical stock price trends.
     - Volume analysis and other metrics.
     - User-friendly interface for exploring data dynamically.
   - **Tools Used**: Created using Pyplot Dash.

## 3. **Binary Classification Model**
   - **Objective**: Predict whether the next day’s stock closing price will be higher than the opening price.
   - **Approach**:
     - Train, validate, and test machine learning models (Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting).
     - Evaluate models using metrics like AUC-ROC.
     - Perform hyperparameter tuning to optimize model performance.
   - **Outcome**: Final tuned Gradient Boosting model with insights into prediction accuracy.

---

### How to Navigate
Each section contains a detailed explanation of the methods, tools, and results:
- **`hypothesis_testing.md`**: Statistical testing methods and results.
- **`dashboard.md`**: Insights of the  stock trends and patterns.
- **`hypothesis_classification.md`**: Model development, tuning process, and evaluation results.

Feel free to explore these reports for a comprehensive understanding of the project 🔍 

---

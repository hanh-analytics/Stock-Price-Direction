# Hypothesis Testing for Amazon Stock Price Prediction

## **1. Introduction**
In this project, we aim to predict the price direction of Amazon.com, Inc. (AMZN) stock based on historical data spanning from 1997 to 2020. Our primary objective is to determine whether a day's closing price is higher than its opening price and to utilize this insight for binary classification tasks.

Hypothesis testing plays a critical role in this project by evaluating whether significant patterns exist in the stock's price movement. These patterns serve as the foundation for developing effective machine learning models. By identifying meaningful trends, we can enhance the model's ability to navigate the complex and volatile stock market.

The specific codes for each value is demonstrated in the Jupyter Notebook [Hypothesis_testing.ipynb](https://github.com/hanh-analytics/Stock-Price-Direction/blob/d36fd13eeac1ce27aeb7b8d59c052a73d1f12694/notebooks/hypothesis_testing.ipynb)

## **2. Problem Definition**
This analysis seeks to determine if there is an inherent directional bias in Amazon's stock price. Specifically, we evaluate whether the proportion of days where the closing price exceeds the opening price deviates significantly from 50%.

## **3. Define the Hypotheses**
- **Null Hypothesis $H_0$:** The proportion of days where the closing price is higher than the opening price (*p*) is equal to 0.50 (*p* = 0.50).
- **Alternative Hypothesis $H_1$:** The proportion of days where the closing price is higher than the opening price (*p*) is not equal to 0.50 (*p* ≠ 0.50).

This is a two-tailed test since we are interested in deviations in both directions. 

The hypothesis test serves as a preliminary step to evaluate whether there is a significant trend in the stock price direction. Identifying such trends ensures that the classification model is built on meaningful patterns, potentially increasing its predictive power.

## **4. Data Preparation**
1. **Dataset Overview:**
   - Historical daily stock prices for Amazon (1997-2020).
   - Key features: Date, Open Price, Close Price, and Price Direction (derived as `1` if Close > Open, otherwise `0`).
2. **Data Cleaning:**
   - Handle missing values by dropping NaNs.
   - Filter for relevant columns.
3. **Descriptive Statistics:**
   - Provide summary statistics for Open and Close prices.
   - Compute the proportion of days where Close > Open.

## **5. Methodology**
1. **Statistical Test:**
   - Perform a one-sample z-test for proportions to test the hypothesis.
   - Assumptions:
     - Random sampling of days.
     - Sufficient sample size to approximate the sampling distribution of the proportion as normal.
2. **Confidence Level:**
   - Use a 95% confidence level (α=0.05) .
3. **Test Statistic:**
   - Formula for z-statistic:
     
$$
z = \frac{{\hat{p} - p_0}}{{\sqrt{{p_0 (1 - p_0) / n}}}}
$$

Where:
$\hat{p}$: Sample proportion, $p_0$: Hypothesized population proportion (0.50), $n$: Sample size.

## **6. Hypothesis Testing Execution**
1. Calculate the sample proportion $\hat{p}$.
2. Compute the z-statistic using the formula.
3. Determine the p-value for the z-statistic.
4. Compare the p-value with α = 0.05:
   - Reject $H_0$ if p-value < α.
   - Fail to reject $H_0$ if p-value ≥ α.

Include code snippets and visualizations (e.g., a histogram of price direction proportions).

## **7. Results and Interpretation**
- Report the z-statistic and p-value.
- Indicate whether the null hypothesis is rejected.
- Discuss implications of the findings:
  - If $H_0$ is rejected, there is evidence of a significant directional bias in the stock price.
  - If $H_0$ is not rejected, the stock price direction appears random.

## **8. Limitations and Assumptions**
- Sample size limitations.
- Assumption of independent daily returns may not hold due to market trends or external factors.

## **9. Conclusion**

Based on the results of the hypothesis test, we fail to reject the null hypothesis. The observed proportion of days where the closing price is higher than the opening price is 0.5003, with a Z-statistic of 0.0526 and a p-value of 0.9581. Since the p-value is much greater than the commonly used significance level of 0.05, we do not have sufficient evidence to suggest that the proportion of days where the closing price is higher than the opening price significantly differs from 0.50. Therefore, we conclude that there is no significant trend in the closing prices relative to the opening prices.

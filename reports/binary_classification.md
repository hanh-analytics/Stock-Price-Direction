# Binary Classification

## 1. **Introduction**
   - **Purpose of the Model**: This model predicts simply the price direction of the stock price, and possibly the closing and open price of the next day.
   - **Target Variable**: The target is binary: 1 if the next day's closing price is higher than the opening price, and 0 if it is not.

## 2. **Data Description**
   - **Dataset**: We have data for the period from 1997 up to year 2020 that we have split that into training (1997-2016), validation (2016-2018) and testing (2018-2020) periods. The data is available in the AMZN_train.csv, AMZN_val.csv and AMZN_test.csv files, respectively.
   - **Features**: Features include moving average over 7 days and 30 days, current price direction, price range, closing price, high, low, volume, and other financial indicators.
   - **Preprocessing**:
     - **Handling Missing Values**: Missing values in the columns of test set were imputed using the means value of the columns.
     - **Label Encoding**: To test whether the closing price was higher than the open price, we added one column named `Target` with labels encoded `0` is `False` and `1` is `True`.
     - **Time-Series Split**: Since the assignments were given by the recruiter, the datasets were ensured to not have data leakage from the future into the training set. 

## 3. **Model Selection**
   - **Algorithms Used**: The model was trained using logistic regression, decision trees, random forests, and gradient boosting.
   - **Model Selection Criteria**: Logistic regression was chosen for its simplicity, while decision trees and random forests were explored for potentially higher accuracy. Gradient boosting was good at apturing complex patterns in the data, especially when dealing with noisy, high-dimensional datasets like stock market data.

## 4. **Model Training and Evaluation**
   - **Training Process**: The models were trained using the training set, with hyperparameters optimized via grid search (for logistic regression) and random search(for decision tree, random forest, and gradient boosting) and 5-fold cross-validation.
   - **Metrics Used**: "The models were evaluated using the ROC-AUC score. The AUC-ROC score was 0.53, indicating that its predictive power is only slightly better than random guessing (AUC = 0.5).

## 5. **Results Interpretation**
   - **Model Performance**: While the Gradient Boosting model was the best performer, its AUC score of 0.5238 suggests that it does not provide a reliable method for predicting daily price direction.
   - **Insights**: The findings indicate that either:
      - The task is inherently difficult due to the nature of the stock market.
      - The data and features used are insufficient for meaningful predictions.

## 6. **Limitations and Future Work**
   - **Limitations**: The model may not fully capture complex market conditions or trends beyond the given features because stock market is complex.
   - **Future Improvements**: Include additional market data such as trading volume (as the data of volume is the highest in feature importance), volatility, or external sentiment data or consider time-series models like ARIMA, LSTM, or Transformer-based approaches that may capture temporal dependencies better.

## 7. **Conclusion**
   - The results suggest that predicting daily price direction is a challenging task, and while the model offers a slight improvement over random guessing, further work is needed to achieve actionable performance.

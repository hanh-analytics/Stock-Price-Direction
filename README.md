# Stock Price Direction 🧮

_This data project has been used as a take-home assignment in the recruitment process for the data science positions at NeuroTrade. The source of this project was gathered from [StrataScratch.com](https://www.stratascratch.com/)_

This project focuses on predicting the day-to-day price direction of Amazon.com, Inc. stock. Rather than forecasting the exact stock price, the objective is to classify whether the next day’s closing price will be higher or lower than the opening price. Furthermore, hypothesis testing and dashboard were created to find more helpful insights of the stock market. 

## Hypothesis Testing
Hypothesis testing is used to evaluate the significance of various factors influencing the stock price direction. By performing statistical tests on features such as volume, opening price, and moving averages, we determine whether these factors are statistically significant in predicting the next day's stock movement. This analysis ensures that the selected features are reliable for the model and that the observed patterns are not due to random chance.

## Model Development
The core of the project involves developing classification models to predict whether the stock price will increase or decrease. Various machine learning algorithms, including Logistic Regression and Decision Trees, are explored, with hyperparameter tuning applied to optimize performance. The model is trained on historical stock data and evaluated using metrics to ensure it can make reliable predictions for stock price direction.

## Dashboard Creation
Interactive dashboards are developed to visualize the performance of the model and offer insights into temporal patterns in stock prices. The dashboards present key metrics, such as prediction accuracy and model performance over time. Additionally, they help uncover seasonal or cyclical trends, allowing stakeholders to identify the best times to act on predictions. Plotly Dash is used to build visualizations that make the data analysis accessible.

### Background
The stock market is inherently complex and highly volatile, making precise price predictions challenging. However, predicting price direction can still support profitable strategies by offering guidance on market trends without requiring exact price estimations.

### Key Objectives
- Develop a model to classify stock price movement direction (Higher or Lower).
- Analyze historical market data to extract relevant features influencing price direction.
- Evaluate model performance to ensure reliable classification predictions.
- Create dashboards for performance analysis and seasonal/temporal analysis to visualize insights.
- Formulate and test hypotheses regarding the significance of various stock-related features (e.g., volume, moving averages) in predicting the direction of stock price movement, ensuring the reliability of the selected features for the classification model.

## Data Description
We have data for the period from 1997 up to 2020 that has been split into:
- **Training period**: 1997-2016
- **Validation period**: 2016-2018
- **Testing period**: 2018-2020
- **Opening Price**: First price of the stock when the market opens.
- **Closing Price**: Last price of the stock when the market closes.
- **Bearish Day**: A trading day where the stock's closing price is lower than its opening price, indicating a downward trend and negative market sentiment.
- **Bullish Day**: A trading day where the stock's closing price is higher than its opening price, reflecting an upward trend and positive market sentiment.

Each dataset has the following 7 columns:
- **Date**: in format YYYY-MM-DD
- **Open**: stock price upon opening of an exchange
- **High**: the highest stock price on a given day
- **Low**: the lowest stock price on a given day
- **Close**: stock price at the end of a trading day
- **Adj Close**: adjusted closing price that takes into account corporate actions
- **Volume**: the amount of shares traded over the course of a trading day

The data files are available in:
- **AMZN_train.csv**: Training data
- **AMZN_val.csv**: Validation data
- **AMZN_test.csv**: Testing data

## Project Structure
- `data/`: Contains raw and processed datasets.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and model development.
- `visualization/`: Interactive dashboards for performance and seasonal/temporal analysis.
- `reports/`: Project documentation and reports.

## Approach
1. **Data Exploration**  
   Historical stock market data for Amazon is analyzed. Features include opening and closing prices, volume, moving averages, and technical indicators.

2. **Data Preprocessing**  
   Missing values and data anomalies are handled. Feature engineering is performed to derive relevant market patterns.

3. **Model Development**  
   Classification models, such as Logistic Regression, Decision Trees, and advanced machine learning algorithms, are developed. Hyperparameter tuning is applied to optimize model performance.

4. **Evaluation Metrics**  
   Accuracy, precision, recall, and F1 score are used to assess prediction performance. Backtesting on historical data simulates real-world scenarios.

5. **Dashboard Creation**  
   Dashboards are developed using Plotly Dash.
   - **Performance Analysis**: Provides a comprehensive view of model metrics and prediction results.
   - **Seasonal or Temporal Analysis**: Visualizes trends and patterns over time, helping identify cyclical behaviors in stock prices.

## Technologies Used
- **Programming Language**: Python
- **Libraries**: pandas, scikit-learn, matplotlib, numpy, Plotly Dash
- **Data Visualization**: matplotlib, seaborn, Tableau, Plotly Dash
- **Model Training and Evaluation**: scikit-learn
- **Dashboard Development**: Plotly Dash

## Key Deliverables
- Trained classification model for predicting Amazon's stock price direction.
- Performance analysis and visualizations.
- Interactive dashboards for performance and temporal analysis.
- Insights into factors influencing daily price movement decisions.

## Usage Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/username/Prediction-of-Stock-Price-Direction.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd Prediction-of-Stock-Price-Direction
    ```

3. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Launch Jupyter Notebook**:
    ```bash
    jupyter notebook
    ```
    - This will open Jupyter in your default web browser.

5. **Open the notebook files**:
    - Open the relevant notebooks from the `notebooks/` folder. For example:
      - `notebooks/binary_classification.ipynb` for model development.
      - `notebooks/dashboard.ipynb` for creating the dashboard.
      - `notebooks/hypothesis_testing.ipynb` for hypothesis testing.

6. **Run the cells in the notebook**:
    - Execute the cells one by one in Jupyter to perform data preprocessing, model training, hypothesis testing, and dashboard creation.

# License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/hanh-analytics/Stock-Price-Direction/blob/65d280b6e67010d3935dba556e009784b49216e1/LICENSE) file for details.


## Results
- Contributed by both the binary classification model and hypothesis testing, there is no strong or clear trend in the daily price direction of the stock. 
- Further insights of the stock market, please visit the folder `report/`

## Future Improvements
- Incorporating additional financial indicators and market sentiment analysis.
- Exploring advanced machine learning models such as LSTM for time-series prediction.
- Enhancing real-time prediction capabilities.
- Expanding dashboard functionalities for deeper insights.

## Contributing
Contributions are welcome! Please follow the steps below to contribute:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Commit your changes and push them to your branch.
- Submit a pull request for review.

## Contact
Author: Hanh Le  
Email: katele2277@gmail.com  
GitHub: [https://github.com/hanh-analytics](https://github.com/hanh-analytics)

Thank you for exploring the **Prediction of Stock Price Direction** project!


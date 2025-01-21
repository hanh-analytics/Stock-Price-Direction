# **Stock Price Dashboard Report: Comprehensive Analysis of Market Trends**  

## **1. Introduction**  
- **Purpose of the Report**:  
   - This report examines stock price trends and trading patterns through visualizations and metrics provided by the dashboard.  
- **Key Definitions**:  
   - **Opening Price**: The first price of the stock when the market opens.  
   - **Closing Price**: The last price of the stock when the market closes.  
   - **Bearish Day**: A trading day where the closing price is lower than the opening price.  
   - **Bullish Day**: A trading day where the closing price is higher than the opening price.  

## **2. Performance Analysis**  
### **2.1. Highest and Lowest Closing Prices**  
- **Visual**: Annotated line chart with marked high and low points.
   ![Highest and Lowest Closing Prices](https://github.com/hanh-analytics/Stock-Price-Direction/blob/b67d589dcad65811a2c27e43fd8b6fadabb79d66/visualization/Closing%20Price%20with%20Peaks%20and%20Trough.png)

- **Data-story telling**:
   The journey of Amazon's stock price from May 1997 to April 2020 presents an insightful picture of long-term growth, market turbulence, and a remarkable recovery.
  
  _1. Early Struggles and Gradual Growth (1997–2016)_:
   
     - **May 1997** marks the trough of the stock's journey, which signifies the challenging early days for Amazon. From here, the stock price begins a gradual increase, highlighting Amazon's steady expansion and the growing recognition of its business model, particularly its e-commerce dominance and tech innovations.
     - **The steady rise** in Amazon's stock price shows a consistent boost in investor confidence. This is likely driven by the company's growth in global markets, its successful expansion into new sectors like cloud services through AWS, and its ability to adapt to changing consumer needs. It reflects the payoff of long-term strategic investments, with the stock price climbing steadily as a result.

   _2. A Surge of Confidence and Sharp Decline (Sep 2017 – Dec 2018)_:

  - From **September 2017 to September 2018**, Amazon’s stock saw a significant increase, fueled by growing investor optimism and positive market reactions to the company’s impressive earnings reports. This period also reflected Amazon’s successful expansion into new markets and innovations like Alexa and the growth of its Prime membership.
 
  - However, this sharp rise was followed by a steep decline in **December 2018**, likely triggered by broader market corrections, concerns over rising costs, or shifts in the economy. This volatility highlights that, despite Amazon’s growth, it was still _vulnerable_ to external market forces.
 
  _3. How the COVID-19 Pandemic Fueled Amazon’s Growth and Stock Surge (April 2020)_:

  - The big rise in Amazon's stock price in April 2020 was driven by the **COVID-19 pandemic**. As more people turned to online shopping, Amazon’s services became essential, leading to a major boost in profits. With more people relying on Amazon for everything from household items to cloud services, the company’s stock soared.
    
  - This surge shows how Amazon was able to not just survive the chaos of the pandemic, but actually thrive by meeting the new needs of consumers, helping its stock price reach new heights.
  
- **Insights**:  
   - **Long-term Growth and Stability**: Despite fluctuations, Amazon’s stock price demonstrated a consistent upward trend over time, reflecting strong business fundamentals and investor confidence in the company’s growth trajectory.
     
   - **Market Sensitivity**: The sharp decline in late 2018 highlights Amazon’s sensitivity to broader market conditions, emphasizing that even dominant companies face challenges during periods of economic uncertainty.
  
   - **How the COVID-19 Pandemic Fueled Amazon's Growth**: The final surge in 2020 highlights Amazon's ability to adapt to the global challenges of the pandemic, meeting the increased demand for e-commerce and essential services. This surge proves Amazon’s resilience, showing how it capitalized on shifting consumer behavior to drive growth and boost its stock price.  

### **2.2. Frequency of Bullish and Bearish Days**  
- **Visual**: A bar chart comparing counts of bullish and bearish days.
  ![Bar Chart](https://github.com/hanh-analytics/Stock-Price-Direction/blob/b67d589dcad65811a2c27e43fd8b6fadabb79d66/visualization/Bullish%20and%20Bearish%20Day%20Bar%20Graph.png)
    
- **Metric**: Count instances where the closing price was higher or lower than the opening price.  
- **Insights**:  
   - **Balanced Market Sentiment**: With only a slight edge in the number of Bullish Days, the market has experienced a relatively balanced sentiment over the period, suggesting a healthy mixture of optimism and pessimism influencing investment decisions.
      
   - **High Market Volatility**: The similar number of Bullish and Bearish days suggests _frequent changes_ in market sentiment, indicating that the market was highly responsive to shifts in confidence. This may highlight that investors were _cautious_ at times, reacting to external uncertainties or market events.

### **2.3. Daily Percentage Price Changes**  
- **Formula**: \(((\text{Close} - \text{Open}) / \text{Open}) \times 100\)  
- **Visual**: Histogram or box plot showing distribution of percentage changes.  
- **Insights**:  
   - Determine the average daily returns and their variability.  
   - Highlight days with extreme percentage changes using annotations.  
   - Include metrics like the median daily return to minimize outlier influence.  

## **3. Seasonal or Temporal Analysis**  
### **3.1. Best and Worst Performing Months/Days of the Week**  
- **Visual**: Bar chart of average closing prices by month or day of the week.  
- **Insights**:  
   - Identify consistent market patterns based on the calendar period.  
   - Incorporate ranges or standard deviations to show variability.  
   - Overlay contextual events (e.g., holidays, quarterly reports) to identify correlations with performance.  

### **3.2. Rolling Performance Metrics**  
- **Visual**: Line chart with 7-day and 30-day rolling averages for prices and volume overlaid on raw prices.  
- **Insights**:  
   - Identify short- and medium-term trends in stock performance.  
   - Highlight periods of significant deviation from rolling averages.  

## **4. Volume Patterns**  
- **Visual**: Line or bar chart showing trading volume over time.  
- **Insights**:  
   - Analyze how trading activity fluctuates over different periods (e.g., high-volume days, market events).  
   - Correlate volume spikes with bullish or bearish trends to assess potential drivers.  


## **5. Refinements and Additional Insights**  
### **5.1. Refinements to Key Metrics**  
- Contextualize peaks and troughs with potential reasons (e.g., major announcements, macroeconomic factors).  
- Analyze bullish/bearish trends by temporal periods for better segmentation.  
- Add contextual overlays to existing visuals to improve clarity.  

### **5.2. Expanding Insights**  
- Include supplementary metrics such as median price changes or variability by season.  
- Highlight extreme outliers in trends with annotations for deeper analysis.  

---

## **6. Conclusion**  
- **Summary of Findings**:  
   - Recap key insights derived from performance and temporal analyses.  
   - Emphasize any patterns or trends of interest to stakeholders.  
- **Recommendations**:  
   - Provide actionable suggestions based on findings (e.g., "Monitor trading volume during high-volatility periods to better predict price swings.")  
   - Suggest next steps for refining the dashboard (e.g., incorporating sentiment analysis or additional financial indicators).  


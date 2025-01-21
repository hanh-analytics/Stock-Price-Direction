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
- **Visual**: A bar chart and line chart comparing counts of bullish and bearish days.
![Bar Chart](https://github.com/hanh-analytics/Stock-Price-Direction/blob/b67d589dcad65811a2c27e43fd8b6fadabb79d66/visualization/Bullish%20and%20Bearish%20Day%20Bar%20Graph.png) ![Line Chart](https://github.com/hanh-analytics/Stock-Price-Direction/blob/f52ec753d2edf7b10ed8daae4c5862d623d97cda/visualization/Bullish%20vs%20Bearish%20Graph.png)
    
- **Metric**: Count instances where the closing price was higher or lower than the opening price.

- **Data-story telling** (Line Chart)

   - There are noticeable spikes in **Bullish Days** around **March and October**, suggesting strong market optimism during these months, possibly linked to seasonal trends or key economic events.
 
   - **Bearish Days** tend to peak in **June, August, and October**, which may reflect times of increased market pessimism or periods of correction.
 
   - Both Bearish Days and Bullish Days peak in October, indicating that October is a month of high market activity and sentiment volatility.  October is historically known for increased market volatility, sometimes referred to as the _"October Effect"_. Thus, it makes investors anxious, leading to more reactive trading and rapid price changes.  
    
- **Insights** (Bar Chart)
  
   - **Balanced Market Sentiment**: With only a slight edge in the number of Bullish Days, the market has experienced a relatively balanced sentiment over the period, suggesting a healthy mixture of optimism and pessimism influencing investment decisions.
      
   - **High Market Volatility**: The similar number of Bullish and Bearish days suggests _frequent changes_ in market sentiment, indicating that the market was highly responsive to shifts in confidence. This may highlight that investors were _cautious_ at times, reacting to external uncertainties or market events.
 
   - **Resilience and Long-Term Growth**: For long-term investors, this balance suggests that while the market can experience short-term downturns, resilience and optimism ultimately outpace the negative days, offering potential for long-term returns. As seen in the line graph, the overall closing price gradually _increase_ over the period.
 
   - **Cyclical Patterns**: The nearly equal split between Bullish and Bearish days signals a market subject to cyclical patterns, where optimism is often followed by corrections, emphasizing the importance of patience and strategy in dealing with short-term market fluctuations.
 
   - **Investor psychology**: Investors often overreact to negative news, causing bearish sentiment to intensify during times of economic uncertainty, while during periods of growth, sentiment can rise quickly, causing bullish days to dominate.
 
- **Recommendations for Action**:

   - **For Investors**: Use insights into seasonality to align investment strategies with market trends, focusing on bullish months for growth-oriented investments and bearish months for value opportunities.
 
   - **For Analysts**: Dive deeper into the specific events or patterns influencing peaks and troughs, such as earnings seasons, economic indicators, or geopolitical developments.
 
   - **For Risk Manangement**: To effectively manage risk, it is advisable to prepare for potential market corrections during bearish periods by maintaining a well-balanced portfolio. This approach helps mitigate the impact of sudden market volatility and provides a safeguard against unforeseen fluctuations.  

### **2.3. Daily Percentage Price Changes**  
- **Formula**: ((Close - Open) / Open) * 100
  
- **Visual**: Histogram  showing distribution of percentage changes.

![Histogram](https://github.com/hanh-analytics/Stock-Price-Direction/blob/157a50cb6ee191f89620b5e54b6ee2aa36791590/visualization/Percentage%20histogram.png)

- **Data-storytelling**:
   - The bell-shaped histogram indicates that the daily percentage changes of the stock follow a roughly **normal distribution**, with most changes concentrated around the mean (near 0%).
 
   - The highest frequency occurs between -2% and 2%. This suggests that the stock is relatively **stable** on a day-to-day basis, with minor fluctuations being the norm.
 
   - While rare, the presence of data points in the tails (beyond ±10%) highlights the possibility of **significant market events** causing dramatic price swings.
     
- **Insights**: If previous charts indicate high market volatility, but this histogram shows a bell-shaped, normal distribution centered around small daily percentage changes, this suggests that the volatility is driven by **occasional extreme days** rather than frequent large movements.
  
   - If previous charts indicate high market volatility, but this histogram shows a bell-shaped, normal distribution centered around small daily percentage changes, this suggests that the volatility is driven by **occasional extreme days** rather than frequent large movements.
      
   - While most daily changes are small, the tails of the histogram (beyond ±5%) reflect rare but **significant price movements**. Previous charts analyzing bearish and bullish days likely captured these outliers, revealing high volatility during those periods.
       
   - The bell-shaped symmetry of the histogram suggests that both bullish and bearish movements occur with similar frequency and magnitude, supporting the idea of **balanced market sentiment** (Bar Chart of Bullish vs Bearish Days) overall. 

## **3. Seasonal or Temporal Analysis**  

### **3.1. Best and Worst Performing Months/Days of the Week**  
- **Visual**: Bar plot of average closing prices by month or day of the week.
  ![Bar](https://github.com/hanh-analytics/Stock-Price-Direction/blob/157a50cb6ee191f89620b5e54b6ee2aa36791590/visualization/Average%20closing%20Price.png)
  
- **Insights**:  
   - The average closing price by month graph shows no significant differences in monthly averages, indicating that the overall price levels are relatively stable and **do not exhibit seasonal patterns**.
     
   - **Short-Term Trading**: Traders should focus on seasonal patterns in **bullish and bearish days**, as these reveal opportunities to capitalize on short-term volatility.
 
   - **Long-Term Investing**: For long-term investors, the **stable average monthly prices** suggest that the stock remains a consistent investment, with short-term fluctuations balancing out over time.

### **3.2. Rolling Performance Metrics**  
- **Visual**: Line chart with 7-day and 30-day rolling averages for prices and volume overlaid on raw prices.
  ![Rolling Performance](https://github.com/hanh-analytics/Stock-Price-Direction/blob/157a50cb6ee191f89620b5e54b6ee2aa36791590/visualization/Rolling%20Average.png)
   
- **Insights**:
  
   - **Long-term uptrend**: The graph shows a steady increase in the stock's closing price over the years, with a significant acceleration in growth after 2015.
     
   - **Increased Volatility in Recent Years**: After 2015, the rolling averages reveal bigger swings, pointing to higher market volatility during this time.
 
   - **Stability in Early Year**: From 2000 to 2010, the rolling averages are relatively flat, reflecting **minimal growth and lower volatility** during this period. This aligns with the earlier observation that the average closing price was low during these years, consistent with the trough observed in 1997. The stock was likely still in its early growth stages.
 
   - **Alignment of Rolling Averages**: The 7-day rolling average closely tracks the 30-day rolling average, particularly in periods of less volatility. This shows that short-term price changes tend to align with longer-term trends, highlighting the consistency of the stock's overall growth.

## **4. Conclusion**  

- **Summary of Findings**:  
   - Together, they tell a cohesive story of the stock's evolution: an **early period of low and stable prices**, followed by **accelerated growth and heightened volatility** in later years.
     
   - The historical patterns emphasize the stock's capacity for growth while also signaling potential risks, making it crucial to balance optimism with caution in future strategies.
      
- **Recommendations**:
  
   - **Exploration of Seasonality:** Dive deeper into seasonal patterns and their influence on price trends by performing time-series decomposition.
     
   - **Volatility Analysis**: Analyze the volatility patterns in greater detail, such as calculating metrics like standard deviation to provide stakeholders with actionable risk insights. 

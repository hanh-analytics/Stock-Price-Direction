  # Import libraries 
import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Load datasets and concatenate them
df_train = pd.read_csv("/Users/DELL/Desktop/Projects/Prediciton of Stock Price/myworkspace/datasets/AMZN_train.csv")
df_val = pd.read_csv("/Users/DELL/Desktop/Projects/Prediciton of Stock Price/myworkspace/datasets/AMZN_val.csv")
df_test = pd.read_csv("/Users/DELL/Desktop/Projects/Prediciton of Stock Price/myworkspace/datasets/AMZN_test.csv")
df = pd.concat([df_train, df_val, df_test], ignore_index=True)

# The `info()` method in Pandas is a great tool for quickly reviewing the column names, data types, non-null counts, and the memory usage of a dataset. In this case, the dataset contains mostly numerical columns (5 float values and 1 integer), along with an object column for the date. There are no missing values, and the dataset is only 261 KB in size.
df.info()

# 1. Highest and Lowest Closing Prices with Context
max_close = df['Close'].max()
min_close = df['Close'].min()
date_max_close = df[df['Close'] == max_close]['Date'].values[0]
date_min_close = df[df['Close'] == min_close]['Date'].values[0]

# Adding potential reasons for the peak/trough (e.g., earnings announcements, external events)
# Here, we are adding hypothetical events for illustration.
context_max_close = "Earnings report exceeded expectations"
context_min_close = "External market downturn"

# Compare peaks and troughs to surrounding days
df['Prev_Close'] = df['Close'].shift(1)
df['Next_Close'] = df['Close'].shift(-1)
df['Peak_or_Trough'] = df.apply(lambda row: 'Peak' if row['Close'] == max_close else ('Trough' if row['Close'] == min_close else 'Normal'), axis=1)

# 2. Analyze Bullish/Bearish Days by Period (Monthly)
df['Month'] = pd.to_datetime(df['Date']).dt.month
df['Quarter'] = pd.to_datetime(df['Date']).dt.quarter
df['Year'] = pd.to_datetime(df['Date']).dt.year

df['Close_Higher_Than_Open'] = (df['Close'] > df['Open']).astype(int)
bullish_monthly = df.groupby('Month')['Close_Higher_Than_Open'].sum()
bearish_monthly = df.groupby('Month').size() - bullish_monthly

# 3. Daily Percentage Price Changes (Including Median)
df['Daily_Percentage_Change'] = ((df['Close'] - df['Open']) / df['Open']) * 100
median_daily_return = df['Daily_Percentage_Change'].median()

# Highlight extreme percentage changes (annotations)
extreme_changes = df[df['Daily_Percentage_Change'].abs() > df['Daily_Percentage_Change'].quantile(0.95)]

# 4. Seasonal/Temporal Analysis (Average Close Prices by Month/Day of Week with Standard Deviations)
df['Day_of_Week'] = pd.to_datetime(df['Date']).dt.day_name()
avg_close_by_month = df.groupby('Month')['Close'].mean()
std_close_by_month = df.groupby('Month')['Close'].std()

avg_close_by_day = df.groupby('Day_of_Week')['Close'].mean()
std_close_by_day = df.groupby('Day_of_Week')['Close'].std()

# 5. Rolling Averages for Trend Analysis
df['Rolling_Avg_Close_7D'] = df['Close'].rolling(window=7).mean()
df['Rolling_Avg_Close_30D'] = df['Close'].rolling(window=30).mean()

# 1. Annotated Line Chart for Peaks and Troughs
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=df['Date'], y=df['Close'], mode='lines', name='Closing Price', line=dict(color='grey')))
fig1.add_trace(go.Scatter(x=[date_max_close, date_min_close], y=[max_close, min_close], mode='markers+text',
                         text=[f"Peak: {max_close} ({date_max_close})", f"Trough: {min_close} ({date_min_close})"],
                         marker=dict(color='rgb(57, 105, 172)', size=12), textposition="bottom center"))

fig1.update_layout(title="Closing Price with Peaks and Troughs", xaxis_title="Date", yaxis_title="Price")

# 2. Bullish/Bearish Days by Month (Bar and Line Chart)
fig2_bar = go.Figure()
fig2_bar.add_trace(go.Bar(
    x=["Bullish Days", "Bearish Days"],
    y=[bullish_monthly.sum(), bearish_monthly.sum()],
    marker_color=['rgb(57, 105, 172)', 'grey']
))
fig2_bar.update_layout(
    title="Bullish vs Bearish Days (Overall)",
    xaxis_title="Market Sentiment",
    yaxis_title="Number of Days",
    template="plotly_white"
)

fig2_line = go.Figure()
fig2_line.add_trace(go.Scatter(x=bullish_monthly.index, y=bullish_monthly.values, mode='lines', name='Bullish Days', line=dict(color='rgb(57, 105, 172)')))
fig2_line.add_trace(go.Scatter(x=bearish_monthly.index, y=bearish_monthly.values, mode='lines', name='Bearish Days', line=dict(color='grey')))
fig2_line.update_layout(title="Bullish and Bearish Days by Month", xaxis_title="Month", yaxis_title="Number of Days")

# 3. Daily Percentage Change (Histogram with Extreme Changes)
# Histogram with adjusted bins and range
fig3_hist = px.histogram(
    df, 
    x='Daily_Percentage_Change', 
    title="Daily Percentage Changes (Histogram)", 
    nbins=30,  # Increased bins
    color_discrete_sequence=['rgb(57, 105, 172)']  # Blue color
)

fig3_hist.update_layout(
    xaxis_title="Daily Percentage Change (%)",
    yaxis_title="Frequency",
    template="plotly_white",
    xaxis_range=[-15, 15]  # Focus on main data cluster
)

# 4. Seasonal/Temporal Analysis (Bar Chart with Standard Deviation)
fig4 = go.Figure()
fig4.add_trace(go.Bar(x=avg_close_by_month.index, y=avg_close_by_month.values, 
                     name="Avg Close", 
                     error_y=dict(type='data', array=std_close_by_month.values, visible=True), 
                     marker_color='rgb(57, 105, 172)'))

fig4.update_layout(title="Average Closing Price by Month", xaxis_title="Month", yaxis_title="Price")

# 5. Rolling Averages for Trends
fig5 = go.Figure()
fig5.add_trace(go.Scatter(x=df['Date'], y=df['Rolling_Avg_Close_7D'], 
                         mode='lines', name="7-Day Rolling Avg", 
                         line=dict(color='grey')))

fig5.add_trace(go.Scatter(x=df['Date'], y=df['Rolling_Avg_Close_30D'], 
                         mode='lines', name="30-Day Rolling Avg", 
                         line=dict(color='rgb(57, 105, 172)', dash='dash')))

fig5.update_layout(title="Rolling Averages of Closing Price", xaxis_title="Date", yaxis_title="Price")

# Make the layout 
app = dash.Dash(__name__)
# Set the font for both dashboard title and graph titles to "Open Sans"
font_family = "Open Sans, sans-serif"

# 1. Update Dashboard Title
app.layout = html.Div([
    html.H1("Stock Price Analysis", 
            style={
                'textAlign': 'center', 
                'padding': '20px', 
                'color': 'rgb(57, 105, 172)', 
                'font-family': font_family  # Set font family here
            }),
    # 2. Add graphs with consistent font family for titles
    html.Div([dcc.Graph(figure=fig1, style={'height': '400px'})], style={'padding': '10px', 'textAlign': 'center'}),
    html.Div([
        html.Div([dcc.Graph(figure=fig2_bar, style={'height': '400px'})], style={'width': '45%', 'display': 'inline-block', 'padding': '10px'}),
        html.Div([dcc.Graph(figure=fig2_line, style={'height': '400px'})], style={'width': '45%', 'display': 'inline-block', 'padding': '10px'})
    ], style={'padding': '20px'}),
    html.Div([
        html.Div([dcc.Graph(figure=fig4, style={'height': '400px'})], style={'width': '45%', 'display': 'inline-block', 'padding': '10px'}),
        html.Div([dcc.Graph(figure=fig5, style={'height': '400px'})], style={'width': '45%', 'display': 'inline-block', 'padding': '10px'})
    ], style={'padding': '20px'}),
    html.Div([
        html.Div([dcc.Graph(figure=fig3_hist, style={'height': '400px'})], style={'padding': '10px', 'textAlign': 'center'})
    ], style={'padding': '20px'})
])

# 3. Update Titles of Graphs with "Open Sans"
fig1.update_layout(title={'text': "Closing Price with Peaks and Troughs", 'font': {'family': font_family}})
fig2_bar.update_layout(title={'text': "Bullish vs Bearish Days (Overall)", 'font': {'family': font_family}})
fig2_line.update_layout(title={'text': "Bullish and Bearish Days by Month", 'font': {'family': font_family}})
fig3_hist.update_layout(title={'text': "Daily Percentage Changes (Histogram)", 'font': {'family': font_family}})
fig4.update_layout(title={'text': "Average Closing Price by Month", 'font': {'family': font_family}})
fig5.update_layout(title={'text': "Rolling Averages of Closing Price", 'font': {'family': font_family}})

# Running the app
if __name__ == '__main__':
    app.run_server(debug=True, port= 8052)


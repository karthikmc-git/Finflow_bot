import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta
from transformers import pipeline
import requests
import json

# Load the language model
nlp = pipeline("text-generation", model="gpt2")

# Set your Hume AI API key
HUME_API_KEY = 'your-hume-ai-api-key'

# Function to fetch data from Yahoo Finance API
def fetch_stock_data(ticker, period='1d', interval='1m'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    return data

# Function to analyze emotions using Hume AI
def analyze_emotions(text):
    url = "https://api.hume.ai/v1/emotions"
    payload = json.dumps({
        "texts": [text]
    })
    headers = {
        'x-api-key': HUME_API_KEY,
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

# Streamlit app
def main():
    st.title("Real-Time Stock Graph with AI Assistant")
    ticker = st.text_input("Enter stock ticker (e.g., AAPL):", "AAPL")
    period = st.selectbox("Select period:", ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])
    interval = st.selectbox("Select interval:", ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1d', '5d', '1wk', '1mo', '3mo'])

    if st.button("Show Graph"):
        with st.spinner("Fetching data..."):
            data = fetch_stock_data(ticker, period, interval)

            if not data.empty:
                # Plot the data
                fig = go.Figure()
                fig.add_trace(go.Candlestick(x=data.index,
                                             open=data['Open'],
                                             high=data['High'],
                                             low=data['Low'],
                                             close=data['Close'],
                                             name='market data'))

                fig.update_layout(title=f'{ticker} Stock Price',
                                  yaxis_title='Stock Price (USD per Shares)')

                st.plotly_chart(fig)
            else:
                st.write("No data found for the selected ticker and time period.")

        st.subheader("AI Assistant")
        user_input = st.text_input("Ask the AI about the candlestick chart:")

        if user_input:
            with st.spinner("Analyzing..."):
                response = nlp(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
                st.write(response)

                # Analyze emotions using Hume AI
                emotions = analyze_emotions(user_input)
                st.subheader("Emotion Analysis")
                st.write(emotions)

if __name__ == "__main__":
    main()

# Finflow_bot

This project is a real-time stock graph web application with an integrated AI assistant. The app uses Streamlit for the web interface, Plotly for interactive charts, and Hugging Face's GPT-2 model for text generation. It also integrates Hume AI for emotion analysis.

Features
Real-Time Stock Data: Fetches and displays real-time stock data using Yahoo Finance.
Interactive Candlestick Chart: Visualizes stock price data with candlestick charts.
AI Assistant: Provides text generation responses using GPT-2.
Emotion Analysis: Analyzes the emotional tone of user input using Hume AI.
Prerequisites
Python 3.x
Streamlit
Plotly
yfinance
transformers
requests
Installation
Clone the Repository

sh
Copy code
git clone https://github.com/your-username/real-time-stock-graph.git
cd real-time-stock-graph
Create a Virtual Environment

sh
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies

sh
Copy code
pip install -r requirements.txt
Add Your API Keys

Hume AI API Key: Replace 'your-hume-ai-api-key' in app.py with your actual Hume AI API key.
Usage
Run the Streamlit App

sh
Copy code
streamlit run app.py
Open the App

After running the above command, Streamlit will open a new tab in your web browser with the app. You can interact with the app by entering stock tickers, selecting periods and intervals, and asking questions about the candlestick charts.

Project Structure
app.py: The main Streamlit application script.
requirements.txt: A file listing the Python dependencies for the project.
logo.png: Your logo image file (ensure to place it in the same directory as app.py).
Customization
Background Color: Change the background color by modifying the CSS in app.py. Look for the CSS block with the background-color property.
Logo: Replace logo.png with your logo file or adjust the path in app.py.
Contributing
Feel free to open issues or submit pull requests if you find bugs or have improvements to suggest.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Streamlit: For creating an easy-to-use web app framework.
Plotly: For providing interactive charting capabilities.
yfinance: For accessing financial data.
Hugging Face: For their transformers library and pre-trained models.
Hume AI: For emotion analysis APIs.

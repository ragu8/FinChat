import time
import pandas as pd
import yfinance as yf
from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_community.chat_models import ChatOpenAI
from app.services.ticker import find_ticker

load_dotenv()

chat = ChatOpenAI(temperature=0.5)
flow_messages = []

initial_messages = [
    SystemMessage(content="Welcome to the Financial Knowledge and Market Prediction AI."),
    SystemMessage(content="I provide concise answers with numerical values and tables to aid your understanding."),
    SystemMessage(content="I'm here to offer insights into financial markets, aiding informed decision-making."),
    SystemMessage(content="Understanding financial concepts and market trends is key to successful investing."),
    SystemMessage(content="Feel free to ask about financial instruments, investment strategies, or market predictions."),
    SystemMessage(content="I can provide information on stock prices, market analysis, economic indicators, and more."),
    SystemMessage(content="Market predictions are based on historical data and analysis, with inherent uncertainties."),
    SystemMessage(content="If you have a specific stock in mind, please provide the stock symbol or company name."),
    SystemMessage(content="Let's explore the world of finance together!")
]

flow_messages += initial_messages

def fetch_yfinance_data(ticker_symbol, start_date='2023-01-01', end_date=None):
    if end_date is None:
        end_date = time.strftime('%Y-%m-%d')

    try:
        data = yf.download(ticker_symbol, start=start_date, end=end_date)
        filename = f"{ticker_symbol}_data.csv"
        data.to_csv(filename, index=True)
        print("Data saved to", filename)
        return data
    except Exception as e:
        print("Error fetching data:", e)
        return None

def get_chatmodel_response(question):
    flow_messages.append(HumanMessage(content=question))
    answer = chat(flow_messages)
    flow_messages.append(AIMessage(content=answer.content))
    return answer.content

def generate_response(message_body):
    ticker_symbol = find_ticker(message_body)
    if ticker_symbol:
        yfinance_data = fetch_yfinance_data(ticker_symbol)
        if yfinance_data is not None:
            yfinance_data_str = yfinance_data.to_string(index=False)
            question = f"Based on the historical data:\n\n{yfinance_data_str}\n\nWhat is your prediction for the next market momentum? Will the market likely trend upwards or downwards?\n\nAdditionally, please provide the next open and close values, specifying whether the market is expected to go up or down."
            response = get_chatmodel_response(question)
            return response
    return "Sorry, I couldn't retrieve the data for your query."

if __name__ == "__main__":
    user_question = 'AAPL'
    response = generate_response(user_question)
    print(response)


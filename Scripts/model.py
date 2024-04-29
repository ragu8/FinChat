from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_community.chat_models import ChatOpenAI
import yfinance_data as yfd
import pandas as pd
import ticker

load_dotenv()

chat = ChatOpenAI(temperature=0.5)

flow_messages = []

initial_messages = [
    SystemMessage(content="Welcome to the Financial Knowledge and Market Prediction AI."),
    SystemMessage(content="I'm here to provide insights from dataframe into financial markets and help you make informed decisions."),
    SystemMessage(content="Understanding financial concepts and market trends is crucial for successful investing."),
    SystemMessage(content="Feel free to ask me anything about financial instruments, investment strategies, or market predictions."),
    SystemMessage(content="I can provide information on stock prices, market analysis, economic indicators, and more."),
    SystemMessage(content="Market prediction is essential, but remember that it's based on historical data and analysis, and there's always a degree of uncertainty."),
    SystemMessage(content="If you have a specific stock in mind, please provide the stock symbol or company name."),
    SystemMessage(content="Let's explore the world of finance together!"),
    SystemMessage(content="you give compute values not steps and other text only compute vales please provide the next open and close values, specifying whether the market is expected to go up or down.")
]

flow_messages += initial_messages


def get_chatmodel_response(user_question):
    tck = ticker.find_ticker(user_question)
    yfinance_data = yfd.yfinance_data(tck)
    # Convert DataFrame to string
    yfinance_data_str = yfinance_data.to_string(index=False)
    question = f"Based on the historical data from the following DataFrame:\n\n{yfinance_data_str}\n\nWhat is your prediction for the next market momentum? Will the market likely trend upwards or downwards?\n\nAdditionally, please provide the next open and close values, specifying whether the market is expected to go up or down."
    flow_messages.append(HumanMessage(content=question))
    answer = chat(flow_messages)
    flow_messages.append(AIMessage(content=answer.content))
    return answer.content


user_question = 'apple'
response = get_chatmodel_response(user_question)
print(response)



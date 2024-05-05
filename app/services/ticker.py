# ticker.py
from dotenv import load_dotenv
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_community.chat_models import ChatOpenAI


load_dotenv()


chat = ChatOpenAI(temperature=0.5)


initial_messages = [
    SystemMessage(content="Welcome to the Find the Yahoo Finance Ticker AI."),
    SystemMessage(content="I'm here to help you find the Yahoo Finance ticker symbol for a company."),
    SystemMessage(content="Please provide the name of the company or a related query."),
    SystemMessage(content="For example, you can ask about a company like 'Apple' or 'AAPL'.")]




def find_ticker(question):
    prompt = f"Based on the {question}, find the Yahoo Finance ticker and return only the ticker symbol. For example, 'AAPL' only one word answer no more ."
    response = chat([HumanMessage(content=prompt)])
    return response.content

if __name__ == "__main__":

    user_question = 'What is the stock symbol for sbi?'


    response = find_ticker(user_question)
    print(response)


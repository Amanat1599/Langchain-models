from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

chat_model = ChatOpenAI(model="gpt-3.5-turbo-instant")

result = chat_model.invoke("Who is the chief of army staff of Pakistan?")
print(result.content) #It is not a string output

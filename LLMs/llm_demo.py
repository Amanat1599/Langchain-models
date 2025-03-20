from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")
chat = llm.invoke("Who is the president of Pakistan?")
print(chat)
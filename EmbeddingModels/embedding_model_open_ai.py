from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

OpenAIEmbeddings()
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)

embedding_model.embed_documents()

result = embedding_model.embed_query("Lahore is capital ofpunjab")
print(str(result))
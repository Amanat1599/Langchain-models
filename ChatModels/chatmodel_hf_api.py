from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

lama_face = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  
    task="text-generation",  
)  

model = ChatHuggingFace(llm=lama_face)

result = model.invoke("Who is the chief of Army staff of Pakistan?")
print(result)
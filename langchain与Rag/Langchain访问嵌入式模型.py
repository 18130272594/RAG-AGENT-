import math
from langchain_ollama import OllamaEmbeddings

model = OllamaEmbeddings(model="bge-m3")

print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你", "我稀饭你", "晚上吃啥"]))
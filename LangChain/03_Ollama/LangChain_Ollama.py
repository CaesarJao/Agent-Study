#pip install -qU langchain_ollama
#pip install -U ollama

from langchain_ollama import ChatOllama

model = ChatOllama(base_url="http://localhost:11434",model="qwen3:1.7b",reasoning = False)

print(model.invoke("你收费吗"))

#批量 异步 流式 带a是异步的

from langchain_openai import ChatOpenAI
from langchain.chat_models import init_chat_model
from openai import OpenAI, api_key
import os
from dotenv import load_dotenv

model = init_chat_model(
    model="qwen-plus",
    model_provider="openai",
    api_key=os.getenv("AQWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


response = model.invoke(
    "你是谁"
)
print(response)
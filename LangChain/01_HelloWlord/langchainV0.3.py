from langchain_openai import ChatOpenAI
from openai import OpenAI, api_key
import os
from dotenv import load_dotenv

# llm = ChatOpenAI(硬编码写死
#     model="gpt-3.5-turbo-0301",
#     api_key=" ",
#     base_url="https://api.dify.ai/v1"
# )


#
# llm = ChatOpenAI(配置进环境变量
#     model="qwen-plus",
#     api_key=os.getenv("ALiQwenApi"),
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
# )


#在.env中读取
load_dotenv(encoding="utf-8")
llm = ChatOpenAI(
    model="deepseek-v3.2",
    api_key=os.getenv("AQWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


response = llm.invoke(
    "你是谁"
)
print(response)
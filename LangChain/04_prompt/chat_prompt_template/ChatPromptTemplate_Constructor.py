"""
使用ChatPromptTemplate构造方法直接实例化
实例化时需要传入messages: Sequence[MessageLikeRepresentation]
messages 参数支持如下格式：
	tuple 构成的列表，格式为[(role, content)]
	dict 构成的列表，格式为[{“role”:... , “content”:...}]
	Message 类构成的列表
"""

from langchain_core.prompts import ChatPromptTemplate
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv


load_dotenv()
chatPromptTemplate = ChatPromptTemplate(#构造方法，获得提示词模板，用提示词模板调用format_messages方法生成提示词
    [
        ("system", "你是一个AI开发工程师，你的名字是{name}。"),
        ("human", "你能帮我做什么?"),
        ("ai", "我能开发很多{thing}。"),#模拟AI
        ("human", "{user_input}"),
    ]
)

prompt = chatPromptTemplate.format_messages(#方法
    name="小谷AI", thing="AI", user_input="7 + 5等于多少")
print(prompt)

llm = init_chat_model(
    model="deepseek-v3.2",
    model_provider="openai",
    api_key=os.getenv("QWEN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
print()
print("======================")

result = llm.invoke(prompt)
print(result)
print(result.content)
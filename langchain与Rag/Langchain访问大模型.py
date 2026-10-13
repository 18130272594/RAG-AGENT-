from platform import system

from langchain_deepseek import ChatDeepSeek
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
model = ChatDeepSeek(model="deepseek-chat")
#
# res = model.invoke(input="你是谁呀能做什么？")
#
# print(res.content)
###########################################################
# res =model.stream(input="你是谁你能做些什么")
# for chunk in res:
#     print(chunk.content,end="",flush=True)
##########################################################
# messages=[
#     SystemMessage(content="你是一名边塞诗人"),
#     HumanMessage(content="给我写一首诗")
#
# ]
# res=model.stream(input=messages)
# for chunk in res:
#     print(chunk.content,end="",flush=True)
###########################################################//简化格式
messages=[
    ("system","你是诗人李白"),
    ("human","帮我写一首符合你风格的诗")
]
res=model.stream(input=messages)
for chunk in res:
    print(chunk.content,end="",flush=True)
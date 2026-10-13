
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek
from langchain.agents import create_agent

@tool(description="获取股价，传入股票名称，返回字符串信息")
def get_price(name:str) ->str:
    return f"股票{name}的价格是49元"
@tool(description="获取股票信息，传入股票名称，返回信息")
def get_information(name:str)->str:
    return f"股票{name},是一家上市公司，IT行业标杆"
agent=create_agent(
    model=ChatDeepSeek(model="deepseek-chat"),
    tools=[get_price,get_information],
    system_prompt="你是一个智能助手,可以回答股票相关问题,记住请告知我思考过程,让我知道你为什么调用某个工具"
)
for chunk in agent.stream({"messages":[{"role":"user","content":"无敌公司股价多少，并介绍一下"}]},stream_mode="values"):
    latest_message=chunk["messages"][-1]
    if latest_message.content:
        print(type(latest_message).__name__,latest_message.content)
    try:
        if latest_message.tool_calls:
            print(f"工具调用:{[tac['name'] for tac in latest_message.tool_calls]}")
    except AttributeError as e:
     pass

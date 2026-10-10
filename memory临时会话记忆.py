from langchain_deepseek import ChatDeepSeek
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

model = ChatDeepSeek(model="deepseek-chat")

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是对话助手。用户会先陆续告诉你一些信息，之后向你提问。请结合历史会话中的信息回答问题，回答要简短。"),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
str_parser = StrOutputParser()
def print_prompt(full_prompt):
    print("=" * 20, full_prompt.to_string(), "=" * 20)
    return full_prompt
base_chain = prompt_template | print_prompt | model | str_parser
history = {}
def chat(session_id, question):
    if session_id not in history:
        history[session_id] = []
    msgs = history[session_id]
    res = base_chain.invoke({"chat_history": msgs, "input": question})
    msgs.append(HumanMessage(question))
    msgs.append(AIMessage(res))
    return res
if __name__ == "__main__":
    SESSION = "user_001"

    print("第1次执行: ", chat(SESSION, question="小明有2个猫"))
    print("第2次执行: ", chat(SESSION, question="小刚有1只狗"))
    print("第3次执行: ", chat(SESSION, question="总共有几个宠物"))
from langchain_core.prompts import  ChatPromptTemplate,MessagesPlaceholder
from langchain_deepseek import ChatDeepSeek
chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system","你是诗人，可以作诗"),
    MessagesPlaceholder("history"),
    ("human","请再来一首诗")
])

history_data = [
("human","你来写一个唐诗"),
("ai","床前明月光,疑是地上霜,举头望明月,低头思故乡"),
("human","好诗再来一个"),
("ai","锄禾日当午,汗滴禾下锄,谁知盘中餐,粒粒皆辛苦")
]
text=chat_prompt_template.invoke({"history":history_data}).to_string()
print(text)

model = ChatDeepSeek(model="deepseek-chat")
res=model.invoke(input=text)
print(res.content)
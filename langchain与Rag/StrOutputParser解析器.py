import langchain_core
from langchain_core.prompts import  PromptTemplate
from langchain_deepseek import ChatDeepSeek
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()
prompt_template = PromptTemplate.from_template(
    "我的女儿姓{lastname},刚生了{gender},你帮我起个名字，简单回答"
)
model = ChatDeepSeek(model="deepseek-chat")
chain=prompt_template|model|parser|model
res =chain.invoke({"lastname":"张","gender":"男"})
print(res.content)



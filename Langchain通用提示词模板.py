from langchain_core.prompts import  PromptTemplate
from langchain_deepseek import ChatDeepSeek

prompt_template = PromptTemplate.from_template(
    "我的女儿姓{lastname},刚生了{gender},你帮我起个名字，简单回答"
)
model = ChatDeepSeek(model="deepseek-chat")
prompt_text = prompt_template.format(lastname="张",gender="女儿")
res=model.invoke(input=prompt_text)
print(res.content)


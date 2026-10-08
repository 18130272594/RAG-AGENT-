from langchain_core.output_parsers import StrOutputParser, JsonOutputParser#字典输出
from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import PromptTemplate
model = ChatDeepSeek(model="deepseek-chat")
str_parser = StrOutputParser()
json_parser = JsonOutputParser()
first_prompt_template = PromptTemplate.from_template(
    "我的女儿姓{lastname},刚生了{gender},你帮我起个名字"
    "并严封装为Json格式返回，要求key为name，value为你取的名字"
)
second_prompt_template = PromptTemplate.from_template(
   "姓名:{name},并帮我解释含义"
)
chain=first_prompt_template|model|json_parser|second_prompt_template|model|str_parser
res=chain.invoke({"lastname":"张","gender":"男"})
print(res)
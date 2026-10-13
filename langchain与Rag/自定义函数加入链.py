from langchain_core.output_parsers import StrOutputParser, JsonOutputParser#字典输出
from langchain_deepseek import ChatDeepSeek
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
model = ChatDeepSeek(model="deepseek-chat")
str_parser = StrOutputParser()

first_prompt_template = PromptTemplate.from_template(
    "我的女儿姓{lastname},刚生了{gender},你帮我起个名字，不需要额外信息"

)
second_prompt_template = PromptTemplate.from_template(
   "姓名:{name},并帮我解释含义"
)
func=RunnableLambda(lambda ai_message:{"name":ai_message.content})
chain=first_prompt_template|model|func|second_prompt_template|model|str_parser
for chunk in chain.stream({"lastname": "张", "gender": ""}):
  print(chunk, end="", flush=True)
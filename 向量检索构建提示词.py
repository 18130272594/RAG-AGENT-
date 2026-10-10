from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_deepseek import ChatDeepSeek



model=ChatDeepSeek(model="deepseek-chat")
prompt= ChatPromptTemplate.from_messages([
    ("system","以我提供的专业资料为准，简单回答用户问题，专业资料{content}"),
    ("user","{input}")
]
)
ve_co=InMemoryVectorStore(
    embedding=OllamaEmbeddings(model="bge-m3")
)
ve_co.add_texts(["减肥就是要少吃多练","在减脂期间吃东西很重要,清淡少油控制卡路里摄入并运动起来","跑步是很好的运动哦"])
inout_co="怎么才能减肥"
result=ve_co.similarity_search(inout_co,2)
ref_text="["+ "。".join([doc.page_content for doc in result])+"]"
def print_prompt(prompt):
    print(prompt.to_string())
    print("#"*20)
    return prompt

chain= prompt| print_prompt | model | StrOutputParser ()
res=chain.invoke({"input":inout_co,"content":ref_text})
print(res)


# """"""""
# retriever :
# - 输入:用户的提问 str
# - 输出:向量库的检索结果 list [Document]
# prompt:
# - 输入:用户的提问 +向量库的检索结果 dict
# - 输出:完整的提示词  PromptValue
#
# """""""


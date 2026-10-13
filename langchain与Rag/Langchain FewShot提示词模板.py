from langchain_core.prompts import  PromptTemplate,FewShotPromptTemplate
from langchain_deepseek import ChatDeepSeek
example_template = PromptTemplate.from_template(
    "单词{world},反义词{antonym}"
)
example_data=[
    {"world":"大","antonym":"小"},
    {"world":"长","antonym":"短"}
]

few_shot=FewShotPromptTemplate(
    example_prompt=example_template,
    examples=example_data,
    prefix="告诉我反义词，提供如下实例" ,
    suffix="基于前面的实例，告诉我{input_word}的反义词" ,
    input_variables=["input_word"]
)
prompt_text=few_shot.invoke(input={"input_word":"左"}).to_string()
print(prompt_text)
model=ChatDeepSeek(model="deepseek-chat")
answer=model.invoke(prompt_text)
print(answer.content)


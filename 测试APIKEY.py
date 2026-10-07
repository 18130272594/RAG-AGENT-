import os
from openai import OpenAI, Stream

client = OpenAI(
    base_url="https://api.deepseek.com",
)

completion = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant，并且不说废话"},
        {"role": "user", "content": "输出1到10的数字，使用python代码？"},
    ],
    stream=True
)
#处理结果

for chunk in completion:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
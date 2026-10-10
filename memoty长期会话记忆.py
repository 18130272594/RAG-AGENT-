import os
import json
from typing import Sequence
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    AIMessage,
    message_to_dict,
    messages_from_dict,
)
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_deepseek import ChatDeepSeek
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id: str, storage_path: str):
        self.session_id = session_id
        self.storage_path = storage_path
        # 完整的文件路径
        self.file_path = os.path.join(self.storage_path, self.session_id)
        # 确保文件夹是存在的
        os.makedirs(self.storage_path, exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        all_messages = list(self.messages)
        all_messages.extend(messages)
        new_messages = [message_to_dict(message) for message in all_messages]
        # 将数据写入文件
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f, ensure_ascii=False)

    @property
    def messages(self) -> list[BaseMessage]:
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                messages_data = json.load(f)
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    def clear(self) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f)


model = ChatDeepSeek(model="deepseek-chat")

prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是对话助手。用户会先陆续告诉你一些信息，之后向你提问。"
            "请结合历史会话中的信息回答问题，回答要简短。",
        ),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

str_parser = StrOutputParser()


def print_prompt(full_prompt):
    print("=" * 20, full_prompt.to_string(), "=" * 20)
    return full_prompt


base_chain = prompt_template | print_prompt | model | str_parser


def get_history(session_id):
    return FileChatMessageHistory(session_id + ".json", "history")


def chat(session_id, question):
    history = get_history(session_id)
    msgs = history.messages
    res = base_chain.invoke({"chat_history": msgs, "input": question})
    history.add_messages([HumanMessage(question), AIMessage(res)])
    return res


if __name__ == "__main__":
    SESSION = "user_002"

    print("第1次执行: ", chat(SESSION, question="小明有2个猫"))
    print("第2次执行: ", chat(SESSION, question="小刚有1只狗"))
    print("第3次执行: ", chat(SESSION, question="总共有几个宠物"))

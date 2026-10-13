from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import OllamaEmbeddings
from langchain_deepseek import ChatDeepSeek

import config_data as config
from history_memory import get_history
from stores import VectorStoreService


class RagService(object):
    def __init__(self):

        self.vector_service = VectorStoreService(
            embedding=OllamaEmbeddings(model=config.embedding_model_name))

        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "以我提供的已知参考资料为主，"
                 "简洁和专业的回答用户问题。参考资料:{context}。"),
                ("system", "并且我提供用户的对话历史记录，如下："),
                MessagesPlaceholder("history"),
                ("user", "请回答用户提问：{input}")
            ]
        )

        self.chat_model = ChatDeepSeek(model=config.chat_model_name, temperature=0)

        self.chain = self._get_chain()

    def _get_chain(self):
        """获取最终的执行链"""
        retriever = self.vector_service.get_retriever()

        def format_document(docs: list[Document]):
            if not docs:
                return "无相关参考资料"

            formatted_str = ""
            for doc in docs:
                formatted_str += f"文档片段：{doc.page_content}\n文档元数据：{doc.metadata}\n\n"

            return formatted_str

        # RunnableWithMessageHistory 传进来的输入形如：
        #     {"input": "用户问题", "history": [历史消息...]}
        # RunnableParallel 让三个分支各取所需，最后合成一个字典喂给提示词模板
        chain = (
            RunnableParallel(
                input=RunnableLambda(lambda x: x["input"]),
                context=RunnableLambda(lambda x: x["input"]) | retriever | format_document,
                history=RunnableLambda(lambda x: x["history"]),
            )
            | self.prompt_template
            | self.chat_model
            | StrOutputParser()
        )


        conversation_chain = RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key="input",
            history_messages_key="history",
        )

        return conversation_chain


if __name__ == '__main__':
    # session id 配置
    session_config = {
        "configurable": {
            "session_id": "user_001",
        }
    }

    res = RagService().chain.invoke({"input": "针织毛衣如何保养？"}, session_config)
    print(res)

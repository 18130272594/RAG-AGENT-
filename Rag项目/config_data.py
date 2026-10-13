import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

md5_path = os.path.join(BASE_DIR, "md5.txt")
persist_directory = os.path.join(BASE_DIR, "persist_dir")
collection_name = "rag"

chunk_size=1000
chunk_overlap=100
max_chunk_size=1000
separators = ["\n\n", "\n", "。", "！", "？", "!", "?", ".", " ", ""]

# 嵌入模型：写侧入库和读侧检索必须用同一个，否则向量不在同一坐标系里，检索结果无意义
embedding_model_name = "bge-m3"

# 聊天模型
chat_model_name = "deepseek-chat"

# 检索时取回几条。原来的名字 similarity_threshold 是错的，它从来不是"阈值"，就是 top-k
top_k = 3

# 滑动窗口：每个会话最多保留多少条历史消息（1轮问答=2条，10条即最近5轮）
max_history_messages = 10

session_config = {
    "configurable": {
        "session_id": "user_001",
    }
}

from langchain_community.document_loaders import JSONLoader
from openai.types.conversations import text_content

LOADER = JSONLoader(
    file_path="./data/stu.json",
    jq_schema=".name",
    text_content=True,
    # json_lines=True
)
docs = LOADER.load()
for doc in docs:
    print(doc)
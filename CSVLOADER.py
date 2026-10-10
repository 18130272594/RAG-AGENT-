from langchain_community.docstore import document
from langchain_community.document_loaders import CSVLoader
loader=CSVLoader(
    file_path=r"/data/stu.csv",
    encoding="utf-8",
)
documents = loader.load()
for document in documents:
 print(document)
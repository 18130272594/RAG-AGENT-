


from langchain_community.document_loaders import CSVLoader
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma


ve_core=Chroma(
    collection_name="test",
    embedding_function=OllamaEmbeddings(model="bge-m3"),
    persist_directory="./哇哇"
)
loader=CSVLoader(
    file_path="./data/yy.csv",
    encoding="utf-8",
    source_column="source"
)
documents=loader.load()
ve_core.add_documents(
    documents=documents,
    ids=["id"+str(i) for i in range(1,len(documents)+1)]
)
ve_core.delete(
    ["id1","id2"]
)
result=ve_core.similarity_search("python容易学",3 )
print(result)

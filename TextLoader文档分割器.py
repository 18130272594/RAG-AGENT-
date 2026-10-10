from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
loader = TextLoader("data/ll.text", encoding="utf-8")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", "。", "！", "？", "!", "?", ".", " ", ""],
    length_function=len,
)

spliter_docs=splitter.split_documents(docs)
for doc in spliter_docs:
    print("=" * 20)
    print(doc)
    print("="*20)
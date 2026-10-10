from langchain_community.document_loaders import  PyPDFLoader
loader = PyPDFLoader(
    mode="single",#只返回一个Document对象
)
i=0
for doc in loader.lazy_load():
    print(doc)
    i+=1
    print("="*20,i)
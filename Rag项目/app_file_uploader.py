import streamlit as st

from knowledge_base import KnowledgeBaseService

st.title("知识库更新")
uploader_file=st.file_uploader(
    "请上传TXT文件",
    type=["txt"],
    accept_multiple_files=False,
)
if "service" not in st.session_state:
    st.session_state["service"]=KnowledgeBaseService()
if uploader_file is not None:
    file_name=uploader_file.name
    file_size=(uploader_file.size/
               1024)
    file_type=uploader_file.type
    st.subheader(f"文件名：{file_name}")
    st.write(f"格式：{file_type}| 大小{file_size:.2f}KB")
    txt=uploader_file.getvalue().decode("utf-8")
    st.write(txt)
    result=st.session_state["service"].upload_by_str(txt,file_name)
    st.write(result)

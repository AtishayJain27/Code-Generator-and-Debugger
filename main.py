import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain


def create_streamlit_app(llm):

    st.title("Code Generator")
    question_input = st.text_input("Enter your Question:")
    submit_button = st.button("Submit" , key="generator")
    answer=llm.give_ans(question_input)
    if submit_button:
        st.code(answer)

    st.title("Code Debugger")
    code_input = st.text_area("Enter your Question:",height=10)
    submit_button1 = st.button("Submit", key="debugger")
    answer=llm.debug_code(code_input)
    if submit_button1:
        st.code(answer)


if __name__ == "__main__":
    chain = Chain()
    st.set_page_config(layout="wide", page_title="Code Generator")
    create_streamlit_app(chain)



import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from chains import Chain

st.set_page_config(layout="wide", page_title="Code Generator")


st.markdown("""
    <style>
    .stTextArea textarea {
        font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .user-message {
        background-color: #E3F2FD;
    }
    .assistant-message {
        background-color: #F5F5F5;
    }
    .message-content {
        margin-top: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("<h1 style='color: #1E88E5; text-align: center;'>💻 Code Generator</h1>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; max-width: 800px; margin: 0 auto 2rem auto;'>
        <p style='color: #616161;'>
        Describe what code you want to generate in natural language. 
        The AI will help you create code snippets, functions, or entire programs based on your description.
        </p>
    </div>
""", unsafe_allow_html=True)

chain = Chain()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history with improved styling
for message in st.session_state.messages:
    message_class = "user-message" if message["role"] == "user" else "assistant-message"
    with st.container():
        st.markdown(f"""
            <div class='chat-message {message_class}'>
                <strong>{'You' if message["role"] == "user" else '🤖 Assistant'}</strong>
                <div class='message-content'>
                    {message["content"]}
                </div>
            </div>
        """, unsafe_allow_html=True)

# Chat input with placeholder
if prompt := st.chat_input("Describe the code you want to generate..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.container():
        st.markdown(f"""
            <div class='chat-message user-message'>
                <strong>You</strong>
                <div class='message-content'>{prompt}</div>
            </div>
        """, unsafe_allow_html=True)

    # Show loading spinner while generating response
    with st.spinner("Generating code..."):
        answer = chain.give_ans(prompt)
    
    # Display assistant response
    with st.container():
        st.markdown(f"""
            <div class='chat-message assistant-message'>
                <strong>🤖 Assistant</strong>
                <div class='message-content'>
                    <pre><code>{answer}</code></pre>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": answer})

# Add helpful tips in the sidebar
with st.sidebar:
    st.markdown("### 💡 Tips for better results")
    st.markdown("""
    - Be specific about the programming language
    - Describe the desired functionality clearly
    - Mention any specific requirements or constraints
    - Ask for explanations if needed
    """)
    
    # Add clear chat button
    if st.button("🗑️ Clear Chat History", type="secondary"):
        st.session_state.messages = []
        st.rerun() 
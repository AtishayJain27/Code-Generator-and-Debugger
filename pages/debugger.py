import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
import sys
import os

# Add the parent directory to Python path to import Chain
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from chains import Chain

st.set_page_config(layout="wide", page_title="Code Debugger")

# Add custom CSS
st.markdown("""
    <style>
    .stTextArea textarea {
        font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
        min-height: 200px !important;
    }
    .debug-result {
        background-color: #F5F5F5;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
    }
    .debug-header {
        color: #1E88E5;
        font-size: 1.2rem;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title section with description
st.markdown("<h1 style='color: #1E88E5; text-align: center;'>🔧 Code Debugger</h1>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; max-width: 800px; margin: 0 auto 2rem auto;'>
        <p style='color: #616161;'>
        Paste your code and describe the issue you're facing. 
        The AI will help identify problems, suggest fixes, and provide optimization recommendations.
        </p>
    </div>
""", unsafe_allow_html=True)

chain = Chain()

# Create two columns for input
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📝 Your Code")
    code_input = st.text_area(
        "Paste your code here:",
        height=300,
        placeholder="Paste your code here...",
        label_visibility="collapsed"
    )

with col2:
    st.markdown("### ❓ Issue Description")
    issue_description = st.text_area(
        "Describe the issue:",
        height=150,
        placeholder="Describe what's wrong with the code...",
        label_visibility="collapsed"
    )

# Add submit button with primary styling
submit_button = st.button("🔍 Analyze Code", type="primary", use_container_width=True)

if submit_button and code_input:
    with st.spinner("Analyzing your code..."):
        # Combine code and description for better context
        full_query = f"Code:\n{code_input}\n\nIssue: {issue_description}"
        answer = chain.debug_code(full_query)
        
        st.markdown("### 📊 Analysis Results")
        st.markdown("""
            <div class='debug-result'>
                <div class='debug-header'>🔍 Debugging Report</div>
            </div>
        """, unsafe_allow_html=True)
        
        # Display the analysis with proper code formatting
        st.code(answer, language="python")

# Add helpful tips in the sidebar
with st.sidebar:
    st.markdown("### 💡 Tips for better results")
    st.markdown("""
    - Make sure your code is properly formatted
    - Include any error messages you're seeing
    - Specify the expected vs actual behavior
    - Mention the programming language used
    """)
    
    st.markdown("### 🎯 Common Issues")
    st.markdown("""
    - Syntax errors
    - Logic errors
    - Performance issues
    - Best practices violations
    - Memory leaks
    """) 
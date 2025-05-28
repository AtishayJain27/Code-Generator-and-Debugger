import streamlit as st

st.set_page_config(layout="wide", page_title="Code Assistant")

# Add custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem !important;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #424242;
        text-align: center;
        margin-bottom: 3rem;
    }
    .feature-header {
        color: #1E88E5;
        font-size: 1.3rem;
        margin-bottom: 1rem;
    }
    .feature-text {
        font-size: 1rem;
        color: #616161;
        padding-left: 1.5rem;
    }
    .feature-container {
        margin-left: 2rem;
        border-left: 2px solid #E3F2FD;
        padding-left: 1.5rem;
        margin-bottom: 2rem;
    }
    .nav-item {
        font-size: 1.2rem;
        color: #1E88E5;
        margin-bottom: 0.5rem;
    }
    .nav-subitem {
        font-size: 1.1rem;
        color: #424242;
        margin-left: 2rem;
        margin-bottom: 2rem;
        padding-left: 1rem;
        border-left: 2px solid #E3F2FD;
    }
    </style>
""", unsafe_allow_html=True)

# Main header
st.markdown("<h1 class='main-header'>🚀 Code Assistant AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Your intelligent coding companion powered by LLAMA 3.0</p>", unsafe_allow_html=True)

# Navigation structure
st.markdown("<div class='nav-item'>🏠 Home</div>", unsafe_allow_html=True)
st.markdown("<div class='nav-subitem'>", unsafe_allow_html=True)

# Create two columns for features
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 class='feature-header'>🤖 Code Generation</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div class='feature-container'>
            <p class='feature-text'>
            • Generate code snippets from natural language descriptions<br>
            • Support for multiple programming languages<br>
            • Get explanations along with the generated code<br>
            • Smart context understanding
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Try Code Generator", type="primary", key="gen_button"):
        st.switch_page("pages/1_generator.py")

with col2:
    st.markdown("<h3 class='feature-header'>🔧 Code Debugging</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div class='feature-container'>
            <p class='feature-text'>
            • Identify and fix bugs in your code<br>
            • Get detailed explanations of issues<br>
            • Receive optimization suggestions<br>
            • Learn best practices
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Try Code Debugger", type="primary", key="debug_button"):
        st.switch_page("pages/2_debugger.py")

st.markdown("</div>", unsafe_allow_html=True)

# Add info section
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem 0;'>
    <h3 style='color: #1E88E5;'>About This Project</h3>
    <p style='color: #616161; max-width: 800px; margin: 0 auto;'>
    This AI-powered coding assistant helps developers generate code snippets and debug their code using state-of-the-art language models. 
    Built with META's LLAMA 3.0, it provides intelligent suggestions and solutions for your coding needs.
    </p>
</div>
""", unsafe_allow_html=True)

# Add getting started section with indented structure
st.markdown("""
<div style='background-color: #f5f5f5; padding: 2rem; border-radius: 10px; margin-top: 2rem;'>
    <h3 style='color: #1E88E5;'>Getting Started</h3>
    <div style='padding-left: 1.5rem; margin-top: 1rem;'>
        <p style='color: #616161;'>
        1. Choose your tool:<br>
        <span style='padding-left: 1.5rem;'>• Code Generator - For creating new code</span><br>
        <span style='padding-left: 1.5rem;'>• Code Debugger - For fixing issues</span><br>
        2. Use the tool:<br>
        <span style='padding-left: 1.5rem;'>• For generation: Describe what you want to create</span><br>
        <span style='padding-left: 1.5rem;'>• For debugging: Paste your code and describe the issue</span><br>
        3. Get results:<br>
        <span style='padding-left: 1.5rem;'>• Review the AI-generated solution</span><br>
        <span style='padding-left: 1.5rem;'>• Apply the suggestions to your code</span>
        </p>
    </div>
</div>
""", unsafe_allow_html=True)
import streamlit as st


# --- PAGE SETUP ---
home_page = st.Page(
    "home.py",
    title="Home Page",
    icon="🏠",
    default=True,
)
generator_page = st.Page(
    "generator.py",
    title="Code Generator",
    icon="🤖",
)
debugger_page = st.Page(
    "debugger.py",
    title="Code Debugger",
    icon="🔧",
)


# NAVIGATION SETUP 


pg = st.navigation(
    {
        "HOME": [home_page],
        "Projects": [generator_page,debugger_page],
    }
)


pg.run()
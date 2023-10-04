import streamlit as st

st.set_page_config(
    layout='wide',
    page_title= "Home"
)

option = st.sidebar.selectbox("Navegar para:", ("Página Inicial", "Página 2", "Página 3"))

st.title("Home")
st.header(option)
st.write('teste')
import streamlit as st

# Função da página inicial
def page_home():
    st.title("Página Inicial")
    st.write("Bem-vindo à página inicial!")

# Função da página 2
def page_2():
    st.title("Página 2")
    st.write("Esta é a segunda página!")

# Função da página 3
def page_3():
    st.title("Página 3")
    st.write("Esta é a terceira página!")

# Barra lateral para navegação
page = st.sidebar.selectbox("Navegar para:", ("Página Inicial", "Página 2", "Página 3"))

# Determina qual página mostrar com base na seleção do usuário
if page == "Página Inicial":
    page_home()
elif page == "Página 2":
    page_2()
elif page == "Página 3":
    page_3()
import streamlit as st

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

nomes = []

st.title("Bem-Vindo ao SGAA!")
st.write("O que é a SGAA?")
st.text("Uma empresa de Sistemas de Gerenciamento de Atividades Acadêmicas (SGAA) éuma organização especializada no desenvolvimento, implementação e manutençãode softwares voltados para a gestão das atividades acadêmicas de instituições deensino. Esses sistemas têm como principal objetivo otimizar a administração de processos relacionados ao ambiente acadêmico, como o planejamento e controle de aulas, matrícula de alunos, avaliação de desempenho, comunicação entre alunos e professores, e outras funções essenciais no contexto educacional.")
st.write("")
st.header("Como devemos o chamar?")
inp_txt = st.text_input("Digite seu nome")

if inp_txt:
    st.write(f"Prazer, {inp_txt}!")

if st.button ("Próximo"):
    st.switch_page("Pages/Cadastro.py") 

st.sidebar.image("https://i.imgur.com/PPJ1vF0.png")
        
st.sidebar.write("💡 Use o menu lateral para navegar!")
import streamlit as st

# --- Configuração da página ---
st.set_page_config(page_title="Chatbot LIM - Frequência", page_icon="⏰", layout="centered")

# --- Título ---
st.title("🤖 Chatbot - FAQ Frequência (LIMs)")

st.write("Olá! Sou o assistente virtual dos LIMs. Escolha uma das opções abaixo para esclarecer sua dúvida:")

# --- Estrutura em árvore (menus e submenus) ---
menu_principal = st.selectbox(
    "Selecione um tema:",
    [
        "Selecione...",
        "Benefícios"
        "Registro de Ponto",
        "Regularização de Frequência",
        "Faltas",
        "Banco de Horas",
        "Horário Fixo",
        "Horário Variável",
        "Outras dúvidas / Enviar e-mail"
    ]
)

# --- Respostas fixas ---
if menu_principal == "Registro de Ponto":
    submenu = st.radio("Escolha uma dúvida:", [
        "Onde devo registrar meu ponto?",
        "Posso registrar o ponto de outro colaborador?"
    ])
    if submenu == "Onde devo registrar meu ponto?":
        st.success("✅ O ponto deve ser registrado exclusivamente no sistema informatizado disponibilizado pelo HC.")
    elif submenu == "Posso registrar o ponto de outro colaborador?":
        st.error("❌ Não. Cada colaborador é responsável pelo próprio registro. O uso indevido gera sanções administrativas.")

elif menu_principal == "Regularização de Frequência":
    submenu = st.radio("Escolha uma dúvida:", [
        "Esqueci de bater o ponto, posso regularizar?",
        "Qual o limite de regularizações por mês?",
        "Como envio documentos comprobatórios?"
    ])
    if submenu == "Esqueci de bater o ponto, posso regularizar?":
        st.success("✅ Sim. O colaborador pode regularizar até 5 vezes por mês, desde que seja apenas um registro (entrada ou saída).")
    elif submenu == "Qual o limite de regularizações por mês?":
        st.info("ℹ️ São permitidas até 5 regularizações por mês, conforme Resolução LIM/XXX/25.")
    elif submenu == "Como envio documentos comprobatórios?":
        st.success("📄 Documentos devem ser enviados via sistema ou entregues à Área de Gestão de Pessoas do LIM.")

elif menu_principal == "Faltas":
    submenu = st.radio("Escolha uma dúvida:", [
        "Qual o limite de faltas justificadas?",
        "O que acontece em caso de falta injustificada?"
    ])
    if submenu == "Qual o limite de faltas justificadas?":
        st.info("ℹ️ As faltas justificadas devem estar acompanhadas de atestado/documento válido, sem limite mensal.")
    elif submenu == "O que acontece em caso de falta injustificada?":
        st.error("❌ A falta injustificada implica desconto do dia e pode gerar medidas administrativas.")

elif menu_principal == "Banco de Horas":
    submenu = st.radio("Escolha uma dúvida:", [
        "Como funciona o banco de horas?",
        "Até quando posso compensar minhas horas?",
        "Quantas horas extras posso acumular por dia?",
        "Posso folgar usando minhas horas acumuladas?"
    ])
    if submenu == "Como funciona o banco de horas?":
        st.info("ℹ️ O banco de horas permite acumular horas excedentes para compensação posterior.")
    elif submenu == "Até quando posso compensar minhas horas?":
        st.success("✅ As horas devem ser compensadas em até 60 dias, salvo regras específicas do LIM.")
    elif submenu == "Quantas horas extras posso acumular por dia?":
        st.info("ℹ️ O limite de horas extras diárias é definido pela Resolução vigente e legislação trabalhista.")
    elif submenu == "Posso folgar usando minhas horas acumuladas?":
        st.success("✅ Sim, mediante acordo prévio com a chefia imediata.")

elif menu_principal == "Horário Fixo":
    submenu = st.radio("Escolha uma dúvida:", [
        "Existe tolerância para atraso ou saída antecipada?",
        "Como funciona o atraso compensado?",
        "O que acontece em caso de falta injustificada?"
    ])
    if submenu == "Existe tolerância para atraso ou saída antecipada?":
        st.info("ℹ️ Há tolerância de até 10 minutos na entrada ou saída, desde que não se repita diariamente.")
    elif submenu == "Como funciona o atraso compensado?":
        st.success("✅ O colaborador pode compensar atrasos no mesmo dia, desde que autorizado pela chefia.")
    elif submenu == "O que acontece em caso de falta injustificada?":
        st.error("❌ Implica desconto do dia e possível abertura de processo administrativo.")

elif menu_principal == "Horário Variável":
    submenu = st.radio("Escolha uma dúvida:", [
        "Preciso cumprir horário fixo de entrada e saída?",
        "O que acontece se eu não compensar minhas horas no mês?"
    ])
    if submenu == "Preciso cumprir horário fixo de entrada e saída?":
        st.info("ℹ️ No horário variável, o colaborador deve cumprir a carga horária diária, sem necessidade de horários fixos.")
    elif submenu == "O que acontece se eu não compensar minhas horas no mês?":
        st.error("❌ As horas não compensadas serão descontadas na folha de pagamento.")

elif menu_principal == "Outras dúvidas / Enviar e-mail":
    st.write("✉️ Não encontrou sua resposta? Clique no botão abaixo para enviar um e-mail para a Área de Gestão de Pessoas.")
    st.markdown("[Enviar e-mail](mailto:gestaopessoas@lim.com.br)")


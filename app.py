import streamlit as st
from groq import Groq
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
st.set_page_config(page_title="Finance AI Agent", page_icon="📊")
st.title("📊 Finance AI Agent")
st.caption("Ask anything about stocks, companies, or financial analysis")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a finance question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analysing..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a professional financial analyst specialising in Pakistani and global markets. Give detailed, data-driven answers."},
                    {"role": "user", "content": prompt}
                ]
            )
            st.markdown(response.choices[0].message.content)
    
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})
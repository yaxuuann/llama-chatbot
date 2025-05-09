import streamlit as st
import requests

# Streamlit page settings
st.set_page_config(page_title="PalmPal Chatbot", layout="wide")
st.title("🌴 PalmPal Chatbot")
st.markdown("Your Personalised Assistant for Palm Plantation Owners")

# Sidebar settings
with st.sidebar:
    st.header("Model Settings")
    selected_model = st.selectbox(
        "Choose LLaMA 3.2 Vision Model:",
        options=["llama3.2-vision:11b", "llama3.2-vision:90b"],
        index=0
    )
    st.info("💡 Tip: Use 11B for general queries. 90B is more powerful but needs more memory.")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("💬 Ask PalmPal something (e.g., crop health tips, fertilizer suggestions):")

# Chat response
if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.spinner("🧠 PalmPal is thinking..."):
        try:
            response = requests.post(
                "http://localhost:11434/api/chat",
                json={
                    "model": selected_model,
                    "messages": st.session_state.chat_history
                }
            )
            response.raise_for_status()
            bot_reply = response.json()["message"]["content"]
            st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Display chat
st.subheader("🗨️ Chat History")
for message in st.session_state.chat_history:
    if message["role"] == "user":
        st.markdown(f"**👤 You:** {message['content']}")
    else:
        st.markdown(f"**🤖 PalmPal:** {message['content']}")

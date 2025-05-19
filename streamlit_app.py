# import streamlit as st
# from huggingface_hub import InferenceClient

# api_key = st.secrets["HUGGINGFACE_API_KEY"]
# client = InferenceClient(api_key=api_key)

# # --- Page Configuration ---
# st.set_page_config(page_title="PalmPal", page_icon="🌴", layout="centered")

# # --- Language Selection ---
# if "language" not in st.session_state:
#     st.session_state.language = "id"  # Default: Bahasa Indonesia

# # --- Language Toggle Button ---
# lang_toggle = st.button("🌐 Switch to English" if st.session_state.language == "id" else "🌐 Ganti ke Bahasa Indonesia")
# if lang_toggle:
#     st.session_state.language = "en" if st.session_state.language == "id" else "id"
#     st.rerun()  # Force rerun to reflect UI change immediately

# # --- Text Translations ---
# TEXT = {
#     "id": {
#         "title": "🌴 PalmPal – Teman Berkebun Kamu",
#         "subtitle": "*Tanya soal sawit, kapan saja, di mana saja.*",
#         "chat_title": "### 💬 Chat dengan PalmPal",
#         "input_placeholder": "Tulis pertanyaanmu di sini (contoh: Kenapa daun sawit saya kuning?)",
#         "send_button": "📨 Kirim",
#         "examples": "#### 📌 Contoh Pertanyaan",
#         "advanced": "⚙️ Pengaturan Lanjutan",
#         "clear_chat": "🧹 Bersihkan Riwayat Chat",
#         "model_info": "Model: `meta-llama/Llama-3.2-3B-Instruct` via HuggingFace API",
#         "footer": "© 2025 SawitPRO – Didukung oleh AI & Llama3 💡",
#         "thinking": "PalmPal sedang berpikir...",
#         "user": "👤 Kamu",
#         "bot": "🤖 PalmPal",
#         "error": "Maaf, PalmPal mengalami gangguan."
#     },
#     "en": {
#         "title": "🌴 PalmPal – Your Farming Friend",
#         "subtitle": "*Ask anything about palm oil, anytime, anywhere.*",
#         "chat_title": "### 💬 Chat with PalmPal",
#         "input_placeholder": "Type your question here (e.g. Why are my palm leaves yellow?)",
#         "send_button": "📨 Send",
#         "examples": "#### 📌 Example Questions",
#         "advanced": "⚙️ Advanced Settings",
#         "clear_chat": "🧹 Clear Chat History",
#         "model_info": "Model: `meta-llama/Llama-3.2-3B-Instruct` via HuggingFace API",
#         "footer": "© 2025 SawitPRO – Powered by AI & Llama3 💡",
#         "thinking": "PalmPal is thinking...",
#         "user": "👤 You",
#         "bot": "🤖 PalmPal",
#         "error": "Sorry, PalmPal encountered an error."
#     }
# }
# lang = st.session_state.language
# t = TEXT[lang]

# # --- Branding ---
# st.image("https://static.wixstatic.com/media/759737_bb3e5ad0e411479782bdaca6f4fa3bda~mv2.png/v1/fit/w_2500,h_1330,al_c/759737_bb3e5ad0e411479782bdaca6f4fa3bda~mv2.png", width=200)
# st.markdown(f"## {t['title']}")
# st.markdown(t['subtitle'])

# # --- Session State Initialization ---
# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# # --- Generate Bot Response ---
# def generate_response(user_input):
#     messages = []
#     for msg in st.session_state.messages[-10:]:
#         role = "user" if msg["role"] == "user" else "assistant"
#         messages.append({"role": role, "content": msg["content"]})
#     messages.append({"role": "user", "content": user_input})

#     with st.spinner(t['thinking']):
#         try:
#             response = client.chat_completion(
#                 model="meta-llama/Llama-3.2-3B-Instruct",
#                 messages=messages,
#                 temperature=0.7,
#                 max_tokens=500,
#                 top_p=0.9
#             )
#             return response.choices[0].message.content
#         except Exception as e:
#             st.error(f"{t['error']}: {str(e)}")
#             return t['error']

# # --- Display Chat History ---
# st.markdown(t['chat_title'])
# with st.container():
#     for msg in st.session_state.messages[-6:]:
#         speaker = t["user"] if msg["role"] == "user" else t["bot"]
#         st.markdown(f"**{speaker}:** {msg['content']}")

# # --- User Input ---
# def process_user_input():
#     if st.session_state.user_input:
#         user_message = st.session_state.user_input
#         st.session_state.messages.append({"role": "user", "content": user_message})
#         bot_response = generate_response(user_message)
#         st.session_state.messages.append({"role": "assistant", "content": bot_response})
#         st.session_state.user_input = ""

# st.text_input(t["input_placeholder"], key="user_input", on_change=process_user_input)
# st.button(t["send_button"], on_click=process_user_input)

# # --- Example Prompts ---
# st.markdown(t["examples"])
# cols = st.columns(2)
# example_prompts = {
#     "id": [
#         "Kenapa daun sawit saya kuning?",
#         "Bagaimana cara pupuk sawit yang bagus?",
#         "Apa hama yang sering menyerang sawit?",
#         "Bagaimana panen sawit yang efektif?"
#     ],
#     "en": [
#         "Why are my palm leaves yellow?",
#         "What's a good way to fertilize palm oil trees?",
#         "What pests commonly attack palm oil plants?",
#         "How to harvest palm oil effectively?"
#     ]
# }
# for i, prompt in enumerate(example_prompts[lang]):
#     if cols[i % 2].button(prompt):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         bot_response = generate_response(prompt)
#         st.session_state.messages.append({"role": "assistant", "content": bot_response})
#         st.rerun()

# # --- Optional Advanced Section ---
# with st.expander(t["advanced"]):
#     if st.button(t["clear_chat"]):
#         st.session_state.messages = []
#         st.rerun()
#     st.markdown(t["model_info"])

# # --- Footer ---
# st.markdown("---")
# st.markdown(t["footer"])

import streamlit as st
from huggingface_hub import InferenceClient

api_key = st.secrets["HUGGINGFACE_API_KEY"]
client = InferenceClient(api_key=api_key)

# --- Page Configuration ---
st.set_page_config(page_title="PalmPal", page_icon="🌴", layout="centered")

# --- Custom CSS for Chat Bubbles ---
st.markdown("""
<style>
    /* Chat container */
    .chat-container {
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        position: relative;
        max-width: 80%;
        clear: both;
    }
    
    /* User message */
    .user-message {
        background-color: #e6f7ff;
        border: 1px solid #91d5ff;
        float: right;
        color: #0c5460;
        margin-left: 20%;
    }
    
    /* Bot message */
    .bot-message {
        background-color: #f0f2f5;
        border: 1px solid #d9d9d9;
        float: left;
        color: #333;
        margin-right: 20%;
    }
    
    /* Message content */
    .message-content {
        padding: 8px 12px;
        font-size: 16px;
    }
    
    /* Avatar circle */
    .avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        position: absolute;
        top: -5px;
    }
    
    /* User avatar */
    .user-avatar {
        background-color: #1890ff;
        right: -10px;
    }
    
    /* Bot avatar */
    .bot-avatar {
        background-color: #52c41a;
        left: -10px;
    }
    
    /* Clear float */
    .clearfix::after {
        content: "";
        clear: both;
        display: table;
    }
    
    /* Space between messages */
    .message-gap {
        height: 15px;
        clear: both;
    }
</style>
""", unsafe_allow_html=True)

# --- Language Selection ---
if "language" not in st.session_state:
    st.session_state.language = "id"  # Default: Bahasa Indonesia

# --- Language Toggle Button ---
lang_toggle = st.button("🌐 Switch to English" if st.session_state.language == "id" else "🌐 Ganti ke Bahasa Indonesia")
if lang_toggle:
    st.session_state.language = "en" if st.session_state.language == "id" else "id"
    st.rerun()  # Force rerun to reflect UI change immediately

# --- Text Translations ---
TEXT = {
    "id": {
        "title": "🌴 PalmPal – Teman Berkebun Kamu",
        "subtitle": "*Tanya soal sawit, kapan saja, di mana saja.*",
        "chat_title": "### 💬 Chat dengan PalmPal",
        "input_placeholder": "Tulis pertanyaanmu di sini (contoh: Kenapa daun sawit saya kuning?)",
        "send_button": "📨 Kirim",
        "examples": "#### 📌 Contoh Pertanyaan",
        "advanced": "⚙️ Pengaturan Lanjutan",
        "clear_chat": "🧹 Bersihkan Riwayat Chat",
        "model_info": "Model: `meta-llama/Llama-3.2-3B-Instruct` via HuggingFace API",
        "footer": "© 2025 SawitPRO – Didukung oleh AI & Llama3 💡",
        "thinking": "PalmPal sedang berpikir...",
        "user": "Kamu",
        "bot": "PalmPal",
        "error": "Maaf, PalmPal mengalami gangguan."
    },
    "en": {
        "title": "🌴 PalmPal – Your Farming Friend",
        "subtitle": "*Ask anything about palm oil, anytime, anywhere.*",
        "chat_title": "### 💬 Chat with PalmPal",
        "input_placeholder": "Type your question here (e.g. Why are my palm leaves yellow?)",
        "send_button": "📨 Send",
        "examples": "#### 📌 Example Questions",
        "advanced": "⚙️ Advanced Settings",
        "clear_chat": "🧹 Clear Chat History",
        "model_info": "Model: `meta-llama/Llama-3.2-3B-Instruct` via HuggingFace API",
        "footer": "© 2025 SawitPRO – Powered by AI & Llama3 💡",
        "thinking": "PalmPal is thinking...",
        "user": "You",
        "bot": "PalmPal",
        "error": "Sorry, PalmPal encountered an error."
    }
}
lang = st.session_state.language
t = TEXT[lang]

# --- Branding ---
st.image("https://static.wixstatic.com/media/759737_bb3e5ad0e411479782bdaca6f4fa3bda~mv2.png/v1/fit/w_2500,h_1330,al_c/759737_bb3e5ad0e411479782bdaca6f4fa3bda~mv2.png", width=200)
st.markdown(f"## {t['title']}")
st.markdown(t['subtitle'])

# --- Session State Initialization ---
if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- Generate Bot Response ---
def generate_response(user_input):
    messages = []
    for msg in st.session_state.messages[-10:]:
        role = "user" if msg["role"] == "user" else "assistant"
        messages.append({"role": role, "content": msg["content"]})
    messages.append({"role": "user", "content": user_input})

    with st.spinner(t['thinking']):
        try:
            response = client.chat_completion(
                model="meta-llama/Llama-3.2-3B-Instruct",
                messages=messages,
                temperature=0.7,
                max_tokens=500,
                top_p=0.9
            )
            return response.choices[0].message.content
        except Exception as e:
            st.error(f"{t['error']}: {str(e)}")
            return t['error']

# --- Display Chat Bubbles ---
st.markdown(t['chat_title'])
chat_container = st.container()

with chat_container:
    for msg in st.session_state.messages[-6:]:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="chat-container user-message">
                <div class="avatar user-avatar">👤</div>
                <div class="message-content">{msg['content']}</div>
            </div>
            <div class="message-gap"></div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-container bot-message">
                <div class="avatar bot-avatar">🤖</div>
                <div class="message-content">{msg['content']}</div>
            </div>
            <div class="message-gap"></div>
            """, unsafe_allow_html=True)
    
    # Add clearfix to ensure container expands properly
    st.markdown('<div class="clearfix"></div>', unsafe_allow_html=True)
# --- Example Prompts ---
st.markdown(t["examples"])
cols = st.columns(2)
example_prompts = {
    "id": [
        "Kenapa daun sawit saya kuning?",
        "Bagaimana cara pupuk sawit yang bagus?",
        "Apa hama yang sering menyerang sawit?",
        "Bagaimana panen sawit yang efektif?"
    ],
    "en": [
        "Why are my palm leaves yellow?",
        "What's a good way to fertilize palm oil trees?",
        "What pests commonly attack palm oil plants?",
        "How to harvest palm oil effectively?"
    ]
}
for i, prompt in enumerate(example_prompts[lang]):
    if cols[i % 2].button(prompt):
        st.session_state.messages.append({"role": "user", "content": prompt})
        bot_response = generate_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.rerun()

# --- User Input ---
def process_user_input():
    if st.session_state.user_input:
        user_message = st.session_state.user_input
        st.session_state.messages.append({"role": "user", "content": user_message})
        bot_response = generate_response(user_message)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.session_state.user_input = ""

input_col, button_col = st.columns([4, 1])
with input_col:
    st.text_input(t["input_placeholder"], key="user_input", on_change=process_user_input)
with button_col:
    st.button(t["send_button"], on_click=process_user_input)


# --- Optional Advanced Section ---
with st.expander(t["advanced"]):
    if st.button(t["clear_chat"]):
        st.session_state.messages = []
        st.rerun()
    st.markdown(t["model_info"])

# --- Footer ---
st.markdown("---")
st.markdown(t["footer"])

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
















# import streamlit as st
# from huggingface_hub import InferenceClient

# api_key = st.secrets["HUGGINGFACE_API_KEY"]
# client = InferenceClient(api_key=api_key)

# # --- Page Configuration ---
# st.set_page_config(page_title="PalmPal", page_icon="🌴", layout="centered")

# # --- Custom CSS for Chat Bubbles ---
# st.markdown("""
# <style>
#     /* Chat container */
#     .chat-container {
#         padding: 10px;
#         border-radius: 10px;
#         margin-bottom: 10px;
#         position: relative;
#         max-width: 80%;
#         clear: both;
#     }
    
#     /* User message */
#     .user-message {
#         background-color: #e6f7ff;
#         border: 1px solid #91d5ff;
#         float: right;
#         color: #0c5460;
#         margin-left: 20%;
#     }
    
#     /* Bot message */
#     .bot-message {
#         background-color: #f0f2f5;
#         border: 1px solid #d9d9d9;
#         float: left;
#         color: #333;
#         margin-right: 20%;
#     }
    
#     /* Message content */
#     .message-content {
#         padding: 8px 12px;
#         font-size: 16px;
#     }
    
#     /* Avatar circle */
#     .avatar {
#         width: 32px;
#         height: 32px;
#         border-radius: 50%;
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         color: white;
#         font-weight: bold;
#         position: absolute;
#         top: -5px;
#     }
    
#     /* User avatar */
#     .user-avatar {
#         background-color: #1890ff;
#         right: -10px;
#     }
    
#     /* Bot avatar */
#     .bot-avatar {
#         background-color: #52c41a;
#         left: -10px;
#     }
    
#     /* Clear float */
#     .clearfix::after {
#         content: "";
#         clear: both;
#         display: table;
#     }
    
#     /* Space between messages */
#     .message-gap {
#         height: 15px;
#         clear: both;
#     }
# </style>
# """, unsafe_allow_html=True)

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
#         "user": "Kamu",
#         "bot": "PalmPal",
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
#         "user": "You",
#         "bot": "PalmPal",
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

# # --- Display Chat Bubbles ---
# st.markdown(t['chat_title'])
# chat_container = st.container()

# with chat_container:
#     for msg in st.session_state.messages[-6:]:
#         if msg["role"] == "user":
#             st.markdown(f"""
#             <div class="chat-container user-message">
#                 <div class="avatar user-avatar">👤</div>
#                 <div class="message-content">{msg['content']}</div>
#             </div>
#             <div class="message-gap"></div>
#             """, unsafe_allow_html=True)
#         else:
#             st.markdown(f"""
#             <div class="chat-container bot-message">
#                 <div class="avatar bot-avatar">🤖</div>
#                 <div class="message-content">{msg['content']}</div>
#             </div>
#             <div class="message-gap"></div>
#             """, unsafe_allow_html=True)
    
#     # Add clearfix to ensure container expands properly
#     st.markdown('<div class="clearfix"></div>', unsafe_allow_html=True)
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

# # --- User Input ---
# def process_user_input():
#     if st.session_state.user_input:
#         user_message = st.session_state.user_input
#         st.session_state.messages.append({"role": "user", "content": user_message})
#         bot_response = generate_response(user_message)
#         st.session_state.messages.append({"role": "assistant", "content": bot_response})
#         st.session_state.user_input = ""

# input_col, button_col = st.columns([4, 1])
# with input_col:
#     st.text_input(t["input_placeholder"], key="user_input", on_change=process_user_input)
# with button_col:
#     st.button(t["send_button"], on_click=process_user_input)


# # --- Optional Advanced Section ---
# with st.expander(t["advanced"]):
#     if st.button(t["clear_chat"]):
#         st.session_state.messages = []
#         st.rerun()
#     st.markdown(t["model_info"])

# # --- Footer ---
# st.markdown("---")
# st.markdown(t["footer"])


















# import streamlit as st
# from huggingface_hub import InferenceClient

# api_key = st.secrets["HUGGINGFACE_API_KEY"]
# client = InferenceClient(api_key=api_key)

# # --- Page Configuration ---
# st.set_page_config(page_title="PalmPal", page_icon="🌴", layout="centered")

# # --- Custom CSS for Chat Bubbles with SawitPRO colors ---
# st.markdown("""
# <style>
#     /* SawitPRO Colors */
#     :root {
#         --sawit-green: #576A34;
#         --sawit-yellow: #E9D037;
#         --sawit-light-green: #8BA262;
#         --sawit-dark-green: #3A4A1F;
#         --sawit-light-yellow: #F5E685;
#     }
    
#     /* Add styling to fix button alignment */
#     .stButton > button {
#         height: 38px;
#         margin-top: 25px;
#         background-color: var(--sawit-green) !important;
#         color: white !important;
#         border: none !important;
#     }
    
#     .stButton > button:hover {
#         background-color: var(--sawit-dark-green) !important;
#         border: none !important;
#     }
    
#     /* Override Streamlit's default styling */
#     .stTextInput > div > div > input {
#         border: 1px solid var(--sawit-green);
#     }
    
#     /* Chat container */
#     .chat-container {
#         padding: 10px;
#         border-radius: 10px;
#         margin-bottom: 10px;
#         position: relative;
#         max-width: 80%;
#         clear: both;
#     }
    
#     /* User message */
#     .user-message {
#         background-color: var(--sawit-light-yellow);
#         border: 1px solid var(--sawit-yellow);
#         float: right;
#         color: #333;
#         margin-left: 20%;
#     }
    
#     /* Bot message */
#     .bot-message {
#         background-color: var(--sawit-light-green);
#         border: 1px solid var(--sawit-green);
#         float: left;
#         color: white;
#         margin-right: 20%;
#     }
    
#     /* Message content */
#     .message-content {
#         padding: 8px 12px;
#         font-size: 16px;
#     }
    
#     /* Avatar circle */
#     .avatar {
#         width: 32px;
#         height: 32px;
#         border-radius: 50%;
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         color: white;
#         font-weight: bold;
#         position: absolute;
#         top: -5px;
#     }
    
#     /* User avatar */
#     .user-avatar {
#         background-color: var(--sawit-yellow);
#         color: #333;
#         right: -10px;
#     }
    
#     /* Bot avatar */
#     .bot-avatar {
#         background-color: var(--sawit-green);
#         left: -10px;
#     }
    
#     /* Clear float */
#     .clearfix::after {
#         content: "";
#         clear: both;
#         display: table;
#     }
    
#     /* Space between messages */
#     .message-gap {
#         height: 15px;
#         clear: both;
#     }
    
#     /* Title styling */
#     h2, h3, h4 {
#         color: var(--sawit-green) !important;
#     }
    
#     /* Example buttons */
#     .examples-container button {
#         background-color: var(--sawit-light-green) !important;
#         color: white !important;
#         border: none !important;
#     }
    
#     .examples-container button:hover {
#         background-color: var(--sawit-green) !important;
#     }
# </style>
# """, unsafe_allow_html=True)

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
#         "user": "Kamu",
#         "bot": "PalmPal",
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
#         "user": "You",
#         "bot": "PalmPal",
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

# # --- Display Chat Bubbles ---
# st.markdown(t['chat_title'])
# chat_container = st.container()

# with chat_container:
#     for msg in st.session_state.messages[-6:]:
#         if msg["role"] == "user":
#             st.markdown(f"""
#             <div class="chat-container user-message">
#                 <div class="avatar user-avatar">👤</div>
#                 <div class="message-content">{msg['content']}</div>
#             </div>
#             <div class="message-gap"></div>
#             """, unsafe_allow_html=True)
#         else:
#             st.markdown(f"""
#             <div class="chat-container bot-message">
#                 <div class="avatar bot-avatar">🤖</div>
#                 <div class="message-content">{msg['content']}</div>
#             </div>
#             <div class="message-gap"></div>
#             """, unsafe_allow_html=True)
    
#     # Add clearfix to ensure container expands properly
#     st.markdown('<div class="clearfix"></div>', unsafe_allow_html=True)

# # --- User Input ---
# def process_user_input():
#     if st.session_state.user_input:
#         user_message = st.session_state.user_input
#         st.session_state.messages.append({"role": "user", "content": user_message})
#         bot_response = generate_response(user_message)
#         st.session_state.messages.append({"role": "assistant", "content": bot_response})
#         st.session_state.user_input = ""

# # Create an input container with columns that align correctly
# input_container = st.container()
# with input_container:
#     cols = st.columns([4, 1])
#     with cols[0]:
#         st.text_input(t["input_placeholder"], key="user_input", on_change=process_user_input)
#     with cols[1]:
#         st.button(t["send_button"], on_click=process_user_input)

# # --- Example Prompts ---
# st.markdown(t["examples"])
# st.markdown('<div class="examples-container">', unsafe_allow_html=True)
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
# st.markdown('</div>', unsafe_allow_html=True)

# # --- Optional Advanced Section ---
# with st.expander(t["advanced"]):
#     if st.button(t["clear_chat"]):
#         st.session_state.messages = []
#         st.rerun()
#     st.markdown(t["model_info"])

# # --- Footer ---
# st.markdown("---")
# st.markdown(t["footer"])













# import streamlit as st
# from huggingface_hub import InferenceClient

# api_key = st.secrets["HUGGINGFACE_API_KEY"]
# client = InferenceClient(api_key=api_key)

# # --- Page Configuration ---
# st.set_page_config(page_title="PalmPal", page_icon="🌴", layout="centered")

# # --- Custom CSS with SawitPRO colors and icons ---
# st.markdown("""
# <style>
#     /* Main colors */
#     :root {
#         --sawit-green: #576A34;
#         --sawit-yellow: #E9D037;
#         --sawit-dark-green: #3A4A1F;
#     }
    
#     /* Chat bubbles with icons */
#     .chat-container {
#         display: flex;
#         margin-bottom: 15px;
#         max-width: 100%;
#         clear: both;
#     }
    
#     .chat-container.user {
#         justify-content: flex-end;
#     }
    
#     .chat-container.bot {
#         justify-content: flex-start;
#     }
    
#     .chat-icon {
#         width: 40px;
#         height: 40px;
#         border-radius: 50%;
#         background-size: cover;
#         background-position: center;
#         flex-shrink: 0;
#         margin-top: auto;
#     }
    
#     .user-icon {
#         background-image: url('https://rspo.org/wp-content/uploads/AN-OIL-PALM-FARMERS-POSITIVE-IMPACT-ON-THE-ENVIRONMENT_large.jpg');
#         margin-left: 10px;
#     }
    
#     .bot-icon {
#         background-image: url('data:image/png;base64,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');
#         margin-right: 10px;
#     }
    
#     .chat-bubble {
#         border-radius: 18px;
#         padding: 12px 16px;
#         max-width: 70%;
#         word-wrap: break-word;
#     }
    
#     .user-bubble {
#         background-color: var(--sawit-yellow);
#         color: #333;
#         border-top-right-radius: 4px;
#     }
    
#     .bot-bubble {
#         background-color: var(--sawit-green);
#         color: white;
#         border-top-left-radius: 4px;
#     }
    
#     /* Fix button alignment */
#     div.stButton > button {
#         margin-top: 24px;
#         background-color: var(--sawit-green);
#         color: white;
#         border: none;
#     }
    
#     div.stButton > button:hover {
#         background-color: var(--sawit-dark-green);
#         color: white;
#         border: none;
#     }
    
#     /* Example prompt styling */
#     .example-section {
#         margin-bottom: 20px;
#     }
    
#     .example-section button {
#         width: 100%;
#         margin-bottom: 10px;
#         background-color: var(--sawit-green) !important;
#         color: white !important;
#         opacity: 0.9;
#     }
    
#     .example-section button:hover {
#         opacity: 1;
#     }
    
#     /* Header colors */
#     h1, h2, h3, h4, h5, h6 {
#         color: var(--sawit-green);
#     }
    
#     /* Create space at bottom of chat container */
#     .chat-end-spacer {
#         height: 20px;
#         clear: both;
#     }
    
#     /* Chat container with fixed height and scrolling */
#     .chat-window {
#         height: 400px;
#         overflow-y: auto;
#         border: 1px solid #eee;
#         border-radius: 10px;
#         padding: 15px;
#         margin-bottom: 20px;
#         background-color: #f9f9f9;
#     }
# </style>
# """, unsafe_allow_html=True)

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
#         "user": "Kamu",
#         "bot": "PalmPal",
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
#         "user": "You",
#         "bot": "PalmPal",
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

# # --- Example Prompts (MOVED ABOVE INPUT) ---
# st.markdown(t["examples"])
# st.markdown('<div class="example-section">', unsafe_allow_html=True)
# example_cols = st.columns(2)
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
#     if example_cols[i % 2].button(prompt, key=f"example_{i}"):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         bot_response = generate_response(prompt)
#         st.session_state.messages.append({"role": "assistant", "content": bot_response})
#         st.rerun()
# st.markdown('</div>', unsafe_allow_html=True)

# # --- Display Chat Bubbles ---
# st.markdown(t['chat_title'])
# chat_container = st.container()

# with chat_container:
#     # Create a fixed-height chat window
#     st.markdown('<div class="chat-window">', unsafe_allow_html=True)
    
#     # Display chat messages with user/bot icons
#     for msg in st.session_state.messages[-6:]:
#         if msg["role"] == "user":
#             st.markdown(f"""
#             <div class="chat-container user">
#                 <div class="chat-bubble user-bubble">{msg['content']}</div>
#                 <div class="chat-icon user-icon"></div>
#             </div>
#             """, unsafe_allow_html=True)
#         else:
#             st.markdown(f"""
#             <div class="chat-container bot">
#                 <div class="chat-icon bot-icon"></div>
#                 <div class="chat-bubble bot-bubble">{msg['content']}</div>
#             </div>
#             """, unsafe_allow_html=True)
    
#     # Close the chat window
#     st.markdown('</div>', unsafe_allow_html=True)

# # --- User Input ---
# def process_user_input():
#     if st.session_state.user_input:
#         user_message = st.session_state.user_input
#         st.session_state.messages.append({"role": "user", "content": user_message})
#         bot_response = generate_response(user_message)
#         st.session_state.messages.append({"role": "assistant", "content": bot_response})
#         st.session_state.user_input = ""  # Clear input field

# # Input area with better alignment
# col1, col2 = st.columns([4, 1])
# with col1:
#     st.text_input(t["input_placeholder"], key="user_input", on_change=process_user_input)
# with col2:
#     st.button(t["send_button"], on_click=process_user_input)

# # --- Optional Advanced Section ---
# with st.expander(t["advanced"]):
#     if st.button(t["clear_chat"]):
#         st.session_state.messages = []
#         st.rerun()
#     st.markdown(t["model_info"])

# # --- Footer ---
# st.markdown("---")
# st.markdown(t["footer"])























# import streamlit as st
# from huggingface_hub import InferenceClient

# api_key = st.secrets["HUGGINGFACE_API_KEY"]
# client = InferenceClient(api_key=api_key)

# # --- Page Configuration ---
# st.set_page_config(page_title="PalmPal", page_icon="🌴", layout="centered")

# # --- Custom CSS with SawitPRO colors and icons ---
# st.markdown("""
# <style>
#     /* Main colors */
#     :root {
#         --sawit-green: #576A34;
#         --sawit-yellow: #E9D037;
#         --sawit-dark-green: #3A4A1F;
#     }
    
#     /* Chat bubbles with icons */
#     .chat-container {
#         display: flex;
#         margin-bottom: 12px;
#         max-width: 100%;
#         clear: both;
#     }
    
#     .chat-container.user {
#         justify-content: flex-end;
#     }
    
#     .chat-container.bot {
#         justify-content: flex-start;
#     }
    
#     .chat-icon {
#         width: 36px;
#         height: 36px;
#         border-radius: 50%;
#         background-size: cover;
#         background-position: center;
#         flex-shrink: 0;
#         margin-top: auto;
#     }
    
#     .user-icon {
#         background-image: url('https://rspo.org/wp-content/uploads/AN-OIL-PALM-FARMERS-POSITIVE-IMPACT-ON-THE-ENVIRONMENT_large.jpg');
#         margin-left: 8px;
#     }
    
#     .bot-icon {
#         background-image: url('data:image/png;base64,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');
#         margin-right: 8px;
#     }
    
#     .chat-bubble {
#         border-radius: 18px;
#         padding: 12px 16px;
#         max-width: 70%;
#         word-wrap: break-word;
#     }
    
#     .user-bubble {
#         background-color: var(--sawit-yellow);
#         color: #333;
#         border-top-right-radius: 4px;
#     }
    
#     .bot-bubble {
#         background-color: var(--sawit-green);
#         color: white;
#         border-top-left-radius: 4px;
#     }
    
#     /* Chat frame */
#     .chat-frame {
#         border: 2px solid #e0e0e0;
#         border-radius: 10px;
#         padding: 15px;
#         margin-bottom: 20px;
#         background-color: #f9f9f9;
#         height: 400px;
#         overflow-y: auto;
#     }
    
#     /* Fix button alignment */
#     div.stButton > button {
#         background-color: var(--sawit-green);
#         color: white;
#         border: none;
#     }
    
#     div.stButton > button:hover {
#         background-color: var(--sawit-dark-green);
#         color: white;
#         border: none;
#     }
    
#     /* Example prompts styling */
#     .example-grid {
#         display: grid;
#         grid-template-columns: 1fr 1fr;
#         grid-gap: 8px;
#         margin-bottom: 15px;
#     }
    
#     .example-grid button {
#         width: 100%;
#         height: 100%;
#         padding: 8px;
#         background-color: var(--sawit-green) !important;
#         color: white !important;
#     }
    
#     /* Example section header */
#     .example-header {
#         margin-bottom: 8px;
#         color: var(--sawit-green);
#         font-weight: bold;
#     }
    
#     /* Align send button */
#     .send-button button {
#         margin-top: 24px;
#     }
    
#     /* Header colors */
#     h1, h2, h3, h4, h5, h6 {
#         color: var(--sawit-green);
#     }
# </style>
# """, unsafe_allow_html=True)

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
#         "examples": "Contoh Pertanyaan:",
#         "advanced": "⚙️ Pengaturan Lanjutan",
#         "clear_chat": "🧹 Bersihkan Riwayat Chat",
#         "model_info": "Model: `meta-llama/Llama-3.2-3B-Instruct` via HuggingFace API",
#         "footer": "© 2025 SawitPRO – Didukung oleh AI & Llama3 💡",
#         "thinking": "PalmPal sedang berpikir...",
#         "user": "Kamu",
#         "bot": "PalmPal",
#         "error": "Maaf, PalmPal mengalami gangguan."
#     },
#     "en": {
#         "title": "🌴 PalmPal – Your Farming Friend",
#         "subtitle": "*Ask anything about palm oil, anytime, anywhere.*",
#         "chat_title": "### 💬 Chat with PalmPal",
#         "input_placeholder": "Type your question here (e.g. Why are my palm leaves yellow?)",
#         "send_button": "📨 Send",
#         "examples": "Example Questions:",
#         "advanced": "⚙️ Advanced Settings",
#         "clear_chat": "🧹 Clear Chat History",
#         "model_info": "Model: `meta-llama/Llama-3.2-3B-Instruct` via HuggingFace API",
#         "footer": "© 2025 SawitPRO – Powered by AI & Llama3 💡",
#         "thinking": "PalmPal is thinking...",
#         "user": "You",
#         "bot": "PalmPal",
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

# # --- Display Chat Bubbles with Frame ---
# st.markdown(t['chat_title'])

# # Ensure the chat frame has a proper height and scrolling
# st.markdown('<div class="chat-frame">', unsafe_allow_html=True)
    
# # Display chat messages with user/bot icons
# for msg in st.session_state.messages[-10:]:
#     if msg["role"] == "user":
#         st.markdown(f"""
#         <div class="chat-container user">
#             <div class="chat-bubble user-bubble">{msg['content']}</div>
#             <div class="chat-icon user-icon"></div>
#         </div>
#         """, unsafe_allow_html=True)
#     else:
#         st.markdown(f"""
#         <div class="chat-container bot">
#             <div class="chat-icon bot-icon"></div>
#             <div class="chat-bubble bot-bubble">{msg['content']}</div>
#         </div>
#         """, unsafe_allow_html=True)

# # Close the chat frame
# st.markdown('</div>', unsafe_allow_html=True)

# # --- Example Prompts RIGHT ABOVE INPUT ---
# st.markdown(f'<p class="example-header">{t["examples"]}</p>', unsafe_allow_html=True)

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

# # Custom HTML grid for examples with equal spacing
# st.markdown('<div class="example-grid">', unsafe_allow_html=True)
# for i, prompt in enumerate(example_prompts[lang]):
#     if st.button(prompt, key=f"example_{i}"):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         bot_response = generate_response(prompt)
#         st.session_state.messages.append({"role": "assistant", "content": bot_response})
#         st.rerun()
# st.markdown('</div>', unsafe_allow_html=True)

# # --- User Input ---
# def process_user_input():
#     if st.session_state.user_input:
#         user_message = st.session_state.user_input
#         st.session_state.messages.append({"role": "user", "content": user_message})
#         bot_response = generate_response(user_message)
#         st.session_state.messages.append({"role": "assistant", "content": bot_response})
#         st.session_state.user_input = ""  # Clear input field

# # Input area with better alignment
# col1, col2 = st.columns([4, 1])
# with col1:
#     st.text_input(t["input_placeholder"], key="user_input", on_change=process_user_input)
# with col2:
#     st.markdown('<div class="send-button">', unsafe_allow_html=True)
#     st.button(t["send_button"], on_click=process_user_input)
#     st.markdown('</div>', unsafe_allow_html=True)

# # --- Optional Advanced Section ---
# with st.expander(t["advanced"]):
#     if st.button(t["clear_chat"]):
#         st.session_state.messages = []
#         st.rerun()
#     st.markdown(t["model_info"])

# # --- Footer ---
# st.markdown("---")
# st.markdown(t["footer"])








# import streamlit as st
# from huggingface_hub import InferenceClient

# api_key = st.secrets["HUGGINGFACE_API_KEY"]
# client = InferenceClient(api_key=api_key)

# # --- Page Configuration ---
# st.set_page_config(page_title="PalmPal", page_icon="🌴", layout="centered")

# # --- Custom CSS with SawitPRO colors and icons ---
# st.markdown("""
# <style>
#     /* Main colors */
#     :root {
#         --sawit-green: #576A34;
#         --sawit-yellow: #E9D037;
#         --sawit-dark-green: #3A4A1F;
#     }
    
#     /* Chat bubbles with icons */
#     .chat-container {
#         display: flex;
#         margin-bottom: 12px;
#         max-width: 100%;
#         clear: both;
#     }
    
#     .chat-container.user {
#         justify-content: flex-end;
#     }
    
#     .chat-container.bot {
#         justify-content: flex-start;
#     }
    
#     .chat-icon {
#         width: 36px;
#         height: 36px;
#         border-radius: 50%;
#         background-size: cover;
#         background-position: center;
#         flex-shrink: 0;
#         margin-top: auto;
#     }
    
#     .user-icon {
#         background-image: url('https://rspo.org/wp-content/uploads/AN-OIL-PALM-FARMERS-POSITIVE-IMPACT-ON-THE-ENVIRONMENT_large.jpg');
#         margin-left: 8px;
#     }
    
#     .bot-icon {
#         background-image: url('data:image/png;base64,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');
#         margin-right: 8px;
#     }
    
#     .chat-bubble {
#         border-radius: 18px;
#         padding: 12px 16px;
#         max-width: 70%;
#         word-wrap: break-word;
#     }
    
#     .user-bubble {
#         background-color: var(--sawit-yellow);
#         color: #333;
#         border-top-right-radius: 4px;
#     }
    
#     .bot-bubble {
#         background-color: var(--sawit-green);
#         color: white;
#         border-top-left-radius: 4px;
#     }
    
#     /* Chat frame */
#     .chat-frame {
#         border: 2px solid #e0e0e0;
#         border-radius: 10px;
#         padding: 15px;
#         margin-bottom: 20px;
#         background-color: #f9f9f9;
#         height: 400px;
#         overflow-y: auto;
#     }
    
#     /* Fix button alignment */
#     div.stButton > button {
#         background-color: var(--sawit-green);
#         color: white;
#         border: none;
#     }
    
#     div.stButton > button:hover {
#         background-color: var(--sawit-dark-green);
#         color: white;
#         border: none;
#     }
    
#     /* Example prompts styling */
#     .example-grid {
#         display: grid;
#         grid-template-columns: 1fr 1fr;
#         grid-gap: 8px;
#         margin-bottom: 15px;
#     }
    
#     .example-grid button {
#         width: 100%;
#         height: 100%;
#         padding: 8px;
#         background-color: var(--sawit-green) !important;
#         color: white !important;
#     }
    
#     /* Example section header */
#     .example-header {
#         margin-bottom: 8px;
#         color: var(--sawit-green);
#         font-weight: bold;
#     }
    
#     /* Align send button */
#     .send-button button {
#         margin-top: 24px;
#     }
    
#     /* Header colors */
#     h1, h2, h3, h4, h5, h6 {
#         color: var(--sawit-green);
#     }
# </style>
# """, unsafe_allow_html=True)

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
#         "input_placeholder": "Tulis pertanyaanmu di sini (contoh: Kenapa daun sawit saya kuning?)",
#         "send_button": "📨 Kirim",
#         "examples": "Contoh Pertanyaan:",
#         "advanced": "⚙️ Pengaturan Lanjutan",
#         "clear_chat": "🧹 Bersihkan Riwayat Chat",
#         "model_info": "Model: `meta-llama/Llama-3.2-3B-Instruct` via HuggingFace API",
#         "footer": "© 2025 SawitPRO – Didukung oleh AI & Llama3 💡",
#         "thinking": "PalmPal sedang berpikir...",
#         "user": "Kamu",
#         "bot": "PalmPal",
#         "error": "Maaf, PalmPal mengalami gangguan."
#     },
#     "en": {
#         "title": "🌴 PalmPal – Your Farming Friend",
#         "subtitle": "*Ask anything about palm oil, anytime, anywhere.*",
#         "input_placeholder": "Type your question here (e.g. Why are my palm leaves yellow?)",
#         "send_button": "📨 Send",
#         "examples": "Example Questions:",
#         "advanced": "⚙️ Advanced Settings",
#         "clear_chat": "🧹 Clear Chat History",
#         "model_info": "Model: `meta-llama/Llama-3.2-3B-Instruct` via HuggingFace API",
#         "footer": "© 2025 SawitPRO – Powered by AI & Llama3 💡",
#         "thinking": "PalmPal is thinking...",
#         "user": "You",
#         "bot": "PalmPal",
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

# # --- Display Chat Bubbles with Frame ---
# # Removed the chat title

# # Ensure the chat frame has a proper height and scrolling
# st.markdown('<div class="chat-frame">', unsafe_allow_html=True)
    
# # Display chat messages with user/bot icons
# for msg in st.session_state.messages[-10:]:
#     if msg["role"] == "user":
#         st.markdown(f"""
#         <div class="chat-container user">
#             <div class="chat-bubble user-bubble">{msg['content']}</div>
#             <div class="chat-icon user-icon"></div>
#         </div>
#         """, unsafe_allow_html=True)
#     else:
#         st.markdown(f"""
#         <div class="chat-container bot">
#             <div class="chat-icon bot-icon"></div>
#             <div class="chat-bubble bot-bubble">{msg['content']}</div>
#         </div>
#         """, unsafe_allow_html=True)

# # Close the chat frame
# st.markdown('</div>', unsafe_allow_html=True)

# # --- Example Prompts RIGHT ABOVE INPUT ---
# st.markdown(f'<p class="example-header">{t["examples"]}</p>', unsafe_allow_html=True)

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

# # Custom HTML grid for examples with equal spacing
# st.markdown('<div class="example-grid">', unsafe_allow_html=True)
# for i, prompt in enumerate(example_prompts[lang]):
#     if st.button(prompt, key=f"example_{i}"):
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         bot_response = generate_response(prompt)
#         st.session_state.messages.append({"role": "assistant", "content": bot_response})
#         st.rerun()
# st.markdown('</div>', unsafe_allow_html=True)

# # --- User Input ---
# def process_user_input():
#     if st.session_state.user_input:
#         user_message = st.session_state.user_input
#         st.session_state.messages.append({"role": "user", "content": user_message})
#         bot_response = generate_response(user_message)
#         st.session_state.messages.append({"role": "assistant", "content": bot_response})
#         st.session_state.user_input = ""  # Clear input field

# # Input area with better alignment
# col1, col2 = st.columns([4, 1])
# with col1:
#     st.text_input(t["input_placeholder"], key="user_input", on_change=process_user_input)
# with col2:
#     st.markdown('<div class="send-button">', unsafe_allow_html=True)
#     st.button(t["send_button"], on_click=process_user_input)
#     st.markdown('</div>', unsafe_allow_html=True)

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

# --- Custom CSS with SawitPRO colors and icons ---
st.markdown("""
<style>
    /* Main colors */
    :root {
        --sawit-green: #576A34;
        --sawit-yellow: #E9D037;
        --sawit-dark-green: #3A4A1F;
    }
    
    /* Chat bubbles with icons */
    .chat-container {
        display: flex;
        margin-bottom: 12px;
        max-width: 100%;
        clear: both;
    }
    
    .chat-container.user {
        justify-content: flex-end;
    }
    
    .chat-container.bot {
        justify-content: flex-start;
    }
    
    .chat-icon {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        background-size: cover;
        background-position: center;
        flex-shrink: 0;
        margin-top: auto;
    }
    
    .user-icon {
        background-image: url('https://rspo.org/wp-content/uploads/AN-OIL-PALM-FARMERS-POSITIVE-IMPACT-ON-THE-ENVIRONMENT_large.jpg');
        margin-left: 8px;
    }
    
    .bot-icon {
        background-image: url('data:image/png;base64,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');
        margin-right: 8px;
    }
    
    .chat-bubble {
        border-radius: 18px;
        padding: 12px 16px;
        max-width: 70%;
        word-wrap: break-word;
    }
    
    .user-bubble {
        background-color: var(--sawit-yellow);
        color: #333;
        border-top-right-radius: 4px;
    }
    
    .bot-bubble {
        background-color: var(--sawit-green);
        color: white;
        border-top-left-radius: 4px;
    }
    
    /* No more chat frame - messages will appear directly on page */
    .chat-area {
        padding: 15px 5px;
        margin-bottom: 20px;
        height: 400px;
        overflow-y: auto;
    }
    
    /* Fix button alignment */
    div.stButton > button {
        background-color: var(--sawit-green);
        color: white;
        border: none;
    }
    
    div.stButton > button:hover {
        background-color: var(--sawit-dark-green);
        color: white;
        border: none;
    }
    
    /* Example prompts styling */
    .example-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-gap: 8px;
        margin-bottom: 15px;
    }
    
    .example-grid button {
        width: 100%;
        height: 100%;
        padding: 8px;
        background-color: var(--sawit-green) !important;
        color: white !important;
    }
    
    /* Example section header */
    .example-header {
        margin-bottom: 8px;
        color: var(--sawit-green);
        font-weight: bold;
    }
    
    /* Align send button */
    .send-button button {
        margin-top: 24px;
    }
    
    /* Header colors */
    h1, h2, h3, h4, h5, h6 {
        color: var(--sawit-green);
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
        "input_placeholder": "Tulis pertanyaanmu di sini (contoh: Kenapa daun sawit saya kuning?)",
        "send_button": "📨 Kirim",
        "examples": "Contoh Pertanyaan:",
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
        "input_placeholder": "Type your question here (e.g. Why are my palm leaves yellow?)",
        "send_button": "📨 Send",
        "examples": "Example Questions:",
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

# --- Display Chat Bubbles (No Frame) ---
# Using a regular container without the frame styling
st.markdown('<div class="chat-area">', unsafe_allow_html=True)
    
# Display chat messages with user/bot icons
for msg in st.session_state.messages[-10:]:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="chat-container user">
            <div class="chat-bubble user-bubble">{msg['content']}</div>
            <div class="chat-icon user-icon"></div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-container bot">
            <div class="chat-icon bot-icon"></div>
            <div class="chat-bubble bot-bubble">{msg['content']}</div>
        </div>
        """, unsafe_allow_html=True)

# Close the chat area
st.markdown('</div>', unsafe_allow_html=True)

# --- Example Prompts RIGHT ABOVE INPUT ---
st.markdown(f'<p class="example-header">{t["examples"]}</p>', unsafe_allow_html=True)

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

# Custom HTML grid for examples with equal spacing
st.markdown('<div class="example-grid">', unsafe_allow_html=True)
for i, prompt in enumerate(example_prompts[lang]):
    if st.button(prompt, key=f"example_{i}"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        bot_response = generate_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# --- User Input ---
def process_user_input():
    if st.session_state.user_input:
        user_message = st.session_state.user_input
        st.session_state.messages.append({"role": "user", "content": user_message})
        bot_response = generate_response(user_message)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.session_state.user_input = ""  # Clear input field

# Input area with better alignment
col1, col2 = st.columns([4, 1])
with col1:
    st.text_input(t["input_placeholder"], key="user_input", on_change=process_user_input)
with col2:
    st.markdown('<div class="send-button">', unsafe_allow_html=True)
    st.button(t["send_button"], on_click=process_user_input)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Optional Advanced Section ---
with st.expander(t["advanced"]):
    if st.button(t["clear_chat"]):
        st.session_state.messages = []
        st.rerun()
    st.markdown(t["model_info"])

# --- Footer ---
st.markdown("---")
st.markdown(t["footer"])

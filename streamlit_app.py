import streamlit as st
from huggingface_hub import InferenceClient
import requests
import json

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
        --light-gray: #f5f5f5;
    }

    /* Reduce space but not as extreme as before */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        margin-top: -2rem !important;
    }

    /* Further reduce space in the main area */
    .main .block-container {
        padding: 1rem !important;
        max-width: 100% !important;
    }

    /* Reduce spaces and gaps - but leave some breathing room */
    .css-1y4p8pa {
        margin-top: -1rem !important;
        padding-top: 0.5rem !important;
        padding-bottom: 0rem !important;
    }

    /* Reduce space above the chat messages */
    .css-1544g2n {
        padding-top: 0.5rem !important;
        margin-top: 0 !important;
    }

    /* Reduce any extra margins around elements */
    .element-container, .stMarkdown, .stButton, .stImage {
        margin-top: 0.2rem !important;
        margin-bottom: 0.2rem !important;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }

    /* Reduce space around image */
    img {
        margin-bottom: 0.5rem !important;
    }

    /* Keep more breathing room in title and subtitle */
    h2 {
        margin-top: 0 !important;
        margin-bottom: 0.2rem !important;
        padding-top: 0 !important;
    }

    p {
        margin-bottom: 0.5rem !important;
        padding: 0 !important;
        line-height: 1.2 !important;
    }

    /* Chat bubbles with icons - slightly more room */
    .chat-container {
        display: flex;
        margin-bottom: 8px !important;
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
        padding: 10px 14px;
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

    /* Restore SawitPRO brand colors for example prompts */
    .example-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-gap: 8px;
        margin-bottom: 8px;
    }

    .example-grid button {
        width: 100%;
        height: 100%;
        padding: 8px;
        background-color: var(--sawit-green) !important;
        color: white !important;
        font-size: 0.95em !important;
    }

    /* Example section header */
    .example-header {
        margin-bottom: 5px;
        color: var(--sawit-green);
        font-weight: bold;
    }

    /* Language toggle button styling */
    .lang-toggle {
        display: inline-block;
        margin-bottom: 8px;
    }

    .lang-toggle button {
        background-color: var(--sawit-green) !important;
        color: white !important;
        border: none !important;
        font-size: 0.9em !important;
    }

    /* Align send button */
    .send-button button {
        margin-top: 24px;
    }

    /* Header colors */
    h1, h2, h3, h4, h5, h6 {
        color: var(--sawit-green);
    }

    /* Add moderate padding to gently push things up */
    .filler {
        height: 1px;
        margin-top: -150px !important;
    }

    /* Hide footer but keep header */
    footer {
        display: none !important;
    }

    /* Make textfields look better */
    .stTextInput > div {
        margin-top: 0 !important;
        margin-bottom: 8px !important;
    }

    /* Custom styling for buttons */
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

    /* Product card styling */
    .product-card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 12px;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .product-name {
        font-weight: bold;
        color: var(--sawit-green);
        margin-bottom: 6px;
    }

    .product-price {
        color: var(--sawit-dark-green);
        font-weight: bold;
        margin-bottom: 8px;
    }

    .product-button {
        background-color: white !important;
        color: var(--sawit-green) !important;
        border: 1px solid var(--sawit-green) !important;
        padding: 5px 10px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 0.8em;
        width: 100%;
        margin-top: 8px;
    }

    .product-button:hover {
        background-color: var(--sawit-green) !important;
        color: white !important;
    }

    .recommendation-section {
        background-color: var(--light-gray);
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 12px;
    }

    .recommendation-title {
        color: var(--sawit-green);
        font-weight: bold;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- Add a filler div to push things up but not too aggressively ---
st.markdown('<div class="filler"></div>', unsafe_allow_html=True)

# --- Translation function for existing messages ---
def translate_content(text, from_lang, to_lang):
    if from_lang == to_lang:
        return text

    translations = {
        ("id", "en"): {
            "Kenapa daun sawit saya kuning?": "Why are my palm leaves yellow?",
            "Bagaimana cara pupuk sawit yang bagus?": "What's a good way to fertilize palm oil trees?",
            "Apa hama yang sering menyerang sawit?": "What pests commonly attack palm oil plants?",
            "Bagaimana panen sawit yang efektif?": "How to harvest palm oil effectively?"
        },
        ("en", "id"): {
            "Why are my palm leaves yellow?": "Kenapa daun sawit saya kuning?",
            "What's a good way to fertilize palm oil trees?": "Bagaimana cara pupuk sawit yang bagus?",
            "What pests commonly attack palm oil plants?": "Apa hama yang sering menyerang sawit?",
            "How to harvest palm oil effectively?": "Bagaimana panen sawit yang efektif?"
        }
    }

    trans_dict = translations.get((from_lang, to_lang), {})

    if text.strip() in trans_dict:
        return trans_dict[text.strip()]

    try:
        target_language = "English" if to_lang == "en" else "Indonesian"
        source_language = "Indonesian" if from_lang == "id" else "English"

        translation_prompt = f"""Translate the following text from {source_language} to {target_language}.
        This is about palm oil farming. Provide only the translation, no explanations:

        Text to translate: {text}

        Translation:"""

        response = client.chat_completion(
            model="meta-llama/Llama-3.2-3B-Instruct",
            messages=[{"role": "user", "content": translation_prompt}],
            temperature=0.3,
            max_tokens=300,
            top_p=0.9
        )

        translated_text = response.choices[0].message.content.strip()

        if "Translation:" in translated_text:
            translated_text = translated_text.split("Translation:")[-1].strip()
        if translated_text.startswith('"') and translated_text.endswith('"'):
            translated_text = translated_text[1:-1]

        return translated_text

    except Exception as e:
        translated_text = text
        sorted_translations = sorted(trans_dict.items(), key=lambda x: len(x[0]), reverse=True)

        for original, translation in sorted_translations:
            if original.lower() in translated_text.lower():
                import re
                pattern = re.compile(re.escape(original), re.IGNORECASE)
                translated_text = pattern.sub(translation, translated_text)

        return translated_text

# --- Language Selection ---
if "language" not in st.session_state:
    st.session_state.language = "id"

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
        "error": "Maaf, PalmPal mengalami gangguan.",
        "lang_toggle": "🌐 Switch to English",
        "recommendations": "Rekomendasi Produk",
        "fetch_recommendations": "Dapatkan Rekomendasi Produk",
        "similar_products": "Produk Serupa",
        "fetch_similar_products": "Dapatkan Produk Serupa",
        "loading": "Memuat...",
        "no_products": "Tidak ada produk yang ditemukan"
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
        "error": "Sorry, PalmPal encountered an error.",
        "lang_toggle": "🌐 Ganti ke Bahasa Indonesia",
        "recommendations": "Product Recommendations",
        "fetch_recommendations": "Get Product Recommendations",
        "similar_products": "Similar Products",
        "fetch_similar_products": "Get Similar Products",
        "loading": "Loading...",
        "no_products": "No products found"
    }
}
lang = st.session_state.language
t = TEXT[lang]

# --- Restored Language Toggle Button with AI Translation Feature ---
st.markdown('<div class="lang-toggle">', unsafe_allow_html=True)
lang_toggle = st.button(t["lang_toggle"])
if lang_toggle:
    old_lang = st.session_state.language
    new_lang = "en" if st.session_state.language == "id" else "id"

    if 'messages' in st.session_state and st.session_state.messages:
        with st.spinner("Translating messages..." if new_lang == "en" else "Menerjemahkan pesan..."):
            translated_messages = []
            for message in st.session_state.messages:
                original_content = message["content"]
                translated_content = translate_content(original_content, old_lang, new_lang)
                translated_messages.append({
                    "role": message["role"],
                    "content": translated_content
                })

            st.session_state.messages = translated_messages

    st.session_state.language = new_lang
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# --- Only use one st.image with smaller dimensions ---
st.image("https://static.wixstatic.com/media/759737_bb3e5ad0e411479782bdaca6f4fa3bda~mv2.png/v1/fit/w_2500,h_1330,al_c/759737_bb3e5ad0e411479782bdaca6f4fa3bda~mv2.png", width=120)
st.markdown(f"## {t['title']}")
st.markdown(t['subtitle'])

# --- Session State Initialization ---
if 'messages' not in st.session_state:
    st.session_state.messages = []
    
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None
    
if 'similar_products' not in st.session_state:
    st.session_state.similar_products = {}

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

# --- Fetch Recommendations from API ---
def fetch_recommendations():
    api_url = "https://icp-t02-grp4-api.onrender.com/api/v1/ecommerce/recommendation/user/13f5223e-f04a-4fa8-9ef2-cf36060f0d6d"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        recommendations = response.json()
        st.session_state.recommendations = recommendations.get("items", [])
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching recommendations: {e}")
        st.session_state.recommendations = None

# --- Fetch Similar Products from API ---
def fetch_similar_products(product_id):
    if product_id in st.session_state.similar_products:
        return st.session_state.similar_products[product_id]
    
    api_url = f"https://icp-t02-grp4-api.onrender.com/api/v1/ecommerce/recommendations/products/{product_id}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        similar_products = response.json()
        products = similar_products.get("items", [])
        st.session_state.similar_products[product_id] = products
        return products
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching similar products: {e}")
        return None

# --- Display Chat Bubbles ---
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

# --- Button to Fetch Recommendations ---
if st.button(t["fetch_recommendations"]):
    with st.spinner(t["loading"]):
        fetch_recommendations()

# --- Display Recommendations ---
if st.session_state.recommendations:
    st.markdown(f"""
    <div class="recommendation-section">
        <div class="recommendation-title">{t["recommendations"]}</div>
    </div>
    """, unsafe_allow_html=True)
    
    for item in st.session_state.recommendations:
        product_id = item['product_id']
        product_name = item['product_name_en'] if lang == "en" else item.get('product_name_id', item['product_name_en'])
        
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"""
            <div class="product-card">
                <div class="product-name">{product_name}</div>
                <div class="product-price">IDR {item['price']:,}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if st.button(t["fetch_similar_products"], key=f"similar_{product_id}"):
                with st.spinner(t["loading"]):
                    similar_products = fetch_similar_products(product_id)
                    
                    if similar_products:
                        st.markdown(f"""
                        <div class="recommendation-section">
                            <div class="recommendation-title">{t["similar_products"]} ({product_name})</div>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        for similar_item in similar_products:
                            similar_name = similar_item['product_name_en'] if lang == "en" else similar_item.get('product_name_id', similar_item['product_name_en'])
                            st.markdown(f"""
                            <div class="product-card">
                                <div class="product-name">{similar_name}</div>
                                <div class="product-price">IDR {similar_item['price']:,}</div>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        st.warning(t["no_products"])

# --- User Input ---
def process_user_input():
    if st.session_state.user_input:
        user_message = st.session_state.user_input
        st.session_state.messages.append({"role": "user", "content": user_message})
        bot_response = generate_response(user_message)
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.session_state.user_input = ""

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
        st.session_state.recommendations = None
        st.session_state.similar_products = {}
        st.rerun()
    st.markdown(t["model_info"])

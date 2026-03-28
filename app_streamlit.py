import streamlit as st
import tempfile

# Assuming these are your local modules
from pdf_loader import load_pdf
from chunking import chunk_text
from embeddings import embed_chunks, model
from vector_store import create_index
from retriever import search
from llm import ask_llm

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Research Paper Assistant",
    page_icon="📄",
    layout="wide"
)

# -------------------------
# BACKGROUND IMAGE URL
# -------------------------
bg_image = "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=1950&q=80"

# -------------------------
# CSS FIX (BRIGHT INPUTS + WALLPAPER)
# -------------------------
st.markdown(f"""
<style>

/* 1. APPLY BACKGROUND TO THE ENTIRE APP */
.stApp {{
    background-image: url("{bg_image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* 2. REMOVE STREAMLIT'S DEFAULT WHITE OVERLAYS */
[data-testid="stAppViewContainer"] {{
    background-color: transparent !important;
}}

[data-testid="stHeader"] {{
    background-color: rgba(0,0,0,0) !important;
}}

/* 3. SEMI-TRANSPARENT OVERLAY FOR DEPTH */
.stApp::before {{
    content: "";
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0, 0, 0, 0.2); 
    z-index: -1;
}}

/* 4. MAIN CONTENT BOX */
.block-container {{
    max-width: 1000px !important;
    padding: 3rem !important;
    background: rgba(255, 255, 255, 0.98); 
    border-radius: 24px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    margin-top: 50px;
    margin-bottom: 50px;
}}

/* 5. FIX THE "BLACK BOX" IN INPUT FIELDS */
.stTextInput>div>div>input {{
    background-color: white !important;
    color: #111 !important;
    border: 1px solid #ddd !important;
    border-radius: 10px !important;
    padding: 12px !important;
}}

/* 6. FIX THE "BLACK BOX" IN UPLOADER & BUTTONS */
[data-testid="stFileUploader"] section {{
    background-color: #ffffff !important;
    border: 2px dashed #0b5ed7 !important;
    border-radius: 12px !important;
}}

[data-testid="stFileUploader"] button {{
    background-color: #0b5ed7 !important;
    color: white !important;
    border: none !important;
    opacity: 1 !important;
}}

/* Fix text colors inside the uploader */
[data-testid="stFileUploader"] label, 
[data-testid="stFileUploader"] div, 
[data-testid="stFileUploader"] small {{
    color: #222 !important;
}}

/* 7. BUTTON STYLING */
.stButton>button {{
    background-color: #0b5ed7 !important;
    color: white !important;
    font-weight: bold;
    border-radius: 10px;
    width: 100%;
    border: none;
    padding: 10px;
    transition: 0.3s;
}}

.stButton>button:hover {{
    background-color: #084298 !important;
    color: white !important;
}}

/* 8. TYPOGRAPHY */
h1, h2, h3 {{
    color: #0b5ed7 !important;
    text-align: center;
}}

p, label, span {{
    color: #111 !important;
}}

</style>
""", unsafe_allow_html=True)

# -------------------------
# APP CONTENT
# -------------------------

# Header
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=120)

st.markdown("<h1>🤖 Research Paper Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Analyze your PDFs with AI-powered retrieval.</p>", unsafe_allow_html=True)

# Session State
if "index" not in st.session_state:
    st.session_state.index, st.session_state.chunks, st.session_state.ready = None, None, False

# Sidebar
st.sidebar.title("⚙️ Workflow")
st.sidebar.info("Upload your document, click process, and ask questions.")

# Upload Section
st.markdown("### 📤 Step 1: Upload Paper")
uploaded_file = st.file_uploader("Choose a research paper (PDF)", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    if st.button("⚙️ Process Document"):
        with st.status("Reading & Indexing...", expanded=True) as status:
            text = load_pdf(pdf_path)
            chunks = chunk_text(text)
            embeddings = embed_chunks(chunks)
            index = create_index(embeddings)
            
            st.session_state.index = index
            st.session_state.chunks = chunks
            st.session_state.ready = True
            status.update(label="Ready!", state="complete", expanded=False)

# Question Section
st.markdown("---")
st.markdown("### 💬 Step 2: Ask Questions")
# Text Input (The "Black Box" fix is in the CSS section #5)
question = st.text_input("What would you like to know?")

if st.button("🚀 Ask AI"):
    if not st.session_state.ready:
        st.error("Please process a document first!")
    elif question:
        with st.spinner("Analyzing paper..."):
            retrieved = search(question, model, st.session_state.index, st.session_state.chunks)
            context = "\n".join(retrieved)
            answer = ask_llm(context, question)

            st.markdown("#### 📌 Answer")
            st.info(answer)
            
            with st.expander("Show retrieved context"):
                st.write(context)
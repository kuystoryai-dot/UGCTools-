import streamlit as st
import google.generativeai as genai

# 1. Konfigurasi Tampilan (Dark Mode Style)
st.set_page_config(page_title="UGC PROMPT FINDER", page_icon="✨", layout="wide")

# Custom CSS biar tampilannya mirip aplikasi premium
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #4F46E5; color: white; }
    .stTextInput>div>div>input { background-color: #1f2937; color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Setup API (Masukkan API Key Gratisan Lu di Sini)
# Ambil di: aistudio.google.com
API_KEY = "AIzaSyDObUlzZU4IxP0CTjZIkut1qiZslRoJgnk"
genai.configure(api_key=API_KEY)
model =genai.GenerativeModel('gemini-1.5-flash'). # Model Nano Banana

# 3. Sidebar Menu
st.sidebar.title("🛠️ UGC Tool Menu")
pilihan = st.sidebar.radio("Mau buat apa hari ini?", 
    ["Script Video Viral", "Generate Foto Produk (UGC)", "Ide Konten 30 Hari"])

# 4. Fitur 1: Script Generator (Review Jujur ala Nexabot)
if pilihan == "Script Video Viral":
    st.header("📝 Script Video Viral Generator")
    st.write("Buat skrip review jujur yang bikin orang betah nonton.")
    
    nama_produk = st.text_input("Apa nama produknya?", placeholder="Contoh: Skincare Serum Brightening")
    target = st.selectbox("Gaya Bahasa", ["Gaul/Skena", "Formal/Edukasi", "Ibu-ibu Friendly"])
    
    if st.button("Generate Script"):
        with st.spinner('Lagi mikir bentar...'):
            prompt = f"Buat skrip video TikTok/Reels untuk produk {nama_produk}. Gaya bahasa {target}. Harus ada Hook di awal, isi yang jujur, dan ajakan klik keranjang kuning."
            response = model.generate_content(prompt) # Menggunakan Gemini Flash
            st.success("Selesai! Ini skrip lu:")
            st.write(response.text)

# 5. Fitur 2: Generate Foto Produk (UGC Visual)
elif pilihan == "Generate Foto Produk (UGC)":
    st.header("📸 Foto Produk UGC Creator")
    st.write("Bikin foto produk estetik meskipun lu gak punya barangnya.")
    
    deskripsi = st.text_input("Deskripsi Foto", placeholder="Contoh: Botol parfum di meja kayu dengan sinar matahari")
    
    if st.button("Proses Foto"):
        with st.spinner('Lagi gambar pake AI...'):
            # Prompt rahasia biar hasilnya photorealistic
            prompt_foto = f"Create a photorealistic UGC style photography of {deskripsi}. Aesthetic room background, natural lighting, high resolution, looks like taken by smartphone."
            # Catatan: Jatah 500 foto/hari
            response = model.generate_content(prompt_foto) 
            st.info("Gambar sedang diproses... (Tampilan gambar akan muncul di sini)")
            # Logika penampilan gambar akan muncul sesuai integrasi API Imagen lu

# 6. Fitur 3: Ide Konten 30 Hari
elif pilihan == "Ide Konten 30 Hari":
    st.header("📅 Kalender Konten Affiliate")
    produk_ide = st.text_input("Produk untuk 30 hari:", placeholder="Contoh: Powerbank")
    
    if st.button("Buat Jadwal"):
        prompt_ide = f"Buat daftar 30 ide konten video pendek untuk mempromosikan {produk_ide} selama sebulan. Variasikan antara edukasi, komedi, dan unboxing."
        response = model.generate_content(prompt_ide)
        st.write(response.text)

st.divider()
st.caption("Powered by Gemini 3 Flash - Jatah 500 Request Gratis/Hari")

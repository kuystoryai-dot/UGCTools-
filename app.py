import streamlit as st
import google.generativeai as genai
from PIL import Image

# Konfigurasi API
genai.configure(AIzaSyDObUlzZU4IxP0CTjZIkut1qiZslRoJgnk") # Pastikan API Key lu tetap aman

st.set_page_config(page_title="UGC PRO AI - Photo & Script", layout="centered")

st.title("🚀 UGC PRO AI: Photo & Script")
st.subheader("Bikin Konten Viral dari Teks atau Foto")

# Sidebar untuk Pengaturan
with st.sidebar:
    st.header("Pengaturan")
    gaya_bahasa = st.selectbox("Gaya Bahasa", ["Gaul/Skena", "Professional", "Hard Selling", "Storytelling"])
    model_ai = st.selectbox("Model AI", ["gemini-1.5-flash"])

# Input Teks
nama_produk = st.text_input("Apa nama produknya?", placeholder="Misal: Serum Brightening")

# Input Gambar (Fitur Baru!)
uploaded_file = st.file_uploader("Atau Upload Foto Produk (Opsional)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Foto Produk Berhasil Diunggah", use_container_width=True)

if st.button("Generate Script Viral"):
    if not nama_produk and uploaded_file is None:
        st.warning("Isi nama produk atau upload foto dulu ya, Bro!")
    else:
        with st.spinner("AI lagi mikir keras..."):
            model = genai.GenerativeModel(model_ai)
            
            prompt = f"Buatkan 3 ide skrip video TikTok viral untuk produk {nama_produk}. Gaya bahasa: {gaya_bahasa}. Buat yang hook-nya kuat dan bikin orang mau beli."
            
            if uploaded_file is not None:
                # Jika ada gambar, AI akan menganalisis gambarnya
                response = model.generate_content([prompt, image])
            else:
                # Jika hanya teks
                response = model.generate_content(prompt)
                
            st.success("Ini Ide Skrip Buat Lu:")
            st.write(response.text)

st.divider()
st.caption("UGC Tool by KuyStory AI - Powered by Gemini 1.5 Flash")

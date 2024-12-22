# 🧠 Brain Tumor Classifier

**Klasifikasi Tumor Otak dalam Sekejap!**  
Proyek ini adalah aplikasi web berbasis Flask yang memanfaatkan kekuatan AI untuk menganalisis gambar MRI otak. Dalam hitungan detik, aplikasi ini dapat mengenali jenis tumor otak, membantu para profesional medis mengambil keputusan lebih cepat.

---

## ✨ **Fitur Utama**
- 🔍 **Identifikasi Tumor**: Prediksi jenis tumor otak dengan akurasi tinggi (Meningioma, Glioma, atau Pituitari).  
- 📂 **Unggah Gambar**: Cukup unggah gambar MRI Anda dan biarkan AI bekerja.  
- ⚡ **Cepat & Akurat**: Hasil dalam hitungan detik dengan tingkat akurasi 92%.  

---

### 🚀 **Langkah Instalasi**
Ikuti langkah mudah ini untuk menjalankan aplikasi di komputer Anda:

1. Clone Repository
   ```bash
   git clone https://github.com/rubygurlexe/TUMOR-BRAIN-CLASSIFICATION.git
   TUMOR-BRAIN-CLASSIFICATION
2. Buat Virtual Environment
   ```bash
   # Untuk Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   # Untuk Windows
   python -m venv venv
   venv\Scripts\activate
3. Instal Dependencies
   ```bash
   pip install -r requirements.txt
4. Jalankan Aplikasi
   ```bash
   python app.py

## 📚 Tentang Model
Model deep learning kami menggunakan Convolutional Neural Network (CNN) untuk memproses gambar MRI otak:

- Input: Gambar MRI ukuran 150x150 piksel.
- Output: Probabilitas dari tiga jenis tumor:
  a. Meningioma
  b. Glioma
  c. Pituitari

## 🧪 Performansi Model
Akurasi: 92%
F1-Score: 0.90

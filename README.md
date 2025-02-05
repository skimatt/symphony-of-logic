# Simfoni Logika: Visualisasi Pengurutan Musikal 🎵 📊

Visualisasi interaktif yang indah dari algoritma pengurutan yang diiringi dengan suara piano. Saksikan dan dengarkan saat algoritma mengurutkan data sambil menciptakan melodi musikal berdasarkan elemen yang dibandingkan.

## 🌟 Fitur Utama

- **Umpan Balik Musikal**: 
  - Setiap perbandingan menghasilkan nada piano
  - Menciptakan melodi unik selama proses pengurutan
  - Arpeggio kemenangan saat selesai
- **Visualisasi Memukau**: 
  - Gradien warna yang elegan
  - Animasi yang halus
  - Efek pencahayaan dinamis
  - Tampilan resolusi tinggi
- **Kontrol Interaktif**:
  - Tekan spasi untuk memulai pengurutan
  - Tekan R untuk mengacak ulang data
- **Suara Piano yang Ditingkatkan**:
  - Amplop ADSR untuk nada piano realistis
  - Sintesis suara kaya harmonik
  - Arpeggio perayaan saat pengurutan selesai

## 🛠️ Prasyarat

- Python 3.7 atau lebih tinggi
- Pygame
- NumPy

## 📦 Instalasi

1. Klon repositori ini:
```bash
git clone https://github.com/nama-pengguna-anda/simfoni-logika.git
cd simfoni-logika
```

2. Buat dan aktifkan lingkungan virtual (opsional tapi direkomendasikan):
```bash
python -m venv venv
source venv/bin/activate  # Di Windows: venv\Scripts\activate
```

3. Pasang paket yang diperlukan:
```bash
pip install pygame numpy
```

## 🎮 Cara Penggunaan

Jalankan program:
```bash
python visualisasi_pengurutan.py
```

### Kontrol:
- **Spasi**: Mulai visualisasi pengurutan
- **R**: Atur ulang/Acak data
- **Tutup Jendela**: Keluar program

## 🎨 Kustomisasi

Anda dapat memodifikasi berbagai parameter dalam kode untuk menyesuaikan visualisasi:

- `WIDTH, HEIGHT`: Dimensi layar
- `N`: Jumlah elemen yang akan diurutkan
- `PIANO_NOTES`: Frekuensi untuk nada musik
- Skema warna:
  - `BACKGROUND`: Warna latar
  - `GRADIENT_TOP`: Warna gradien atas
  - `GRADIENT_BOTTOM`: Warna gradien bawah
  - `HIGHLIGHT`: Warna sorotan

## 🤝 Kontribusi

Kontribusi sangat diterima! Berikut beberapa cara Anda dapat berkontribusi:

1. Menambahkan algoritma pengurutan baru
2. Meningkatkan efek visual
3. Menyempurnakan sintesis suara
4. Menambahkan fitur baru
5. Memperbaiki bug

Silakan kirim issues dan pull requests.


## 🙏 Ucapan Terima Kasih

- Terinspirasi dari proyek-proyek visualisasi pengurutan
- Sintesis suara piano berdasarkan prinsip amplop ADSR
- Dibangun dengan Pygame dan NumPy


Jika Anda memiliki pertanyaan atau saran, silakan buka issue di repositori GitHub.


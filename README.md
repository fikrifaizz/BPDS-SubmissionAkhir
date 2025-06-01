# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Selama lebih dari dua dekade, institusi ini telah mencetak banyak lulusan berkualitas dan memiliki reputasi yang baik di masyarakat. Namun, di balik pencapaian tersebut, terdapat permasalahan serius yang tengah dihadapi, yaitu tingginya angka mahasiswa yang tidak menyelesaikan studinya atau dropout.

Fenomena dropout tidak hanya merugikan mahasiswa secara pribadi, tetapi juga berdampak langsung terhadap reputasi institusi, efisiensi penggunaan sumber daya, dan keberlanjutan program akademik. Semakin banyak mahasiswa yang keluar sebelum lulus, semakin besar pula potensi kerugian finansial dan sosial bagi pihak kampus.

Melihat kondisi tersebut, manajemen Jaya Jaya Institut memandang perlu adanya solusi yang bersifat preventif. Salah satunya adalah dengan membangun sistem berbasis data yang mampu memprediksi risiko dropout mahasiswa sejak dini, sehingga pihak kampus dapat mengambil langkah-langkah intervensi seperti pemberian bimbingan akademik, bantuan finansial, atau konsultasi psikologis sebelum mahasiswa benar-benar keluar dari sistem pendidikan.

Dengan memanfaatkan pendekatan data science, diharapkan institusi mampu tidak hanya memahami pola dropout yang terjadi, tetapi juga meresponsnya secara proaktif untuk meningkatkan kualitas layanan pendidikan secara keseluruhan.

### Permasalahan Bisnis
1. Tingkat dropout mahasiswa yang masih tinggi (32.12%)
2. Mahasiswa dengan nilai rendah cenderung mengalami dropout
3. Banyak mahasiswa dropout tidak menerima beasiswa
4. Tidak adanya sistem peringatan dini berdasarkan indikator risiko

### Cakupan Proyek
Proyek ini bertujuan untuk membangun sistem prediksi dropout mahasiswa dengan pendekatan data science. Proyek terdiri dari tahapan-tahapan sebagai berikut:

1. Persiapan
  - Mengimpor library yang diperlukan seperti `pandas`, `numpy`, `seaborn`, `matplotlib`, `sklearn`, dan `joblib`.
  - Mengambil dan memuat dataset mahasiswa dari sumber terpercaya (UCI Machine Learning Repository).

2. Data Understanding
  - Menjelaskan struktur dan deskripsi tiap fitur (variabel) dalam dataset.
  - Melakukan analisis deskriptif (univariate dan multivariate).
  - Menampilkan distribusi dan hubungan antar variabel terhadap `Status` (Dropout, Graduate, Enrolled).
  - Menilai outliers, distribusi usia, status beasiswa, nilai, beban studi, dan faktor administratif (pembayaran dan utang).

3. Data Preparation / Preprocessing
  - Melakukan label encoding pada fitur kategorikal.
  - Membagi dataset menjadi data latih dan data uji.
  - Menstandarkan fitur numerik menggunakan `StandardScaler`.

4. Modeling
  - Melatih model machine learning (Random Forest) dengan data yang telah diproses.
  - Menyimpan model dan scaler ke dalam file `.pkl` menggunakan `joblib`.

5. Evaluation
  - Mengukur performa model menggunakan metrik akurasi, precision, recall, dan confusion matrix.
  - Menilai kemampuan model dalam memprediksi mahasiswa yang berisiko dropout secara tepat.

6. Deployment (Streamlit)
  - Membangun aplikasi berbasis web menggunakan **Streamlit**.
  - Aplikasi mampu menerima input fitur mahasiswa dan memberikan output prediksi status.
  - Model dan scaler dimuat ulang melalui `joblib` dan diintegrasikan dengan antarmuka pengguna.

7. Visualisasi Data dan Monitoring
   - Pembuatan dashboard interaktif untuk monitoring status mahasiswa.
   - Visualisasi indikator penting seperti nilai, usia pendaftaran, status beasiswa, dan pembayaran.

### Persiapan
#### Sumber Data
Dataset yang digunakan dalam proyek ini berasal dari [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success), dengan judul **"Predict Students Dropout and Academic Success"**. Dataset ini berisi informasi terkait:

- Data demografis mahasiswa (jenis kelamin, usia, status pernikahan)
- Data akademik (nilai masuk, jumlah mata kuliah, hasil evaluasi)
- Informasi administratif (status pembayaran, beasiswa, status utang)
- Label target berupa status akhir mahasiswa: `Graduate`, `Dropout`, atau `Enrolled`

Dataset digunakan dalam format `.csv` dan dimuat langsung menggunakan pustaka `pandas`.

#### Setup environment - Metabase:

1. Install Docker
2. Jalankan perintah berikut pada Terminal/Command Prompt/PowerShell guna memanggil (pull) Docker image untuk menjalankan Metabase. 

    ```docker pull metabase/metabase:v0.46.4```
3. Apabila proses pembuatan docker image telah selesai, Anda dapat menjalankan image tersebut menggunakan perintah berikut.

    ```docker run -p 3000:3000 --name metabase metabase/metabase```
4. Jalankan Metabase di lokal server dengan tautan berikut.

    ```http://localhost:3000/setup```
5. Setelah melakukan setup metabase, langkah selanjutnya adalah menambahkan data dan pada kasus ini menggunakan PostgreSQL.
6. Selesai

#### Setup environment - Python dengan Virtualenv

1. Membuat virtual environment

    ```python -m venv venv```
2. Mengaktifkan virtual environment

    - Untuk Windows
        ```venv\Scripts\activate```        

    - Untuk MacOS/Linux
        ```source venv/bin/activate```
3. Menginstall dependencies

    ```pip install -r requirements.txt```

## Business Dashboard

<img src="https://github.com/user-attachments/assets/8954f71d-f575-452b-8bb1-a59cec0375bd" alt="Dashboard" title="Dashboard">

Sebagai bagian dari proyek analisis dropout mahasiswa di Jaya Jaya Institut, telah dibangun sebuah **dashboard interaktif** menggunakan **Metabase**. Dashboard ini berfungsi sebagai alat monitoring yang memvisualisasikan tren dan indikator utama penyebab dropout berdasarkan data historis mahasiswa.

---

### Tujuan Dashboard
Dashboard ini dibuat untuk membantu:
- Manajemen kampus dalam **mengidentifikasi pola dropout**
- Staf akademik dan keuangan untuk **menemukan kelompok mahasiswa berisiko tinggi**
- Memberikan **bukti visual berbasis data** sebagai dasar intervensi pendidikan

---

### Komponen-Komponen Visual dalam Dashboard

1. **Ringkasan Angka Kunci**:
   - Total persentase dropout: **32.12%**
   - Jumlah mahasiswa Dropout: **1.421**
   - Jumlah mahasiswa Graduate: **2.209**
   - Jumlah mahasiswa Enrolled (aktif): **794**

2. **Distribusi Nilai dan Akademik**:
   - Rata-rata nilai masuk (`Admission Grade`) menurut status
   - Rata-rata jumlah mata kuliah yang diambil per status
   - Perbandingan rata-rata nilai semester 1 dan semester 2

3. **Demografi Mahasiswa**:
   - Distribusi usia saat mendaftar
   - Perbandingan status terhadap jenis kelamin dan status pernikahan (dapat difilter)

4. **Faktor Sosial Ekonomi**:
   - Pengaruh beasiswa terhadap dropout: mahasiswa tanpa beasiswa cenderung lebih banyak dropout
   - Status debitur: mahasiswa dengan utang lebih berisiko dropout
   - Status pembayaran kuliah: mahasiswa yang belum membayar lebih rentan dropout

---

### Link Akses Dashboard

**🔗 [Akses Dashboard Publik Monitoring Dropout Mahasiswa](http://localhost:3000/public/dashboard/538ad8aa-36a2-426a-b06a-cebf6fead3a5)**  

Untuk mengakses dashboard Metabase, gunakan kredensial berikut:
- Email: root@mail.com
- Password: root123

---

### Manfaat Bisnis
Dashboard ini memungkinkan pimpinan dan staf kampus untuk:
- Melakukan **deteksi dini** terhadap pola dropout
- Menganalisis **hubungan antar variabel** (nilai, keuangan, akademik)
- Mengambil **kebijakan berbasis data** untuk meningkatkan tingkat kelulusan dan efisiensi program

## Menjalankan Sistem Machine Learning

Sebagai bagian dari implementasi solusi, telah dikembangkan sebuah **prototype sistem prediksi dropout mahasiswa** berbasis machine learning menggunakan framework **Streamlit**. Sistem ini memungkinkan pengguna untuk menginput data mahasiswa secara manual dan memperoleh prediksi status akademik secara real-time.

---

### 🛠️ Cara Menjalankan Prototype

Sistem ini dapat dijalankan dengan dua cara:

#### 1. Melalui Hosting Online (Direkomendasikan)
Prototype telah dideploy ke **Streamlit Community Cloud** dan dapat diakses melalui link berikut:

🔗 **[Akses Sistem Prediksi Dropout Mahasiswa](https://bpds-submissionakhir-kjglnfkhntcnucex5vcxmk.streamlit.app/)**

#### 2. Menjalankan Secara Lokal (Opsional)
Jika ingin menjalankan sistem secara lokal:

1. Pastikan telah menginstal semua dependensi:
   
   ```pip install streamlit pandas numpy scikit-learn joblib```
2. Letakkan file berikut dalam satu direktori:
   - app.py (file Streamlit utama)
   - rf.pkl (model machine learning Random Forest)
   - scaler.pkl (standarisasi fitur numerik)
3. Jalankan dengan perintah:

   ```streamlit run app.py```
   

## Conclusion

Proyek ini berhasil membangun sebuah sistem prediksi dan monitoring dropout mahasiswa berbasis data science yang dapat membantu Jaya Jaya Institut dalam memahami dan mengatasi permasalahan tingginya angka mahasiswa yang tidak menyelesaikan studi.

Beberapa poin utama yang dapat disimpulkan dari proyek ini adalah:

1. **Analisis data historis mahasiswa menunjukkan pola dropout yang dapat dikenali**  
   Mahasiswa dengan nilai akademik rendah, keterlambatan pembayaran, tidak menerima beasiswa, serta mengambil sedikit mata kuliah di awal perkuliahan, cenderung memiliki risiko dropout lebih tinggi.

2. **Model machine learning mampu memprediksi status mahasiswa secara cukup akurat**  
   Dengan menggunakan algoritma Random Forest, sistem berhasil melakukan klasifikasi terhadap status mahasiswa (`Dropout`, `Graduate`, `Enrolled`) berdasarkan data input.

3. **Dashboard monitoring mendukung pengambilan keputusan strategis**  
   Dashboard interaktif yang dibangun dengan Metabase memungkinkan pihak manajemen untuk mengawasi tren dropout secara visual dan mendalam, serta melakukan segmentasi berdasarkan variabel kunci seperti usia, gender, dan status keuangan.

4. **Prototype sistem prediksi telah berhasil diimplementasikan secara online**  
   Aplikasi berbasis Streamlit yang dikembangkan dapat diakses oleh pengguna untuk melakukan prediksi status mahasiswa secara real-time, sehingga bermanfaat dalam proses bimbingan atau evaluasi akademik.

---

### Kesimpulan Akhir

Dengan adanya integrasi antara **analisis data**, **model machine learning**, dan **sistem visualisasi**, institusi kini memiliki alat yang dapat dimanfaatkan untuk **deteksi dini risiko dropout** dan **pengambilan keputusan berbasis data**. Proyek ini diharapkan dapat menjadi fondasi awal bagi pengembangan sistem manajemen pendidikan yang lebih adaptif dan responsif terhadap permasalahan akademik mahasiswa.

## Rekomendasi Action Items
Berdasarkan hasil analisis data, model prediksi machine learning, dan visualisasi dashboard yang telah dibangun, berikut adalah rekomendasi **action items** yang dapat dilakukan oleh Jaya Jaya Institut untuk mengurangi angka dropout dan meningkatkan tingkat kelulusan mahasiswa:


1. Implementasi Sistem Deteksi Dini Dropout
   - Gunakan prototype sistem prediksi untuk **menilai status risiko mahasiswa baru dan aktif** secara berkala.
   - Integrasikan sistem ini dengan data akademik kampus agar dapat dipantau secara real-time oleh tim akademik.

2. Penguatan Program Beasiswa Terarah
   - Berdasarkan data, mahasiswa yang **tidak menerima beasiswa** lebih berisiko dropout.
   - Rekomendasi: alokasikan dana beasiswa secara lebih strategis kepada mahasiswa dengan risiko tinggi berdasarkan prediksi model.

3. Bimbingan Akademik Khusus untuk Mahasiswa Berisiko
   - Buat program pendampingan akademik khusus untuk mahasiswa dengan:
     - Nilai semester awal rendah
     - Jumlah mata kuliah yang diambil sangat sedikit
     - Riwayat evaluasi buruk

4. Pendampingan Keuangan Mahasiswa
   - Mahasiswa dengan status **belum membayar** atau **berutang** menunjukkan tren dropout yang tinggi.
   - Rekomendasi:
     - Buat program pengingat dan mediasi pembayaran
     - Tawarkan skema cicilan, bantuan sosial, atau moratorium pembayaran bagi yang kesulitan

5. Optimalisasi Dashboard sebagai Alat Monitoring Rutin
   - Gunakan dashboard Metabase sebagai bagian dari **rapat evaluasi bulanan** akademik dan keuangan.
   - Tambahkan filter dinamis seperti jurusan, angkatan, dan dosen pembimbing untuk **analisis lebih dalam per kelompok**.

6. Kolaborasi Antarbagian
   - Koordinasikan penggunaan sistem prediksi antara:
     - Bagian akademik (bimbingan)
     - Bagian keuangan (pemantauan pembayaran)
     - BEM dan konselor kampus (dukungan sosial)

Dengan melaksanakan action items di atas secara terintegrasi dan berkelanjutan, Jaya Jaya Institut akan lebih siap dalam mengelola risiko dropout, meningkatkan efisiensi operasional, serta memperkuat reputasi institusi sebagai perguruan tinggi yang peduli terhadap keberhasilan mahasiswanya.

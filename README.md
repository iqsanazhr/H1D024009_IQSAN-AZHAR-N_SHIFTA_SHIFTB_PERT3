# Laporan Praktikum Kecerdasan Buatan - Pertemuan 3

## Logika Fuzzy Metode Mamdani

### PRAKTIKUM

- **Materi Praktikum:** Logika Fuzzy Dua
- **Metode:** Mamdani
- **Tujuan:** Menyelesaikan Studi Kasus Menggunakan Logika Fuzzy

---

### STUDI KASUS SATU: UDIN PET SHOP

Studi kasus ini bertujuan untuk mengoptimalkan persediaan stok makanan hewan peliharaan.

#### Variabel Input

1. **Barang Terjual:** 0 - 100 unit
2. **Permintaan:** 0 - 300 unit
3. **Harga Per Item:** 0 - 100.000 rupiah
4. **Profit:** 0 - 4.000.000 rupiah

#### Variabel Output

- **Stok Makanan:** 0 - 1.000 unit

#### Hasil Perhitungan

- **Input:**
  - Barang Terjual: 80 unit
  - Permintaan: 255 unit
  - Harga Per Item: 25.000 rupiah
  - Profit: 3.500.000 rupiah
- **Hasil Akhir Stok Makanan:** 834,62 unit

![Visualisasi Hasil Kasus 1](visualisasi%20grafik/stok_petshop_result.png)

**Penjelasan Grafik:**
Grafik di atas menunjukkan fungsi keanggotaan untuk variabel output **Stok Makanan** yang terdiri dari kategori 'sedang' dan 'banyak'. Garis vertikal tebal pada nilai **834.62** merupakan hasil dari proses defuzzifikasi menggunakan metode *Centroid*. Hasil ini merepresentasikan nilai tegas (crisp) dari stok makanan yang harus disediakan berdasarkan kombinasi input barang terjual, permintaan, harga, dan profit yang telah dimasukkan.


**Output Terminal:**
```text
Hasil Perhitungan Stok Makanan: 834.62
Grafik visualisasi output disimpan sebagai: stok_petshop_result.png
```

---

### STUDI KASUS DUA: PELAYANAN MASYARAKAT KOTA SEJAHTERA

Studi kasus ini bertujuan untuk menentukan tingkat kepuasan layanan pengaduan masyarakat.

#### Variabel Input

1. **Kejelasan Informasi:** 0 - 100
2. **Kejelasan Persyaratan:** 0 - 100
3. **Kemampuan Petugas:** 0 - 100
4. **Ketersediaan Sarana dan Prasarana:** 0 - 100

#### Variabel Output

- **Kepuasan Pelayanan:** 0 - 400

#### Analisis Implementasi

- **Input yang diuji:**
  - Kejelasan Informasi: 80
  - Kejelasan Persyaratan: 60
  - Kemampuan Petugas: 50
  - Ketersediaan Sarpras: 90
- **Hasil Perhitungan:**
  Sistem kini menggunakan 81 aturan secara komprehensif dari data CSV. Dengan input yang diberikan, aturan-aturan terkait berhasil terpicu dan memproses logika fuzzy untuk memberikan hasil tingkat kepuasan pelayanan sebesar **237,14**. Angka ini masuk ke dalam kategori "Cukup".

![Visualisasi Hasil Kasus 2](visualisasi%20grafik/pelayanan_result.png)

**Penjelasan Grafik:**
Grafik di atas menunjukkan fungsi keanggotaan untuk variabel output **Kepuasan Pelayanan**. Garis vertikal hitam tegas menunjukkan letak nilai hasil perhitungan akhir dari defuzzifikasi menggunakan metode *Centroid* di nilai **237,14**.

**Output Terminal:**
```text
Berhasil memuat 81 aturan dari CSV.
Hasil Perhitungan Tingkat Kepuasan Pelayanan: 237.14
Grafik hasil visualisasi output disimpan: visualisasi grafik\pelayanan_result.png
```

---

### KESIMPULAN

Implementasi Logika Fuzzy Mamdani telah berhasil dilakukan untuk kedua studi kasus. Program telah dilengkapi dengan visualisasi grafik untuk setiap variabel dan penanganan kesalahan jika aturan tidak terpenuhi. Semua grafik visualisasi dan kode sumber telah tersedia di folder praktikum.

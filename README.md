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

![Visualisasi Hasil Kasus 1](visaliasasi%20grafik/stok_petshop_result.png)

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
- **Hasil Analisis:**
  Pada pengujian Kasus Dua dengan nilai input tersebut tidak ada aturan dari tiga belas aturan di modul yang terpenuhi. Hal ini terjadi karena nilai Kejelasan Persyaratan dan Kemampuan Petugas berada pada kategori Tidak Memuaskan, sedangkan Aturan Sepuluh sampai Tiga Belas mewajibkan kategori minimal Cukup Memuaskan untuk input tersebut agar dapat menghasilkan output.

![Himpunan Fuzzy Output Kasus 2](visaliasasi%20grafik/pelayanan_variables.png)

**Penjelasan Grafik:**
Grafik di atas menampilkan himpunan fuzzy untuk variabel output **Kepuasan Pelayanan** dengan lima kategori: 'tidak', 'kurang', 'cukup', 'memuaskan', dan 'sangat'. Berbeda dengan Kasus 1, pada grafik ini tidak muncul garis hasil perhitungan (defuzzifikasi). Hal ini dikarenakan tidak adanya aturan (*rules*) yang terpenuhi oleh kombinasi nilai input yang diuji, sehingga sistem tidak dapat mengagregasi output ke dalam nilai akhir yang spesifik.


**Output Terminal:**
```text
[PERINGATAN]: Tidak ada aturan fuzzy yang terpenuhi (fired) untuk input ini.
Grafik himpunan fuzzy output disimpan: pelayanan_variables.png
```

---

### KESIMPULAN

Implementasi Logika Fuzzy Mamdani telah berhasil dilakukan untuk kedua studi kasus. Program telah dilengkapi dengan visualisasi grafik untuk setiap variabel dan penanganan kesalahan jika aturan tidak terpenuhi. Semua grafik visualisasi dan kode sumber telah tersedia di folder praktikum.

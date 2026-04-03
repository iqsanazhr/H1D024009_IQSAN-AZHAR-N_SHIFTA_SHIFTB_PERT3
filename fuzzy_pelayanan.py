import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import os
import pandas as pd


# 1. Definisi Variabel Input dan Output
informasi = ctrl.Antecedent(np.arange(0, 101, 1), 'informasi')
persyaratan = ctrl.Antecedent(np.arange(0, 101, 1), 'persyaratan')
petugas = ctrl.Antecedent(np.arange(0, 101, 1), 'petugas')
sarpras = ctrl.Antecedent(np.arange(0, 101, 1), 'sarpras')
kepuasan = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan')

# 2. Definisi Membership Functions (MF)
# Input MF (Kejelasan Informasi, Persyaratan, dsb)
for var in [informasi, persyaratan, petugas, sarpras]:
    var['tidak'] = fuzz.trapmf(var.universe, [0, 0, 60, 75])
    var['cukup'] = fuzz.trimf(var.universe, [60, 75, 90])
    var['memuaskan'] = fuzz.trapmf(var.universe, [75, 90, 100, 100])

# Output MF (Kepuasan Pelayanan)
kepuasan['tidak'] = fuzz.trapmf(kepuasan.universe, [0, 0, 50, 75])
kepuasan['kurang'] = fuzz.trimf(kepuasan.universe, [50, 75, 100])
kepuasan['cukup'] = fuzz.trapmf(kepuasan.universe, [150, 175, 250, 275])
kepuasan['memuaskan'] = fuzz.trapmf(kepuasan.universe, [250, 275, 325, 350])
kepuasan['sangat'] = fuzz.trapmf(kepuasan.universe, [325, 350, 400, 400])

# 3. Definisi Aturan Fuzzy (Membaca dari 81_fuzzy_rules.csv)
mapping = {
    'Tidak Memuaskan': 'tidak',
    'Cukup Memuaskan': 'cukup',
    'Memuaskan': 'memuaskan',
    'Kurang Memuaskan': 'kurang',
    'Sangat Memuaskan': 'sangat'
}

rules = []
if os.path.exists('81_fuzzy_rules.csv'):
    df_rules = pd.read_csv('81_fuzzy_rules.csv')
    for _, row in df_rules.iterrows():
        rule = ctrl.Rule(
            informasi[mapping[row['Kejelasan Informasi']]] &
            persyaratan[mapping[row['Kejelasan Persyaratan']]] &
            petugas[mapping[row['Kemampuan Petugas']]] &
            sarpras[mapping[row['Ketersediaan Sarpras']]],
            kepuasan[mapping[row['Kepuasan Pelayanan']]]
        )
        rules.append(rule)
    print(f"Berhasil memuat {len(rules)} aturan dari CSV.")
else:
    print("[WARNING]: File 81_fuzzy_rules.csv tidak ditemukan. Menggunakan aturan default (kosong).")


# 4. Kontrol Sistem
kepuasan_ctrl = ctrl.ControlSystem(rules)
kepuasan_sim = ctrl.ControlSystemSimulation(kepuasan_ctrl)

# 5. Input Nilai Sesuai Kasus (Halaman 5 PDF)
kepuasan_sim.input['informasi'] = 80
kepuasan_sim.input['persyaratan'] = 60
kepuasan_sim.input['petugas'] = 50
kepuasan_sim.input['sarpras'] = 90

import matplotlib.pyplot as plt

# 6. Perhitungan dengan penanganan error
try:
    kepuasan_sim.compute()
    # 7. Output Hasil
    print(f"Hasil Perhitungan Tingkat Kepuasan Pelayanan: {kepuasan_sim.output['kepuasan']:.2f}")

    # 8. Visualisasi (Jika berhasil)
    informasi.view()
    persyaratan.view()
    petugas.view()
    # Pastikan folder visualisasi tersedia
    output_dir = 'visualisasi grafik'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    kepuasan.view(sim=kepuasan_sim)
    plt.title("Hasil Visualisasi Kepuasan Pelayanan - Kasus 2")
    save_path = os.path.join(output_dir, 'pelayanan_result.png')
    plt.savefig(save_path)
    print(f"Grafik hasil visualisasi output disimpan: {save_path}")
    plt.show(block=False) # Tampilkan semua jendela grafik (non-blocking)
except (ValueError, KeyError):
    print("\n[PERINGATAN]: Tidak ada aturan fuzzy yang terpenuhi (fired) untuk input ini.")
    # Visualisasi variabel input dan output meskipun simulasi gagal
    informasi.view()
    persyaratan.view()
    petugas.view()
    sarpras.view()
    kepuasan.view()
    plt.title("Himpunan Fuzzy Output (Kepuasan Pelayanan)")
    
    # Pastikan folder visualisasi tersedia
    output_dir = 'visualisasi grafik'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    save_path = os.path.join(output_dir, 'pelayanan_variables.png')
    plt.savefig(save_path)
    print(f"Grafik himpunan fuzzy output disimpan: {save_path}")
    plt.show(block=False) # Tampilkan semul jendela grafik (non-blocking)
except Exception as e:
    print(f"Terjadi kesalahan: {e}")

# Tahan jendela terminal agar tidak langsung tertutup
input("\nTekan Enter pada terminal untuk keluar dan menutup semua grafik...")
plt.close('all')

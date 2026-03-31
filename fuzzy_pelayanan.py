import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import os

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

# 3. Definisi Aturan Fuzzy (Sesuai Aturan 1-13)
rules = [
    ctrl.Rule(informasi['tidak'] & persyaratan['tidak'] & petugas['tidak'] & sarpras['tidak'], kepuasan['tidak']),
    ctrl.Rule(informasi['tidak'] & persyaratan['tidak'] & petugas['tidak'] & sarpras['cukup'], kepuasan['tidak']),
    ctrl.Rule(informasi['tidak'] & persyaratan['tidak'] & petugas['tidak'] & sarpras['memuaskan'], kepuasan['tidak']),
    ctrl.Rule(informasi['tidak'] & persyaratan['tidak'] & petugas['cukup'] & sarpras['tidak'], kepuasan['tidak']),
    ctrl.Rule(informasi['tidak'] & persyaratan['tidak'] & petugas['cukup'] & sarpras['cukup'], kepuasan['tidak']),
    ctrl.Rule(informasi['tidak'] & persyaratan['tidak'] & petugas['cukup'] & sarpras['memuaskan'], kepuasan['cukup']),
    ctrl.Rule(informasi['tidak'] & persyaratan['tidak'] & petugas['memuaskan'] & sarpras['tidak'], kepuasan['tidak']),
    ctrl.Rule(informasi['tidak'] & persyaratan['tidak'] & petugas['memuaskan'] & sarpras['cukup'], kepuasan['cukup']),
    ctrl.Rule(informasi['tidak'] & persyaratan['tidak'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['cukup']),
    ctrl.Rule(informasi['cukup'] & persyaratan['cukup'] & petugas['cukup'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    ctrl.Rule(informasi['cukup'] & persyaratan['cukup'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    ctrl.Rule(informasi['cukup'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat']),
    ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat'])
]

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
    output_dir = 'visaliasasi grafik'
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
    output_dir = 'visaliasasi grafik'
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

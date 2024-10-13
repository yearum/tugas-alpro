# Fungsi untuk menghitung tunjangan istri
def hitung_tunjangan_istri(gaji_pokok, status):
    if status == "IUTK":  # Istri untuk tanggungan
        return 0.10 * gaji_pokok
    else:
        return 0

# Fungsi untuk menghitung tunjangan anak
def hitung_tunjangan_anak(gaji_pokok, jumlah_anak):
    if jumlah_anak >= 2:
        return 0.05 * gaji_pokok * 2  # Hanya sampai anak kedua
    else:
        return 0.05 * gaji_pokok * jumlah_anak

# Fungsi untuk menghitung tunjangan beras (misalnya Rp 10.000 per kg)
def hitung_tunjangan_beras(jumlah_tanggungan):
    harga_beras_per_kg = 10000  # Harga beras per kilogram
    tunjangan_beras = jumlah_tanggungan * 10 * harga_beras_per_kg
    return tunjangan_beras

# Fungsi untuk menghitung potongan pajak (misal 2% dari total gaji)
def hitung_potongan_pajak(total_gaji):
    pajak = 0.02 * total_gaji  # Potongan pajak 5%
    return pajak

# Fungsi untuk menghitung tambahan lembur (misal Rp 10.000 per jam lembur)
def hitung_lembur(jam_lembur):
    tarif_lembur_per_jam = 10000  # Tarif lembur per jam
    return jam_lembur * tarif_lembur_per_jam

# Fungsi utama untuk menghitung gaji total dengan lembur dan pajak
def hitung_gaji_total(nama, status, golongan, jumlah_anak, jam_lembur):
    # Tentukan gaji pokok berdasarkan golongan
    if golongan == "A":
        gaji_pokok = 3000000
    elif golongan == "B":
        gaji_pokok = 3500000
    elif golongan == "C":
        gaji_pokok = 4000000
    else:
        print("Golongan tidak valid!")
        return 0

    # Hitung tunjangan istri, anak, dan beras
    tunjangan_istri = hitung_tunjangan_istri(gaji_pokok, status)
    tunjangan_anak = hitung_tunjangan_anak(gaji_pokok, jumlah_anak)
    jumlah_tanggungan = 1 
    if status == "IUTK":
        jumlah_tanggungan += 1  
    jumlah_tanggungan += min(jumlah_anak, 2)  

    tunjangan_beras = hitung_tunjangan_beras(jumlah_tanggungan)

    # Lembur
    lembur = hitung_lembur(jam_lembur)

    # Hitung total gaji sebelum pajak
    total_gaji_sebelum_pajak = gaji_pokok + tunjangan_istri + tunjangan_anak + tunjangan_beras + lembur

    # Hitung pajak
    potongan_pajak = hitung_potongan_pajak(total_gaji_sebelum_pajak)

    # Hitung total gaji setelah pajak
    total_gaji = total_gaji_sebelum_pajak - potongan_pajak

    # Tampilkan hasil
    print(f"Nama Pegawai: {nama}")
    print(f"Golongan: {golongan}")
    print(f"Gaji Pokok: Rp {gaji_pokok}")
    print(f"Tunjangan Istri: Rp {tunjangan_istri}")
    print(f"Tunjangan Anak: Rp {tunjangan_anak}")
    print(f"Tunjangan Beras: Rp {tunjangan_beras}")
    print(f"Tambahan Lembur: Rp {lembur}")
    print(f"Total Gaji Sebelum Pajak: Rp {total_gaji_sebelum_pajak}")
    print(f"Potongan Pajak: Rp {potongan_pajak}")
    print(f"Total Gaji Setelah Pajak: Rp {total_gaji}")

# Input dari pengguna
nama = input("Masukkan nama pegawai: ")
status = input("Masukkan status pegawai (IUTK/Tidak): ")
golongan = input("Masukkan golongan pegawai (A/B/C): ")
jumlah_anak = int(input("Masukkan jumlah anak: "))
jam_lembur = int(input("Masukkan jumlah jam lembur: "))

# Panggil fungsi untuk menghitung gaji total
hitung_gaji_total(nama, status, golongan, jumlah_anak, jam_lembur)

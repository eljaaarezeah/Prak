print("=== Sistem Pendaftaran Member Gym ===")

umur = int(input("Masukkan umur Anda (Tahun): "))

if umur < 15:
    print("Error: Maaf, usia minimal mendaftar adalah 15 tahun.")
else:
    pilihan_kelas = input("Pilihan Kelas (yoga / boxing / zumba): ")
    
    if pilihan_kelas == "yoga":
        biaya_kelas = 300000
        nama_kelas = "Yoga"
    elif pilihan_kelas == "boxing":
        biaya_kelas = 400000
        nama_kelas = "Boxing"
    elif pilihan_kelas == "zumba":
        biaya_kelas = 250000
        nama_kelas = "Zumba"
    else:
        print("Info: Kelas tidak dikenali, dialihkan ke Kelas Reguler.")
        biaya_kelas = 200000
        nama_kelas = "Reguler"
        
    sewa_loker = input("Apakah Anda ingin menyewa loker? (y/t): ")
    biaya_loker = 0
    
    if sewa_loker == "y":
        biaya_loker = 50000
        print("Info: Fasilitas loker ditambahkan.")
        
    total_bayar = biaya_kelas + biaya_loker
    
    print("\n=== Rincian Tagihan Gym ===")
    print("Kelas Dipilih :", nama_kelas)
    print("Biaya Kelas   : Rp", biaya_kelas)
    print("Biaya Loker   : Rp", biaya_loker)
    print("------------------------- +")
    print("TOTAL BAYAR   : Rp", total_bayar)
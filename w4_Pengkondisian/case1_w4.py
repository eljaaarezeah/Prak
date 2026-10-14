#267006111085
#Youhan Nelja Haezer
#Kelas A

print("===== Sistem Pendaftaran Member Gym =====")
nama = input("Masukkan Nama Anda: ")
umur = int(input("Masukkan Umur Anda (Tahun): "))
if umur >= 12:
    kelas = input("Masukkan Pilihan Kelas (yoga / boxing / zumba): ")
    if kelas == "yoga":
        tarif_kls = 300000
    elif kelas == "boxing":
        tarif_kls = 400000
    elif kelas == "zumba":
        tarif_kls = 250000
    else:
        kelas = "Reguler"
        tarif_kls = 200000
        print("Pilihan kelas tidak dikenali, dialihkan ke kelas Reguler.")
    loker = input("Apakah Anda ingin menyewa loker? (y/t): ")
    if loker == "y" or loker == "Y":
        tarif_lkr = 50000
        print("Fasilitas loker tersedia.")
    else:
        tarif_lkr = 0
    total_tarif = tarif_kls + tarif_lkr
    print("\n===== Rincian Tagihan =====")
    print("Nama:", nama)
    print("Umur:", umur)
    print("Kelas:", kelas)
    print("Tarif Kelas: Rp", tarif_kls)
    print("Tarif Loker: Rp", tarif_lkr)
    print("------------------------------ +")
    print("Total Bayar: Rp", total_tarif)
else:
    print("Error: Maaf, usia minimal mendaftar adalah 12 tahun")
    exit()
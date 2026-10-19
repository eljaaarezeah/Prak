#267006111085
#Youhan Nelja Haezer
#Kelas A

print("===== Sistem Perhitungan Tarif Parkir =====")
kendaraan = input("Masukkan jenis kendaraan (mobil/motor): ")
durasi = int(input("Masukkan durasi parkir (jam): "))
if durasi > 0:
    if kendaraan == "mobil":
        tarif = 10000
    elif kendaraan == "motor":
        tarif = 5000
    else:
        print("Info: Kendaraan tidak dikenali, otomatis masuk ke tarif Sepeda/Lainnya.")
        kendaraan = "Sepeda/Lainnya"
        tarif = 2000
    karcis = input("Apakah karcis parkir Anda hilang? (y/t): ")
    if karcis == "y" or karcis == "Y":
        tarif_denda = 50000
        print("Anda mendapatkan denda Rp50.000 karena tidak memiliki karcis parkir!")
    else:
        print("Terima kasih, Anda memiliki karcis parkir.")
        tarif_denda = 0

    tarif_akhir = tarif + tarif_denda
    uang = int(input("Masukkan jumlah uang Anda: Rp"))
    if uang == tarif_akhir:
        print("\nTransaksi berhasil! Uang Anda pas.")
        print("Gerbang parkir terbuka, silakan keluar.")
    elif uang >= tarif_akhir:
        kembalian = uang - tarif_akhir
        print("\nTransaksi berhasil! Kembalian Anda: Rp", kembalian)
        print("Gerbang parkir terbuka, silakan keluar.")
    else:
        kekurangan = tarif_akhir - uang
        print("\nTransaksi gagal! Uang Anda kurang! Kekurangan: Rp", kekurangan)
        print("Gerbang parkir tertutup, silakan isi kekurangan uang Anda.")

    print("\n===== Rincian Tarif Parkir =====")
    print("Jenis Kendaraan:", kendaraan)
    print("Durasi Parkir:", durasi, "jam")
    print("Tarif Parkir: Rp", tarif)
    print("Denda Karcis Parkir: Rp", tarif_denda)
    print("------------------------------------- +")
    print("Total Tarif Parkir: Rp", tarif_akhir)
else:
    print("Error: Durasi parkir tidak valid.")
    exit()
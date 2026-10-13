print("===== Sistem Perhitungan Tarif Parkir =====")
kendaraan = input("Masukkan jenis kendaraan (mobil/motor): ")
durasi = int(input("Masukkan durasi parkir (jam): "))
if durasi > 0:
    if kendaraan == "mobil":
        tarif = 5000
        if durasi > 1:
            tarif_prog = 3000 * (durasi - 1)
        tarif_baru = tarif + tarif_prog
    elif kendaraan == "motor":
        tarif = 3000
        if durasi > 1:
            tarif_prog = 1000 * (durasi - 1)
        tarif_baru = tarif + tarif_prog
    else:
        print("Jenis kendaraan tidak dikenali.")
        tarif = 2000
        if durasi > 1:
            tarif_prog = 1000 * (durasi - 1)
        tarif_baru = tarif + tarif_prog
    karcis = input("Apakah Anda memiliki karcis parkir? (y/t): ")
    if karcis == "t" or karcis == "T":
        tarif_denda = 50000
        print("Anda mendapatkan denda Rp50.000 karena tidak memiliki karcis parkir!")
    else:
        print("Terima kasih, Anda memiliki karcis parkir.")
        tarif_denda = 0

    tarif_akhir = tarif_baru + tarif_denda

    print("\n===== Rincian Tarif Parkir =====")
    print("Jenis Kendaraan:", kendaraan)
    print("Durasi Parkir:", durasi, "jam")
    print("Tarif Parkir: Rp", tarif_baru)
    print("Denda Karcis Parkir: Rp", tarif_denda)
    print("------------------------------------- +")
    print("Total Tarif Parkir: Rp", tarif_akhir)
else:
    print("Error: Durasi parkir harus lebih dari 0 jam.")
    exit()
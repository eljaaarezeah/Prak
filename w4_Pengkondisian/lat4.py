#267006111085
#Youhan Nelja Haezer
#Kelas A

print("=== Pengecekan Tiket Roller Coaster ===")
umur = int(input("Masukkan umur Anda (Tahun): "))
tinggi = int(input("Masukkan tinggi badan Anda (cm): "))
harga = 50000
if umur >= 12:
    if tinggi >= 150:
        print("\nSyarat terpenuhi, Anda boleh naik.")
        member = input("Apakah Anda member? (y/t): ")
        if member == "y" or member == "Y":
            harga -= 10000
            print("Anda mendapatkan diskon!")
            print("Total harga tiket: Rp", harga)
            uang = float(input("Masukkan jumlah uang Anda: Rp"))
        if uang == harga:
            print("Transaksi berhasil! Uang Anda pas.")
        elif uang >= harga:
            kembalian = uang - harga
            print("Transaksi berhasil! Kembalian Anda: Rp", kembalian)
        else:
            kekurangan = harga - uang
            print("Gagal! Uang Anda kurang! Kekurangan: Rp", kekurangan)
    else:
        print("Maaf Anda tidak boleh masuk, tinggi badan Anda belum mencukupi (Minimal 150 cm).")
else:
    print("Maaf, wahana ini khusus untuk usia 12 tahun ke atas")
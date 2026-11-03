#267006111085
#Youhan Nelja Haezer
#Kelas A

print("=== Simulasi Sistem ATM ===")
pin = 1234
kesempatan = 3
saldo = 500000
riwayat_transaksi = []

while kesempatan > 0:
    input_pin = int(input("Masukkan PIN Anda: "))
    if input_pin == pin:
        print("Login berhasil!")
        break
    else:
        kesempatan -= 1
        print("PIN salah! Sisa kesempatan:", kesempatan)
if kesempatan == 0:
    print("Kartu blokir")
else:
    while True:
        print("\n=== Menu ATM ===")
        print("1. Tarik Tunai")
        print("2. Riwayat Transaksi")
        print("3. Keluar")

        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            nominal_tarik = int(input("Masukkan jumlah tarik tunai: "))
            if nominal_tarik > saldo:
                print("Saldo tidak mencukupi")
            else:
                saldo -= nominal_tarik
                riwayat_transaksi.append(("Tarik Tunai: Rp", nominal_tarik))
                print("Tarik tunai berhasil! Sisa saldo:", saldo)
        elif pilihan == "2":
            print("Riwayat Transaksi:")
            if len(riwayat_transaksi) == 0:
                print("Belum ada transaksi.")
            for transaksi in riwayat_transaksi:
                print(transaksi)
        elif pilihan == "3":
            print("Terima kasih telah menggunakan layanan ATM.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
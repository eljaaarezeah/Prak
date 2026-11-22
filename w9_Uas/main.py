import json
import random
import math
import datetime
import os

FILE_NASABAH = "data_nasabah.json"

def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

def muat_data():
    if not os.path.exists(FILE_NASABAH):
        return []
    with open(FILE_NASABAH, 'r') as file:
        return json.load(file)

def simpan_data():
    with open(FILE_NASABAH, 'w') as file:
        json.dump(data_nasabah, file, indent=4)

def cari_rekening(no_rek):
    i = 0
    while i < len(data_nasabah):
        if data_nasabah[i]['no_rek'] == no_rek:
            return i
        i += 1
    return "tidak ada"

def waktu_transaksi():
    return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def buat_no_ref():
    return random.randint(100000, 999999)

def cek_saldo(index):
    while True:
        saldo = data_nasabah[index]["saldo"]
        bunga = math.floor(saldo * 0.005)

        print("\n--- Informasi Saldo ---")
        print(f"Nama       : {data_nasabah[index]['nama']}")
        print(f"Saldo      : Rp {saldo}")
        print(f"Bunga 0.5% : Rp {bunga}")

        konf_kembali = input("Kembali ke menu? (y/n): ")
                
        if konf_kembali.lower() == "y":
            break
        elif konf_kembali.lower() == "n":
            continue
        else:
            print("Masukkan tidak valid.")
            continue

def tarik_tunai(index):
    while True:
        nominal = int(input("Masukkan nominal tarik tunai: Rp "))

        if nominal <= 0:
            print("Nominal harus lebih dari 0.")
            continue

        if nominal > data_nasabah[index]["saldo"]:
            print("Saldo tidak mencukupi.")
            konf_kembali = input("Kembali ke menu? (y/n): ")
                    
            if konf_kembali.lower() == "y":
                break
            elif konf_kembali.lower() == "n":
                continue
            else:
                print("Masukkan tidak valid.")
                continue

        data_nasabah[index]["saldo"] -= nominal
        no_ref = buat_no_ref()
        simpan_data()

        print(f"Tarik tunai berhasil!")
        print(f"Nomor referensi: YNH{no_ref}")
        print(f"Waktu transaksi: {waktu_transaksi()}")
        print(f"Sisa saldo: Rp {data_nasabah[index]['saldo']}")

        konf_kembali = input("Kembali ke menu? (y/n): ")
                
        if konf_kembali.lower() == "y":
            break
        elif konf_kembali.lower() == "n":
            continue
        else:
            print("Masukkan tidak valid.")
            continue

def setor_tunai(index):
    while True:
        nominal = int(input("Masukkan nominal setor tunai: Rp "))

        if nominal <= 0:
            print("Nominal harus lebih dari 0.")
            continue

        data_nasabah[index]["saldo"] += nominal
        no_ref = buat_no_ref()
        simpan_data()

        print(f"Setor tunai berhasil!")
        print(f"Nomor referensi: YNH{no_ref}")
        print(f"Waktu transaksi: {waktu_transaksi()}")
        print(f"Saldo sekarang: Rp {data_nasabah[index]['saldo']}")
                        
        konf_kembali = input("Kembali ke menu? (y/n): ")
        
        if konf_kembali.lower() == "y":
            break
        elif konf_kembali.lower() == "n":
            continue
        else:
            print("Masukkan tidak valid.")
            continue

def transfer(index):
    while True:
        no_tujuan = input("Masukkan nomor rekening tujuan: ")
        tujuan = cari_rekening(no_tujuan)

        if tujuan == "tidak ada":
            print("Rekening tujuan tidak ditemukan.")
            continue

        if tujuan == index:
            print("Tidak dapat transfer ke rekening sendiri.")
            continue

        nama_tujuan = data_nasabah[tujuan]["nama"]
        print("Nama pemilik rekening:", nama_tujuan)

        konfirmasi = input("Lanjutkan transfer? (y/n): ")

        if konfirmasi.lower() != "y":
            print("Transfer dibatalkan.")
            konf_kembali = input("Kembali ke menu? (y/n): ")

            if konf_kembali.lower() == "y":
                break
            elif konf_kembali.lower() == "n":
                continue
            else:
                print("Masukkan tidak valid.")
                continue

        nominal = int(input("Masukkan nominal transfer: Rp "))

        if nominal <= 0:
            print("Nominal harus lebih dari 0.")
            continue

        if nominal > data_nasabah[index]["saldo"]:
            print("Saldo tidak mencukupi.")
            konf_kembali = input("Kembali ke menu? (y/n): ")
                   
            if konf_kembali.lower() == "y":
                break
            elif konf_kembali.lower() == "n":
                continue
            else:
                print("Masukkan tidak valid.")
                continue

        data_nasabah[index]["saldo"] -= nominal
        data_nasabah[tujuan]["saldo"] += nominal
        no_ref = buat_no_ref()
        simpan_data()

        print(f"\nTransfer berhasil!")
        print(f"Nomor referensi: YNH{no_ref}")
        print(f"Waktu transaksi: {waktu_transaksi()}")
        print(f"Nama penerima: {nama_tujuan}")
        print(f"Nominal transfer: Rp {nominal}")
        print(f"Sisa saldo: Rp {data_nasabah[index]['saldo']}")

        konf_kembali = input("Kembali ke menu? (y/n): ")
        
        if konf_kembali.lower() == "y":
            break
        if konf_kembali.lower() != "y" and konf_kembali.lower() != "n":
            print("Masukkan tidak valid.")
            continue

def login():
    no_rek = input("Masukkan nomor rekening: ")
    index = cari_rekening(no_rek)

    if index == "tidak ada":
        print("Rekening tidak ditemukan.")
        return "tidak ada"

    pin = input("Masukkan PIN: ")

    if pin != data_nasabah[index]["pin"]:
        print("PIN salah.")
        return "tidak ada"

    return index

def menu_atm(index):
    clrscr()
    while True:
        clrscr()
        print("===== SIMULASI MESIN ATM =====")
        print(f"Selamat datang, {data_nasabah[index]['nama']}")
        print(f"No. Rekening: {data_nasabah[index]['no_rek']}")
        print("\n===== MENU ATM =====")
        print("1. Cek Saldo")
        print("2. Setor Tunai")
        print("3. Tarik Tunai")
        print("4. Transfer")
        print("5. Keluar")

        pilihan = int(input("Pilih menu: "))

        if pilihan == 1:
            cek_saldo(index)
            print()

        elif pilihan == 2:
            setor_tunai(index)
            print()

        elif pilihan == 3:
            tarik_tunai(index)
            print()

        elif pilihan == 4:
            transfer(index)
            print()

        elif pilihan == 5:
            print("Terima kasih telah menggunakan ATM.")
            exit()

        else:
            print("Pilihan tidak valid.")

def main():
    while True:
        global data_nasabah

        data_nasabah = muat_data()

        print("===== SIMULASI MESIN ATM =====")
        index = login()

        if index != "tidak ada":
            menu_atm(index)

if __name__ == "__main__":
    main()
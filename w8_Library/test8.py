#267006111085
#Youhan Nelja Haezer
#Kelas A

import json
import random
import math
import datetime
import os

FILE_STOK = "stok_minimarket.json"

# Fungsi untuk membaca data dari file JSON
def muat_stok():
    if not os.path.exists(FILE_STOK):
        return []
    with open(FILE_STOK, 'r') as file:
        return json.load(file)

def simpan_stok(data):
    with open(FILE_STOK, 'w') as file:
        json.dump(data, file, indent=4)

# FUNGSI PENCARI
def cari_barang(data_stok, kode):
    i = 0
    while i < len(data_stok):
        if data_stok[i]['kode'] == kode:
            return i
        i += 1
    return "tidak ada"

#FUNGSI FITUR UTAMA
def lihat_barang():
    data = muat_stok()
    if len(data) == 0:
        print("\nStok masih kosong! Silahkan tambah barang dulu.")
        return


    print("\nKatalog Minimarket")
    i = 0
    while i < len(data):
        brg = data[i]
        print(f"Kode: {brg['kode']} | {brg['nama']} | Stok: {brg['stok']} | Harga: {brg['harga']}")
        i += 1

def tambah_barang():
    data = muat_stok()
    kode = input("Masukkan kode barang (mis: M01): ")

    if cari_barang(data, kode) != "tidak ada":
        print("Kode barang sudah ada! Silahkan gunakan kode lain.")
        return

    nama = input("Masukkan nama barang: ")
    stok = int(input("Masukkan jumlah stok: "))
    harga = int(input("Masukkan harga barang: "))

    barang_baru = {
        "kode": kode,
        "nama": nama,
        "stok": stok,
        "harga": harga
    }
    data.append(barang_baru)
    simpan_stok(data)
    print(f"Barang {nama} berhasil ditambahkan ke stok.")

def fitur_kasir():
    data = muat_stok()
    if len(data) == 0:
        print("\nStok masih kosong! Silahkan tambah barang dulu.")
        return

    kode_beli = input("Masukkan kode barang yang ingin dibeli: ")
    i = cari_barang(data, kode_beli)

    if i == "tidak ada":
        print("Barang tidak ditemukan! Silahkan cek kode barang.")
        return

    jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))

    if data[i]['stok'] < jumlah_beli:
        print("Stok tidak mencukupi! Silahkan cek jumlah stok.")
        return

    #RUANG VIP

    #Potong stok di memori
    data[i]['stok'] -= jumlah_beli
    simpan_stok(data)

    #Perhitungan uang
    subtotal = data[i]['harga'] * jumlah_beli
    pajak = subtotal * 0.11  # Pajak 11%
    total_bayar = subtotal + pajak

    #Cetak struk
    waktu = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    no_resi = random.randint(1000, 9999)

    print("\n=====================")
    print("STRUK BELANJA")
    print(f"Waktu: {waktu}")
    print(f"No. TRX: INV{no_resi}")
    print("----------------------")
    print(f"{data[i]['nama']} (x{jumlah_beli})")
    print(f"Subtotal: Rp{subtotal}")
    print(f"PPN (11%): Rp{pajak}")
    print("----------------------")
    print(f"Total Bayar: Rp{total_bayar}")
    print("=====================")

#Menu utama
print("=== SISTEM MINIMARKET ===")
while True:
    print("\n[ MENU KASIR ]")
    print("1. Lihat Barang")
    print("2. Tambah Barang")
    print("3. Fitur Kasir") 
    print("4. Tutup Toko")

    pilih = input("Pilih menu (1-4): ")

    if pilih == "4":
        print("Sistem dimatikan. Terima kasih telah menggunakan sistem minimarket.")
        break
    elif pilih == "1":
        lihat_barang()
    elif pilih == "2":
        tambah_barang()
    elif pilih == "3":
        fitur_kasir()
    else:
        print("Pilihan tidak valid! Silahkan pilih menu yang tersedia.")
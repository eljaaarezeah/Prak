#267006111085
#Youhan Nelja Haezer
#Kelas A

import random
import json

kode_transaksi = "TRX" + str(random.randint(1000, 9999))

stok_barang = {
    "kode_transaksi": kode_transaksi,
    "nama_barang": "pensil",
    "stok": 50,
}

with open("stok_barang.json", "w") as file:
    json.dump(stok_barang, file, indent=4)

with open("stok_barang.json", "r") as file:
    data_stok = json.load(file)

print("\n=== DATA STOK BARANG ===")
print("Kode Transaksi :", data_stok["kode_transaksi"])
print("Nama Barang    :", data_stok["nama_barang"])
print("Jumlah Stok    :", data_stok["stok"])
print("========================")   
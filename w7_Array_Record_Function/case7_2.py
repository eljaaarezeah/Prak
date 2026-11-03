#267006111085
#Youhan Nelja Haezer
#Kelas A

barang = [
    {"kode": "A01", "nama": "Pensil", "stok": 10},
    {"kode": "A02", "nama": "Buku", "stok": 5},
    {"kode": "A03", "nama": "Penghapus", "stok": 15}
]

print("Daftar Barang:")
i = 0
while i < len(barang):
    print(barang[i]["kode"],"|", barang[i]["nama"], "|", barang[i]["stok"])
    i += 1
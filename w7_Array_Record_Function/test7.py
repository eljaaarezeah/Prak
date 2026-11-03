perpus = [
    {"kode": "B01", "judul": "Python Dasar", "status": "tersedia"},
    {"kode": "B02", "judul": "Basis Data", "status": "tersedia"},
    {"kode": "B03", "judul": "Jaringan", "status": "dipinjam"}
]
cari = input("Masukkan kode buku yang dicari: ")
i = 0
while i < len(perpus):
    if perpus[i]["kode"] == cari:
        perpus[i]["status"] = "dipinjam"
        print(perpus[i]["kode"], perpus[i]["judul"], perpus[i]["status"])
        break
    i += 1
else:
    print("Buku tidak ditemukan")
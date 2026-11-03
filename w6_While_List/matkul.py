#267006111085
#Youhan Nelja Haezer
#Kelas A

matkul = ["Algoritma", "Basis Data", "Jaringan"]

while True:
    print("Daftar Mata Kuliah:")
    i = 0
    while i < len(matkul):
        print(i + 1, matkul[i])
        i += 1
    print("Jumlah Mata Kuliah:", len(matkul))
    matkul_tambah = input("Mata Kuliah yang ingin ditambahkan: ")
    matkul.append(matkul_tambah)
    print("Mata kuliah ditambahkan:", matkul_tambah)
    print("Daftar Terbaru:")
    i = 0
    while i < len(matkul):
        print(i + 1, matkul[i])
        i += 1
    print("Jumlah Mata Kuliah:", len(matkul))
    matkul_hapus = input("Mata Kuliah yang ingin dihapus: ")
    if matkul_hapus in matkul:
        matkul.remove(matkul_hapus)
        print("Mata kuliah dihapus:", matkul_hapus)
    else:
        print("Mata kuliah tidak ditemukan:", matkul_hapus)
    print("Daftar Akhir:")
    i = 0
    while i < len(matkul):
        print(i + 1, matkul[i])
        i += 1
    print("Jumlah Mata Kuliah:", len(matkul))
    break
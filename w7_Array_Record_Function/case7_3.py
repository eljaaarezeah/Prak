#267006111085
#Youhan Nelja Haezer
#Kelas A

barang = [
    {"kode": "A01", "nama": "Pensil", "stok": 10},
    {"kode": "A02", "nama": "Buku", "stok": 5},
    {"kode": "A03", "nama": "Penghapus", "stok": 15}
]

def tampilkan():
    print("Daftar Barang:")
    i = 0
    while i < len(barang):
        print(barang[i]["kode"], "|", barang[i]["nama"], "|", barang[i]["stok"])
        i += 1

def cari(kode):
    i = 0
    while i < len(barang):
        if barang[i]["kode"] == kode:
            return barang[i]
        i += 1
    return None

def kurangi_stok(kode, jumlah):
    i = 0
    while i < len(barang):
        if barang[i]["kode"] == kode:
            if barang[i]["stok"] >= jumlah:
                barang[i]["stok"] -= jumlah
                print("Stok", barang[i]['nama'], "berhasil dikurangi sebanyak", jumlah, ".")
            else:
                print("Stok", barang[i]['nama'], "kurang.")
            break
        i += 1
    else:
        print("Barang tidak ditemukan.")

while True:
    print("\n=== Sistem Manajemen Stok Barang ===")
    print("\n--- Menu ---")
    print("1. Tampilkan Barang")
    print("2. Cari Barang")
    print("3. Kurangi Stok")
    print("4. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print()
        tampilkan()
    elif pilihan == "2":
        print()
        kode = input("Masukkan kode barang yang ingin dicari: ")
        hasil = cari(kode)
        if hasil:
            print("Barang ditemukan:")
            print(hasil["kode"], "|", hasil["nama"], "|", hasil["stok"])
        else:
            print("Barang tidak ditemukan.")
    elif pilihan == "3":
        print()
        tampilkan()
        print()
        kode = input("Masukkan kode barang yang ingin dikurangi stoknya: ")
        jumlah = int(input("Masukkan jumlah yang ingin dikurangi: "))
        kurangi_stok(kode, jumlah)
        print("Daftar Barang Terbaru:")
        tampilkan()
    elif pilihan == "4":
        print()
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
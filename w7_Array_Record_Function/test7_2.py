perpus = [
    {"kode": "B01", "judul": "Python Dasar", "status": "tersedia"},
    {"kode": "B02", "judul": "Basis Data", "status": "tersedia"},
    {"kode": "B03", "judul": "Jaringan", "status": "dipinjam"}
]

def tampilkan():
    print("\n--- Katalog Buku ---")
    i = 0
    while i < len(perpus):
        print(perpus[i]["kode"], perpus[i]["judul"], perpus[i]["status"])
        i += 1

def cari(kode):
    i = 0
    while i < len(perpus):
        if perpus[i]["kode"] == kode:
            return i
        i += 1
    return "tidak ada"

def pinjam(kode):
    i = cari(kode)
    if i == "tidak ada":
        print("Kode tidak ada")
        return
    if perpus[i]["status"] == "dipinjam":
        print("Buku sedang dipinjam.")
        return
    
    perpus[i]["status"] = "dipinjam"
    print("Buku berhasil dipinjam.")

print("=== Sistem Perpustakaan ===")
while True:
    print("\nMenu:")
    print("1. Tampilkan Katalog")
    print("2. Cari Buku")
    print("3. Pinjam Buku")
    print("4. Keluar")
    pilihan = input("Pilih menu(1/2/3/4): ")

    if pilihan == "1":
        tampilkan()
    elif pilihan == "2":
        kode = input("Masukkan kode buku yang dicari: ")
        hasil = cari(kode)
        if hasil != "tidak ada":
            print("Buku ditemukan:")
            print(perpus[hasil]["kode"], perpus[hasil]["judul"], perpus[hasil]["status"])
        else:
            print("Buku tidak ditemukan.")
    elif pilihan == "3":
        kode = input("Masukkan kode buku yang ingin dipinjam: ")
        pinjam(kode)
    elif pilihan == "4":
        print("Terima kasih telah menggunakan layanan perpustakaan.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
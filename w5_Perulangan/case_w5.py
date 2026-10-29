#267006111085
#Youhan Nelja Haezer
#Kelas A

print("=== Simulasi Pengecekan Tiket Bioskop ===")
print("")
jumlah_studio = int(input("Masukkan jumlah studio yang beroperasi: "))
studio_perbaikan = int(input("Masukkan nomor studio yang sedang diperbaiki (Ketik 0 jika tidak ada): "))
durasi = 0

for studio in range(1, jumlah_studio + 1):
    print("\n=== Memasuki Studio ", studio, " ===")
    for baris in range(1, 4):
        if baris == 2:
            print("Baris 2 adalah area VIP, petugas reguler melewati baris ini.")
            continue
        if studio == studio_perbaikan:
            print("\n[PERHATIAN] Studio ke-", studio_perbaikan, "sedang diperbaiki. Petugas tidak dapat memeriksa tiket di studio ini.")
            break
        print("Tiket penonton di Baris ", baris, " sudah diperiksa.")
    else:
        print("\n[Status]: Pengecekan di Studio ", studio, " tuntas 100%.")
    durasi += 10

if durasi >= 50:
    print("\nTotal Waktu: ", durasi, " menit. Hari yang sangat sibuk, petugas butuh istirahat!")
elif durasi >= 30:
    print("\nTotal Waktu: ", durasi, " menit. Shift kerja berjalan normal.")
else:
    print("\nTotal Waktu: ", durasi," menit. Shift santai, bioskop sedang sepi.")
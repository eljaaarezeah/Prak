#267006111085
#Youhan Nelja Haezer
#Kelas A

print("=== Simulasi Tabungan Liburan ===")

lama_minggu = int(input("Berapa minggu Anda ingin menabung?: "))
total_uang = 0

print("\n=== Mulai Menabung ===")

for minggu in range(1, lama_minggu + 1):
    if minggu == 3:
        print("\n[Darurat! Minggu ke-3 ada keperluan mendadak. Program berhenti! ]")
        break
    print("\nMinggu ke -", minggu)
    for hari in range(1, 4):
        if hari == 2:
            print("   - Hari ke- 2 (Libur, jadwal menabung dilewati)")
            continue
        print("   - Hari ke -", hari)
        for sesi in range(1, 3):
            print("     -> Sesi ke -", sesi, ": Memasukkan uang Rp 5.000")
            total_uang += 5000
else:
    print("\nStatus: Misi menabung selesai! Anda telah menabung selama", lama_minggu, "minggu.")

print("\n=== Hasil Tabungan ===")
if total_uang >= 500000:
    print("Uang Anda Rp", total_uang, "Keren! Bisa dipakai liburan ke luar kota")
elif total_uang >= 200000:
    print("Uang Anda Rp", total_uang, "Lumayan! Bisa dipakai jalan-jalan di dalam kota")
else:
    print("Uang Anda Rp", total_uang, "Sedikit! Bisa dipakai jajan di rumah saja")
print("========= Kalkulator Patungan Makan =========")
nama = input("Masukkan nama Anda: ")
tagihan = int(input("Masukkan total tagihan: "))
persen_tip = int(input("Masukkan persentase tip: "))
jumlah_orang = int(input("Masukkan jumlah orang yang ikut patungan: "))

nominal_tip = (persen_tip / 100) * tagihan
total_tagihan = tagihan + nominal_tip
bayar_per_orang = total_tagihan / jumlah_orang

#Membulatkan nominal tip, total tagihan, dan bayar per orang menjadi 2 desimal
bayar_per_orang = round(bayar_per_orang, 2)

print("\n========= Ringkasan Tagihan =========")
print("Nama Pembeli: " + nama)
print("Total Tagihan: Rp", total_tagihan)
print("Bayar per Orang: Rp", bayar_per_orang)
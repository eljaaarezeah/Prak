print("====== Sistem Cek & Status Pembayaran ======")
nama = input("Masukkan nama anda: ")
harga_satuan = int(input("Masukkan harga satuan: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))
nominal_uang = int(input("Masukkan jumlah nominal uang: "))

total_harga = harga_satuan * jumlah_barang
selisih_uang = nominal_uang - total_harga

uang_cukup = nominal_uang >= total_harga
uang_pas = nominal_uang == total_harga
uang_kurang = nominal_uang < total_harga

print("\n===== Ringkasan Transaksi =====")
print("Nama Pelanggan: ", nama)
print("Total Harga: Rp", total_harga)
print("Selisih Uang (Kembalian/Kekurangan): Rp", selisih_uang)

print("\n===== Status Cek Sistem (True/False) =====")
print("Apakah uang cukup? :", uang_cukup)
print("Apakah uang pas? :", uang_pas)
print("Apakah berhutang? :", uang_kurang)
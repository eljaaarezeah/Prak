# Program Pemesanan Restoran

#input statis
line = "==============================="
nama = "RM Abadi Nan Jaya"
jenis = "Masakan Padang"
buka = True
rating = 4.5

#input dinamis
print(line)
print("Form Pemesanan Restoran")
print(line)
user = input("Masukkan nama Anda: ")
table = int(input("Masukkan nomor meja Anda: "))
pesanan = input("Masukkan pesanan Anda: ")
jumlah = int(input("Masukkan jumlah pesanan Anda: "))

#output
print()
print(line)
print("Informasi Restoran")
print(line)
print("Nama restoran:", nama)
print("Jenis restoran:", jenis)
print("Buka:", buka)
print("Rating:", rating)
print()
print(line)
print("Informasi Pemesanan")
print(line)
print(f"Nama pemesan: {user}")
print(f"Nomor meja: {table}")
print(f"Pesanan: {pesanan}")
print(f"Jumlah pesanan: {jumlah}")
print(line)
print()
print(line)
print("Tipe Data Variabel")
print(line)
print("nama_restoran:", type(nama))
print("jenis_masakan:", type(jenis))
print("jam_buka:", type(buka))
print("rating_restoran:", type(rating))
print("nama_pemesan:", type(user))
print("nomor_meja:", type(table))
print("pesanan:", type(pesanan))
print("jumlah_pesanan:", type(jumlah))
print(line)
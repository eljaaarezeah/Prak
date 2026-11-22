#267006111085
#Youhan Nelja Haezer
#Kelas A

import math

n = int(input("Masukkan jumlah barang: "))
m = int(input("Kapasitas per kardus: "))

kardus = math.ceil(n / m)
print("Jumlah kardus yang dibutuhkan:", kardus)
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukan angka kedua: "))
operator = str(input("Masukkan operator (+, -, *, /, **, //, %): "))

#dictionary untuk menyimpan hasil operasi
hasil = {
    '+': (angka1 + angka2),
    '-': (angka1 - angka2),
    '*': (angka1 * angka2),
    '/': (angka1 / angka2),
    '**': (angka1 ** angka2),
    '//': (angka1 // angka2),
    '%': (angka1 % angka2)
}

#Mengubah hasil menjadi integer jika hasilnya adalah bilangan bulat
output = int(hasil[operator]) if hasil[operator].is_integer() else hasil[operator]

print("Hasil: ", output)
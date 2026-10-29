print("=== Program Pemaanasan Olahraga ===")

nama = input("Masukkan nama atlet: ")
print("Halo", nama, "! Mari kita mulai latihan.")

target_lari = 0
while target_lari <= 0:
    target_lari = int(input("Target keliling lapangan hari ini (harus lebih dari 0): "))

print("\nMulai berlari")
for putaran in range(1, target_lari + 1):
    print("Menyelesaikan putaran ke -", putaran)

jarak_meter = target_lari * 400

print("\nLatihan Selesai!")
if jarak_meter >= 3000:
    print("Hebat! Anda berlari sejauh", jarak_meter, "meter. Stamina monster!.")
elif jarak_meter >= 1000:
    print("Baguss! Anda berlari sejauh", jarak_meter, "meter. Latihan yang solid!.")
else:
    print("Totl:", jarak_meter, "meter. Pemanasan ringan yang baik.")
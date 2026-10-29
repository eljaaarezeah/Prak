while True:
    kata = input("Masukkan kata (ketik: berhenti untuk stop): ")
    key = "berhenti"
    if kata == key:
        break
print("Loop berhenti")

numbers = ["1", "2", "3", "4", "5"]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

print()
numbers.append("6")
print(numbers)
print()
numbers.pop(0)
print(numbers)
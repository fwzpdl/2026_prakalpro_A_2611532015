# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_2015 = int(input("Input angka-1: "))
angka2_2015 = int(input("Input angka-2: "))

# Penjumlahan
hasil_2015 = angka1_2015 + angka2_2015
print("\nOperator Penjumlahan")
print("Hasil =",hasil_2015)

# Pengurangan
hasil_2015 = angka1_2015 - angka2_2015
print("\nOperator Pengurangan")
print("Hasil =",hasil_2015)

# Perkalian
hasil_2015 = angka1_2015 * angka2_2015
print("\nOperator Perkalian")
print("Hasil =",hasil_2015)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_2015 != 0:
    hasil_2015 = angka1_2015 / angka2_2015
    print("\nOperator Pembagian")
    print("Hasil =",hasil_2015)

    hasil_2015 = angka1_2015 // angka2_2015
    print("\nOperator Pembagian Bulat")
    print("Hasil =",hasil_2015)

    hasil_2015 = angka1_2015 % angka2_2015
    print("\nOperator Sisa Bagi")
    print("Hasil =",hasil_2015)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_2015 = angka1_2015 ** angka2_2015
print("\nOperator Pangkat")
print("Hasil =",hasil_2015)
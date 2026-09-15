#program operator assignment dalam python

angka1_2015 = int(input("Input angka-1: "))
angka2_2015 = int(input("Input angka-2: "))

print("\nNilai awal angka1_2015 =", angka1_2015)
print("Nilai angka2_2015 =", angka2_2015)

# Assignmrnt biasa
hasil_2015 = angka1_2015
print("\nAssignment biasa (=)")
print("hasil =", hasil_2015)

# assignment penambahan
hasil_2015 = angka1_2015
hasil_2015 += angka2_2015
print("\nAssignment penjumlahan(+)")
print("hasil =", hasil_2015)

# assignment pengurangan
hasil_2015 = angka1_2015
hasil_2015 -= angka2_2015
print("\nAssignment pengurangan(-)")
print("hasil =", hasil_2015)

# assignment perkalian
hasil_2015 = angka1_2015
hasil_2015 *= angka2_2015
print("\nAssignment perkalian(*)")
print("hasil =", hasil_2015)

# assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2015 != 0:
    hasil_2015 = angka1_2015
    hasil_2015 /= angka2_2015
    print("\nAssignment pembagian(/)")
    print("hasil =", hasil_2015)

    #operasi tambahan
    hasil_2015 = angka1_2015
    hasil_2015 //= angka2_2015
    print("\nAssignment pembagian bulat(//)")
    print("hasil =", hasil_2015)

    hasil_2015 = angka1_2015
    hasil_2015 %= angka2_2015
    print("\nAssignment sisa bagi (%)")
    print("hasil =", hasil_2015)
else:
    print("Pembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh 0")

# Operator tambahan : perpangkatan
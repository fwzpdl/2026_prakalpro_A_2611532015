#Program operator logika dalam python

#memasukkan nilai boolean
#input tidak peka terhadap huruf besar dan kecil

a1_2015 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_2015 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 = ", a1_2015)
print("A2 =", a2_2015)

#Konjungsi : bernilai true jika keduanya true
hasil_2015 = a1_2015 and a2_2015
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_2015)

#disjungsi: bernilai true jika salah satunya true
hasil_2015 = a1_2015 or a2_2015
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_2015)

#Negasi A1: membalik nilai a1
hasil_2015 = not a1_2015
print("\nNegasi A1 (NOt)")
print("not A1=", hasil_2015)

#Negasi A2: membalik nilai a2
hasil_2015 = not a2_2015
print("\nNegasi A2 (NOt)")
print("not A2=", hasil_2015)

# XOR: bernilai true jika kedua nilai berbeda
hasil_2015 = a1_2015 != a2_2015
print("\nDisjungsi ekslusif (XOR)")
print(" A1 XOR A2 =", hasil_2015)


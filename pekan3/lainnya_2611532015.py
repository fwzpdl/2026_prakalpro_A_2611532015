

print("===============================")
print("1. OPERATOR KEANGGOTAAN")
print("===============================")

#INPUT BEBERAPA DATA YANG DIPISAHKAN KOMA
input_data_2015 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list ineteger
data_2015 = [int(angka.strip()) for angka in input_data_2015.split(",")]

nilai_dicari_2015 = int(input("Masukkan angka yang ingin dicari: "))

#Operator in
hasil_2015 = nilai_dicari_2015 in data_2015
print("\nOperator Keanggotaan IN")
print(nilai_dicari_2015, "in", data_2015, "=", hasil_2015)

#Operator not in 
hasil_2015 = nilai_dicari_2015 not in data_2015
print("\nOperator Keanggotaan NOT IN")
print(nilai_dicari_2015, "not in", data_2015, "=", hasil_2015)



print("===============================")
print("2. OPERATOR IDENTITAS")
print("===============================")

# objek1 menggunakan list dari input pengguna
objek1_2015 = data_2015

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2015 = objek1_2015

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2015 = data_2015.copy()

print("objek1 =", objek1_2015)
print("objek2 =", objek2_2015)
print("objek3 =", objek3_2015)

# OPERATOR IS
hasil_2015 = objek1_2015 is objek2_2015
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_2015)

#Operator Is Not
hasil_2015 = objek1_2015 is not objek2_2015
print("\nOperator identitas IS NOT")
print("objek1 is not objek2 =", hasil_2015)

#membandingkan identitas dan nilai
print("\nPerbandingan Identitas dan Nilai")
print("objek1 is objek3 =", objek1_2015 is objek3_2015 )
print("objek1 == objek3 =", objek1_2015 == objek3_2015)
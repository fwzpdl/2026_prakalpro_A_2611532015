#deklarasi variabel dengan type data boolean

is_lulus_2015 = True
is_cumloude_2015 = True

#menggunakan boolean
nilai_2015 = 90
batas_lulus_2015 = 75

#Menentukan Boolean dari kondisi
status_kelulusan_2015 = nilai_2015 >= batas_lulus_2015 #Hasilnya akan lulus 
print("=== Check Kelulusan ===")
print("Nilai", nilai_2015)
print("Apakah Lulus?:", status_kelulusan_2015)
if is_lulus_2015 and is_cumloude_2015:
    print("Selamat, Anda lulus dengan predikat CumLaude!")
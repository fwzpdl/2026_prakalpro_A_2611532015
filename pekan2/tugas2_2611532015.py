# Sistem Biodata dan Validasi Kelulusan Praktikan

# Konstanta batas kelulusan
batas_kelulusan_2015 = 80.0

# Input biodata praktikan
nama_2015 = input("Masukkan Nama: ")
nim_2015 = input("Masukkan NIM: ")
jurusan_2015 = input("Masukkan Jurusan: ")
fakultas_2015 = input("Masukkan Fakultas: ")
universitas_2015 = input("Masukkan Universitas: ")

# Input nilai awal praktikum
nilai_2015 = float(input("Masukkan Nilai Awal Praktikum: "))

# Output biodata
print("\n=== BIODATA PRAKTIKAN ===")
print("Nama:", nama_2015)
print("NIM:", nim_2015)
print("Jurusan:", jurusan_2015)
print("Fakultas:", fakultas_2015)
print("Universitas:", universitas_2015)

# Validasi kelulusan
print("\n=== HASIL VALIDASI ===")
if nilai_2015 >= batas_kelulusan_2015:
    print("Status: LULUS ")
else:
    print("Status: TIDAK LULUS ")

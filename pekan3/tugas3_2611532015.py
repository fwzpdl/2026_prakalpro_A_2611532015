# SISTEM OPERASI TOKO
nama_2015 = input("Masukkan Nama Pelanggan: ")
status_2015 = input("Masukkan Status Pelanggan (member/nonmember): ")
total_belanja_2015 = int(input("Masukkan total belanja: "))
jumlah_barang_2015 = int(input("Masukkan jumlah barang: "))
kode_promo_2015 = input("Masukkan Kode promo : ")

# Daftar promo tersedia
promo_list_2015 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

#OPERATOR PERBANDINGAN
syarat_belanja_2015 = total_belanja_2015 >= 200000
syarat_barang_2015 = jumlah_barang_2015 >= 3
status_member_2015 = status_2015 == "member"
promo_tersedia_2015 = kode_promo_2015 in promo_list_2015

#Operator Logika 
diskon_member_2015 = status_member_2015 and syarat_belanja_2015
promo_dapat_2015 = syarat_barang_2015 or promo_tersedia_2015

#Operator Keanggotaan
cek_promo_2015 = kode_promo_2015 in promo_list_2015
cek_promo_invalid_2015 = kode_promo_2015 not in promo_list_2015

#Operator Aritmatika
diskon_2015 = 0
if diskon_member_2015:
    diskon_2015 = total_belanja_2015 * 10 // 100 #diskon 10%

#operator penugasan
total_bayar_2015 = total_belanja_2015
total_bayar_2015 -= diskon_2015

rata_barang_2015 = total_bayar_2015 / jumlah_barang_2015
sisa_pembagian_2015 = total_bayar_2015 % jumlah_barang_2015

#operator identitas
angka_a_2015 = [1, 2, 3]
angka_b_2015 = [1, 2, 3]
identitas_sama_2015 = angka_a_2015 is angka_b_2015
nilai_sama_2015 = angka_a_2015 == angka_b_2015

#operator bitwise
kode_status_2015 = 0
if status_member_2015: kode_status_2015 |= 0b0001
if syarat_belanja_2015: kode_status_2015 |= 0b0010
if syarat_barang_2015: kode_status_2015 |= 0b0100
if promo_tersedia_2015: kode_status_2015 |= 0b1000

#Pemeriksaan bitwise
cek_member_bit_2015 = kode_status_2015 & 0b0001
cek_promo_bit_2015 = kode_status_2015 & 0b1000
perbandingan_bit_2015 = kode_status_2015 ^ 0b1011
shift_bit_2015 = kode_status_2015 << 1

#OUTPUT
print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan       :", nama_2015)
print("Status Pelanggan     :", status_2015)
print("Total Belanja        : Rp", total_belanja_2015)
print("Jumlah Barang        :", jumlah_barang_2015)
print("Kode Promo           :", kode_promo_2015)

print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000        :", syarat_belanja_2015)
print("Jumlah Barang >= 3         :", syarat_barang_2015)
print("Status Member              :", status_member_2015)
print("Kode Promo Tersedia        :", promo_tersedia_2015)
print("Mendapatkan Diskon         :", diskon_member_2015)
print("Mendapatkan Promo          :", promo_dapat_2015)

print("\n=== HASIL PERHITUNGAN ===")
print("Diskon                     : Rp", diskon_2015)
print("Total Pembayaran           : Rp", total_bayar_2015)
print("Rata-rata Harga Barang     : Rp", int(rata_barang_2015))
print("Sisa Pembagian             :", sisa_pembagian_2015)

print("\n=== HASIL OPERATOR IDENTITAS ===")
print("Apakah identitas sama?     :", identitas_sama_2015)
print("Apakah nilai sama?         :", nilai_sama_2015)

print("\n=== HASIL BITWISE ===")
print("Kode Status (biner)        :", format(kode_status_2015, '04b'))
print("Kode Status (desimal)      :", kode_status_2015)
print("Cek Member (bitwise AND)   :", cek_member_bit_2015)
print("Cek Promo (bitwise AND)    :", cek_promo_bit_2015)
print("Perbandingan XOR           :", perbandingan_bit_2015)
print("Shift Left                 :", shift_bit_2015)

print("\n=== SELESAI ===")
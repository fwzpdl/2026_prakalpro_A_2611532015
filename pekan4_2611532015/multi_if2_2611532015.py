#input dari user
total_belanja_2015 = float(input("Masukkan total belanja (Rp) : "))

# input status member 
input_member_2015 = input("Apkah anda member ?(y/t) : ")
is_member_2015 = input_member_2015 in ["y", 'ya']

#mengecek status kode promo
input_promo_2015 = input("Apakah kode promo valid? (y/t) : ").strip().lower()
kode_promo_valid_2015 = input_promo_2015 in ["y", 'ya']

total_diskon_persen = 0
# multi if terpisah : setiap kondisi diperiksa secara independen
# diskon bisa ditumpuk (akumulasi) jika memnuhi beberapa syarat sekaligus

if total_belanja_2015 > 1000000 :
    total_diskon_persen += 10 # diskon belanja besar

if is_member_2015 :
    total_diskon_persen += 5 # diskon member

if kode_promo_valid_2015 : 
    total_diskon_persen += 15 # diskon voucher

#menghitung nominal diskon dan total bayar
nominal_diskon_2015 = total_diskon_persen * (total_diskon_persen/100)
total_bayar_2015 = total_belanja_2015 - nominal_diskon_2015

#output hasil
print("\n===RINCIAN PEMBAYARAN===")
print(f"Total diskon   : {total_diskon_persen}% (Rp {nominal_diskon_2015})")
print(f"Total bayar    : Rp {total_bayar_2015}")

print(f"total diskon yang anda dapatkan : {total_diskon_persen}")
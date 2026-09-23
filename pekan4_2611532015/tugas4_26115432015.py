print("===SISTEM LOKET ALPRO ADVENTURE PARK===")
nama_2015 = input("\nMasukkan nama pengunjung\t\t : ")
umur_2015 = int(input("Masukkan umur pengunjung\t\t : "))
sim_2015 = input("Apakah anda sudah punya SIM C? (y/t)\t : ").strip().lower()[0]


print("\n\t\t====pilihan paket wahana====".upper())
print("\n\t1. Wahana Safari Rimba (Rp. 50.000)")
print("\t2. Wahana Arung Jeram (Rp. 75.000)")
print("\t3. Wahana Motor ATV Ekstrim (Rp. 120.000)")
print("\t4. Wahana Roller Coaster Kilat (Rp. 100.000)")
print("\t5. Wahana All-Access VIP (Rp. 220.000)")
paket_2015 = int(input("\n\tMasukkan nomor paket yang anda inginkan(1-5) : "))

match paket_2015:
    case 1:
        nama_wahana_2015 = "Wahana Safari Rimba"
        harga_satuan_2015 = 50000
    case 2:
        nama_wahana_2015 = "Wahana Arung Jeram"
        harga_satuan_2015 = 75000
    case 3:
        nama_wahana_2015 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2015 = 120000
    case 4:
        nama_wahana_2015 = "Wahana Roller Coaster Kilat"
        harga_satuan_2015 = 100000
    case 5:
        nama_wahana_2015 = "Wahana All-Access VIP"
        harga_satuan_2015 = 220000
    case _:
        print("Paket Wahana tidak valid!")
        exit()

jumlah_tiket_2015 = int(input("\tMasukkan jumlah tiket anda\t\t : "))
# if tunggal
if jumlah_tiket_2015 <= 0:
    print("\n==TIKET TIDAK VALID==")
    exit()

is_member_2015 = input("\tApakah anda member? (y/t)\t\t : ").strip().lower()[0]
kode_promo_valid_2015 = input("\tApakah kode promo valid? (y/t)\t : ").strip().lower()[0]

print("\n\t===KELAYAKAN PENGENDARA WAHANA===")
if paket_2015 == 3:
    if umur_2015 >= 17 and sim_2015 == "y":
        print("\tStatus Akses: Anda sudah dewasa dan boleh mengendarai ATV sendiri")
    elif umur_2015 >= 17 and sim_2015 != "y":
        print("\tStatus Akses: Anda sudah dewasa tetapi tidak boleh mengendarai ATV sendiri")
    elif umur_2015 < 17 and sim_2015 == "y":
        print("\tStatus Akses: Identitas tidak valid: Anda belum cukup umur untuk memiliki SIM")
    else:
        print("\tStatus Akses: Anda belum cukup umur dan tidak boleh bawa motor ATV")

# untuk selain paket 3
if umur_2015 >= 10:
    print("\tStatus Akses: Anda memenuhi syarat minimum untuk wahana ini")
else:
    print("\tStatus Akses: Anda belum memenuhi syarat minimum untuk wahana ini")

# hitung diskon
subtotal_2015 = harga_satuan_2015 * jumlah_tiket_2015
total_diskon_persen = 0

if subtotal_2015 >= 200000:
    total_diskon_persen += 10  # diskon belanja besar
if is_member_2015 in ['y', 'ya']:
    total_diskon_persen += 5   # diskon member
if kode_promo_valid_2015 in ["y", "ya"]:
    total_diskon_persen += 15  # diskon voucher promo
if jumlah_tiket_2015 >= 5:
    total_diskon_persen += 5   # diskon tambahan rombongan

nominal_diskon_2015 = subtotal_2015 * (total_diskon_persen / 100)
total_bayar_2015 = subtotal_2015 - nominal_diskon_2015

print("\n\t===RINCIAN PEMBAYARAN===")
print(f"\tSubtotal Belanja : Rp. {subtotal_2015:,.0f}")
print(f"\tTotal Diskon\t : {total_diskon_persen}%")
print(f"\tTotal Bayar\t : Rp. {total_bayar_2015:,.0f}")

if total_bayar_2015 >= 300000:
    print("\n\tCatatan Layanan: Selamat! Anda berhak mendapatkan Souvenir Gratis")
else:
    print("\tCatatan Layanan: Terima kasih telah berkunjung")

print("\n\t\t====Program Selesai====")
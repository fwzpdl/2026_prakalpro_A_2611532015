umur_2015 = int(input("Masukkan umur anda : "))
sim_2015 = input("Apakah anda sudah memiliki SIM  (y/t) : ")[0]

if umur_2015 >= 17 and sim_2015 == "y":
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_2015 >= 17 and sim_2015 != "y":
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_2015 < 17 and sim_2015 == "y":
    print("Anda belum cukup umur untuk punya SIM")

if umur_2015 < 17 and sim_2015 != "y":
    print("Anda belum cukup umur bawa motor")
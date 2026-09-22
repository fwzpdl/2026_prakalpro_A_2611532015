umur_2015 = int(input("Masukkan umur anda : "))
sim_2015 = input("Apakah anda sudah memiliki SIM C (y/t) : ")[0]

if umur_2015 >= 17 and sim_2015 == "y":
    print("Anda sudah dewasa dan boleh bawa motor")

elif umur_2015 >= 17 and sim_2015 != "y":
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

elif umur_2015 < 17 and sim_2015 == "y":
    print("Anda belum cukup umur untuk punya SIM")

else:
    print("Anda belum cukup umur bawa motor")

print("Program selesai")

sisi_2015 = int(input("Masukkan panjang sisi : "))
for i_2015 in range(1, sisi_2015 + 1):
   for j_2015 in range(sisi_2015 - i_2015):
      print(" ", end="")
   for k_2015 in range(i_2015):
      print("*", end=" ")
   print()
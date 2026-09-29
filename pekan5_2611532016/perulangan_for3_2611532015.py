ulang_2015 = int(input("Masukkan jumlah_2015 perulangan : "))
jumlah_2015 = 0
for i in range(1, ulang_2015+1):
    print(i, end=" ")
    jumlah_2015 += i

    if i < ulang_2015:
        print("+", end=" ")
    else:
        print("=", jumlah_2015, end=" " )

print()
print("Jumlah =", jumlah_2015)
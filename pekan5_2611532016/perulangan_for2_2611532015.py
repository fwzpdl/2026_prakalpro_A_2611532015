#buat program perulangan for dalam python

ulang_2015 = int(input("Masukkan jumlah perulangan : "))
print("Perulangan ke-0 sampai ke", ulang_2015-1)

for i in range(ulang_2015):
    print(i, end=" ")
print()

print("Perulangan ke-1 sampai ke-", ulang_2015)
for i in range(1, ulang_2015+1):
    print(i, end=" ")
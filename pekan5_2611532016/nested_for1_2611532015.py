batas_2015 = int(input("Masukkan nilai batas: "))
for line_2015 in range(1, batas_2015+1):
    for j_2015 in range(1, (-1 * line_2015 + batas_2015) + 1):
        print(".", end=" ")
    print(line_2015)


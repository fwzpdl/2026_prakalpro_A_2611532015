tinggi_2015 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2015 %2  != 0:
    print("Tinggi harus bilangan genap!!")
else:
    a_2015 = tinggi_2015
    c_2015 = a_2015
    lebar_2015 = (2 * tinggi_2015 ) - 2

    for i_2015 in range (1, tinggi_2015 + 1):
        b_2015 = c_2015 + 1

        for j_2015 in range(1, lebar_2015 + 1):
            # baris atas dan bawah
            if i_2015 == 1 or i_2015 == tinggi_2015:
                if j_2015 == 1 or j_2015 == lebar_2015:
                    print("#", end="")
                else:
                    print("=", end="")
            else:
                if j_2015 == 1 or j_2015 == lebar_2015:
                    print("|", end="")
                else:
                    if j_2015 == c_2015:
                        print("<", end="")
                    elif j_2015 == b_2015:
                        print(">", end="")
                    elif j_2015 == (lebar_2015 - c_2015):
                        print("<", end="")
                    elif j_2015 == (lebar_2015 - c_2015 + 1):
                        print(">", end="")
                    elif j_2015 > b_2015 and j_2015 < (lebar_2015 - c_2015):
                        print(".", end="") 
                    else:
                        print(" ", end="")
        print()

# logika asli java
        a_2015 -= 2
        if a_2015 <= 0:
            c_2015  =  (-a_2015) + 2
        else:
            c_2015 = a_2015

                    
                    


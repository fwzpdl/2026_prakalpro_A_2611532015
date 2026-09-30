print("=====PROGRAM JAM PASIR KRISTAL POLINDROMIK (PEKAN 5)===")
n_2015 = int(input("Masukkan ukuran skala jam pasir : "))

print("#", end="")
for i_2015 in range(4 * n_2015 + 5):
    print("=", end="")
print("#", end="")
print()

for baris_2015 in range(n_2015, 0, -1):
    print("| ", end="")
    for s_2015 in range(2*(n_2015 - baris_2015)):
        print(" ", end="")
    for a_2015 in range(baris_2015, 0, -1):
        print(a_2015, end="")
        print(" ", end="")
    print("<*>", end="")
    for a_2015 in range(1, baris_2015 + 1):
        print(" ", end="")
        print(a_2015, end="")
    for s_2015 in range(2*(n_2015 - baris_2015)):
        print(" ", end="")
    print(" |", end="")
    print()

print("|", end="")
for s_2015 in range(2*n_2015 + 1):
    print(' ', end="")
print("<*>", end="")
for s_2015 in range(2*n_2015 + 1):
    print(' ', end="")
print("|", end="")
print()

for baris_2015 in range(1, n_2015+1):
    print("| ", end="")
    for s_2015 in range(2*(n_2015 - baris_2015)):
        print(" ", end="")
    for a_2015 in range(1, baris_2015+1):
        print(a_2015,end="")
        print(" ", end="")
    print("<*>", end=" ")
    for a_2015 in range(1, baris_2015+1):
            print(a_2015,end="")
            print(" ", end="")
    for s_2015 in range(2*(n_2015 - baris_2015)):
            print(" ", end="")
    print("|", end="")
    print()
print("#", end="")
for i_2015 in range(4*n_2015 + 5):
     print("=", end="")
print("#", end="")


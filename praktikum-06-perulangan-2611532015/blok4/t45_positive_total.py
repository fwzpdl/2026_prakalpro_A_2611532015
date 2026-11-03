result = 0
while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break
    if number == 0:
        continue

    print(f"Positive number : {number}")
    result += number

    # program untuk memberhentikan loop, di panduan tidak ada pak
    isStop = input("Apakah ingin lanjut?(n/y): ")
    if isStop == "n": 
        break

print(f"Result : {result}")

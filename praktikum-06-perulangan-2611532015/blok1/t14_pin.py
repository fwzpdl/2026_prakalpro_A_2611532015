pin = input("Enter pin :")
correct_pin = "1234"

attempt = 1
MAX_ATTEMPS = 3

if pin == correct_pin:
    print("Access granted")
else:
    print("Incorrect pin")


while pin != correct_pin and attempt < MAX_ATTEMPS:
    pin = input("Enter pin : ")
    attempt += 1

print("Account locked")

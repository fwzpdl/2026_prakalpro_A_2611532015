from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2015 = float(input('Masukkan nilai jari-jari: '))
luas_2015 = PI * jari_2015 * jari_2015
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2015, luas_2015))
angka_pertama = int(input("Masukkan angka pertama = "))
angka_kedua = int(input("Masukkan angka Kedua = "))

metode = int(input("pilih metode = "))

if metode == 1:
    print("hasilnya", angka_pertama + angka_kedua)
elif metode == 2:
    print("hasilnya", angka_pertama - angka_kedua)
elif metode == 3:
    print("hasilnya", angka_pertama * angka_kedua)
else:
    print("eror")

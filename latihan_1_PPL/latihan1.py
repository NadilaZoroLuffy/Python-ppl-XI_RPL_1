# membuat variabel atau box bernama buah
buah = ["apel", "anggur", "semangka", "kiwi", "alpukat", "mangga", "pear"]
sayur = ["pockoy", "sledri", "bayam", "kangkung", "asam"]

#operasi aritmatika tipe data list
jualan_hari_ini = buah + sayur
print(jualan_hari_ini)

for gerobak in jualan_hari_ini:
    print(gerobak)

# tampilakan data yg ada divariabel 2
print(buah)

# tampilaka data yang berurutan dari awal hingga akhir
for gerobak in buah:
    print(gerobak)

# cara tampilkan 1 nama
    print(buah[0])

# cara tampilkan 2 nama
    print(buah[2],buah[4])

# cara menambahkan item buah dipaling belakang
buah.append("pisang")
print (buah)

#cara menghapus item yg ada dibuah
buah.remove("kiwi")
print(buah)

#cara menghapus item yg ada dibuah sebanyak-bnyknya tidak mengggunakan variabel
print(buah[1:3])

#cara nambahin data 
kasir = input("Mau tambah apa lagi? : ")
buah.append(kasir)
print(buah)
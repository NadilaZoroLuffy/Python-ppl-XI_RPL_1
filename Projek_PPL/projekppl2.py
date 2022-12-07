#Fungsi Garisnya 
def garis1():
    print ("==========================================")

def garis2():
    print ("------------------------------------------")

#Perpus Kosong Untuk Menyimpan Buku
buku = []

#Fungsi Show Buku ( Perlihatkan Buku)
def show_buku():
    if len(buku) <= 0:
        print("Buku Kosong Tsay")
        garis2()
    else:
        for indeks in range(len(buku)):
            garis1()
            print("[{}] {}".format (indeks, buku [indeks]))
            garis1()

#Fungsi Untuk Edit Buku
def edit_buku():
    show_buku()
    indeks = int(input("Inputkan ID Buku : "))
    if indeks > len(buku):
        print("ID Salah")
        garis2()
    else:
        Judul_Baru = input("Judul Baru : ")
        buku[indeks] = Judul_Baru
        garis2()
        print("Buku Berhasil Ditambahkan")
        show_buku()
        garis1()

#Fungsi Insert Buku
def insert_buku():
    garis1()
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)
    garis2()
    print("Buku Berhasil Ditambahkan")
    garis1()

#Fungsi Delete Buku
def delete_buku():
    show_buku()
    indeks = int(input("Inputkan ID Buku : "))
    if indeks > len(buku):
        print ("ID SALAH")
    else:
        buku.remove(buku[indeks])
        garis1()
        print ("Buku berhasil dihapus!")
        garis2()

#Menu Untuk Tampilan Perpustakaan
def show_menu():
    print("\n")
    print("--Selamat Datang Di Prpustakaan--")
    print("1. Show Data")
    print("2. Insert Data")
    print("3. Edit Data")
    print("4. Delete Data")
    print("5. Keluar")

    menu = int(input("Pilih Menu : > "))
    
    if menu == 1:
        show_buku()
    elif menu == 2:
        insert_buku()
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delete_buku()
    elif menu == 5:
        exit()
    else:
        print("Upss Salahh")
#Tampilkan Menu
if __name__ == "__main__":
    while True:
        show_menu()
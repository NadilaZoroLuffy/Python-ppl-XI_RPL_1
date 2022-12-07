#latihan atribut
#class siswa
class siswa:
    nama = None
    mantan = None

    def perkenalan(self):
        print(f' perkenalkan saya {self.nama} dan nama mantan saya adalah {self.mantan}')

dhea = siswa()
dhea.nama = "Dhea aisya andhini"
dhea.mantan = "firgi"

dhea.perkenalan()
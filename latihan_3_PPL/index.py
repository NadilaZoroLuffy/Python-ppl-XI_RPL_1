# Buat 3 Object Orang , Pelajar, Pekerja
# 3 Orang = kelas Induk
# Pelajar, Pekerja = Kelas Turunan

class Orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
    
    def perkenalan(self):
        print("annyeong nae ileum-eun",self.nama,"naneun chulsin-ida",self.asal)

class Pelajar(Orang):
    def __init__(self, nama, asal, sekolah):
        Orang.__init__(self, nama, asal)
        self.sekolah = sekolah

class Pekerja(Orang):
    def __init__(self, nama, asal, kantor):
        super().__init__(nama, asal)
        self.kantor = kantor

minho = Orang('Lee Minho','Jakarta')
minho.perkenalan()

dohyun = Pelajar('Lee dohyun','Subang', 'SMKJP1')
dohyun.perkenalan()
print(f'naneun haggyoeseo wass-eoyo {dohyun.sekolah}\n')

jongsuk = Pekerja('Lee Jongsuk', 'Bandung', 'SM Entrataiment')
jongsuk.perkenalan()
print(f'naneun eseo ilhanda {jongsuk.kantor}\n')
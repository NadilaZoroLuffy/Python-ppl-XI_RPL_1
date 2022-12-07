# Praktek Enkapsulasi
# Buatlah Masing2 parameter
# Siswa - Public
# Guru - Protected
# Kepsek - Private

#Tampilkan 
# 1. Siswa kami bernama euroski  yg ganteng
# 2. Guru kami bernama bu anita yg cantik
# 3. Kepsek kami bernama pak lilik

#Public
class siswa:
    def __init__(self,siswa):
        self.siswa = siswa

euroski = siswa('Euroski')
print(f'Siswa kami bernama{euroski.siswa}')

#Protected
class Buguru:
    def __init__(self, guru):
        self._guru = guru

class gurucans(Buguru):
    def __init__(self, guru):
        super().__init__(guru)

    def guyu(self):
        print(f'Guru Kami Bernama {self._guru}\n')

cwek = gurucans('Anita')
cwek.guyu()

# Private

class kepsek:
    def __init__(self, keps):
        self.__keps = keps 

    def tampilkan_kepsek(self):
        print(f'Nama Kepseknya {self.__keps}')

sklh = kepsek('Pak Lilik')
sklh.tampilkan_kepsek()

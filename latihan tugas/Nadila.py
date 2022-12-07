class Agama:
    def __init__(self, nama, agama):
        self.nama = nama
        self.agama = agama

    def perkenalan(self):
        print(self.nama,"Beragama",self.agama)
        
class Islam(Agama):
    def __init__(self, nama, agama, sholat):
        Agama.__init__(self, nama, agama)
        self.sholat = sholat

class Kristen(Agama):
        def __init__(self, nama, agama, sembahyang):
            super().__init__(nama,agama)
            self.sembahyang = sembahyang


hisyam = Islam('Hisyam', 'Islam', 'Sholat')
hisyam.perkenalan()
print(f'Hisyam Beribadah Dengan Melakukan {hisyam.sholat}\n')

abraham = Kristen('Abraham', 'Kristen', 'Sembahyang')
abraham.perkenalan()
print(f'Abraham Beribadah Dengan Melakukan {abraham.sembahyang}\n')

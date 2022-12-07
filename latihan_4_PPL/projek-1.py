# Jenis enkapsulasi : public, protected, private

# membuat public class
class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi;

# instansasi
segitiga_besar = segitiga(100, 80)

# print
print('Ini adalah public class')

print(f'Alas : {segitiga_besar.alas}')
print(f'Tinggi : {segitiga_besar.tinggi}')
print(f'Luas : {segitiga_besar.luas}\n')

# membuat protected class

class mobil: #class Induk
    def __init__(self,merk):
        self._merk = merk #protected class declaration

class mobilefwan(mobil): #class turunan
    def __init__(self, merk, total_gear):
        super().__init__(merk) #panggil merk diabgian sini
        self._total_gear = total_gear

    def pamer(self):
        #hak akses_merk dari subclass
        print(f'Ini adalah mobil {self._merk} dengan total gearnya {self._total_gear}\n')

#instansasi 
print('Ini adalah protected class')
ferrari = mobilefwan('Ferrari ',8)
ferrari.pamer()

#Membuat private class
class motor:
    def __init__(self, merk):
        self.__merk = merk #private class decoration

    def tampilkan_merk(self):
        print(f'Merk Motornya : {self.__merk}')
        #panggil private disini

#instansasi
print('Ini adalah private class')
moge = motor('Harley')
moge.tampilkan_merk()
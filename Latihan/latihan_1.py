#belajar object dan class

class kocheng : 
    warna = None
    usia = None

#membuat instance/variabel sebagai "obyek nyata"
kocheng1 = kocheng()
kocheng1.warna ="grey"
kocheng1.usia ="4 Bulan"

kocheng2 = kocheng()
kocheng2.warna ="white"
kocheng2.usia ="3 Bulan"

print(kocheng1.warna, kocheng1.usia)
print(kocheng2.warna, kocheng2.usia)


#masing2 manusia mempunyai organ hati, masing2 manusia mempunyai nama yang berbeda

class organ_tubuh:
    torso = "Hati"

class identitas:
    nama = None

orang = organ_tubuh()
orang = identitas()
orang.torso = "Hati"
orang.nama = "Nisa"

print(orang.nama,"mempunyai", orang.torso,"yang baik dan tidak sombong")

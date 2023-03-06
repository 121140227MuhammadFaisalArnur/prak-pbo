class Orang_Faisal_227:
    
    def __init__(self,nama,nim,kelas,sks,):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.sks = sks
    
    def manggil_orang(self):
        print ("Hai",self.nama, "Nim kamu", self.nim, "Kamu Kelas",self.kelas,". dan sks kamu",self.sks)

orang1 = Orang_Faisal_227("Yanto", 1405, "RB", 4)

orang1.manggil_orang()
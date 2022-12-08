#Bu kısımda gerekli kütüphaneleri içe aktarıyoruz.
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import requests

#Bu kısımda bir pencere oluşturuyoruz.
class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Instagram Video İndirme")
        self.setGeometry(100, 100, 300, 200)

        #Bu kısımda pencerenin içeriğini oluşturuyoruz.
        #Bu içeriğe, video bağlantısı girdi alanı ve indir düğmesi ekliyoruz.
        self.baglanti = QtWidgets.QLineEdit(self)
        self.baglanti.move(100, 50)
        self.indir = QtWidgets.QPushButton("İndir", self)
        self.indir.move(100, 75)
        self.indir.clicked.connect(self.video_indir)

    #Bu kısımda video indiriliyor ve kaydediliyor.
    def video_indir(self):
        #Bu kısımda verilen bağlantıdan video dosyasını indiriyoruz.
        baglanti = self.baglanti.text()
        response = requests.get(baglanti)
        video_dosyasi = response.content

        #Bu kısımda indirilen video dosyasını kaydediyoruz.
        with open("video.mp4", "wb") as f:
            f.write(video_dosyasi)

        #Bu kısımda indirme işlemi tamamlandıktan sonra bir mesaj yazdırılıyor.
        self.sonuc = QtWidgets.QLabel("İndirme tamamlandı!", self)
        self.sonuc.move(100, 100)
        self.sonuc.show()

#Bu kısımda pencere çalıştırılıyor.
if __name__ == "__main__":
    uygulama = QApplication([])
    p

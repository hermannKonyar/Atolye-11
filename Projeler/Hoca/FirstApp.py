import sys
import os
import audioplayer

from PyQt5.QtWidgets import QLabel, QListWidget, QWidget, QApplication, QPushButton, QVBoxLayout, QFileDialog, \
    QHBoxLayout


class Mp3Player(QWidget):
    def __init__(self):

        super().__init__()
        self.dosyaIsmi = None
        self.muzikList = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Mp3 Player")
        self.buton1 = QPushButton("Oynat")
        self.buton2 = QPushButton("Aç")
        self.buton3 = QPushButton("Durdur")
        self.buton4 = QPushButton("Devam Et")
        self.buton5 = QPushButton("Sesi Arttır")
        self.buton6 = QPushButton("Sesi Azalt")
        self.yaziAlani = QLabel("")
        self.listem = QListWidget()

        hBox0 = QHBoxLayout()
        hBox0.addWidget(self.listem)

        hBox = QHBoxLayout()
        hBox.addWidget(self.buton1)
        hBox.addWidget(self.buton2)

        hBox1 = QHBoxLayout()
        hBox1.addWidget(self.buton3)
        hBox1.addWidget(self.buton4)

        hBox2 = QHBoxLayout()
        hBox2.addWidget(self.buton5)
        hBox2.addWidget(self.buton6)

        vBox = QVBoxLayout()
        vBox.addLayout(hBox0)
        vBox.addWidget(self.yaziAlani)
        vBox.addStretch()
        vBox.addLayout(hBox)
        vBox.addLayout(hBox1)
        vBox.addLayout(hBox2)
        self.setLayout(vBox)
        self.setFixedSize(300, 400)

        self.buton2.clicked.connect(self.klasorAc)
        self.buton1.clicked.connect(self.oynat)
        self.buton3.clicked.connect(self.durdur)
        self.buton4.clicked.connect(self.devamEt)
        self.buton5.clicked.connect(self.sesiArttir)
        self.buton6.clicked.connect(self.sesiAzalt)

        self.show()

    def klasorAc(self):
        self.dosyaIsmi = QFileDialog.getOpenFileName(self, "Dosya Seç", os.getenv("HOME"), "Mp3 (*mp3)")
        isimler = self.dosyaIsmi[0]
        self.muzikList.append(isimler)
        isimler2 = isimler.split("/")
        self.listem.addItem(isimler2[-1])

    def oynat(self):
        try:
            ad = self.listem.selectedItems()[0].text()
            print(ad)
            for i in self.muzikList:
                if i.split("/")[-1] == ad:
                    ad = i
            print(ad)
            self.muzik = audioplayer.AudioPlayer(ad)
            self.muzik.play(loop=False, block=False)
        except:
            self.yaziAlani.setText("Yanlış İşlem yaptınız...")

    def durdur(self):
        try:
            self.muzik.pause()
        except:
            self.yaziAlani.setText("Yanlış İşlem yaptınız...")

    def devamEt(self):
        try:
            self.muzik.resume()
        except:
            self.yaziAlani.setText("Yanlış İşlem yaptınız...")

    def sesiArttir(self):
        try:
            self.muzik.volume += 10
        except:
            self.yaziAlani.setText("Yanlış İşlem yaptınız...")

    def sesiAzalt(self):
        try:
            self.muzik.volume -= 10
        except:
            self.yaziAlani.setText("Yanlış İşlem yaptınız...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mp3Player = Mp3Player()
    sys.exit(app.exec_())
    print("Program sonlandırıldı...")
    for i in range(100000):
        print(i)
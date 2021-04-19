import vacheTaureau2
from PyQt5 import QtWidgets, QtGui
from random import randint

def test(n):
    for i in range(len(str(n))):
        if str(n)[i] in str(n)[i+1:]:
            return False
    return True

def leentier():
    x = False
    while not x:
        n = randint(1023, 9999)
        x = test(n)
    return n

def vacheouTaureau(n,x):
    ch = str(n)
    ch2 = str(x)
    v = 0
    t = 0
    for i in range(len(ch)):
        if ch[i] == ch2[i]:
            t += 1
    for i in range(len(ch)):
        if ch[i] != ch2[i] and ch[i] in ch2:
            v += 1
    return (v,t)

class designWindow(QtWidgets.QMainWindow, vacheTaureau2.Ui_MainWindow):
    def __init__(self):
        super(designWindow, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("vache taureau v1.0")
        self.setWindowIcon(QtGui.QIcon('cow.png'))

        self.pushButton_0.clicked.connect(self.degitpressed)
        self.pushButton_1.clicked.connect(self.degitpressed)
        self.pushButton_2.clicked.connect(self.degitpressed)
        self.pushButton_3.clicked.connect(self.degitpressed)
        self.pushButton_4.clicked.connect(self.degitpressed)
        self.pushButton_5.clicked.connect(self.degitpressed)
        self.pushButton_6.clicked.connect(self.degitpressed)
        self.pushButton_7.clicked.connect(self.degitpressed)
        self.pushButton_8.clicked.connect(self.degitpressed)
        self.pushButton_9.clicked.connect(self.degitpressed)
        self.ok.clicked.connect(self.provide)
        self.pushButton.clicked.connect(self.rejouer)
        self.indice = 0
        self.lentier = leentier()


    def degitpressed(self):
        button = self.sender()
        if self.Ecran.text() == "Hello":
            self.Ecran.setText("")
        self.Ecran.setText(self.Ecran.text() + button.text())
        if len(self.Ecran.text()) == 5:
            self.Ecran.setText("")
        elif self.Ecran.text() == "0":
            self.Ecran.setText("")

    def provide(self):
        x = self.lentier
        #print(x)
        if len(self.Ecran.text()) < 4:
            self.Ecran.setText("")
        elif len(self.Ecran.text()) == 4:
            self.indice += 1
            if self.indice == 1:
                self.label_e1.setText(self.Ecran.text())
                n = int(self.Ecran.text())
                t = vacheouTaureau(n,x)
                self.label_011.setText(str(t[0]))
                self.label_021.setText(str(t[1]))
                self.Ecran.setText("")
                if t[1] == 4:
                    self.Ecran.setText("Bravo")
                    self.indice = 0
                    self.pushButton_0.setDisabled(True)
                    self.pushButton_1.setDisabled(True)
                    self.pushButton_2.setDisabled(True)
                    self.pushButton_3.setDisabled(True)
                    self.pushButton_4.setDisabled(True)
                    self.pushButton_5.setDisabled(True)
                    self.pushButton_6.setDisabled(True)
                    self.pushButton_7.setDisabled(True)
                    self.pushButton_8.setDisabled(True)
                    self.pushButton_9.setDisabled(True)
                    self.ok.setDisabled(True)
            elif self.indice == 2:
                self.label_e2.setText(self.Ecran.text())
                n = int(self.Ecran.text())
                t = vacheouTaureau(n,x)
                self.label_012.setText(str(t[0]))
                self.label_022.setText(str(t[1]))
                self.Ecran.setText("")
                if t[1] == 4:
                    self.Ecran.setText("Bravo")
                    self.indice = 0
                    self.pushButton_0.setDisabled(True)
                    self.pushButton_1.setDisabled(True)
                    self.pushButton_2.setDisabled(True)
                    self.pushButton_3.setDisabled(True)
                    self.pushButton_4.setDisabled(True)
                    self.pushButton_5.setDisabled(True)
                    self.pushButton_6.setDisabled(True)
                    self.pushButton_7.setDisabled(True)
                    self.pushButton_8.setDisabled(True)
                    self.pushButton_9.setDisabled(True)
                    self.ok.setDisabled(True)
            elif self.indice == 3:
                self.label_e3.setText(self.Ecran.text())
                n = int(self.Ecran.text())
                t = vacheouTaureau(n,x)
                self.label_013.setText(str(t[0]))
                self.label_023.setText(str(t[1]))
                self.Ecran.setText("")
                if t[1] == 4:
                    self.Ecran.setText("Bravo")
                    self.indice = 0
                    self.pushButton_0.setDisabled(True)
                    self.pushButton_1.setDisabled(True)
                    self.pushButton_2.setDisabled(True)
                    self.pushButton_3.setDisabled(True)
                    self.pushButton_4.setDisabled(True)
                    self.pushButton_5.setDisabled(True)
                    self.pushButton_6.setDisabled(True)
                    self.pushButton_7.setDisabled(True)
                    self.pushButton_8.setDisabled(True)
                    self.pushButton_9.setDisabled(True)
                    self.ok.setDisabled(True)
            elif self.indice == 4:
                self.label_e4.setText(self.Ecran.text())
                n = int(self.Ecran.text())
                t = vacheouTaureau(n,x)
                self.label_014.setText(str(t[0]))
                self.label_024.setText(str(t[1]))
                self.Ecran.setText("")
                if t[1] == 4:
                    self.Ecran.setText("Bravo")
                    self.indice = 0
                    self.pushButton_0.setDisabled(True)
                    self.pushButton_1.setDisabled(True)
                    self.pushButton_2.setDisabled(True)
                    self.pushButton_3.setDisabled(True)
                    self.pushButton_4.setDisabled(True)
                    self.pushButton_5.setDisabled(True)
                    self.pushButton_6.setDisabled(True)
                    self.pushButton_7.setDisabled(True)
                    self.pushButton_8.setDisabled(True)
                    self.pushButton_9.setDisabled(True)
                    self.ok.setDisabled(True)
            elif self.indice == 5:
                self.label_e5.setText(self.Ecran.text())
                n = int(self.Ecran.text())
                t = vacheouTaureau(n,x)
                self.label_015.setText(str(t[0]))
                self.label_025.setText(str(t[1]))
                self.Ecran.setText("")
                if t[1] == 4:
                    self.Ecran.setText("Bravo")
                    self.indice = 0
                    self.pushButton_0.setDisabled(True)
                    self.pushButton_1.setDisabled(True)
                    self.pushButton_2.setDisabled(True)
                    self.pushButton_3.setDisabled(True)
                    self.pushButton_4.setDisabled(True)
                    self.pushButton_5.setDisabled(True)
                    self.pushButton_6.setDisabled(True)
                    self.pushButton_7.setDisabled(True)
                    self.pushButton_8.setDisabled(True)
                    self.pushButton_9.setDisabled(True)
                    self.ok.setDisabled(True)
            elif self.indice == 6:
                self.label_e6.setText(self.Ecran.text())
                n = int(self.Ecran.text())
                t = vacheouTaureau(n,x)
                self.label_016.setText(str(t[0]))
                self.label_026.setText(str(t[1]))
                self.Ecran.setText("")
                if t[1] == 4:
                    self.Ecran.setText("Bravo")
                    self.indice = 0
                    self.pushButton_0.setDisabled(True)
                    self.pushButton_1.setDisabled(True)
                    self.pushButton_2.setDisabled(True)
                    self.pushButton_3.setDisabled(True)
                    self.pushButton_4.setDisabled(True)
                    self.pushButton_5.setDisabled(True)
                    self.pushButton_6.setDisabled(True)
                    self.pushButton_7.setDisabled(True)
                    self.pushButton_8.setDisabled(True)
                    self.pushButton_9.setDisabled(True)
                    self.ok.setDisabled(True)
            elif self.indice == 7:
                self.label_e7.setText(self.Ecran.text())
                n = int(self.Ecran.text())
                t = vacheouTaureau(n,x)
                self.label_017.setText(str(t[0]))
                self.label_027.setText(str(t[1]))
                self.Ecran.setText("")
                if t[1] == 4:
                    self.Ecran.setText("Bravo")
                else:
                    self.Ecran.setText(":"+str(self.lentier)+":")
                self.pushButton_0.setDisabled(True)
                self.pushButton_1.setDisabled(True)
                self.pushButton_2.setDisabled(True)
                self.pushButton_3.setDisabled(True)
                self.pushButton_4.setDisabled(True)
                self.pushButton_5.setDisabled(True)
                self.pushButton_6.setDisabled(True)
                self.pushButton_7.setDisabled(True)
                self.pushButton_8.setDisabled(True)
                self.pushButton_9.setDisabled(True)
                self.ok.setDisabled(True)

    def rejouer(self):
        self.indice = 0
        self.lentier = leentier()
        self.Ecran.setText("Hello")
        self.label_e1.setText("")
        self.label_e2.setText("")
        self.label_e3.setText("")
        self.label_e4.setText("")
        self.label_e5.setText("")
        self.label_e6.setText("")
        self.label_e7.setText("")
        self.label_011.setText("0")
        self.label_012.setText("0")
        self.label_013.setText("0")
        self.label_014.setText("0")
        self.label_015.setText("0")
        self.label_016.setText("0")
        self.label_017.setText("0")
        self.label_021.setText("0")
        self.label_022.setText("0")
        self.label_023.setText("0")
        self.label_024.setText("0")
        self.label_025.setText("0")
        self.label_027.setText("0")
        self.label_026.setText("0")
        self.pushButton_0.setDisabled(False)
        self.pushButton_1.setDisabled(False)
        self.pushButton_2.setDisabled(False)
        self.pushButton_3.setDisabled(False)
        self.pushButton_4.setDisabled(False)
        self.pushButton_5.setDisabled(False)
        self.pushButton_6.setDisabled(False)
        self.pushButton_7.setDisabled(False)
        self.pushButton_8.setDisabled(False)
        self.pushButton_9.setDisabled(False)
        self.ok.setDisabled(False)
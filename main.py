import designWindow
from PyQt5 import QtWidgets
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = designWindow.designWindow()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
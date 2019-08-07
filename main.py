import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from postboy import Postboy_window

def app():
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("IMG/icon.icns"))
    postboy = Postboy_window()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()

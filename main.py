import sys
from PyQt5.Qt import QApplication

from window import MainReceivePanel, MainSendPanel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainReceivePanel()
    m = MainSendPanel()
    w.show()
    m.show()
    sys.exit(app.exec_())

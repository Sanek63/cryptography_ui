import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QMainWindow, QApplication


__all__ = ['MainReceivePanel']


class Ui_ReceiveWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 299)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.reverce_label = QtWidgets.QLabel(self.centralwidget)
        self.reverce_label.setGeometry(QtCore.QRect(20, 10, 181, 51))

        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.reverce_label.setFont(font)
        self.reverce_label.setObjectName("reverce_label")

        self.message_receive_label = QtWidgets.QLabel(self.centralwidget)
        self.message_receive_label.setGeometry(QtCore.QRect(20, 60, 81, 21))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.message_receive_label.setFont(font)
        self.message_receive_label.setObjectName("message_receive_label")

        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(20, 160, 81, 31))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")

        self.password_text_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_text_edit.setGeometry(QtCore.QRect(80, 160, 261, 32))
        self.password_text_edit.setObjectName("password_text_edit")

        self.message_send_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.message_send_text_edit.setGeometry(QtCore.QRect(20, 80, 321, 71))
        self.message_send_text_edit.setObjectName("message_send_text_edit")

        self.decode_btn = QtWidgets.QPushButton(self.centralwidget)
        self.decode_btn.setGeometry(QtCore.QRect(280, 240, 111, 31))
        self.decode_btn.setObjectName("decode_btn")

        self.alg_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.alg_combo_box.setGeometry(QtCore.QRect(80, 200, 87, 32))
        self.alg_combo_box.setObjectName("alg_combo_box")
        self.alg_combo_box.addItem("")
        self.alg_combo_box.addItem("")
        self.alg_combo_box.addItem("")
        self.alg_combo_box.addItem("")
        self.alg_combo_box.addItem("")
        self.alg_combo_box.addItem("")

        self.alg_label = QtWidgets.QLabel(self.centralwidget)
        self.alg_label.setGeometry(QtCore.QRect(10, 200, 61, 31))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.alg_label.setFont(font)
        self.alg_label.setObjectName("alg_label")

        self.result_label = QtWidgets.QLabel(self.centralwidget)
        self.result_label.setGeometry(QtCore.QRect(370, 10, 181, 51))

        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.result_label.setFont(font)
        self.result_label.setObjectName("result_label")

        self.message_decode_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.message_decode_text_edit.setGeometry(QtCore.QRect(370, 80, 321, 141))
        self.message_decode_text_edit.setObjectName("message_decode_text_edit")

        self.message_decode_label = QtWidgets.QLabel(self.centralwidget)
        self.message_decode_label.setGeometry(QtCore.QRect(370, 60, 81, 21))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.message_decode_label.setFont(font)
        self.message_decode_label.setObjectName("message_decode_label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.reverce_label.setText(_translate("MainWindow", "Получение"))
        self.message_receive_label.setText(_translate("MainWindow", "Сообщение"))
        self.password_label.setText(_translate("MainWindow", "Пароль"))
        self.decode_btn.setText(_translate("MainWindow", "Декодировать"))
        self.alg_combo_box.setItemText(0, _translate("MainWindow", "SHA-224"))
        self.alg_combo_box.setItemText(1, _translate("MainWindow", "SHA-256"))
        self.alg_combo_box.setItemText(2, _translate("MainWindow", "SHA-384"))
        self.alg_combo_box.setItemText(3, _translate("MainWindow", "SHA-512"))
        self.alg_combo_box.setItemText(4, _translate("MainWindow", "MD4"))
        self.alg_combo_box.setItemText(5, _translate("MainWindow", "MD5"))
        self.alg_label.setText(_translate("MainWindow", "Алгоритм"))
        self.result_label.setText(_translate("MainWindow", "Результат"))
        self.message_decode_label.setText(_translate("MainWindow", "Сообщение"))


class MainReceivePanel(QMainWindow):
    def __init__(self, parent=None):
        super(MainReceivePanel, self).__init__(parent)
        self.ui = Ui_ReceiveWindow()
        self.ui.setupUi(self)

        self.setFixedSize(699, 299)
        self.settings_ui(self.ui)

    @staticmethod
    def settings_ui(ui):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainReceivePanel()
    w.show()
    sys.exit(app.exec_())

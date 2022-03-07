import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QMainWindow, QApplication


__all__ = ['MainSendPanel']


class Ui_SendWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 296)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.sha_224_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.sha_224_checkbox.setGeometry(QtCore.QRect(410, 80, 88, 22))
        self.sha_224_checkbox.setObjectName("sha_224_checkbox")

        self.hash_func_label = QtWidgets.QLabel(self.centralwidget)
        self.hash_func_label.setGeometry(QtCore.QRect(410, 10, 181, 51))

        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.hash_func_label.setFont(font)
        self.hash_func_label.setObjectName("hash_func_label")

        self.sha_256_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.sha_256_checkbox.setGeometry(QtCore.QRect(410, 100, 88, 22))
        self.sha_256_checkbox.setObjectName("sha_256_checkbox")

        self.sha_label = QtWidgets.QLabel(self.centralwidget)
        self.sha_label.setGeometry(QtCore.QRect(410, 60, 58, 18))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sha_label.setFont(font)
        self.sha_label.setObjectName("sha_label")

        self.sha_384_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.sha_384_checkbox.setGeometry(QtCore.QRect(410, 120, 88, 22))
        self.sha_384_checkbox.setObjectName("sha_384_checkbox")

        self.sha_512_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.sha_512_checkbox.setGeometry(QtCore.QRect(410, 140, 88, 22))
        self.sha_512_checkbox.setObjectName("sha_512_checkbox")

        self.md_label = QtWidgets.QLabel(self.centralwidget)
        self.md_label.setGeometry(QtCore.QRect(500, 60, 58, 18))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.md_label.setFont(font)
        self.md_label.setObjectName("md_label")

        self.md_4_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.md_4_checkbox.setGeometry(QtCore.QRect(500, 80, 88, 22))
        self.md_4_checkbox.setObjectName("md_4_checkbox")

        self.md_5_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.md_5_checkbox.setGeometry(QtCore.QRect(500, 100, 88, 22))
        self.md_5_checkbox.setObjectName("md_5_checkbox")

        self.send_label = QtWidgets.QLabel(self.centralwidget)
        self.send_label.setGeometry(QtCore.QRect(20, 10, 181, 51))

        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.send_label.setFont(font)
        self.send_label.setObjectName("send_label")

        self.message_label = QtWidgets.QLabel(self.centralwidget)
        self.message_label.setGeometry(QtCore.QRect(20, 60, 81, 21))

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.message_label.setFont(font)
        self.message_label.setObjectName("message_label")

        self.message_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.message_text_edit.setGeometry(QtCore.QRect(20, 80, 321, 71))
        self.message_text_edit.setObjectName("message_text_edit")

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

        self.submit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.submit_btn.setGeometry(QtCore.QRect(250, 240, 111, 31))
        self.submit_btn.setObjectName("submit_btn")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sha_224_checkbox.setText(_translate("MainWindow", "SHA-224"))
        self.hash_func_label.setText(_translate("MainWindow", "Хеш-функции"))
        self.sha_256_checkbox.setText(_translate("MainWindow", "SHA-256"))
        self.sha_label.setText(_translate("MainWindow", "SHA"))
        self.sha_384_checkbox.setText(_translate("MainWindow", "SHA-384"))
        self.sha_512_checkbox.setText(_translate("MainWindow", "SHA-512"))
        self.md_label.setText(_translate("MainWindow", "MD"))
        self.md_4_checkbox.setText(_translate("MainWindow", "MD4"))
        self.md_5_checkbox.setText(_translate("MainWindow", "MD5"))
        self.send_label.setText(_translate("MainWindow", "Отправление"))
        self.message_label.setText(_translate("MainWindow", "Сообщение"))
        self.password_label.setText(_translate("MainWindow", "Пароль"))
        self.submit_btn.setText(_translate("MainWindow", "Подтвердить"))


class MainSendPanel(QMainWindow):
    def __init__(self, parent=None):
        super(MainSendPanel, self).__init__(parent)
        self.ui = Ui_SendWindow()
        self.ui.setupUi(self)

        self.setFixedSize(601, 296)
        self.settings_ui(self.ui)

    @staticmethod
    def settings_ui(ui):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainSendPanel()
    w.show()
    sys.exit(app.exec_())

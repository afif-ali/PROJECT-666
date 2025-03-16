from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from pygame import mixer
import sys
import blessings

def contract(app):

    WIDTH = 700
    HEIGHT = 500

    contract_win = QMainWindow()
    contract_win.setWindowTitle("PROJECT 666")
    contract_win.setFixedSize(WIDTH, HEIGHT)
    contract_win.setWindowFlag(Qt.WindowCloseButtonHint, False)

    background_image = QLabel(contract_win)
    background_image.setPixmap(QPixmap("res/img/contract_bg_1.jpg"))
    background_image.setGeometry(0, 0, WIDTH, HEIGHT)

    larry_speech = QLabel(contract_win)
    larry_speech.setPixmap(QPixmap("res/img/larry_speech.png"))
    larry_speech.setGeometry(-80, 0, WIDTH, HEIGHT)

    larry_speech_text = QLabel(contract_win)
    larry_speech_text.setText("It’s you...\nI was waiting for you...\nThe creator has left something for you...\nbut before...\nI need to tell you something...\nBeware of IT.\n\n[PRESS SPACE]")
    larry_speech_text.setGeometry(180, 70, 360, 170)
    larry_speech_text.setStyleSheet("font-size: 16px;")
    contract_win.show()

    contract = QLabel(contract_win)
    contract.setPixmap(QPixmap("res/img/contract.jpg"))
    contract.setGeometry(100, 0, WIDTH, HEIGHT)
    
    def sign():
        msg = QMessageBox()
        msg.setText("ARE YOU SURE?")
        msg.setInformativeText("Do you really want to sign the contract???")
        msg.setWindowTitle("PROJECT666")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Yes)
        msg.exec_()
        mixer.music
        contract_win.hide()
        blessings.blessings(app)
        
        

    sign_contract = QPushButton("SIGN", contract_win)
    sign_contract.setGeometry(100, 430, 315, 50)
    sign_contract.setStyleSheet("font-size:16px; background-color:transparent;")
    sign_contract.clicked.connect(sign)


    def keyPressEvent(event):
        if event.key() == Qt.Key_Space:
            background_image.setPixmap(QPixmap("res/img/contract_bg_2.jpg"))
            larry_speech.hide()
            larry_speech_text.hide()
            contract.show()
            sign_contract.show()

    def closeEvent(event):
        event.ignore()

    contract_win.keyPressEvent = keyPressEvent
    contract_win.closeEvent = closeEvent

    mixer.init()
    mixer.music.load("res/audio/heartaches.mp3")
    mixer.music.play(-1)

    sys.exit(app.exec_())
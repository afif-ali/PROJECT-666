import ending
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import random
from pygame import mixer
import time

def demotivational_speech(app):
    WIDTH = 500
    HEIGHT = 500
    audio_text = [
        "Failure suits you!",
        "You have something on your\nchin... No, THE OTHER\nONE!",
        "Your best isn't good\nenough, AND NEITHER IS\nYOUR WORST!",
        "GIVE UP! IT'S NOT\nHAPPENING!",
        "If failure was an art,\nyou'd be the MONA LISA!",
        "You're a waste of oxygen!",
        "Life gives everyone a\npurpose, except you!\n(Apparently)",
        "You bring everyone so\nmuch joy when you\nleave the room.",
        "Your birth certificate\nis just an appology letter\nfrom the hospital!",
        "Y O U    S U C K",
        "You should kill\nyourself!",
        "You're a mistake!"
    ]
    window = QMainWindow()
    window.setWindowFlags(
            window.windowFlags() | 
            Qt.FramelessWindowHint | 
            Qt.WindowStaysOnTopHint
        )
    window.setGeometry(
        random.randrange(0, QDesktopWidget().availableGeometry().width()-WIDTH),
        random.randrange(0, QDesktopWidget().availableGeometry().height()-HEIGHT),
        WIDTH, HEIGHT)
    window.setAttribute(Qt.WA_TranslucentBackground, on=True)

    peter_pic = QLabel(window)
    peter_pic.setPixmap(QPixmap("res/img/peter.png"))
    peter_pic.setGeometry(0,0,WIDTH,HEIGHT)

    peter_speech = QLabel(window)
    peter_speech.setGeometry(240,50,200,80)
    peter_speech.setStyleSheet("font-size:16px;")

    index = random.randrange(1,12)

    peter_speech.setText(audio_text[index-1])

    window.show()

    mixer.init()
    mixer.music.load("res/audio/demotivational_speech/" + str(index) + ".mp3")
    mixer.music.play()

    while mixer.music.get_busy():
        app.processEvents()

def jumpscare(app):
    WIDTH = 500
    HEIGHT = 500
    window1 = QMainWindow()
    window1.setWindowFlags(
            window1.windowFlags() | 
            Qt.FramelessWindowHint | 
            Qt.WindowStaysOnTopHint
        )
    window1.setGeometry(
        random.randrange(0, QDesktopWidget().availableGeometry().width()-WIDTH),
        random.randrange(0, QDesktopWidget().availableGeometry().height()-HEIGHT),
        WIDTH, HEIGHT)
    window1.setAttribute(Qt.WA_TranslucentBackground, on=True)

    pic1 = QLabel(window1)
    pic1.setPixmap(QPixmap("res/img/jumpscares/"+str(random.randrange(1,10))+".png"))
    pic1.setGeometry(0,0,WIDTH,HEIGHT)
    window1.show()


    window2 = QMainWindow()
    window2.setWindowFlags(
            window2.windowFlags() | 
            Qt.FramelessWindowHint | 
            Qt.WindowStaysOnTopHint
        )
    window2.setGeometry(
        random.randrange(0, QDesktopWidget().availableGeometry().width()-WIDTH),
        random.randrange(0, QDesktopWidget().availableGeometry().height()-HEIGHT),
        WIDTH, HEIGHT)
    window2.setAttribute(Qt.WA_TranslucentBackground, on=True)

    pic2 = QLabel(window2)
    pic2.setPixmap(QPixmap("res/img/jumpscares/"+str(random.randrange(1,10))+".png"))
    pic2.setGeometry(0,0,WIDTH,HEIGHT)
    window2.show()


    window3 = QMainWindow()
    window3.setWindowFlags(
            window3.windowFlags() | 
            Qt.FramelessWindowHint | 
            Qt.WindowStaysOnTopHint
        )
    window3.setGeometry(
        random.randrange(0, QDesktopWidget().availableGeometry().width()-WIDTH),
        random.randrange(0, QDesktopWidget().availableGeometry().height()-HEIGHT),
        WIDTH, HEIGHT)
    window3.setAttribute(Qt.WA_TranslucentBackground, on=True)

    pic3 = QLabel(window3)
    pic3.setPixmap(QPixmap("res/img/jumpscares/"+str(random.randrange(1,10))+".png"))
    pic3.setGeometry(0,0,WIDTH,HEIGHT)
    window3.show()


    window4 = QMainWindow()
    window4.setWindowFlags(
            window4.windowFlags() | 
            Qt.FramelessWindowHint | 
            Qt.WindowStaysOnTopHint
        )
    window4.setGeometry(
        random.randrange(0, QDesktopWidget().availableGeometry().width()-WIDTH),
        random.randrange(0, QDesktopWidget().availableGeometry().height()-HEIGHT),
        WIDTH, HEIGHT)
    window4.setAttribute(Qt.WA_TranslucentBackground, on=True)

    pic4 = QLabel(window4)
    pic4.setPixmap(QPixmap("res/img/jumpscares/"+str(random.randrange(1,10))+".png"))
    pic4.setGeometry(0,0,WIDTH,HEIGHT)
    window4.show()


    mixer.init()
    mixer.music.load("res/audio/jumpscare.mp3")
    mixer.music.play()

    while mixer.music.get_busy():
        app.processEvents()

def dialog_spam():
    threads = []
    for i in range(20):
        for j in range(20):
            msg = QMessageBox()
            msg.setText("666")
            msg.setWindowTitle("666")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.No)
            msg.setGeometry(i*50 + j*100, i*50, 500, 200)
            msg.show()
            threads.append(msg)
    time.sleep(3)

def blessings(app):
    time.sleep(10)
    dialog_spam()
    time.sleep(10)
    jumpscare(app)
    time.sleep(10)
    demotivational_speech(app)
    time.sleep(10)
    ending.ending(app)
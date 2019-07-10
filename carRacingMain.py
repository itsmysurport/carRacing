from carRacing import *
import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)


xStat = 20
x1Stat = 20
winner = ''

def event(self):
    self.pushButton.clicked.connect(self.setXY)
    self.pushButton_2.clicked.connect(self.setXY2)
    self.restartButton.clicked.connect(self.setRestart)

def setXY(self):
    global xStat, winner
    xStat += 30
    self.frame.setGeometry(QtCore.QRect(xStat, 134, 200, 97))
    if xStat == 1310 and winner == '':
        winner = 'A Player'
        print('{} is WINNER!'.format(winner))
        self.restartButton.setText('A Player is Winner!')
        self.restartButton.setGeometry(QtCore.QRect(0, 0, 1371, 671))

def setXY2(self):
    global x1Stat, winner
    x1Stat += 30
    self.frame_2.setGeometry(QtCore.QRect(x1Stat, 435, 200, 97))
    if x1Stat == 1310 and winner == '':
        winner = 'B Player'
        print('{} is WINNER!'.format(winner))
        self.restartButton.setText('B Player is Winner!')
        self.restartButton.setGeometry(QtCore.QRect(0, 0, 1371, 671))
def setRestart(self):
        global winner
        self.restartButton.setGeometry(QtCore.QRect(460, 690, 16, 16))
        self.frame.setGeometry(QtCore.QRect(20, 134, 200, 97))
        self.frame_2.setGeometry(QtCore.QRect(20, 435, 200, 97))
        winner = ''

def updating(self):
        global x1Stat, xStat, winner
        while True:
                input_state = GPIO.input(18)
                input_state1 = GPIO.input(23)
                if input_state == False:
                        xStat += 30
                        self.frame.setGeometry(QtCore.QRect(xStat, 134, 200, 97))
                        if xStat == 1310 and winner == '':
                                winner = 'A Player'
                                print('{} is WINNER!'.format(winner))
                                self.restartButton.setText('A Player is Winner!')
                                self.restartButton.setGeometry(QtCore.QRect(0, 0, 1371, 671))
                                while GPIO.input(18) == False:
                                        pass
                if input_state1 == False:
                        x1Stat += 30
                        self.frame_2.setGeometry(QtCore.QRect(x1Stat, 435, 200, 97))
                        if x1Stat == 1310 and winner == '':
                                winner = 'B Player'
                                print('{} is WINNER!'.format(winner))
                                self.restartButton.setText('B Player is Winner!')
                                self.restartButton.setGeometry(QtCore.QRect(0, 0, 1371, 671))
                                while GPIO.input(18) == False:
                                        pass


Ui_MainWindow.event = event
Ui_MainWindow.setXY = setXY
Ui_MainWindow.setXY2 = setXY2
Ui_MainWindow.setRestart = setRestart
Ui_MainWindow.updating = updating

if __name__=="__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        ui.event()
        t = threading.Thread(target=ui.updating, args=())
        t.start()
        MainWindow.show()
        sys.exit(app.exec_())
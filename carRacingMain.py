from carRacing import *

xStat = 20
x1Stat = 20
winner = ''

def event(self):
    self.pushButton.clicked.connect(self.setXY)
    self.pushButton_2.clicked.connect(self.setXY2)

def setXY(self):
    global xStat, winner
    xStat += 30
    self.frame.setGeometry(QtCore.QRect(xStat, 134, 200, 97))
    if xStat == 1310 and winner == '':
        winner = 'A Player'
        print('{} is WINNER!'.format(winner))

def setXY2(self):
    global x1Stat, winner
    x1Stat += 30
    self.frame_2.setGeometry(QtCore.QRect(x1Stat, 435, 200, 97))
    if x1Stat == 1310 and winner == '':
        winner = 'B Player'
        print('{} is WINNER!'.format(winner))

Ui_MainWindow.event = event
Ui_MainWindow.setXY = setXY
Ui_MainWindow.setXY2 = setXY2

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.event()
    MainWindow.show()
    sys.exit(app.exec_())
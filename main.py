# MonteCarlo
# Qt Documentation: https://doc.qt.io/qtforpython/

# Импорт
import sys, math, random
from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from design import Ui_MainWindow  # импорт дизайн-файла

# Переменные, константы и флаги
initFlag = 1
InRoundCounter = 0
# Построение окна
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
ui.statusbar.showMessage("Ready")
# Инструменты
ellipsePen = QtGui.QPen()
ellipsePen.setStyle(QtCore.Qt.SolidLine)
ellipsePen.setWidth(2)
ellipsePen.setBrush(QtCore.Qt.green)

colorRed = QtGui.QColor.fromRgb(255, 0, 0, 255)
redBrush = QtGui.QBrush(colorRed, style=QtCore.Qt.SolidPattern)
# Сцены
scene = QtWidgets.QGraphicsScene()


# Функции

def sceneCreate():
    global initFlag, InRoundCounter

    if initFlag == 0:   # Если это не первое вычисление
        scene.clear()

    InRoundCounter = 0
    radius = int(ui.spinBox.text())     # Считываем радиус
    dotsAmount = int(ui.comboBox.currentText())    # Считываем количество точек

    ellipse = QtWidgets.QGraphicsEllipseItem(200-radius, 200-radius, 2*radius, 2*radius)  # Создаем объект эллипса Item(x, y ,h, w)
    ellipse.setPen(ellipsePen)  # Задаем ручку
    scene.addItem(ellipse)      # Добавляем в сцену эллипс
    for i in range(0, dotsAmount):
        rectX = random.randrange(200-radius, 200+radius)
        rectY = random.randrange(200-radius, 200+radius)
        scene.addRect(rectX, rectY, 1, 1)
        isInRound(rectX, rectY, radius)
    S = 4*(InRoundCounter/dotsAmount)*math.pow(radius, 2)
    Pi = 4*(InRoundCounter/dotsAmount)
    ui.S_lineEdit.setText(str(round(S, 2)))
    ui.Pi_lineEdit.setText(str(Pi))
    ui.statusbar.showMessage("OK")
    initFlag = 0


def monte():
    sceneCreate()
    ui.graphicsView.setScene(scene)


def isInRound(gX, gY, r):
    global InRoundCounter
    mX = gX-200     # Преобразуем графические координаты X в математические
    mY = 200-gY     # Преобразуем графические координаты Y в математические
    OXY = math.sqrt(math.pow(mX, 2)+math.pow(mY, 2))  # Длина вектора OXY
    if OXY <= r:
        InRoundCounter += 1

# Привязывание кнопок к функциям
ui.calculation_Button.pressed.connect(monte)

# Обработка выхода
sys.exit(app.exec_())

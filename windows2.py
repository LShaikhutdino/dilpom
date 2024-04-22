from PyQt6.QtWidgets import *
from PyQt6 import uic #, QStringList
# from PyQt6.QtCore import QMap
import sys
from mainwindow import *
from statistic import *


class Window2(QMainWindow):
    def __init__(self, textNames={}, fileNames=[]):
        super().__init__()
        self.ui = uic.loadUi('window2.ui', self)

        # Свойства основного окна
        # 1. Список файлов/текстов
        # ?? self.fileNames = fileNames
        # 2. Словарь Номер текста - Текст
        self.textNames = textNames

        # for fileName in fileNames:
        self.listWidget.addItems(fileNames)

        # authenticate when the login button is clicked
        # self.ui.btn_login.clicked.connect(self.authenticate)
        # 0. Запуск статистики
        self.stat = Statistic(fileNames=fileNames)
        # 1. Перейьт обратно в первое окно
        # по кнопке Назад
        self.ui.pushButton_2.clicked.connect(self.openMain)

        # 2. Открыть файл/текст
        self.ui.pushButton.clicked.connect(self.openFileOrText)

        self.show()
    
    def openMain(self):
        # TODO передать список файлов назад...
        # ...
        MainWindow()
        self.stat.close()
        self.close()
    
    def openFileOrText(self):
        selectedItem = self.listWidget.selectedItems()[0].text()
        self.stat.doSomething(selectedItem)
        # TODO обработать отсутствие выборанного файла...
        # ... не помню, что это.
        # TODO открыть всё-таки файл или текст...
        # ...done
        # try...except конечно, костыль здесь, но мне лень
        try:
            if int(selectedItem.replace('Text ','')) in self.textNames:
                QMessageBox.information(self, selectedItem, self.textNames[int(selectedItem.replace('Text ',''))])
            else:
                with open(selectedItem, 'r', encoding="utf-8") as f:
                    QMessageBox.information(self, selectedItem, f.read())
        except ValueError:
            with open(selectedItem, 'r', encoding="utf-8") as f:
                QMessageBox.information(self, selectedItem, f.read())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Window2()
    sys.exit(app.exec())
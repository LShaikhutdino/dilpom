from PyQt6.QtWidgets import *
from PyQt6 import uic #, QStringList
# from PyQt6.QtCore import Slot
import sys
import cachetools
import time

class Statistic(QMainWindow):
    def __init__(self, fileNames=[]):
        super().__init__()
        self.ui = uic.loadUi('statistic.ui', self)

        # Свойства статистики
        # 1. Кэши LFU и LRU. Размер 3 записи
        self.LFU_cache = cachetools.LFUCache(maxsize=3) #fileNames
        self.LRU_cache = cachetools.LRUCache(maxsize=3) #fileNames
        # Заполнение кэшей
        for fileName in fileNames:
            self.LFU_cache[fileName] = 0
            self.LRU_cache[fileName] = 0

        # Функции
        # 1. Вывод кэшей на форму
        self.updateCachesOnForm()
        
        # self.ui.pushButton.clicked.connect(self.downloadFile)

        self.show()

    def updateCachesOnForm(self):
        self.listWidget.clear()
        self.listWidget_2.clear()
        # time.sleep(1)
        for key in self.LRU_cache:
            self.listWidget.addItem(key + " - раз откр-ся " + str(self.LRU_cache[key]))
        for key in self.LFU_cache:
            self.listWidget_2.addItem(key + " - раз откр-ся " + str(self.LFU_cache[key]))

# Слот/функция для приёма сигнала об открытии текста или файла в другом окне
    # @Slot(str)
    def doSomething(self, fileName):
        # QMessageBox.critical(self, 'Error',str(fileName))
        # Some magic action
        if fileName in self.LFU_cache:
            self.LFU_cache[fileName] = self.LFU_cache[fileName] + 1
        else:
            self.LFU_cache[fileName] = 0

        if fileName in self.LRU_cache:
            self.LRU_cache[fileName] = self.LRU_cache[fileName] + 1
        else:
            self.LRU_cache[fileName] = 0
        self.updateCachesOnForm()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Statistic()
    sys.exit(app.exec())
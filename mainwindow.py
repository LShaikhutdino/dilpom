from PyQt6.QtWidgets import *
from PyQt6 import uic #, QStringList
from PyQt6.QtCore import Qt
import sys
# from windows2 import *
# from statistic import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('mainwindow.ui', self)
        # self.ui = uic.loadUi('window2.ui', self)
        # self.ui = uic.loadUi('window2.ui', self)

        # Свойства основного окна
        # 1. Список файлов/текстов
        # self.fileNames = QStringList()
        # 2. Словарь Номер текста - Текст
        self.textNames = {}

        # authenticate when the login button is clicked
        # self.ui.btn_login.clicked.connect(self.authenticate)
        # 1. Загрузить файл - открыть диалоговое окно работы с файлами и сохранить путь до файла
        # по кнопке Добавить файл
        self.ui.pushButton.clicked.connect(self.downloadFile)
        # 2. Удалить выделенную строку из списка
        self.ui.pushButton_2.clicked.connect(self.deleteItemFrmList)
        # 3. Загрузить текст - сохранить текст в памяти и добавить строчку о нём в общий список
        self.ui.pushButton_4.clicked.connect(self.addText)
        # 4. Открыть 2-ое окно и окно статистики
        self.ui.pushButton_5.clicked.connect(self.openSecondWindow)
        # 5. Открыть файл/текст
        self.ui.pushButton_7.clicked.connect(self.openFileOrText)
        # 6. Анализ метрик
        self.ui.pushButton_6.clicked.connect(self.analizeMetrics)

        self.show()

    def analizeMetrics(self):
        selectedItem = self.listWidget.selectedItems()[0].text()
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

    def openFileOrText(self):
        selectedItem = self.listWidget.selectedItems()[0].text()
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
    
    def downloadFile(self):
        dialog = QFileDialog(self)
        # параметры диалогового окна
        dialog.setNameFilter("Python source code (*.py)")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        if dialog.exec():
            # if self.fileNames is None:
            fileNames = dialog.selectedFiles()
            if fileNames:
                for fileName in fileNames:
                    items = self.listWidget.findItems(str(fileName),Qt.MatchFlag.MatchExactly)
                    if len(items) == 0:
                        self.listWidget.addItem(str(fileName))
                    try:
                        # TODO: подцепить метрики из доп библиотеки
                        # self.listFilesAndTexts[str(fileName)].analizeJSON = что-то там на аналайзерском
                        pass
                    except Exception as e:
                        print("Error with analize")
                        # TODO: заглушка с нулями для анлиза
                        print(e)

    def deleteItemFrmList(self):
        for item in self.listWidget.selectedItems():
            # QMessageBox.critical(self, 'Error',str((type(item))))
            # self.listWidget.removeItemWidget(item)- не работает))
            self.listWidget.takeItem(self.listWidget.row(item))
        # TO_DO удалить текст из self.textNames
    
    def addText(self):
        # добавить текст в словарь
        maxTextId = 0
        if self.textNames != {}:
            maxTextId = max(self.textNames)
        self.textNames[maxTextId + 1] = self.textEdit.toPlainText()
        # добавить его название в общий список
        self.listWidget.addItems([str("Text " + str(maxTextId + 1))])
        # QMessageBox.critical(self, 'Error', "Text " + str(maxTextId + 1))
        # очистить textEdit
        self.textEdit.clear()
        self.tabWidget.setCurrentIndex(0)
        # *Обратно получить текст по его Id - название текста минус "Text "
        try:
            # TODO: подцепить метрики из доп библиотеки
            # self.listFilesAndTexts[[str("Text " + str(maxTextId + 1))]].analizeJSON = что-то там на аналайзерском
            pass
        except Exception as e:
            print("Error with analize")
            # TODO: заглушка с нулями для анлиза
            print(e)

    
    def openSecondWindow(self):
        pass
        # lw=self.listWidget
        # Window2(textNames=self.textNames, fileNames=[lw.item(x).text() for x in range(lw.count())])
        # # window2.show()
        # # statistic.show()
        # self.close()

    # def authenticate(self):
    #     email = self.email_line_edit.text()
    #     password = self.password_line_edit.text()

    #     if email == 'john@test.com' and password == '123456':
    #         QMessageBox.information(self, 'Success',"You're logged in!")
    #     else:
    #         QMessageBox.critical(self, 'Error',"Invalid email or password.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec())
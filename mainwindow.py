from PyQt6.QtWidgets import *
from PyQt6 import uic #, QStringList
from PyQt6.QtCore import Qt
import sys
import analyze_code as ac
import dialog
import dill
import pandas as pd
# Импорт библио, файлов и проч
# https://stackoverflow.com/questions/2349991/how-do-i-import-other-python-files

# from windows2 import *
# from statistic import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Строка 20. Используется стандартный метод подключения интерфейса. Сконфигурированный файл с расширением .ui создан в прикладной 
        # программе Qt Designer и подложен в папку с основным скриптом программы.
        self.ui = uic.loadUi('mainwindow.ui', self)
        # self.ui = uic.loadUi('window2.ui', self)
        # self.ui = uic.loadUi('window2.ui', self)

        # Свойства основного окна
        # 1. Список файлов/текстов
        # self.fileNames = QStringList()
        # 2. В строке 29 происходит определение словаря "Номер текста - Текст". Он используется для хранения текста, введенного текста
        # вручную на второй из вкладок основного окна.
        self.textNames = {}
        # 3. В строке 32 - определение словаря "Файл/текст" - "Показатели кода Файла/текста". Соответствующему файлу или тексту сопоставляется
        # список посчитанных показателей кода.
        self.listFilesAndTexts = {}
        # 4. В строке 35 - загрузка обученной модели градиентного бустинга. В основе процесса использована расширенная версия библиотеки pickle под названием dill.
        # С её помощью можно выгружать более сложные типы объектов, например, такие, как объекты с лямбда-функциями, обёртки методов, slice (срезы) и так далее.
        with open('model.pkl', 'rb') as f:
            self.automl = dill.load(f) #, pickle_module=dill)

        # authenticate when the login button is clicked
        # self.ui.btn_login.clicked.connect(self.authenticate)
        # С 43 по 55 строки реализована сигнал-слотовая связь. По методу нажатия кнопки pushButton вызывается один из методов, описанных в классе.
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
        # 6. Анализ кода на дефекты
        self.ui.pushButton_5.clicked.connect(self.totalAnalize)

        self.show()

    def totalAnalize(self):
        # В строках 61-62 и 113-115 по выделенному элементу строки (тексту программы или файлу, его содержащему) из таблицы происходит копирование списка метрик в отдельную переменную, обработка и занесение их в прогностическую модель компьютерного (машинного) обучения. На шаге занесения метрик в обучающую модель выдается результат предсказания - вероятность присутствия дефектов в интересуемом коде.
        selectedItem = self.tableWidget.selectedItems()[0].text()
        text_json = self.listFilesAndTexts[selectedItem]['analizeJSON'].copy()

        try:
            text_json['loc'] = text_json['LOC']
            text_json['v(g)'] = text_json['v_g']
            text_json['ev(g)'] = text_json['ev_g']
            text_json['iv(g)'] = text_json['iv_g']
            text_json['n'] = text_json['length']
            text_json['v'] = text_json['volume']
            text_json['l'] = text_json['calculated_length']
            text_json['d'] = text_json['difficulty']
            text_json['i'] = text_json['intelligence']
            text_json['e'] = text_json['effort']
            text_json['b'] = text_json['bugs']
            text_json['t'] = text_json['time']
            text_json['lOCode'] = text_json['SLOC']
            text_json['lOComment'] = text_json['single_comments']
            text_json['lOBlank'] = text_json['blank']
            text_json['locCodeAndComment'] = text_json['multi']
            text_json['uniq_Op'] = text_json['h1']
            text_json['uniq_Opnd'] = text_json['h2']
            text_json['total_Op'] = text_json['N1']
            text_json['total_Opnd'] = text_json['N2']
            text_json['branchCount'] = text_json['count_branch']

            del text_json['LOC']
            del text_json['v_g']
            del text_json['ev_g']
            del text_json['iv_g']
            del text_json['length']
            del text_json['volume']
            del text_json['calculated_length']
            del text_json['difficulty']
            del text_json['intelligence']
            del text_json['effort']
            del text_json['bugs']
            del text_json['time']
            del text_json['SLOC']
            del text_json['single_comments']
            del text_json['blank']
            del text_json['multi']
            del text_json['h1']
            del text_json['h2']
            del text_json['N1']
            del text_json['N2']
            del text_json['count_branch']
        except:
            exit()

        for k, v in text_json.items():
            text_json[k] = [v]
        text_json_pd = pd.DataFrame(text_json)
        text_json_pd
        pred = self.automl.predict(text_json_pd)

        i = self.ui.tableWidget.currentRow()

        print( str(pred[0, 'WeightedBlend_0']) )
        # В строках 121-122 результат предсказания преобразовывается в широко распространенный формат данных NumPy для дальнейшей обработки и вывода в колонку напротив выделенного элемента строки, использованному на предыдущем этапе.
        pred = pred.to_numpy()
        self.ui.tableWidget.setItem(i, 1, QTableWidgetItem( str(pred[0, 'WeightedBlend_0']) ))

    def analizeMetrics(self):
        selectedItem = self.tableWidget.selectedItems()[0].text()
        # print(selectedItem)
        if 'Text ' in selectedItem:
            dlg = dialog.Dialog( self.listFilesAndTexts[selectedItem]['analizeJSON'], textName = selectedItem, text = self.textNames[int(selectedItem.replace('Text ',''))] )
        else:
            dlg = dialog.Dialog( self.listFilesAndTexts[selectedItem]['analizeJSON'], file = selectedItem )
        if dlg.exec(): # == QMessageBox.StandardButton.Ok):
            QMessageBox.information(self, selectedItem, str( dlg.returnAnalizeJSON() ))
        # try...except конечно, костыль здесь, но мне лень
        # try:
        #     if int(selectedItem.replace('Text ','')) in self.textNames:
        #         QMessageBox.information(self, selectedItem, self.textNames[int(selectedItem.replace('Text ',''))])
        #     else:
        #         with open(selectedItem, 'r', encoding="utf-8") as f:
        #             QMessageBox.information(self, selectedItem, f.read())
        # except ValueError:
        #     with open(selectedItem, 'r', encoding="utf-8") as f:
        #         QMessageBox.information(self, selectedItem, f.read())

    def openFileOrText(self):
        selectedItem = self.tableWidget.selectedItems()[0].text()
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
                    items = self.tableWidget.findItems(str(fileName),Qt.MatchFlag.MatchExactly)
                    if len(items) == 0:
                        # done: добавить всё тож самое в таблицу
                        i = self.ui.tableWidget.rowCount()
                        self.ui.tableWidget.setRowCount(i + 1)
                        self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(fileName)))
                        try:
                            # подцепить метрики из доп библиотеки
                            with open(fileName, 'r', encoding="utf-8") as f:
                                code = f.read()
                            self.listFilesAndTexts[str(fileName)] = {}
                            self.listFilesAndTexts[str(fileName)]['analizeJSON'] = ac.analyzeCode(code)
                            # print( type(ac.analyzeCode(code)) )
                            pass
                        except Exception as e:
                            print("Error with analize")
                            # done: заглушка с нулями для анлиза
                            self.listFilesAndTexts[str(fileName)] = {}
                            self.listFilesAndTexts[str(fileName)]['analizeJSON'] = ac.analyzeCode()
                            print(e)

    def deleteItemFrmList(self):
        self.ui.tableWidget.removeRow( self.ui.tableWidget.currentRow() )

        # TODO: удалить текст из self.textNames
        # TODO 2: удалить текст из self.listFilesAndTexts
    
    def addText(self):
        # добавить текст в словарь
        maxTextId = 0
        if self.textNames != {}:
            maxTextId = max(self.textNames)
        self.textNames[maxTextId + 1] = self.textEdit.toPlainText()
        # добавить его название в общий список
        # done: добавить всё тож самое в таблицу
        i = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(i + 1)
        self.ui.tableWidget.setItem(i, 0, QTableWidgetItem( str("Text " + str(maxTextId + 1)) ))
        # QMessageBox.critical(self, 'Error', "Text " + str(maxTextId + 1))
        # очистить textEdit
        self.textEdit.clear()
        self.tabWidget.setCurrentIndex(0)
        # *Обратно получить текст по его Id - название текста минус "Text "
        try:
            # TODO: подцепить метрики из доп библиотеки
            self.listFilesAndTexts[str("Text " + str(maxTextId + 1))] = {}
            self.listFilesAndTexts[str("Text " + str(maxTextId + 1))]['analizeJSON'] = ac.analyzeCode(str(self.textNames[maxTextId + 1]))
            pass
        except Exception as e:
            print("Error with analize")
            # done: заглушка с нулями для анлиза
            self.listFilesAndTexts[str("Text " + str(maxTextId + 1))] = {}
            self.listFilesAndTexts[str("Text " + str(maxTextId + 1))]['analizeJSON'] = ac.analyzeCode()
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
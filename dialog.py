from PyQt6.QtWidgets import QDialog
from PyQt6 import uic #, QStringList
import sys
from staticfg import CFGBuilder
from pathlib import Path
# https://stackoverflow.com/questions/678236/how-do-i-get-the-filename-without-the-extension-from-a-path-in-python

class Dialog(QDialog):
    def __init__(self, analizeJSON = {}, file = None, textName = None, text = None):
        super().__init__()
        self.ui = uic.loadUi('dialog.ui', self)
        self.analizeJSON = analizeJSON
        # 1. Вывод метрик на форму
        self.lineEdit.setText( str(analizeJSON['LOC']) )
        self.lineEdit_8.setText( str(analizeJSON['SLOC']) )
        self.lineEdit_4.setText( str(analizeJSON['blank']) )
        self.lineEdit_5.setText( str(analizeJSON['multi']) )
        self.lineEdit_3.setText( str(analizeJSON['single_comments']) )

        self.lineEdit_8.setText( str(analizeJSON['v_g']) )
        self.lineEdit_10.setText( str(analizeJSON['ev_g']) )
        self.lineEdit_9.setText( str(analizeJSON['iv_g']) )

        self.lineEdit_11.setText( str(analizeJSON['h1']) )
        self.lineEdit_13.setText( str(analizeJSON['h2']) )
        self.lineEdit_12.setText( str(analizeJSON['N1']) )
        self.lineEdit_14.setText( str(analizeJSON['N2']) )

        self.lineEdit_15.setText( str(analizeJSON['length']) )
        self.lineEdit_14.setText( str(analizeJSON['volume']) )
        self.lineEdit_19.setText( str(analizeJSON['calculated_length']) )
        self.lineEdit_16.setText( str(analizeJSON['intelligence']) )
        self.lineEdit_18.setText( str(analizeJSON['effort']) )
        self.lineEdit_17.setText( str(analizeJSON['difficulty']) )
        self.lineEdit_20.setText( str(analizeJSON['bugs']) )
        self.lineEdit_21.setText( str(analizeJSON['time']) )
        
        self.lineEdit_22.setText( str(analizeJSON['count_branch']) )
        # 2. Открыть граф из кода
        self.file = file
        self.text = text
        self.textName = textName
        self.ui.pushButton_3.clicked.connect(self.openGraf)
        # 3.1. Редактировать поле ev(g)
        self.ui.pushButton.clicked.connect(self.editEvG)
        # 3.2. Редактировать поле iv(g)
        self.ui.pushButton_2.clicked.connect(self.editIvG)

    def editEvG(self):
        currentState = self.ui.lineEdit_10.isEnabled()
        self.ui.lineEdit_10.setEnabled( not currentState )
        if currentState:
            self.analizeJSON['ev_g'] = str( self.ui.lineEdit_10.text() )
        else:
            self.ui.lineEdit_10.setFocus()

    def editIvG(self):
        currentState = self.ui.lineEdit_9.isEnabled()
        self.ui.lineEdit_9.setEnabled( not currentState )
        if currentState:
            self.analizeJSON['iv_g'] = str( self.ui.lineEdit_9.text() )
        else:
            self.ui.lineEdit_9.setFocus()

    def openGraf(self):

        #создаем объект класса CFGBuilder
        # with open(filepath, 'r') as src_file:
        #     src = src_file.read()
        if self.text:
            cfg = CFGBuilder().build_from_src(self.textName, self.text)
            #сохраняем визуализацию
            cfg.build_visual(self.textName,'png')
        if self.file:
            fileName = Path(self.file).stem
            cfg = CFGBuilder().build_from_file(fileName,self.file)
            #сохраняем визуализацию
            cfg.build_visual(fileName,'png')

    def returnAnalizeJSON(self):
        return self.analizeJSON
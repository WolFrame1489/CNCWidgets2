import sys
import asyncio
import asyncua
from CNCWidgets import (ActionButtons, InputString, MonitorWidgetX, Editor, MonitorWidgetY, ToolBox, MonitorWidgetStatus, MonitorWidgetStatusX
                        )
from PyQt5.Qsci import QsciScintilla, QsciLexerPython
from CNCActions import OPCClient
from CNCActions import OPCActions
from CNCActions import FTP
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout,
                              QGridLayout, QLineEdit, QLabel)
from PyQt5.QtCore import QSize

class PyQtWindow(QWidget): # эта функция создает окно на которое будем ставить наши виджежты
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Layouttest")
        #self.setFixedSize(1920,1080)
        self.count = 0

        self.layout = QGridLayout()                                   # + self.layout
        self.setLayout(self.layout)

        #self._insert_mywidget()                                       # - (layout)

        #self.labels = [QLabel("Label " + str(i+1)) for i in range(5)]
        #for i, label in enumerate(self.labels):
         #   self.layout.addWidget(label, 1, i)

        #self.edits = [QLineEdit(self) for _ in range(10)]
        #for i, edit in enumerate(self.edits):
         #   self.layout.addWidget(edit, 2, i)

    def insert_mywidget(self, widget):# передаем виджет                                 # - , layout):
        self.widget = widget
        # add my widget
#        self.layout.addWidget(self.widget, 0, 0, 0, 10)
        self.layout.addWidget(self.widget, 0, 0, self.count + 1, 10)  # + 1
        self.count += 1

#        layout.addLayout(self.widget.layout(), 0, 0, 0, 10)

if __name__ == "__main__":
    loop = asyncio.get_event_loop() # луп для корутин
    client = asyncua.Client("opc.tcp://10.0.1.10:4841/")
    app = QApplication(sys.argv)

    OPCClient.Globalclient = client
    OPCActions.Globalclient = client
    while True:
        if (loop.run_until_complete(OPCClient.Connect(client))): # подключение к серверу
            break
    window = PyQtWindow()
    window.layout.addWidget(MonitorWidgetX.CoordX(), 5, 0, 5, 1) #виджет координат
    window.layout.addWidget(MonitorWidgetY.CoordY(), 6, 0, 6, 1) 
    window.insert_mywidget(InputString.GCodeInput(), 0, 0, 1, 1) #виджет строки для блока
    #window.insert_mywidget((ActionButtons.PowerButton()), 0, 0, 1, 1) виджет кнопки
    window.show()
    sys.exit(app.exec_())

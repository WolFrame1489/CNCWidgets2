import sys
import asyncio
import asyncua
from CNCWidgets import (ActionButtons, InputString, MonitorWidgets
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
    #FTP.Connect()
    client = asyncua.Client("opc.tcp://192.168.133.2:4841/")

    app = QApplication(sys.argv)

    OPCClient.Globalclient = client
    OPCActions.Globalclient = client
    #while True:
        #if (loop.run_until_complete(OPCClient.Connect(client))):
    #        break
    window = PyQtWindow()
    #window.insert_mywidget(ActionButtons.UploadFile())
    window.layout.addWidget(ActionButtons.StartBlockButton(), 0, 1, 1, 3)
    window.layout.addWidget(ActionButtons.StopBlockButton(), 1, 2, 1, 3)
    #window.insert_mywidget(InputString.GCodeInput())
    #window.insert_mywidget(MonitorWidgets.CoordX())  #лейблы должны создавться раньше кнопок хз почему

    #window.insert_mywidget((ActionButtons.PowerButton()))
    #window.insert_mywidget(ActionButtons.HomeAllHereButton())
    window.show()
    sys.exit(app.exec_())
    print(editor.getCursorPosition())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

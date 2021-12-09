import sys
import asyncio
import asyncua
from CNCWidgets import testwidget
from CNCActions import OPCClient
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QWidget, QApplication, QHBoxLayout,
                              QGridLayout, QLineEdit, QLabel)
from PyQt5.QtCore import QSize

class PyQtWindow(QWidget): # эта функция создает окно на которое будем ставить наши виджежты
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Layouttest")

        self.layout = QGridLayout()                                   # + self.layout
        self.setLayout(self.layout)

        self._insert_mywidget()                                       # - (layout)

        self.labels = [QLabel("Label " + str(i+1)) for i in range(5)]
        for i, label in enumerate(self.labels):
            self.layout.addWidget(label, 1, i)

        self.edits = [QLineEdit(self) for _ in range(10)]
        for i, edit in enumerate(self.edits):
            self.layout.addWidget(edit, 2, i)

    def _insert_mywidget(self, widget):       # передаем виджет                                 # - , layout):
        self.widget = widget
        # add my widget
#        self.layout.addWidget(self.widget, 0, 0, 0, 10)
        self.layout.addWidget(self.widget, 0, 0, 1, 10)                # + 1

#        layout.addLayout(self.widget.layout(), 0, 0, 0, 10)
loop = asyncio.get_event_loop()
client = asyncua.Client("opc.tcp://localhost:4841/")
app = QApplication(sys.argv)
OPCClient.Globalclient = client
loop.run_until_complete(OPCClient.Connect(client))
loop.run_until_complete(OPCClient.CNCActionPower())
#window = PyQtWindow()
#window.show()

sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

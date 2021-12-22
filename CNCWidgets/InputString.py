from PyQt5.QtWidgets import QLineEdit
from CNCActions import OPCActions
import asyncio
class GCodeInput(QLineEdit):
    def __init__(self):
        super().__init__()
        self.editingFinished.connect(self.send)
    def send(self):
        print(self.text())
        OPCActions.GlobalGCODEString = self.text()

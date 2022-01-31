from PyQt5.QtWidgets import QComboBox
from CNCActions import OPCActions
class Toolbox(QComboBox):
    def __init__(self):
        super(Toolbox, self).__init__()
        self.addItems(['1', '2', '3', '4', '5'])
        OPCActions.Tool = int(self.currentText())
        self.currentIndexChanged.connect(self.Act)
    def Act(self):
        print(self.currentText())
        OPCActions.Tool = int(self.currentText())



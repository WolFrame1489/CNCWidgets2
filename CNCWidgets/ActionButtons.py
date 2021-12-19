from PyQt5.QtWidgets import QPushButton
import asyncio
from CNCActions import OPCActions
class PowerButton(QPushButton):
    def __init__(self):
        super(PowerButton, self).__init__()
        self.setText("ВАСЯ ИДИ НАХУЙ")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionPower(0))
class HomeAllHereButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.setText("ВАСЯ ЭТА КНОПКА ВСЕ ХОУМИТ")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("XY", 0))
class HomeAllEndButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.setText("ВАСЯ ЭТА КНОПКА ВСЕ ХОУМИТ")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("XY", 3))
class HomeAllOldButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.setText("ВАСЯ ЭТА КНОПКА ВСЕ ХОУМИТ")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("XY", 1488))
class HomeXHereButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.setText("ВАСЯ ЭТА КНОПКА X ХОУМИТ")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("X", 0))
class HomeXEndButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.setText("ВАСЯ ЭТА КНОПКА x ХОУМИТ")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("X", 3))
class HomeXOldButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.setText("ВАСЯ ЭТА КНОПКА X ХОУМИТ")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("X", 1488))
class HomeYHereButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.setText("ВАСЯ ЭТА КНОПКА Y ХОУМИТ")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("Y", 0))
class HomeXEndButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.setText("ВАСЯ ЭТА КНОПКА Y ХОУМИТ")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("Y", 3))
class HomeXOldButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.setText("ВАСЯ ЭТА КНОПКА Y ХОУМИТ")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("Y", 1488))
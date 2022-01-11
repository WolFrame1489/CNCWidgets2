from PyQt5.QtWidgets import QPushButton
import asyncio
from CNCActions import (OPCActions, FTP)
class PowerButton(QPushButton):
    def __init__(self):
        super(PowerButton, self).__init__()
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
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("XY", 3))
class HomeAllOldButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("XY", 1488))
class HomeXHereButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("X", 0))
class HomeXEndButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("X", 3))
class HomeXOldButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("X", 1488))
class HomeYHereButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("Y", 0))
class HomeXEndButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("Y", 3))
class HomeXOldButton(QPushButton):
    def __init__(self):
        super(HomeAllHereButton, self).__init__()
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionHoming("Y", 1488))
class StartBlockButton(QPushButton):
    def __init__(self):
        super(StartBlockButton, self).__init__()
        self.setText("Start NC Program")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionStartBlock(OPCActions.GlobalGCODEString))
class StopBlockButton(QPushButton):
    def __init__(self):
        super(StopBlockButton, self).__init__()
        self.setText("Stop NC Block")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionStopBlock())
class UploadFile(QPushButton):
    def __init__(self):
        super(UploadFile, self).__init__()
        self.setText("Upload File")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(FTP.TransferFile())
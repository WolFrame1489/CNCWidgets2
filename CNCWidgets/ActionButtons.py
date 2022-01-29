from PyQt5.QtWidgets import QPushButton
import asyncio
from CNCActions import (OPCActions, FTP)
Tool = 0
Power = 1
class PowerButton(QPushButton):
    def __init__(self):
        super(PowerButton, self).__init__()
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
        global Power
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionPower(not Power))
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
        self.setText("Stop NC Program")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionStopBlock())
class ContinueBlockButton(QPushButton):
    def __init__(self):
        super(ContinueBlockButton, self).__init__()
        self.setText("Continue NC Program")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionContinueBlock())
class PauseBlockButton(QPushButton):
    def __init__(self):
        super(PauseBlockButton, self).__init__()
        self.setText("Pause NC Program")
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionPauseBlock())
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
class SwitchModeButton(QPushButton):
    def __init__(self):
        super(SwitchModeButton, self).__init__()
        self.setText("Normal Mode")
        self.mode = 0
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        if (self.mode == 0):
            self.mode = 1
            self.setText('Single step mode')
        else:
            self.mode = 0
            self.setText('Normal Mode')
        self.loop.run_until_complete(OPCActions.SwitchMode(self.mode))
class JoggingModeButton(QPushButton):
    def __init__(self):
        super(JoggingModeButton, self).__init__()
        self.setText("Jogging is now OFF")
        self.mode = 0
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Debug(self):
        print("YES")
    def Act(self):
        if (self.mode == 0):
            self.mode = 1
            self.setText('Jogging is now OFF')
        else:
            self.mode = 0
            self.setText('Jogging is now ON')
        self.loop.run_until_complete(OPCActions.JogMode(self.mode))
class JogXPos(QPushButton):
    def __init__(self):
        super(JogXPos, self).__init__()
        self.setText("X+")
        self.setCheckable(True)
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
        self.amount = 32767
        self.stop = 0
    def Debug(self):
        print("YES")
    def Act(self):
        if self.isChecked():
            self.stop = 0
            self.go  = 1
            self.loop.run_until_complete(OPCActions.CNCActionJogX(self.amount, self.go, self.stop))
        else:
            self.stop = 1
            self.go = 0
            self.loop.run_until_complete(OPCActions.CNCActionJogX(self.amount, self.go, self.stop))
class JogXNeg(QPushButton):
    def __init__(self):
        super(JogXNeg, self).__init__()
        self.setText("X-")
        self.setCheckable(True)
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
        self.amount = (-32767)
        self.stop = 0
    def Debug(self):
        print("YES")
    def Act(self):
        if self.isChecked():
            self.stop = 0
            self.go  = 1
            self.loop.run_until_complete(OPCActions.CNCActionJogX(self.amount, self.go, self.stop))
        else:
            self.stop = 1
            self.go = 0
            self.loop.run_until_complete(OPCActions.CNCActionJogX(self.amount, self.go, self.stop))
class JogYPos(QPushButton):
    def __init__(self):
        super(JogYPos, self).__init__()
        self.setText("Y+")
        self.setCheckable(True)
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
        self.amount = 32767
        self.stop = 0
    def Debug(self):
        print("YES")
    def Act(self):
        if self.isChecked():
            self.stop = 0
            self.go  = 1
            self.loop.run_until_complete(OPCActions.CNCActionJogY(self.amount, self.go, self.stop))
        else:
            self.stop = 1
            self.go = 0
            self.loop.run_until_complete(OPCActions.CNCActionJogY(self.amount, self.go, self.stop))
class JogYNeg(QPushButton):
    def __init__(self):
        super(JogYNeg, self).__init__()
        self.setText("Y-")
        self.setCheckable(True)
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
        self.amount = (-32767)
        self.stop = 0
    def Debug(self):
        print("YES")
    def Act(self):
        if self.isChecked():
            self.stop = 0
            self.go  = 1
            self.loop.run_until_complete(OPCActions.CNCActionJogY(self.amount, self.go, self.stop))
            print("go y")
        else:
            print("stop y")
            self.stop = 1
            self.go = 0
            self.loop.run_until_complete(OPCActions.CNCActionJogY(self.amount, self.go, self.stop))
class ChangeTool(QPushButton):
    def __init__(self):
        super(ChangeTool, self).__init__()
        self.setText("Change Tool")
        global Tool
        self.tool = Tool
        self.clicked.connect(self.Act)
        self.loop = asyncio.get_event_loop()
    def Act(self):
        self.loop.run_until_complete(OPCActions.CNCActionChangeTool(self.tool))
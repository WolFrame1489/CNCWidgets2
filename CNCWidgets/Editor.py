from PyQt5.QtWidgets import *
import asyncio
import asyncua
import logging
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import QsciScintilla, QsciLexerPython
Globalclient = asyncua.Client("opc.tcp://192.168.133.2:4841/")
class SubscriptionThread(QThread): #отдельный поток для цикла подписки
    def __init__(self, nodestring, widget, parent = None ):
        super().__init__()
        self.widget = widget
        self.nodestring = nodestring
        self.handler = SubscriptionHandler()
    def run(self):
        print("in")
        self.loop = asyncio.new_event_loop()
        self.loop.run_until_complete(self.test())
    async def test(self):
        a = 0
        await Globalclient.connect()
        var = Globalclient.get_node(self.nodestring)
        handler = SubscriptionHandler()
        # We create a Client Subscription.
        subscription = await Globalclient.create_subscription(100, handler)
        # We subscribe to data changes for two nodes (variables).
        await subscription.subscribe_data_change(var)
        print("sub created")
        while True:
            await asyncio.sleep(0.01)
            self.widget.setCursorPosition(handler.value, 0)
class SubscriptionHandler():
    """
    The SubscriptionHandler is used to handle the data that is received for the subscription.
    """
    def __init__(self):
        self.value = 0
    status = 2
    def datachange_notification(self, node, val, data):
        """
        Callback for asyncua Subscription.
        This method will be called when the Client received a data change message from the Server.
        """
        print('datachange_notification %r %s', node, val, data)
        _logger.info('datachange_notification %r %s', node, val)
        self.value = val
        status = 1
logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger('asyncua')
from CNCActions import OPCClient
class GCodeEditor(QsciScintilla):
    ARROW_MARKER_NUM = 8
    def __init__(self, parent=None):
        super(GCodeEditor, self).__init__(parent)
        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.setFont(font)
        self.setMarginsFont(font)
        self.setCaretLineVisible(1)
        self.setText(open('testcnc.PRG', 'r').read())
        self.Thread = SubscriptionThread("ns=6;s=::AsGlobalPV:X", widget=self) #TODO: Поменять на переменную станка для подписки
        self.Thread.start()  # cоздаем отдельный поток qt

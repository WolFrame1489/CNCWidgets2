import asyncua
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QThread
from asyncqt import QEventLoop, QThreadExecutor
import asyncio
import logging
import threading
import sys
sys.path.insert(0, "..")
import os
# os.environ['PYOPCUA_NO_TYPO_CHECK'] = 'True'
import qasync
import asyncio
import logging
from concurrent.futures import ProcessPoolExecutor
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from asyncua import Client, Node, ua
Globalclient = asyncua.Client("opc.tcp://localhost:4841/")
value = 0
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
            self.widget.setText(str(handler.value))




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
        return value
logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger('asyncua')
from CNCActions import OPCClient
p = ProcessPoolExecutor(1)
class CoordX(QLabel):
    def __init__(self):
        super(CoordX, self).__init__()
        self.setText("sex")
        self.data = 0
        self.Thread = SubscriptionThread("ns=6;s=::AsGlobalPV:X", widget=self)
        self.Thread.start() #cоздаем отдельный поток qt
        print(threading.active_count())



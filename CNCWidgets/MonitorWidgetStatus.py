import asyncua
import random
import re
import csv
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QThread
import asyncio
import logging
import threading
import sys
sys.path.insert(0, "..")
import os
# os.environ['PYOPCUA_NO_TYPO_CHECK'] = 'True'
import asyncio
import logging
from concurrent.futures import ProcessPoolExecutor
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from asyncua import Client, Node, ua
Globalclient = asyncua.Client("opc.tcp://192.168.133.2:4841/")
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
        a = ''
        b =''
        await Globalclient.connect()
        var = Globalclient.get_node(self.nodestring)
        varstring = Globalclient.get_node("ns=6;s=::FileInput:ErrorText2")
        varconnection = Globalclient.get_node("ns=6;s=::Program:Connection")
        handler = SubscriptionHandler()
        # We create a Client Subscription.
        subscription = await Globalclient.create_subscription(100, handler)
        # We subscribe to data changes for two nodes (variables).
        await subscription.subscribe_data_change(var)
        print("sub created")
        while True:
            await asyncio.sleep(1)
            x = random.randint(1, 1000)
            dv = ua.DataValue(ua.Variant(int(x), ua.VariantType.Int16))
            await varconnection.set_value(dv)
            if (await varstring.get_value() != ''):
                a = a + await varstring.get_value()
                varstring = Globalclient.get_node("ns=6;s=::FileInput:ErrorText2")
                #a = a + await varstring.get_value()
                varstring = Globalclient.get_node("ns=6;s=::FileInput:ErrorText3")
                a = a + await varstring.get_value()
                varstring = Globalclient.get_node("ns=6;s=::FileInput:ErrorText4")
                a = a + await varstring.get_value()
                varstring = Globalclient.get_node("ns=6;s=::FileInput:ErrorText5")
                a = a + await varstring.get_value()
                varstring = Globalclient.get_node("ns=6;s=::FileInput:ErrorText6")
                a = a + await varstring.get_value()
                varstring = Globalclient.get_node("ns=6;s=::FileInput:ErrorText7")
                a = a + await varstring.get_value()
                a.split()
                ' '.join(a.split())
                print(a)
                re.sub(r'\s', '', a)
                re.sub(r'\n', '', a)
                print(a)
                b = a

            self.widget.setText(str(self.widget.starttext + (str(handler.value)) + ' ' + a))
            #print((self.widget.holder))




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
p = ProcessPoolExecutor(4)
class StatusLabel(QLabel):
    def __init__(self):
        super(StatusLabel, self).__init__()
        self.setText("Last CNC status message: ")
        self.starttext = 'Last CNC status message: '
        self.data = 0
        self.holder = dict()
        self.Thread = SubscriptionThread("ns=6;s=::FileInput:ErrorMess", widget=self)
        self.Thread.start() #cоздаем отдельный поток qt
        print(threading.active_count())
    def readfile(self):
        i  = 0
        with open('arnc0err.csv') as f:
            r = csv.reader(f)
            cont = [row for row in r]
            print(type(cont))
            for i in range(len(cont) - 1):
                #print(cont[i])
                if ('F' not in cont[i][0]):
                    print(int(cont[i][0]), cont[i][1])
                    self.holder.update(dict.fromkeys([int(cont[i][0]), cont[i][1]]))


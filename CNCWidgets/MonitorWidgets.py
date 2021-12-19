from PyQt5.QtWidgets import QLabel
from CNCActions import OPCSub
import asyncio
import logging
import sys
sys.path.insert(0, "..")
import os
# os.environ['PYOPCUA_NO_TYPO_CHECK'] = 'True'

import asyncio
import logging

from asyncua import Client, Node, ua

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger('asyncua')
from CNCActions import OPCClient
class CoordX(QLabel):
    def __init__(self):
        super(CoordX, self).__init__()
        self.loop = asyncio.get_event_loop()
        self.loop.get_debug()
        self.setText("sex")
        self.data = 0
    async def sub(self):
        task = list()
        task.append(asyncio.create_task(OPCSub.main()))
        asyncio.gather(task[0])
        return True
    async def text(self):
        while True:
            print(str(OPCClient.SubscriptionHandler.value))
            self.setText(str(OPCClient.SubscriptionHandler.value))
from asyncua import (Client, ua)
import logging
import asyncio
import sys
sys.path.insert(0, "..")
import os
# os.environ['PYOPCUA_NO_TYPO_CHECK'] = 'True'

import asyncio
import logging

from asyncua import Client, Node, ua

logging.basicConfig(level=logging.INFO)
_logger = logging.getLogger('asyncua')
Globalclient = Client("opc.tcp://192.168.133.2:4841/")
async def Connect(client):
    await client.connect()
    Globalclient = client
    print("Connected")
    return True






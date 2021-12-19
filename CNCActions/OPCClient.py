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
Globalclient = Client("opc.tcp://localhost:4841/")
async def Connect(client):
    await client.connect()
    Globalclient = client
    print("Connected")
    return True
class SubscriptionHandler():
    """
    The SubscriptionHandler is used to handle the data that is received for the subscription.
    """
    value = 0
    def datachange_notification(self, node, val, data):
        """
        Callback for asyncua Subscription.
        This method will be called when the Client received a data change message from the Server.
        """
        print('datachange_notification %r %s', node, val, data)
        _logger.info('datachange_notification %r %s', node, val)
        value = val


async def subscribe(nodestring): #эта функция должна крутиться постоянно, так что ее надо вызывать через asyncio.run()
    """
    Main task of this Client-Subscription example.
    """
    data = ""
    client1 = Globalclient
    var = Globalclient.get_node(nodestring)
    handler = SubscriptionHandler()
    # We create a Client Subscription.
    subscription = await Globalclient.create_subscription(100, handler)
    # We subscribe to data changes for two nodes (variables).
    await subscription.subscribe_data_change(var)
    print("sub created")
    await asyncio.sleep((10))

    # We let the subscription run for ten seconds

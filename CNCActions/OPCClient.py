from asyncua import Client
client = Client("opc.tcp://localhost:4841/")
async def Connect():
    while True:
        Client.connect()

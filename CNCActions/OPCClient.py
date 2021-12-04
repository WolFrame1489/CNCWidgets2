from asyncua import Client
client = Client("opc.tcp://localhost:4841/")
def Connect():
    while True:
        Client.connect()

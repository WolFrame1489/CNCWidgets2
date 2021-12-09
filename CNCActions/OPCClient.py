from asyncua import (ua, Client)
Globalclient = Client("opc.tcp://localhost:4841/")
async def Connect(client):
    await client.connect()
    Globalclient = client
    print("Connected")
    return True
async def CNCActionPower():
    var = Globalclient.get_node("ns=6;s=::Program:Power")
    dv = ua.DataValue(ua.Variant(0, ua.VariantType.Boolean))
    await var.set_value(dv)
    print("power on")
    return True
async def CNCActionHoming(axis, homingtype):
    if (axis == "XY"):
        print("homing all axes")
        var = Globalclient.get_node("ns=6;s=::Program:Power")



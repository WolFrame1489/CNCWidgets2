from asyncua import (ua, Client)
Globalclient = Client("opc.tcp://localhost:4841/")
async def Connect(client):
    await client.connect()
    Globalclient = client
    print("Connected")
    return True
async def CNCActionPower(power):
    print("power")
    var = Globalclient.get_node("ns=6;s=::Program:Power")
    dv = ua.DataValue(ua.Variant(power, ua.VariantType.Boolean))
    await var.set_value(dv)
    return True
async def CNCActionHoming(axis, homingtype):
    if (axis == "XY"):
        print("homing all axes")
        var = Globalclient.get_node("ns=6;s=::Program:Homing_type")
        dv = ua.DataValue(ua.Variant(homingtype, ua.VariantType.Int16))
        await var.set_value(dv)
        dv = ua.DataValue(ua.Variant(bool(1), ua.VariantType.Boolean))
        var = Globalclient.get_node("ns=6;s=::Program:RehomeX")
        await var.set_value(dv)
        var = Globalclient.get_node("ns=6;s=::Program:RehomeY")
        await var.set_value(dv)
        print(await var.get_value())
        if ((await Globalclient.get_node("ns=6;s=::Program:RehomeX").get_value() == True) and (await Globalclient.get_node("ns=6;s=::Program:RehomeY").get_value() == True)):
            return True
        else:
            print((Globalclient.get_node("ns=6;s=::Program:AxisInit_1.HomingDone").get_value()))
    if (axis == "X"):
        print("homing axis X")
        var = Globalclient.get_node("ns=6;s=::Program:Homing_type")
        dv = ua.DataValue(ua.Variant(homingtype, ua.VariantType.Int16))
        await var.set_value(dv)
        dv = ua.DataValue(ua.Variant(bool(1), ua.VariantType.Boolean))
        var = Globalclient.get_node("ns=6;s=::Program:RehomeX")
        await var.set_value(dv)
        if ((await Globalclient.get_node("ns=6;s=::Program:RehomeX").get_value() == True)):
            return True
    if (axis == "Y"):
        print("homing axis Y")
        var = Globalclient.get_node("ns=6;s=::Program:Homing_type")
        dv = ua.DataValue(ua.Variant(homingtype, ua.VariantType.Int16))
        await var.set_value(dv)
        dv = ua.DataValue(ua.Variant(bool(1), ua.VariantType.Boolean))
        var = Globalclient.get_node("ns=6;s=::Program:RehomeY")
        await var.set_value(dv)
        if ((await Globalclient.get_node("ns=6;s=::Program:RehomeY").get_value() == True)):
            return True


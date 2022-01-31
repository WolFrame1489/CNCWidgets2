from asyncua import (ua, Client)
import asyncio
Globalclient = Client("opc.tcp://192.168.133.2:4841/")
GlobalGCODEString = "" #cрока для хранения жкода
Tool = 1
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
async def CNCActionStartBlock(block):
    print("start block")
    #var = Globalclient.get_node("ns=6;s=::AsGlobalPV:InputBlock")
    #dv = ua.DataValue(ua.Variant(block, ua.VariantType.String))
    #await var.set_value(dv)
    var = Globalclient.get_node("ns=6;s=::FileInput:Start")
    dv = ua.DataValue(ua.Variant(bool(1), ua.VariantType.Boolean))
    await var.set_value(dv)
    return True
async def CNCActionStopBlock():
    print("stop block")
    var = Globalclient.get_node("ns=6;s=::FileInput:Stop")
    dv = ua.DataValue(ua.Variant(bool(1), ua.VariantType.Boolean))
    await var.set_value(dv)
    return True
async def CNCActionContinueBlock():
    print("continue block")
    var = Globalclient.get_node("ns=6;s=::FileInput:Continue")
    dv = ua.DataValue(ua.Variant(bool(1), ua.VariantType.Boolean))
    await var.set_value(dv)
    return True
async def SwitchMode(inp):
    print("mode change")
    var = Globalclient.get_node("ns=6;s=::FileInput:Mode")
    val = inp
    dv = ua.DataValue(ua.Variant(bool(inp), ua.VariantType.Boolean))
    await var.set_value(dv)
    return True
async def JogMode(inp):
    print("jog")
    var = Globalclient.get_node("ns=6;s=::Program:Jogging")
    val = inp
    dv = ua.DataValue(ua.Variant(bool((val)), ua.VariantType.Boolean))
    await var.set_value(dv)
    return True
async def CNCActionJogX(am, g, s):
    var = Globalclient.get_node("ns=6;s=::Program:MoveXAmount")
    dv = ua.DataValue(ua.Variant(((am)), ua.VariantType.Float))
    await var.set_value(dv)
    var = Globalclient.get_node("ns=6;s=::Program:MoveXExec")
    dv = ua.DataValue(ua.Variant((bool(g)), ua.VariantType.Boolean))
    await var.set_value(dv)
    var = Globalclient.get_node("ns=6;s=::Program:StopX")
    dv = ua.DataValue(ua.Variant((bool(s)), ua.VariantType.Boolean))
    await var.set_value(dv)
    return True
async def CNCActionJogY(am, g, s):
    var = Globalclient.get_node("ns=6;s=::Program:MoveYAmount")
    dv = ua.DataValue(ua.Variant(((am)), ua.VariantType.Float))
    await var.set_value(dv)
    var = Globalclient.get_node("ns=6;s=::Program:MoveYExec")
    dv = ua.DataValue(ua.Variant((bool(g)), ua.VariantType.Boolean))
    await var.set_value(dv)
    var = Globalclient.get_node("ns=6;s=::Program:StopY")
    dv = ua.DataValue(ua.Variant((bool(s)), ua.VariantType.Boolean))
    await var.set_value(dv)
    return True
async def CNCActionChangeTool():
    global Tool
    var = Globalclient.get_node("ns=6;s=::Program:NeededTool")
    dv = ua.DataValue(ua.Variant(((Tool)), ua.VariantType.Int16))
    await var.set_value(dv)
    return True
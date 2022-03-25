# CNCWidgets2
This is a thesis work aimed at recreating LinuxCNC widget system on CNC machines, that have their own CNC controller aboard, using the PyQT5 and asyncua modules
For example, this code controls CNC Lathe based on B&R X20CP1586 controller within ACP10 and ARNC0 motion system, and uses OPC UA protocol for connection.
Most comments are in russian, I will translate them later
Contains several functions:
1) Tranfering PRG G-code files via FTP to the machine, starting, pausing, and stopping them
2) Scintilla editor for Single-step debug mode
3) Buttons widgets for homing, jogging axes, buttons for tool changing (you can find whole list in ActionButtons.py)
4) Status Widgets for monitoring done using subcription method
Folders and scripts:
main.py - draws interface with widgets, connects to the machine via OPC UA
OPCActions.py - Contains functions, that change the values of machine variables syncronously, use it for button functions
FTP.py - transfers a file
OPCClient.py - connects to OPC server
Widget files
ActionButtons.py - contains buttons for functions
Editor.py - Scintilla editor
InputString.py - String to input g-codes
MonitorWidgetStatus.py, MonitorWidgetStatusX.py, MonitorWidgetStatusY.py - current status and errors of cnc machine
MonitorWidgetX.py, MonitorWidgetY.py - shows curebnt axis positions
ToolBox - menu for changing tool

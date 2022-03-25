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
1. main.py - draws interface with widgets, connects to the machine via OPC UA
2. OPCActions.py - Contains functions, that change the values of machine variables syncronously, use it for button functions
3. FTP.py - transfers a file
4. OPCClient.py - connects to OPC server
5. Widget files
6. ActionButtons.py - contains buttons for functions
7. Editor.py - Scintilla editor
8. InputString.py - String to input g-codes
9. MonitorWidgetStatus.py, MonitorWidgetStatusX.py, MonitorWidgetStatusY.py - current status and errors of cnc machine
10. MonitorWidgetX.py, MonitorWidgetY.py - shows curebnt axis positions
11. ToolBox - menu for changing tool
Another branch with mappCNC version will be availible soon.

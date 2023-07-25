import subprocess
import psutil

def runMaya():
    version = 'Maya2024'
    mayaPyPath = 'C:\\Program Files\\Autodesk\\' + version + '\\bin\\maya.exe'
    isRunning = "maya.exe" in (p.name() for p in psutil.process_iter())

    s = subprocess.check_output('tasklist', shell= True)
    if not isRunning:
        maya = subprocess.Popen([mayaPyPath])
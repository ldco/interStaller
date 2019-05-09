from local import OSdist, userDir, Ul
from lang import lang

if OSdist == 'Win':
    import os
    import sys
    import shutil
    import sysconfig
    import winreg
    from win32com.client import Dispatch
    from vars import appName
    from local import applicationDir

    def get_reg(name, path):
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0,
                                          winreg.KEY_READ)
            value, regtype = winreg.QueryValueEx(registry_key, name)
            winreg.CloseKey(registry_key)
            return value
        except WindowsError:
            return None


# Package name
packageName = appName

# Scripts directory (location of launcher script)
scriptsDir = applicationDir

# Target of shortcut
target = os.path.join(scriptsDir, packageName + '.exe')

# Name of link file
linkName = packageName + '.lnk'

# Path to location of link file
_pathLink = os.path.join(userDir, 'Desktop')
pathLink = os.path.join(_pathLink, linkName)


def createWinShortcut():
    try:
        print(lang[Ul][47])
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(pathLink)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = scriptsDir
        shortcut.IconLocation = target
        shortcut.save()
        print(lang[Ul][48])
    except Exception as e:
        print(lang[Ul][49])
        print(e)


def removeWinShortcut():
    try:
        print(lang[Ul][50])
        os.remove(pathLink)
        print(lang[Ul][52])
    except Exception as e:
        print(lang[Ul][51])
        print(e)

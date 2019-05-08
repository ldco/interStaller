from download import Down
from unzip import Unzip
from local import Folder, localFilename, localDataFilename, applicationDir, localDataFoldername, Ul, OSdist
from threading import Timer

if OSdist == 'Win':
    from desktop import createWinShortcut
    from desktop import removeWinShortcut


f = Folder()
d = Down()
z = Unzip()

print("USER LANG = " + Ul)


def installApp():
    d.connectFTP()
    if not f.appExists:
        f.mkDirApp()
    else:
        f.uninstallApp()
        f.mkDirApp()
    d.downloadAppFiles()
    d.disConnectFTP()
    z.unzippApp(localFilename, applicationDir)
    if OSdist == 'Win':
        createWinShortcut()


def installData():
    d.connectFTP()
    if not f.dataExists:
        if f.configExists:
            f.uninstallConfig()
            f.mkDirConfig()
        f.mkDirConfig()
        f.mkDirData()
    else:
        f.uninstallConfig()
        f.mkDirConfig()
        f.mkDirData()

    d.downloadDataFiles()
    d.disConnectFTP()
    z.unzippApp(localDataFilename, localDataFoldername)


def uninstalAll():
    t = Timer(2.0, f.uninstallApp)
    f.uninstallConfig()
    t.start()
    if OSdist == 'Win':
        removeWinShortcut()


def installAppData():
    installApp()
    installData()


def backupData():
    pass

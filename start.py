from local import Folder
from download import Down


f = Folder()
d = Down()

f.exist()

if not f.appExists:
    f.mkDirApp()
else:
    f.uninstallApp()
    f.mkDirApp()

d.connectFTP()
d.downloadAppFiles()

if not f.dataExists:
    f.mkDirData()
    d.downloadDataFiles()
else:
    q = input(
        'Data folder exist. Overwrite with initial data? WARNING: all data will be lost!\nn/y\n')
    if q == 'y':
        f.uninstallData()
        f.mkDirData()
        # d.downloadDataFiles()
    elif q == 'n':
        print('Data folder will not be reset')
    else:
        print('Please select y or n. n is recomended')

d.disConnectFTP()

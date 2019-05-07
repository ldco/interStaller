from local import Folder
from download import Down
from unzip import Unzip
from local import localFilename
from local import localDataFilename
from local import applicationDir
from local import localDataFoldername


f = Folder()
d = Down()
z = Unzip()

f.exist()
if not f.appExists:
    f.mkDirApp()
else:
    f.uninstallApp()
    f.mkDirApp()

d.connectFTP()
d.downloadAppFiles()

if not f.dataExists:
    if f.configExists:
        f.uninstallConfig()
        f.mkDirConfig()
    f.mkDirConfig()
    f.mkDirData()
    d.downloadDataFiles()
else:
    q = input(
        'Data folder exist. Overwrite with initial data? WARNING: all data will be lost!\nn/y\n')
    if q == 'y':
        f.uninstallConfig()
        f.mkDirConfig()
        f.mkDirData()
        d.downloadDataFiles()
    elif q == 'n':
        print('Data folder will not be reset')
    else:
        print('Please select y or n. n is recomended')

d.disConnectFTP()

z.unzippApp(localFilename, applicationDir)
z.unzippApp(localDataFilename, localDataFoldername)

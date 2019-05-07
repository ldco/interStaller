import os
import sys
import platform
import shutil
from vars import appName

if platform.system() == 'Linux':
    OSdist = 'Lin'
    userDir = os.environ['HOME']
    localAppData = os.path.join(userDir, '.config')
    innerPath = ""
if platform.system() == 'Windows':
    OSdist = 'Win'
    userDir = os.environ['HOMEPATH']
    localAppData = os.environ['APPDATA']
    innerPath = ""

applicationDir = os.path.join(userDir, appName)
applicationData = os.path.join(localAppData, appName)
appFilename = appName + OSdist + 'Dist.zip'
localDataFoldername = applicationData + '/' + 'Data'
localFilename = applicationDir + '/' + appFilename
localDataFilename = localDataFoldername + '/' + 'Data.zip'


class Folder:
    appExists = False
    dataExists = False
    configExists = False

    def exist(self):
        print('Checking for existing app folders')
        if os.path.exists(applicationDir):
            self.appExists = True
            print('App directory exists')
        else:
            self.appExists = False
            print('App directory not exists')

        if os.path.exists(applicationData):
            self.configExists = True
            print('Config directory exists')
        else:
            self.configExists = False
            print('Config directory not exists')

        if os.path.exists(localDataFoldername):
            self.dataExists = True
            print('Data directory exists')
        else:
            self.dataExists = False
            print('Data directory not exists')

    def uninstallApp(self):
        print('Removing old version')
        try:
            shutil.rmtree(applicationDir)
            print('Old version removed')
        except Exception as e:
            print(e)
            print('Error removing old version')
        # FOR WINDOWS
        taskKill = 'taskkill /f /im  ' + appName + '.exe'
        if OSdist == 'Win':
            print('killing Windows task')
            try:
                os.system(taskKill)
                print('Windows task killed')
            except Exception as e:
                print(e)
                print('Error killing Windows task')

    def uninstallConfig(self):
        print('Removing Config and Data!')
        try:
            shutil.rmtree(applicationData)
            print('Config and Data removed')
        except Exception as e:
            print(e)
            print('Error removing Config and Data')

    def mkDirApp(self):
        try:
            print('Creating new app folder')
            os.makedirs(applicationDir)
            print('New app folder created as ' + applicationDir)
        except Exception as e:
            print(e)
            print('Error create new app folder')

    def mkDirConfig(self):
        try:
            print('Creating new config folder')
            os.makedirs(applicationData)
            print('New config folder created as ' + applicationData)
        except Exception as e:
            print(e)
            print('Error create new config folder')

    def mkDirData(self):
        try:
            print('Creating new data folder')
            os.makedirs(localDataFoldername)
            print('New Data folder created as ' + localDataFoldername)
        except Exception as e:
            print(e)
            print('Error create new Data folder')

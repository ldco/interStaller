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


class Folder:
    appExists = False
    dataExists = False

    def exist(self):
        if os.path.exists(applicationDir):
            self.appExists = True
            print('App directory exists')
        else:
            self.appExists = False
            print('App directory not exists')
        if os.path.exists(applicationData):
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
        except:
            print('Error removing old version')
        # FOR WINDOWS
        taskKill = 'taskkill /f /im  ' + appName + '.exe'
        if OSdist == 'Win':
            print('killing Windows task')
            try:
                os.system(taskKill)
                print('Windows task killed')
            except:
                print('Error killing Windows task')

    def uninstallData(self):
        print('Removing Data!')
        try:
            shutil.rmtree(applicationData)
            print('Data removed')
        except:
            print('Error removing Data')

    def mkDirApp(self):
        try:
            os.makedirs(applicationDir)
            print('New app folder created')
        except:
            print('Error create new app folder')

    def mkDirData(self):
        try:
            os.makedirs(applicationData)
            print('New Data folder created')
        except:
            print('Error create new Data folder')

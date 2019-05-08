import os
import sys
import platform
import shutil
import locale
from vars import appName
from lang import lang

# GET OS
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
    import ctypes

# GET USER LOCAL LANGUAGE
if OSdist == 'Lin':
    locale.setlocale(locale.LC_ALL, "")
    userLang = locale.getlocale(locale.LC_MESSAGES)[0]

if OSdist == 'Win':
    windll = ctypes.windll.kernel32
    windll.GetUserDefaultUILanguage()
    userLang = locale.windows_locale[windll.GetUserDefaultUILanguage()]

Ul = userLang[:2]


# FOLDERS & FILES VARS
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
        print(lang[Ul][15])
        if os.path.exists(applicationDir):
            self.appExists = True
            print(lang[Ul][16])
        else:
            self.appExists = False
            print(lang[Ul][17])

        if os.path.exists(applicationData):
            self.configExists = True
            print(lang[Ul][18])
        else:
            self.configExists = False
            print(lang[Ul][19])

        if os.path.exists(localDataFoldername):
            self.dataExists = True
            print(lang[Ul][20])
        else:
            self.dataExists = False
            print(lang[Ul][21])

    def uninstallApp(self):
        print(lang[Ul][22])
        try:
            self.killWinTask()
            shutil.rmtree(applicationDir)
            print(lang[Ul][23])
        except Exception as e:
            print(e)
            # print(lang[Ul][24])

    def uninstallConfig(self):
        print(lang[Ul][28])
        try:
            self.killWinTask()
            shutil.rmtree(applicationData)
            print(lang[Ul][44])
        except Exception as e:
            print(e)
            print(lang[Ul][29])

    def mkDirApp(self):
        try:
            print(lang[Ul][30])
            os.makedirs(applicationDir)
            print(lang[Ul][31] + applicationDir)
        except Exception as e:
            print(e)
            print(lang[Ul][32])

    def mkDirConfig(self):
        try:
            print(lang[Ul][33])
            os.makedirs(applicationData)
            print(lang[Ul][34] + applicationData)
        except Exception as e:
            print(e)
            print(lang[Ul][35])

    def mkDirData(self):
        try:
            print(lang[Ul][36])
            os.makedirs(localDataFoldername)
            print(lang[Ul][37] + localDataFoldername)
        except Exception as e:
            print(e)
            print(lang[Ul][38])

    def killWinTask(self):
        # FOR WINDOWS
        taskKill = 'taskkill /f /im  ' + appName + '.exe'
        if OSdist == 'Win':
            print(lang[Ul][25])
            try:
                os.system(taskKill)
                print(lang[Ul][26])
            except Exception as e:
                print(e)
                print(lang[Ul][27])

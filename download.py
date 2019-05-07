from ftplib import FTP
from local import OSdist
from local import applicationDir
from local import applicationData
from local import localDataFilename
from local import localFilename
from local import appFilename
from vars import *


class Down:

    url = appName + '/Dist/' + OSdist
    dataUrl = appName + '/Data/'

    dataFileName = 'Data.zip'

    def connectFTP(self):
        try:
            global ftp
            ftp = FTP(ftpHost)
            ftp.login(user=ftpUsername, passwd=ftpPassword)
            print('Connected to FTP')
            # printL("מחובר לשרת")
        except Exception as e:
            print(e)
            print('Error connect to FTP')
            # printL("אירעה שגיאה...")

    def downloadAppFiles(self):
        try:
            ftp.cwd(self.url)
            print('Changed directory to ' + ftp.pwd())
            # printL("מוריד קבצים")
        except Exception as e:
            print(e)
            print('Error change directory to Dist')
            # printL("אירעה שגיאה...")
        try:
            print('Downloading app files...')

            open(localFilename, 'wb')
            ftp.retrbinary('RETR ' + appFilename,
                           open(localFilename, 'wb').write)
            print('Zip app downloaded')
        except Exception as e:
            print(e)
            print('Error downloading app')
            # printL("אירעה שגיאה...")

    def downloadDataFiles(self):
        try:
            print('Changing directory to Data')
            ftp.cwd('..')
            ftp.cwd('..')
            ftp.cwd('Data')
            print('Changed directory to ' + ftp.pwd())
            # printL("מוריד קבצים")
        except Exception as e:
            print(e)
            print('Error change directory to Data')
            # printL("אירעה שגיאה...")
        try:
            print('Downloading Data file...')
            open(localDataFilename, 'wb')
            ftp.retrbinary('RETR ' + self.dataFileName,
                           open(localDataFilename, 'wb').write)
            print('Zip Data downloaded')
        except Exception as e:
            print(e)
            print('Error downloading Data')
            # printL("אירעה שגיאה...")

    def disConnectFTP(self):
        try:
            print('Disconnecting from FTP...')
            ftp.quit()
            print('Disconnected from FTP')
            # printL("נותק מהשרת")

        except Exception as e:
            print(e)
            print('Error disconnect from ftp')
            # printL("אירעה שגיאה...")

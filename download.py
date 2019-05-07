from ftplib import FTP
from local import OSdist
from local import applicationDir
from local import applicationData
from vars import *


class Down:

    url = appName + '/Dist/' + OSdist
    dataUrl = appName + '/Data/'
    appFilename = appName + OSdist + 'Dist.zip'
    localFilename = applicationDir + '/' + appFilename
    dataFilename = 'Data.zip'
    localDataFilename = applicationData + '/' + dataFilename

    def connectFTP(self):
        try:
            global ftp
            ftp = FTP(ftpHost)
            ftp.login(user=ftpUsername, passwd=ftpPassword)
            print('Connected to FTP')
            # printL("מחובר לשרת")
        except:
            print('Error connect to FTP')
            # printL("אירעה שגיאה...")

    def downloadAppFiles(self):
        try:
            ftp.cwd(self.url)
            print('Changed directory to Dist')
            # printL("מוריד קבצים")
        except:
            print('Error change directory to Dist')
            # printL("אירעה שגיאה...")
        try:
            print('Downloading app files...')
            open(self.localFilename, 'wb')
            ftp.retrbinary('RETR ' + self.appFilename,
                           open(self.localFilename, 'wb').write)
            print('Zip app downloaded')
        except:
            print('Error downloading app')
            # printL("אירעה שגיאה...")

    def downloadDataFiles(self):
        try:
            ftp.cwd(self.dataUrl)
            print('Changed directory to Data')
            # printL("מוריד קבצים")
        except:
            print('Error change directory to Data')
            # printL("אירעה שגיאה...")
        try:
            print('Downloading Data file...')
            open(self.localDataFilename, 'wb')
            ftp.retrbinary('RETR ' + self.dataFilename,
                           open(self.localDataFilename, 'wb').write)
            print('Zip Data downloaded')
        except:
            print('Error downloading Data')
            # printL("אירעה שגיאה...")

    def disConnectFTP(self):
        try:
            print('Disconnecting from FTP...')
            ftp.quit()
            print('Disconnected from FTP')
            # printL("נותק מהשרת")

        except:
            print('Error disconnect from ftp')
            # printL("אירעה שגיאה...")

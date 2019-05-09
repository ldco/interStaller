from ftplib import FTP
from local import OSdist, applicationDir, applicationData, localDataFilename, localFilename, appFilename, Ul
from vars import *
from lang import lang


class Down:

    url = appName + '/Dist/' + OSdist
    dataUrl = appName + '/Data/'

    dataFileName = 'Data.zip'

    def connectFTP(self):
        try:
            global ftp
            ftp = FTP(ftpHost)
            ftp.login(user=ftpUsername, passwd=ftpPassword)
            print(lang[Ul][1])

        except Exception as e:
            print(e)
            print(lang[Ul][2])

    def downloadAppFiles(self):
        try:
            print(lang[Ul][43])
            ftp.cwd(self.url)
            print(lang[Ul][3] + ftp.pwd())

        except Exception as e:
            print(e)
            print(lang[Ul][4] + ftp.pwd())

        try:
            print(lang[Ul][5])

            open(localFilename, 'wb')
            ftp.retrbinary('RETR ' + appFilename,
                           open(localFilename, 'wb').write)
            print(lang[Ul][6])
        except Exception as e:
            print(e)
            print(lang[Ul][7])

    def downloadDataFiles(self):
        try:
            print(lang[Ul][8])
            ftp.cwd(self.dataUrl)
            print(lang[Ul][3] + ftp.pwd())

        except Exception as e:
            print(e)
            print(lang[Ul][4] + ftp.pwd())

        try:
            print(lang[Ul][9])
            open(localDataFilename, 'wb')
            ftp.retrbinary('RETR ' + self.dataFileName,
                           open(localDataFilename, 'wb').write)
            print(lang[Ul][10])
        except Exception as e:
            print(e)
            print(lang[Ul][11])

    def disConnectFTP(self):
        try:
            print(lang[Ul][12])
            ftp.quit()
            print(lang[Ul][13])

        except Exception as e:
            print(e)
            print(lang[Ul][14])

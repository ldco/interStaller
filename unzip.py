import zipfile
import os


class Unzip:
    def unzippApp(self, file, dest):
        try:
            zip = zipfile.ZipFile(file)
            print('Extracting files from ' + file + "...")
            # printL("מחלץ קבצים")
            zip.extractall(dest)
            print('Extracted files from ' + file + "...")
        except Exception as e:
            print(e)
            print('Error extracting files from ' + file + "...")
        try:
            print('Removing zip ' + file + "...")
            zip.close()
            os.remove(file)
        except Exception as e:
            print(e)
            print('Error removing zip ' + file + "...")

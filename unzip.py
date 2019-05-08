import zipfile
import os
from local import Ul
from lang import lang


class Unzip:
    def unzippApp(self, file, dest):
        try:
            zip = zipfile.ZipFile(file)
            print(lang[Ul][39] + file + "...")
            zip.extractall(dest)
            print(lang[Ul][40] + file + "...")
        except Exception as e:
            print(e)
            print(lang[Ul][41] + file + "...")
        try:
            print(lang[Ul][45] + file + "...")
            zip.close()
            os.remove(file)
            print(lang[Ul][46] + file + "...")
        except Exception as e:
            print(e)
            print(lang[Ul][42] + file + "...")

from start import installApp, installData, installAppData, uninstalAll, backupData
from local import Folder, Ul
from lang import lang


class CLI:
    f = Folder()
    f.exist()
    if f.appExists:
        if f.dataExists:
            print(lang[Ul][60])
            q = input(lang[Ul][53])
        if not f.dataExists:
            print(lang[Ul][62])
            q = input(lang[Ul][54])
    if not f.appExists:
        if f.dataExists:
            print(lang[Ul][63])
            q = input(lang[Ul][55])
        if not f.dataExists:
            print(lang[Ul][61])
            q = input(lang[Ul][56])
    print(q)
    if q == '1':
        installApp()
    elif q == '2':
        installAppData()
    elif q == '3':
        uninstalAll()
    elif q == '4':
        backupData()
    elif q == '5':
        exit()

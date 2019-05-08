from start import installApp, installData, uninstalAll, backupData
from local import Folder, Ul
from lang import lang

f = Folder()
f.exist()
if f.appExists:
    if f.dataExists:
        q = input(lang[Ul][53])
    if not f.dataExists:
        q = input(lang[Ul][54])
if not f.appExists:
    if f.dataExists:
        q = input(lang[Ul][55])

    if not f.dataExists:
        q = input(lang[Ul][56])
print(q)
if q == '1':
    installApp()
elif q == '2':
    installApp()
    installData()
elif q == '3':
    uninstalAll()
elif q == '4':
    backupData()
elif q == '5':
    exit()

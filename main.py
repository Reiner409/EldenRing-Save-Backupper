import os.path
import datetime
import shutil


def dataOdierna():
    dataAttuale = datetime.datetime.now()
    return f'{dataAttuale.year}_{dataAttuale.month}_{dataAttuale.day} {dataAttuale.hour}_{dataAttuale.minute}'


BackupFolderName = "Backup"
Save = "ER0000.sl2"
BackupSave = "ER0000.sl2.bak"
data = dataOdierna()
Cartella = os.path.expandvars(r'%APPDATA%\EldenRing')
print(Cartella)
ListaCartelleER = os.listdir(Cartella)
for i in ListaCartelleER:
    if i == "GraphicsConfig.xml":
        continue
    print(i)
    src = os.path.expandvars(fr'%APPDATA%\EldenRing\{i}')
    ListaCartella = os.listdir(src)
    if not ListaCartella.__contains__(BackupFolderName):
        print("Non ho trovato la cartella allora la creo")
        os.mkdir(os.path.expandvars(fr'{src}\{BackupFolderName}'))
    try:
        os.mkdir(os.path.expandvars(fr'{src}\{BackupFolderName}\Backup - {data}'))
    except:
        folder = fr'{src}\{BackupFolderName}\Backup - {data}'
        os.remove(os.path.expandvars(fr'{folder}\{Save}'))
        os.remove(os.path.expandvars(fr'{folder}\{BackupSave}'))
    finally:
        dst = fr'{src}\{BackupFolderName}\Backup - {data}'
        shutil.copyfile(os.path.expandvars(fr'{src}\{Save}'), os.path.expandvars(fr'{dst}\{Save}'))
        shutil.copyfile(os.path.expandvars(fr'{src}\{BackupSave}'), os.path.expandvars(fr'{dst}\{BackupSave}'))
        print("Copiato con successo tutti i files")
        os.system("pause")


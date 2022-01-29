import ftplib
import asyncio
text = """"""
def ftp_upload(ftp_obj, path, ftype='PRG'):
    """
    Функция для загрузки файлов на FTP-сервер
    @param ftp_obj: Объект протокола передачи файлов
    @param path: Путь к файлу для загрузки
    """
    if ftype == 'PRG':
        with open(path) as fobj:
            ftp_obj.storlines('STOR ' + path, fobj)
    else:
        with open(path, 'rb') as fobj:
            ftp_obj.storbinary('STOR ' + path, fobj, 1024)

async def TransferFile():
    ftp = ftplib.FTP()
    HOST = '192.168.133.2'
    PORT = 21
    ftp.connect(HOST, PORT)

    ftp.login('user', 'aaa')
    ftp.cwd(r'C:\CNC_Prg')
    filename = 'testcnc.PRG'
    with open(filename, "rb") as file:
        # use FTP's STOR command to upload the file
        ftp.storbinary(f"STOR {filename}", file)
    ftp.quit()
    return True
def Connect():
    ftp = ftplib.FTP()
    HOST = '192.168.133.2'
    PORT = 21
    ftp.connect(HOST, PORT)

    ftp.login('user', 'aaa')
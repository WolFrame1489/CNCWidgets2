import ftplib

def ftp_upload(ftp_obj, path, ftype='TXT'):
    """
    Функция для загрузки файлов на FTP-сервер
    @param ftp_obj: Объект протокола передачи файлов
    @param path: Путь к файлу для загрузки
    """
    if ftype == 'TXT':
        with open(path) as fobj:
            ftp_obj.storlines('STOR ' + path, fobj)
    else:
        with open(path, 'rb') as fobj:
            ftp_obj.storbinary('STOR ' + path, fobj, 1024)


def TransferFile(PathToFile):
    ftp = ftplib.FTP('host', 'username', 'password')
    ftp.login()

    path = '/path/to/something.txt'
    ftp_upload(ftp, path)
    ftp.quit()
def Connect():
    ftp = ftplib.FTP()
    HOST = 'ftp.cse.buffalo.edu'
    PORT = 12345
    ftp.connect(HOST, PORT)
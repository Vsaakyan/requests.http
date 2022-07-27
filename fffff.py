
from yy import YandexDisk

TOKEN = ""

if __name__ == '__main__':
    ya = YandexDisk(token="")
    ya.upload_file_to_disk("netoloy.dz", "yadisk.txt")
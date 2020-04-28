import os
import shutil
import datetime
import time


# создание файла
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


# создание папки
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Same folder already exists')


# список файлов
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# удаление папки/файла
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


# копирование файла/папки
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Same folder already exists')
    else:
        shutil.copy(name, new_name)


# информация о файле/папке
def info(name):
    result = os.stat(name)
    print(f'Inode protection mode - {result.st_mode}')
    print(f'Inode number - {result.st_ino}')
    print(f'Device inode resides on - {result.st_dev}')
    print(f'Number of links to the inode - {result.st_nlink}')
    print(f'User id of the owner - {result.st_uid}')
    print(f'Group id of the owner - {result.st_gid}')
    print(f'Size in bytes of a plain file - {result.st_size}')
    print(f'Time of last access - {time.ctime(result.st_atime)}')
    print(f'Time of last modification - {time.ctime(result.st_mtime)}')
    print(f'Time of creation - {time.ctime(result.st_ctime)}')


# запись инф-ции о работе
def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')

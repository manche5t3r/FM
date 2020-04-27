import sys
from func_for_FM import create_file, create_folder, get_list, delete_file, copy_file, save_info, inf_file

save_info('start')

try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо ввести команду. Попробуйте: help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        name = sys.argv[2]
        create_folder(name)
    elif command == 'delete':
        name = sys.argv[2]
        delete_file(name)
    elif command == 'copy':
        name = sys.argv[2]
        new_name = sys.argv[3]
        copy_file(name, new_name)
    elif command == 'inf_file':
        name = sys.argv[2]
        inf_file(name)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла/папки')
        print('copy - копирование файла/папки')
        print('inf_file - информация о файле')

    save_info('End')


    # if __name__ == '__main__':

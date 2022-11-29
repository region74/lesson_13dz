import sys
import os
import shutil
import platform
import pickle

while True:
    print('1. Создать папку')
    print('2. Удалить файл/папку')
    print('3. Копировать файл/папку')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Сохранение содержимого рабочей директории')
    print('6. Просмотреть информацию об ОС')
    print('7. Создатель программы')
    print('8. Смена рабочей дирректории*')
    print('9. выход (и проверка сохранения)')

    choice = input('Выберите пункт меню: \n')

    # создать папку
    if choice == '1':
        folder = input('Введите имя папки: ')
        if os.path.exists(f'{folder}'):
            print('Такая папка уже есть!\n')
        else:
            os.mkdir(f'{folder}')
            print('Папка создана!\n')

    # удалить папку
    elif choice == '2':
        del_folder = input('Введите имя папки: ')
        if os.path.exists(f'{del_folder}'):
            print(f'Папка {del_folder} удалена! ')
            os.rmdir(f'{del_folder}')
        else:
            print('Папка не найдена!')

    # копировать папку
    elif choice == '3':
        copy_folder = input('Введите целевой папки: ')
        if os.path.exists(f'{copy_folder}'):
            print(f'Папка {copy_folder} скопирована, введите новое имя папки:')
            new_folder = input()
            shutil.copytree(f'{copy_folder}', f'{new_folder}')
            print('Копия создана!\n')
        else:
            print('Папка не найдена!\n')

    # просмотр содержимого рабочей дирректории
    elif choice == '4':
        print(os.listdir())

    # сохранение списка рабочей дирректории
    elif choice == '5':
        list_folders = []
        list_files = []
        for i in os.listdir():
            if os.path.isdir(i):
                list_folders.append(i)
            else:
                list_files.append(i)
        folders_dict = {
            'files': list_files,
            'folders': list_folders
        }
        with open('folders.txt', 'wb') as f:
            pickle.dump(folders_dict, f)
        print(folders_dict)

    # сведения о системе
    elif choice == '6':
        print(sys.platform)
        print(os.name)
        print(platform.uname())
        print(platform.platform())
        print(platform.architecture())
        print(platform.system())

    # автор проги
    elif choice == '7':
        print(f'Автор программы: {os.getlogin()}')

    # смена каталога
    elif choice == '8':
        print(f'Текущий катлог: {os.getcwd()}')
        link = input('Введите новый путь: ')
        os.chdir(link)
        print(f'Текущий катлог: {os.getcwd()}')

    # выход
    elif choice == '9':
        with open('folders.txt', 'rb') as f:
            result = pickle.load(f)
            print(result)
        break
    else:
        print('Неверный пункт меню')
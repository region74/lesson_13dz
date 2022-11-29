import sys
import os
import shutil
import platform

if __name__ == '__main__':
    while True:
        print('1. ������� �����')
        print('2. ������� ����/�����')
        print('3. ���������� ����/�����')
        print('4. �������� ����������� ������� ����������')
        print('5. ����������� ������ �����')
        print('6. ����������� ������ �����')
        print('7. ����������� ���������� �� ��')
        print('8. ��������� ���������')
        print('9. ������ � ���������')
        print('10. ������ � ���������� ����')
        print('11. ����� ������� �����������*')
        print('12. �����')

        choice = input('�������� ����� ����: \n')
        if choice == '1':
            folder = input('������� ��� �����: ')
            if os.path.exists(f'{folder}'):
                print('����� ����� ��� ����!\n')
            else:
                os.mkdir(f'{folder}')
                print('����� �������!\n')
        elif choice == '2':
            del_folder = input('������� ��� �����: ')
            if os.path.exists(f'{del_folder}'):
                print(f'����� {del_folder} �������! ')
                os.rmdir(f'{del_folder}')
            else:
                print('����� �� �������!')
        elif choice == '3':
            copy_folder = input('������� ������� �����: ')
            if os.path.exists(f'{copy_folder}'):
                print(f'����� {copy_folder} �����������, ������� ����� ��� �����:')
                new_folder = input()
                shutil.copytree(f'{copy_folder}', f'{new_folder}')
                print('����� �������!\n')
            else:
                print('����� �� �������!\n')
        elif choice == '4':
            print(os.listdir())
        elif choice == '5': 
            list_folders = []
            list_files = []
            for i in os.listdir():
                if os.path.isdir(i):
                    list_folders.append(i)
                else:
                    list_files.append(i)

        elif choice == '6':
            list_files = []
            for i in os.listdir():
                if os.path.isfile(i):
                    list_files.append(i)
            print(list_files)
        elif choice == '7':
            print(sys.platform)
            print(os.name)
            print(platform.uname())
            print(platform.platform())
            print(platform.architecture())
            print(platform.system())
        elif choice == '8':
            print(f'����� ���������: {os.getlogin()}')
        elif choice == '9':
            pass
        elif choice == '10':
            pass
        elif choice == '11':
            print(f'������� ������: {os.getcwd()}')
            link = input('������� ����� ����: ')
            os.chdir(link)
            print(f'������� ������: {os.getcwd()}')
        elif choice == '12':
            break
        else:
            print('�������� ����� ����')
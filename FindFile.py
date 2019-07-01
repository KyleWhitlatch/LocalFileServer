import os
import re
from sys import argv
from pathlib import Path
import shutil



def move_file(src_path,dst_path):
    # obj = re.search('[A-Z]:','C:\\Windows')
    # if obj.span() in [(0,2)]:
    #     print(True)
    #C:\Users\John\Desktop\file.txt
    # folders = re.match('[A-Z]:\\\\(.+\\\\)*',path)
    # folder = folders.group(0)
    # folder = add_backslashes(folder)

    #Idea Contributed by userman2 on Twitch or sharkbound on GitHub
    src_path = Path(src_path)
    dst_path = Path(dst_path)
    print(f'CWD: {os.getcwd()}')
    if not src_path.exists():
        print('Source Path Does Not Exist.')
    if not dst_path.exists():
        print('Destination Path Does not Exist')
    if not (src_path.exists() and dst_path.exists()):
        exit(1337)
    if not src_path.is_file():
        print('Source Path does not point to a file')
    if dst_path.is_file():
        print('Destination Path points to file, will not be able to restore')
    if not (src_path.is_file() and not dst_path.is_file()):
        exit(42)
    newpath = shutil.copy(src_path,dst_path)







# def add_backslashes(string):
#     splitpath = string.split('\\')
#     print(splitpath)
#     path = '\\\\'.join(splitpath)
#     path = path[:len(path)-2]
#     return path



# path = Path(argv[1])
# print(f'path: {path}')
# print(f'path exists? {path.exists()}')
# print(f'absolute path: {path.absolute()}')
# print(f'is file? {path.is_file()}')
# print(f'is directory? {path.is_dir()}')
# print(f'parent? {path.parent}')

move_file(argv[1])
#add_backslashes(argv[1])

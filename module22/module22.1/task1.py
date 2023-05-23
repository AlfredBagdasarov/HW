import os

rel_path = os.path.join('access', 'admin.bat')
abs_path = os.path.abspath(rel_path)
print('Относительный путь до файла:', rel_path)
print('Абсолютный путь до файла:', abs_path)

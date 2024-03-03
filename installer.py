import tkinter.messagebox
import os

#Display message 1
tkinter.messagebox.showinfo(title='Установка FastType', message='Подождите пожалуйста, идет установка программы FastType, данное окно можно закрыть')

#Installing
os.system('mkdir C:\ProgramFiles\FastType')
os.system('mkdir C:\ProgramFiles\FastType\img')
os.system('mkdir C:\ProgramFiles\FastType\levels')
os.system('wget -P C:\ProgramFiles\FastType https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_3/NewVersion.exe')

print('su')
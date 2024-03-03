import tkinter.messagebox
import os

#Display message 1
tkinter.messagebox.showinfo(title='Установка FastType', message='Подождите пожалуйста, идет установка программы FastType, данное окно можно закрыть')

#Making structure
os.system('mkdir C:\Program Files\FastType')
os.system('mkdir C:\Program Files\FastType\img')
os.system('mkdir C:\Program Files\FastType\levels')

#Download files
os.system('curl -o C:\Program Files\FastType\FastType.exe https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/FastType.exe')
for i in range (0, 10):
	os.system(f'curl -o C:\Program Files\FastType\img\level{i}.txt https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/levels/level{i}.txt')
os.system('curl -o C:\Program Files\FastType\img\clock_64.png https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/img/clock_64.png')
os.system('curl -o C:\Program Files\FastType\img\home.png https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/img/home.png')
os.system('curl -o C:\Program Files\FastType\img\key_64.png https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/img/key_64.png')
os.system('curl -o C:\Program Files\FastType\img\menu.png https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/img/menu.png')
os.system('curl -o C:\Program Files\FastType\img\mist_64.png https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/img/mist_64.png')

#Add link
os.system('curl -o C:\ProgramData\Microsoft\Windows\Start Menu\Programs\FastType.ink https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/installer/FastType.ink')

print('su')
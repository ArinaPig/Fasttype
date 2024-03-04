import customtkinter as ctk
import os
import threading
import tkinter.messagebox

#Display message 1
def window1():
	global progressbar, install

	install = ctk.CTk()
	install.title("Идёт установка...")
	install.wm_attributes("-topmost", 1)
	install.geometry("600x400")
	
	#Generating interface
	frm = ctk.CTkFrame(install)
	ctk.CTkLabel(frm, text="Идет установка программы...", font=('Arial', 23)).pack()
	progressbar = ctk.CTkProgressBar(frm, orientation="horizontal")
	progressbar.set(0)
	progressbar.pack()
	frm.pack(expand=True)
	ctk.CTkLabel(install, text="Подождите пожалуйста", font=('Arial', 17)).pack()
	
	#Start window
	install.mainloop()

def installing():
	#Making structure
	os.system(r'mkdir "C:\Program Files\FastType"')
	os.system(r'mkdir "C:\Program Files\FastType\img"')
	os.system(r'mkdir "C:\Program Files\FastType\levels"')
	
	#Download files
	os.system(r'curl -o "C:\Program Files\FastType\FastType.exe" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/FastType.exe')
	progressbar.set(0.3)
	os.system(r'curl -o "C:\Program Files\FastType\levels\level1(true).txt" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/levels/level1(true).txt')
	os.system(r'curl -o "C:\Program Files\FastType\levels\level1.txt" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/levels/level1.txt')
	os.system(r'curl -o "C:\Program Files\FastType\levels\level2.txt" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/levels/level2.txt')
	os.system(r'curl -o "C:\Program Files\FastType\levels\level3.txt" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/levels/level3.txt')
	os.system(r'curl -o "C:\Program Files\FastType\levels\level4.txt" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/levels/level4.txt')
	os.system(r'curl -o "C:\Program Files\FastType\levels\level5.txt" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/levels/level5.txt')
	os.system(r'curl -o "C:\Program Files\FastType\levels\level6.txt" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/levels/level6.txt')
	os.system(r'curl -o "C:\Program Files\FastType\levels\level7.txt" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/levels/level7.txt')
	os.system(r'curl -o "C:\Program Files\FastType\levels\level8.txt" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/levels/level8.txt')
	os.system(r'curl -o "C:\Program Files\FastType\levels\level9.txt" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/levels/level9.txt')
	os.system(r'curl -o "C:\Program Files\FastType\levels\level10.txt" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/levels/level10.txt')
	os.system(r'curl -o "C:\Program Files\FastType\levels\level11.txt" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/levels/level11.txt')
	os.system(r'curl -o "C:\Program Files\FastType\levels\level12.txt" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/levels/level12.txt')
	progressbar.set(0.6)
	os.system(r'curl -o "C:\Program Files\FastType\img\clock_64.png" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/img/clock_64.png')
	os.system(r'curl -o "C:\Program Files\FastType\img\home.png" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/img/home.png')
	os.system(r'curl -o "C:\Program Files\FastType\img\key_64.png" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/img/key_64.png')
	os.system(r'curl -o "C:\Program Files\FastType\img\menu.png" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/img/menu.png')
	os.system(r'curl -o "C:\Program Files\FastType\img\mist_64.png" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/App/img/mist_64.png')
	progressbar.set(0.9)

	#Add link
	os.system(r'curl -o "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\FastType.lnk" https://raw.githubusercontent.com/ArinaPig/Fasttype/main/version_4/installer/FastType.lnk')
	progressbar.set(1)
	tkinter.messagebox.showinfo(title='Успешно!', message='FastType установлен на ваш компьютер! Окно установщика можно закрыть')
	threading.Thread(target=os.system(r'"C:\Program Files\FastType\FastType.exe"'), name='end').start()
	exit()


th2 = threading.Thread(target=window1, name="Main")
th2.start()
installing()
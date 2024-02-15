import os

if os.name == "nt":
    import ctypes

    def msgbox(title: str, prompt: str):
        ctypes.windll.user32.MessageBoxW(0, prompt, title, 0x1000)

else:
    from tkinter import messagebox

    def msgbox(title: str, prompt: str):
        messagebox.showinfo(title, prompt)

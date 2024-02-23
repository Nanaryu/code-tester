import os

match os.name:
    case "nt":
        import ctypes

        def msgbox(title: str, prompt: str):
            ctypes.windll.user32.MessageBoxW(0, prompt, title, 0x1000)

    case "posix":
        from tkinter import messagebox

        def msgbox(title: str, prompt: str):
            messagebox.showinfo(title, prompt)

import pytesseract
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


def trans():
    contents.delete('1.0', tk.END)
    transTxt = pytesseract.image_to_string(Image.open(filePath.get()), lang='chi_sim')
    transTxt = transTxt.strip('\n\r')
    contents.insert(tk.INSERT, transTxt.replace(' ', '').replace('\n\n', '\n').replace('\r', ''))


def openfile():
    filename.delete('1.0', tk.END)
    filePath.set(tk.filedialog.askopenfilename())
    filename.insert(1.0, filePath.get())
    org_img = Image.open(filePath.get())
    width, height = org_img.size
    if width > 600:
        height = int(height * 600 / width)
        width = 600
    if height > 800:
        width = int(width * 800 / height)
        height = 800
    img = ImageTk.PhotoImage(org_img.resize((width, height)))
    showPic.config(image=img)
    showPic.image = img


top = tk.Tk()
top.title("OCR图片转文字工具  引擎：Tesseract-OCR  By: 轩哥啊哈OvO")
top.geometry("1200x800")

filePath = tk.StringVar()

frame1 = tk.Frame(top, relief=tk.RAISED, borderwidth=2)
frame1.pack(side=tk.TOP, fill=tk.BOTH, ipady=5, expand=0)
tk.Label(frame1, height=1, text="图片路径：").pack(side=tk.LEFT)
filename = tk.Text(frame1, height=2)
filename.pack(side=tk.LEFT, padx=1, pady=0, expand=True, fill=tk.X)
tk.Button(frame1, text="打开文件", command=openfile).pack(side=tk.LEFT, padx=5, pady=0)
tk.Button(frame1, text="中文识别", command=trans).pack(side=tk.LEFT, padx=5, pady=0)

frame2 = tk.Frame(top, relief=tk.RAISED, borderwidth=2)
frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
tk.Label(frame2, text='图片显示：', borderwidth=5).pack(side=tk.TOP, padx=20, pady=5)
showPic = tk.Label(frame2, text='图片显示区')
showPic.pack(side=tk.BOTTOM, expand=1, fill=tk.BOTH)

frame3 = tk.Frame(top)
frame3.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
tk.Label(frame3, text='识别结果：', borderwidth=5).pack(side=tk.TOP, padx=20, pady=10)
contents = tk.Text(frame3, font=('Arial', 15))
contents.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
tk.Label(frame3, text='Copyright (c) 2023 轩哥啊哈OvO ALL Rights Reserved.', borderwidth=5).pack(side=tk.BOTTOM, padx=20, pady=10)

top.mainloop()

#coding=utf-8
# 自制操作系统代码

from tkinter import *
from tkinter import messagebox
import os.path as path

def assignToOsName1():
    global code, os_name

    os_name = entry.get()

    if os_name == None :
        print(os_name)

        osPrint(os_name)
        osPrint(">>")

        label.pack_forget()
        entry.pack_forget()
        button.pack_forget()

        window2()
    else:
        messagebox.showerror("错误！", "名称不能为空！")
 
def assignToOsName2():
    global code, main, os_name

    code = f"{code}\n.wait_input:\n\tmov ah, 0x00\n\tint 0x16\n\tcmp al, '1'\n\tje .check_input\n\tcmp al, 'c'\n\tje .check_input_\n"
    cmd = entry1.get()
    command = entry2.get()
    
    if cmd == None or command == None :

        print(cmd)
        print(command)

        label.pack_forget()
        entry.pack_forget()
        button.pack_forget()

        window2()

        osFirst(cmd)

        code = f"{code}\n\tcmp al, 0x0D\n\tje .bad_input\n\tmov ah, 0x0E\n\tint 0x10\n\tjmp .wait_input\n.check_input:\n\tmov ah, 0x0E\n\tint 0x10\n\tmov ah, 0x00\n\tint 0x16\n\tmov ah, 0x0E\n\tint 0x10\n\tcmp al, '2'\n\tjne .wait_input\n\tmov ah, 0x00\n\tint 0x16\n\tmov ah, 0x0E\n\tint 0x10\n\tcmp al, '3'\n\tjne .wait_input\n\tmov ah, 0x00\n\tint 0x16\n\tcmp al, 0x0D\n\tjne .wait_input\n\tmov ah, 0x0E\n\tmov al, 0x0D\n\tint 0x10\n\tmov al, 0x0A\n\tint 0x10\n\tmov al, '4'\n\tint 0x10\n\tmov al, '5'\n\tint 0x10\n\tmov al, '6'\n\tint 0x10\n\tmov al, '!'\n\tint 0x10\n\tmov al, 0x0D\n\tint 0x10\n\tmov al, 0x0A\n\tint 0x10\n\tmov al, '>'\n\tint 0x10\n\tmov ah, 0x0E\n\tmov al, '>'\n\tint 0x10\n\tjmp .wait_input\n.check_input_:\n\tmov ah, 0x0E\n\tint 0x10\n\tmov ah, 0x00\n\tint 0x16\n\tmov ah, 0x0E\n\tint 0x10\n\tcmp al, 'l'\n\tjne .wait_input\n\tmov ah, 0x00\n\tint 0x16\n\tmov ah, 0x0E\n\tint 0x10\n\tcmp al, 's'\n\tjne .wait_input\n\tmov ah, 0x00\n\tint 0x16\n\tcmp al, 0x0D\n\tjne .wait_input\n\tmov ah, 0x0E\n\tmov al, 0x0D\n\tint 0x10\n\tmov al, 0x0A\n\tint 0x10\n\tmov ax, 0x0600\n\tmov bx, 0x0700\n\tmov cx, 0\n\tmov dx, 0x184f\n\tint 0x10\n\tmov ah, 02h\n\txor bh, bh\n\tmov dh, 0\n\tmov dl, 0\n\tint 10h\n\tmov ah, 0x0E\n\tmov al, 0x0D\n\tint 0x10\n\tmov al, 0x0A\n\tint 0x10\n\tmov al, '>'\n\tint 0x10\n\tmov ah, 0x0E\n\tmov al, '>'\n\tint 0x10\n\tjmp .wait_input\n\t.bad_input:\n\tmov ah, 0x0E\n\tmov al, 0x0D\n\tint 0x10\n\tmov al, 0x0A\n\tint 0x10\n\tmov al, 'b'\n\tint 0x10\n\tmov al, 'a'\n\tint 0x10\n\tmov al, 'd'\n\tint 0x10\n\tmov al, '!'\n\tint 0x10\n\tmov ah, 0x0E\n\tmov al, 0x0D\n\tint 0x10\n\tmov al, 0x0A\n\tint 0x10\n\tmov al, '>'\n\tint 0x10\n\tmov al, '>'\n\tint 0x10\n\tjmp .wait_input\n\t.done:\n\tret\n"
        code = f"{code}\n.check_input_{cmd}:\n\tmov ah, 0x0E\n\tint 0x10"
    
        osOther(cmd)
        osPrint(command)

        osEndPrint()
        osEnd()

        os_id = getOSID()
        os_file = open(f'os_{int(os_id)}.asm', 'w')
        os_file.write(code)
        os_file.close()
    else:
        messagebox.showerror("错误！", "命令不能为空！")

def getOSID():
    id = 0
    if path.exists(f'os_{id}.asm'):
        while path.exists(f'os_{id}.asm'):
            id += 1
    return id

def osPrint(string):
    global code
    for s in string:
        code = f"{code}\n\tmov al, '{s}'\n\tint 0x10\n"
 
def osFirst(string):
    global code
    i = 0
    for s in string:
        i += 1
        code = f"{code}\n\tcmp al, '{s}'\n\tje .check_input_{string}\n"
        if i >= 1:
            break
 
def osOther(string):
    global code
    string = string[1:]
    i = 0
    for s in string:
        i += 1
        code = f"{code}\n\t\n\tmov ah, 0x00\n\tint 0x16\n\tmov ah, 0x0E\n\tint 0x10\n\tcmp al, '{s}'\n\tjne .wait_input\n"
    code = f"{code}\n\t\n\tmov ah, 0x00\n\tint 0x16\n\tcmp al, 0x0D\n\tjne .wait_input\n\tmov ah, 0x0E\n\tmov al, 0x0D\n\tint 0x10\n\tmov al, 0x0A\n\tint 0x10\n"
 
def osEndPrint():
    global code
    code = f"{code}\n\tmov ah, 0x0E\n\tmov al, 0x0D\n\tint 0x10\n\tmov al, 0x0A\n\tint 0x10\n\tmov al, '>'\n\tint 0x10\n\tmov al, '>'\n\tint 0x10\n\tjmp .wait_input\n"
 
def osEnd():
    global code
    code = f"{code}\ntimes 510-($-$$) db 0\ndw 0xAA55\n"
 
root = Tk()
root.title("自制操作系统")
root.geometry("400x300")

def window1():
    global label, entry, button

    label = Label(root, text="操作系统名称")  # 用于显示输入的文字
    label.pack()
 
    entry_var = StringVar()
    entry = Entry(root, textvariable=entry_var)
    entry.pack()
 
    button = Button(root, text="确认", command=assignToOsName1)
    button.pack()

code = '\n[org 0x7c00]\n\nstart:\n\t\n\tmov bp, 0x8000\n\tmov sp, bp\n\n\t\n\tmov ax, 0x0600\n\tmov bx, 0x0700\n\tmov cx, 0\n\tmov dx, 0x184f\n\tint 0x10\n\n\n\tmov ah, 0x0E\n'

def window2():
    global label, entry1, entry2, button

    label = Label(root, text="添加命令")  # 用于显示输入的文字
    label.pack()
 
    entry_var1 = StringVar()
    entry1 = Entry(root, textvariable=entry_var1)
    entry1.pack()
    
    entry_var2 = StringVar()
    entry2 = Entry(root, textvariable=entry_var2)
    entry2.pack()
 
    button = Button(root, text="完成", command=assignToOsName2)
    button.pack()
    
    button = Button(root, text="退出", command=exit)
    button.pack()
 
window1()
root.mainloop()
 
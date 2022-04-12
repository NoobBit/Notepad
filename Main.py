import os
import getpass
import win32print
import win32api
from tkinter import *
from tkinter import font
from tkinter import colorchooser

# MainWin
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
# Main
root = Tk()
root.title('Notepad')
root.iconbitmap(default='icon.ico')
root.geometry('500x450')

# Editor
font_type = StringVar(root)
font_type.set('Arial')
font_size = StringVar(root)
font_size.set('25')
wrap = 'none'

# File
file_path = ''
file_name = ''

# User
user = getpass.getuser()
maindir = 'C:/Users/' + user

# Bar
fileImg = PhotoImage(file='assets/file.png')
newwinImg = PhotoImage(file='assets/newwin.png')
openImg = PhotoImage(file='assets/open.png')
saveImg = PhotoImage(file='assets/save.png')
saveasImg = PhotoImage(file='assets/saveas.png')
settingsImg = PhotoImage(file='assets/settings.png')
printImg = PhotoImage(file='assets/print.png')
exitImg = PhotoImage(file='assets/exit.png')

undoImg = PhotoImage(file='assets/undo.png')
redoImg = PhotoImage(file='assets/redo.png')
cutImg = PhotoImage(file='assets/cut.png')
copyImg = PhotoImage(file='assets/copy.png')
pasteImg = PhotoImage(file='assets/paste.png')
boldImg = PhotoImage(file='assets/bold.png')
italicImg = PhotoImage(file='assets/italic.png')
selectallImg = PhotoImage(file='assets/selectall.png')
clearallImg = PhotoImage(file='assets/clearall.png')
selecttcImg = PhotoImage(file='assets/selecttc.png')
selecttaImg = PhotoImage(file='assets/selectta.png')
selectbaImg = PhotoImage(file='assets/selectba.png')

# MainSaving
def save_file_path(path):
    global file_path
    global file_name
    file_path = path
    file_name = os.path.basename(path)

# Save As
def save():
    if file_path == '':
        path = asksaveasfilename(initialdir=maindir,
                                initialfile='*.txt',
                                 filetypes=[('Text Documents', '*.txt'), ('All Files', '*.*')])
        if os.path.basename(path) == '':
            status('File was not saved')
        else:
            root.title('Notepad - ' + os.path.basename(path))
            status('File:   ' + os.path.basename(path))
            while 1==1:
                code = editor.get('1.0', END)
                path = file_path
                with open(path, 'w') as file:
                    file.write(code)
                    save_file_path(path)
                if code == os.path.basename(path):
                    root.title('Notepad - ' + os.path.basename(path))
                else:
                    root.title('*Notepad - ' + os.path.basename(path))
        return

    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        save_file_path(path)

# Save As
def save_as(e):
    if file_path == '':
        path = asksaveasfilename(initialdir=maindir,
                                initialfile='*.txt',
                                 filetypes=[('Text Documents', '*.txt'), ('All Files', '*.*')])
        if os.path.basename(path) == '':
            status('File was not saved')
        else:
            root.title('Notepad - ' + os.path.basename(path))
            status('File:   ' + os.path.basename(path))
        return

    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        save_file_path(path)

# New File
def new_file(e):
    if file_path == '':
        editor.delete('1.0', END)
        root.title('*Notepad - Untitled')
        status('Untitled') 
    else:
        new_file_message = messagebox.askyesno('Alert', 'Would you like to save before you open')
        if new_file_message == True:
            save_as(e)
            status('New File was created')
        else:
            editor.delete('1.0', END)
            root.title('*Notepad - Untitled')
            status('Untitled') 


def new_window(e):
    messagebox.showinfo('Alert', 'New Window Is Unavailable')
    status('New Window Is Unavailable')
    print('New Window Is Unavailable')

def open_file(e):
    def ask_open():
            path = askopenfilename(initialdir=maindir, initialfile='*.txt', filetypes=[('Text Documents', '*.txt'), ('All Files', '*.*')])
            if os.path.basename(path) == '':
                status('File was not opened')
            else:
                try:
                    root.title('Notepad - ' + os.path.basename(path))
                    with open(path, 'r') as file:
                        code = file.read()
                        editor.delete('1.0', END)
                        editor.insert('1.0', code)
                        save_file_path(path)
                        status('File:   ' + file_name)
                except EXCEPTION:
                    status('File Could Not Be Read')
                    print('File Could Not be Read')
            return
    if file_path == '':
        save_message = messagebox.askyesnocancel('Alert', 'Would you like to Save Before you open?', icon='warning')
        if save_message == True:
            save_as(e)
        else:
            if save_message == False:
                ask_open()
            else:
                status('Opening Canceled')
        return
    else:
        
        ask_open()


def bold_text(e):
    bold_font = font.Font(editor, editor.cget('font'))
    bold_font.configure(weight='bold')

    editor.tag_configure('bold', font=bold_font)

    current_tags = editor.tag_names('sel.first')

    if 'bold' in current_tags:
        editor.tag_remove('bold', 'sel.first', 'sel.last')
    else:
        editor.tag_add('bold', 'sel.first', 'sel.last')


def italic_text(e):
    italic_font = font.Font(editor, editor.cget('font'))
    italic_font.configure(slant='italic')

    editor.tag_configure('italic', font=italic_font)

    current_tags = editor.tag_names('sel.first')

    if 'italic' in current_tags:
        editor.tag_remove('italic', 'sel.first', 'sel.last')
    else:
        editor.tag_add('italic', 'sel.first', 'sel.last')


def select_all(e):
    editor.tag_add('sel', '1.0', 'end')
    status('Selected All')


def clear_all(e):
    clear_message = messagebox.askyesno('Alert', 'Are you sure you would like to clear all?', icon='warning')
    if clear_message == True:
        editor.delete('1.0', END)
        status('Cleared All')
    else:
        status('Stoped Clearing')


def text_color():
    my_color = colorchooser.askcolor()[1]
    print('New Text Color: ' + my_color)

    if my_color:
        color_font = font.Font(editor, editor.cget('font'))

        editor.tag_configure('colored', font=color_font, foreground=my_color)

        current_tags = editor.tag_names('sel.first')

        if 'colored' in current_tags:
            editor.tag_remove('colored', 'sel.first', 'sel.last')
            status('Color Removed')
        else:
            editor.tag_add('colored', 'sel.first', 'sel.last')
            status('New Text Color:   ' + my_color)


def bg_color():
    my_color = colorchooser.askcolor()[1]
    print('New Background Color: ' + my_color)
    if my_color:
        status('New Background Color:   ' + my_color)
        editor.config(bg=my_color)


def fg_color():
    my_color = colorchooser.askcolor()[1]
    print('New Text Color: ' + my_color)
    if my_color:
        status('New Text Color:   ' + my_color + ' ')
        editor.config(fg=my_color)


def wr_char():
    wrap = 'char'
    editor.config(root, font=(font_type.get(), font_size.get()), undo=True, wrap=wrap)


def wr_word():
    wrap = 'word'
    editor.config(root, font=(font_type.get(), font_size.get()), undo=True, wrap=wrap)


def wr_off():
    wrap = 'none'
    editor.config(root, font=(font_type.get(), font_size.get()), undo=True, wrap=wrap)


def settings(e):
    settings_app = Tk()
    settings_app.title('Notepad - Settings')
    settings_app.iconbitmap(default='icon.ico')
    settings_app.geometry('215x200')

    # Selected Text Color
    color_s_label = Label(settings_app, text='Selected Text Color:           ')
    color_s_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)
    color_s_button = Button(settings_app, text='Change', command=text_color)
    color_s_button.grid(row=0, column=1, sticky=W)

    # All Text Color
    color_a_label = Label(settings_app, text='All Text Color:           ')
    color_a_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)
    color_a_button = Button(settings_app, text='Change', command=fg_color)
    color_a_button.grid(row=1, column=1, sticky=W)

    # BackGround Color
    color_bg_label = Label(settings_app, text='Background Color:           ')
    color_bg_label.grid(row=2, column=0, sticky=W, padx=5)
    color_bg_button = Button(settings_app, text='Change', command=bg_color)
    color_bg_button.grid(row=2, column=1, sticky=W)

    # Text Wrap
    # text_w_label = Label(settings_app, text='Text Wrap:           ')
    # text_w_label.grid(row=3, column=0, sticky=W, padx=5)
    # text_w_1_button = Button(settings_app, text='Char', command=wr_char)
    # text_w_1_button.grid(row=3, column=1, sticky=W)
    # text_w_2_button = Button(settings_app, text='Word', command=wr_word)
    # text_w_2_button.grid(row=3, column=2, sticky=W)
    # text_w_1_button = Button(settings_app, text='Off', command=wr_off)
    # text_w_1_button.grid(row=3, column=3, sticky=W)

    settings_app.mainloop()


def exit_app(e):
    if file_path == '':
        exit(0)
        return
    else:
        exit_message = messagebox.askyesno('Alert', 'Would you like to save before you open', icon='warning')
        if exit_message == True:
            save_as(e)
        else:
            exit(0)


def print_file(e):
    printer_name = win32print.GetDefaultPrinter()
    print(printer_name)
    file_to_print = askopenfilename(filetypes=[('Text Documents', '*.txt'), ('All Files', '*.*')])
    if file_to_print:
        status('Printing   ' + file_to_print)
        win32api.ShellExecute(0, 'print', file_to_print, None, '.', 0)


def copy(e):
    editor.event_generate('<<Copy>>')
    status('Copied   ')


def cut(e):
    editor.event_generate('<<Cut>>')
    status('Cut')


def paste(e):
    editor.event_generate('<<Paste>>')
    status('Pasted')


def help():
    messagebox.showinfo('Help', '(C) Notepad 2021 Created By Parteek Deol \nV. 2021.4.13.0 \nHelp: '
                                'https://parteekdeol.netlify.app/py/notepad/help')


def about():
    messagebox.showinfo('About', '(C) Notepad 2021 \nCreated By Parteek Deol \nV. 2021.4.13.0 \nPython Version: 3.9.3')


def w_new():
    w_new = Tk()
    w_new.title('Notepad - Whats New')
    w_new.iconbitmap(default='icon.ico')
    w_new.geometry('330x310')
    w_new.resizable(False, False)

    w_l = Label(w_new, text='Whats New', font=('Arial', 25))
    w_l.grid(row=0, column=0, padx=20, pady=10)

    w_t_1 = Label(w_new, text='Save Feature Updated', font=('Arial', 15))
    w_t_1.grid(row=1, column=0, padx=0)

    w_l_1 = Label(w_new, text='When you Now click exit in the menu without \nsaving it will create a new message', font=('Arial', 10))
    w_l_1.grid(row=2, column=0)

    w_t_2 = Label(w_new, text='Open and Save fixed', font=('Arial', 15))
    w_t_2.grid(row=3, column=0, padx=70)
    w_l_2 = Label(w_new, text='When you click the open file on\n the menu and clicked cancel the titlebox\n would say Notepad - . Now However it is '
                              'fixed',
                  font=('Arial', 10))
    w_l_2.grid(row=4, column=0)

    w_t_2 = Label(w_new, text='Deafault Dir', font=('Arial', 15))
    w_t_2.grid(row=5, column=0, padx=70)
    w_l_2 = Label(w_new, text='Now It shows your main dir.', font=('Arial', 10))
    w_l_2.grid(row=6, column=0)

    w_v = Label(w_new, text='V. 2021.4.13.0', font=('Arial', 10))
    w_v.grid(row=7, column=0, pady=10)


def status(input):
    status_bar.config(text=input + '   ')


status_bar = Label(root, text='Ready   ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=1)

scroll_bar = Scrollbar()
scroll_bar.pack(side=RIGHT, fill=Y)

hor_bar = Scrollbar(orient='horizontal')
hor_bar.pack(side=BOTTOM, fill=X)

editor = Text(root, font=(font_type.get(), font_size.get()), undo=True, wrap=wrap)
editor.pack()

scroll_bar.config(command=editor.yview)
hor_bar.config(command=editor.xview)

# MenuBar
menu_bar = Menu(root)

file_bar = Menu(menu_bar, tearoff=0)
file_bar.add_command(label='New', command=lambda: new_file(False), image=fileImg, compound='left', accelerator='Ctrl+N')
file_bar.add_command(label='New Window', command=lambda: new_window(False), image=newwinImg, compound='left', accelerator='Ctrl+Shift+N')
file_bar.add_command(label='Open', command=lambda: open_file(False), image=openImg, compound='left', accelerator='Ctrl+O')
file_bar.add_command(label='Save', command=lambda: save_as(False), image=saveImg, compound='left', accelerator='Ctrl+S')
file_bar.add_command(label='Save As', command=lambda: save_as(False), image=saveasImg, compound='left', accelerator='Ctrl+Shift+S')
file_bar.add_command(label='Settings', command=lambda: settings(False), image=settingsImg, compound='left', accelerator='Ctrl+E')
file_bar.add_separator()
file_bar.add_command(label='Print', command=lambda: print_file(False), image=printImg, compound='left', accelerator='Ctrl+P')
file_bar.add_separator()
file_bar.add_command(label='Exit', command=lambda: exit_app(False), image=exitImg, compound='left')
menu_bar.add_cascade(label='File', menu=file_bar)

edit_bar = Menu(menu_bar, tearoff=0)
edit_bar.add_command(label='Undo', command=editor.edit_undo, image=undoImg, compound='left', accelerator='Ctrl+Z')
edit_bar.add_command(label='Redo', command=editor.edit_redo, image=redoImg, compound='left', accelerator='Ctrl+Y')
edit_bar.add_separator()
edit_bar.add_command(label='Cut', command=lambda: cut(False), image=cutImg, compound='left', accelerator='Ctrl+X')
edit_bar.add_command(label='Copy', command=lambda: copy(False), image=copyImg, compound='left', accelerator='Ctrl+C')
edit_bar.add_command(label='Paste', command=lambda: paste(False), image=pasteImg, compound='left', accelerator='Ctrl+V')
edit_bar.add_separator()
edit_bar.add_command(label='Bold', command=lambda: bold_text(False), image=boldImg, compound='left', accelerator='Ctrl+B')
edit_bar.add_command(label='Italic', command=lambda: italic_text(False), image=italicImg, compound='left', accelerator='Ctrl+T')
edit_bar.add_separator()
edit_bar.add_command(label='Select All', command=lambda: select_all(False), image=selectallImg, compound='left', accelerator='Ctrl+A')
edit_bar.add_command(label='Clear All', command=lambda: clear_all(False), image=clearallImg, compound='left', accelerator='Ctrl+R')
edit_bar.add_separator()
edit_bar.add_command(label='Color of Selected Text', image=selecttcImg, compound='left', command=text_color)
edit_bar.add_command(label='Color of All Text', image=selecttaImg, compound='left', command=fg_color)
edit_bar.add_command(label='Color of Background', image=selectbaImg, compound='left', command=bg_color)
menu_bar.add_cascade(label='Edit', menu=edit_bar)

help_bar = Menu(menu_bar, tearoff=0)
help_bar.add_command(label='Whats New', command=w_new)
help_bar.add_command(label='About', command=about)
help_bar.add_command(label='Help', command=help)
menu_bar.add_cascade(label='Help', menu=help_bar)

root.config(menu=menu_bar)

root.bind('<Control-n>', new_file)
root.bind('<Control-o>', open_file)
root.bind('<Control-s>', save_as)
root.bind('<Control-e>', settings)
root.bind('<Control-p>', print_file)

root.bind('<Control-x>', cut)
root.bind('<Control-c>', copy)

root.bind('<Control-b>', bold_text)
root.bind('<Control-t>', italic_text)

root.bind('<Control-a>', select_all)
root.bind('<Control-r>', clear_all)

if __name__ == '__main__':
    root.mainloop()
else:
    root.mainloop()
    status('Notepad was opened by an external program')
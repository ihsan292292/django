from tkinter import *
from tkinter.filedialog import asksaveasfilename

compiler = Tk()
compiler.title("iam inevitable")

def run():
    code = editor.get('1.0',END)
    exec(code)

def save_as():
    path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    with open(path,'w') as file:
        code = editor.get('1.0',END)
        file.write(code)

def open_file():
    print("Here open the file")


menu_bar =Menu(compiler)

file_menu =Menu(menu_bar,tearoff=0)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save As',command=save_as)
file_menu.add_command(label='Exit',command=exit)
menu_bar.add_cascade(label='File',menu=file_menu)

run_bar =Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run',command=run)
menu_bar.add_cascade(label='Run',menu=run_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()
compiler.mainloop()

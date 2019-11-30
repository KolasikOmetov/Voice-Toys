import sys
import executeProgram as ep




#Глобальные переменные
text = '' # хранение текста



def main(s, fp):
    # try:
        command = TC.Translate_Commands(s)
        print(command)
        if command == '':
            pass
        elif command[len(command)-1] == ')':
            exec('global text\ntext = cp.' + command)
            if text == '':
                delete_file_text()
                show_file_text()
                return 0
            talk("В файл записано")
            print(text)
            show_in_dialog(text, 'bublle')
            delete_file_text()
            show_file_text()
        else:
            show_in_dialog('Нет такой команды', 'bublle')
    # except SystemExit:
    #     sys.exit(0)
    # except:
    #     show_in_dialog('Попробуйте снова','bublle')
    #button_movie = AG.AnimatedGIF(dialog_window, "button.gif")
    #button_movie.place(x=dialog_window.winfo_screenwidth() / 4 - 50, y=dialog_window.winfo_screenheight() - 200)


def delete_file_text():
    for child in file_window.winfo_children():
        child.destroy()


def show_in_dialog(text, who):
    if who == 'user':
        dialog_box = tk.Label(dialog_window, bg='#D60062', text=text, compound=tk.LEFT)
    else:
        dialog_box = tk.Label(dialog_window, bg='#EF4F9F', text=text, compound=tk.LEFT)
        talk(text)
    dialog_box.pack(side=tk.TOP)


TC.show_in_dialog = show_in_dialog
cp.show_in_dialog = show_in_dialog
cp.talk = talk

cp.fp = cp._open_file()

fileshow = open(cp.fp.fileNameFull, "r")
cp.data = fileshow.readlines()
fileshow.close()

# def open_gui():
root = tk.Tk()
# шапка навигации bg(цвет) bd(граница)
toolbar = tk.Frame(bg='#F81894', bd=2)
# растянет и закрепит в верхней части окна
toolbar.pack(side=tk.TOP, fill=tk.X)
dialog_window = tk.Frame(bg='#FFFFFF', bd=2)
dialog_window.pack(side=tk.LEFT, fill = tk.Y)

# self.add_img = tk.PhotoImage(file = "BUBLEGUM_icon.jpg")
button_file = tk.Button(toolbar, text="Save", command=lambda: cp.save_file(), bg='#F81894', bd=0,
                        compound=tk.TOP)
button_file.pack(side=tk.LEFT)
button_edit = tk.Button(toolbar, text="Exit", command=lambda: exit(0), bg='#F81894', bd=0,
                        compound=tk.TOP)
button_edit.pack(side=tk.RIGHT)
button_start_program = tk.Button(dialog_window, text="BUBLLE",
                                 command=lambda: main(listen(), cp.fp),#STT.listen()
                                 bg='#F81894', bd=0,
                                 compound=tk.TOP)
# button_start_program.place(y=tk.Frame.winfo_screenheight(self)-100)
# Анимированная штука
button_movie = AG.AnimatedGIF(dialog_window, "button.gif")
button_movie.place(x=50, y=20)

button_start_program.pack(padx=300, pady = 20)

file_window = tk.Frame(bg='#EA69A3', bd=2)
file_window.pack(side=tk.LEFT, fill=tk.Y)
show_file_text()
size_screen = str(root.winfo_screenwidth()) + "x" + str(root.winfo_screenheight()) + "+0+0"
root.title("BUBLLEGUM")
root.iconbitmap('BUBLEGUM_icon.ico')
root.geometry(size_screen)  # размер окна  и координаты
# root.resizable(False, False)# нерастяжимое
root.mainloop()  # запуск


# main('создай функцию hello print("hello")')
# main('вызови её')
# main('создай ввод')
# main('запусти программу')

#'создай функцию hello print("hello")'
# f = open("outPut.py", "r")
# container = f.read()
# launch_programm()
# f.close()


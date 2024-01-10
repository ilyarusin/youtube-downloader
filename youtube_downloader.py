from tkinter import *
from tkinter import ttk  
import pytube
from pytube import YouTube
from pytube import Playlist
from tkinter import messagebox

# отрисовка главного окна
root = Tk()
root.geometry("1000x250")
root.resizable(False,False)
icon = PhotoImage(file = "C:\Python projects\Youtube Downloader\Favicon\Dtafalonso-Android-Lollipop-Youtube.32.png")
root.iconphoto(True, icon)
root.configure(bg='white')

# заголовок окна
root.title("YouTube загрузчик")

# цвет фона
root.config(bg='#D3D3D3')

# механика кнопки Скачать
def download():
    # пробуем скачать видео по ссылке
    try:
        # формируем адрес
        ytlink = link1.get()
        # переводим его в нужный формат
        youtubelink = YouTube(ytlink)
        youtubelink.streams.get_by_resolution(selection).download()
        # выводим результат
        Result = "Загрузка завершена"
        messagebox.showinfo("Готово",Result)
    # если скачать не получилось
    except:
        # выводим сообщение об ошибке
        Result = "Ссылка не работает"
        messagebox.showerror("Ошибка",Result)


'''
# механика кнопки Скачать плейлист
def download_playlist():
    url=YouTube(str(En1.get()))
    playlist=Playlist(url)
    for i in playlist.video_urls:
        print(i)
'''

# при нажатии на кнопку очистки очищаем строку с адресом видео
def reset():
    link1.set("")

# при нажатии на кнопку выхода — закрываем окно с интерфейсом
def Exit():
    root.destroy()


# заголовок формы
lb = Label(root,text="Загрузка видео с YouTube",font=('Arial,15,bold'),bg='#D3D3D3')
lb.pack(pady=15)

# пояснительный текст для поля с адресом
lb1 = Label(root,text="Ссылка на видео :",font=('Arial,15,bold'),bg='#D3D3D3')
lb1.place(x=15,y=80)

# пояснительный текст для поля с выбором разрешения видео
lb2 = Label(root,text="Выберите в каком разрешении вы хотите загрузить видео :",font=('Arial,15,bold'),bg='#D3D3D3')
lb2.place(x=15,y=120)

# поле ввода адреса видео
link1=StringVar()
En1=Entry(root,textvariable=link1,font=('Arial,15,bold'),width=50)
En1.place(x=200,y=80)

# выпадающий список для типов разрешения видео
video_resolutions = ['720p', '480p', '360p', '240p']
combobox = ttk.Combobox(values=video_resolutions,font=('Arial,15,bold'),state="readonly")
combobox.place(x=580,y=120)

def selected(event):
    global selection
    selection = combobox.get()

combobox.bind("<<ComboboxSelected>>", selected)

# кнопка скачивания
btn1 = Button(root,text="Скачать",font=('Arial,10,bold'),bd=4,command=download)
btn1.place(x=480,y=190)

'''
# запуск окна скачивания плейлистов
def click():
    window=Tk()
    window.title("")
    window.geometry("850x150")
    window.config(bg='#D3D3D3')
    lbtxt=Label(window,text="Ссылка на плейлист",font=('Arial,15,bold'),bg='#D3D3D3')
    lbtxt.place(x=15,y=10)
    link2=StringVar()
    En2=Entry(window,textvariable=link2,font=('Arial,15,bold'),width=70)
    En2.place(x=15,y=50)
        
    # кнопка скачивания
    btn5=Button(window,text="Скачать",font=('Arial,10,bold'),bd=4,command=download_playlist)
    btn5.place(x=250,y=90)
    btn6=Button(window,text="Очистить",font=('Arial,10,bold'),bd=4,command=reset)
    btn6.place(x=100,y=90)

# кнопка скачивания плейлиста
btn4=Button(root,text="Скачать плейлист",font=('Arial,10,bold'),bd=4,command=download_playlist)
btn4.place(x=600,y=190)

'''

# кнопки очистки и выхода
btn2 = Button(root,text="Очистить",font=('Arial,10,bold'),bd=4,command=reset)
btn2.place(x=200,y=190)
btn3 = Button(root,text="Выход",font=('Arial,10,bold'),bd=4,command=Exit)
btn3.place(x=350,y=190)

# запускаем окно
root.mainloop()

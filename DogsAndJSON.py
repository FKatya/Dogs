# Получаем изображение собачек с сайта https://dog.ceo,
# исользуя API и изучаем формат JSON

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import Image,ImageTk
import requests
from io import BytesIO


def show_image():
    image_url = get_dog_image()
    if image_url:
        try:
            # Получаем картинку в виде бинарного файла по url
            # и преобразовываем в изображение и сжимаем до размера
            # 640x480
            response = requests.get(image_url,stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img_size = (int(width_spinbox.get()),int(height_spinbox.get()))
            img.thumbnail(img_size)
            img=ImageTk.PhotoImage(img)
            new_window = Toplevel(window)
            new_window.title('Случайное изображение')
            lb = ttk.Label(new_window,image=img)
            lb.pack()
            lb.image = img
        except Exception as e:
            mb.showerror('Ошибка',f' Не удалось получить изображение: {e}')
    progress.stop()


def get_dog_image():
    try:
        # response вернет в формате json
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        # print(response)
        data = response.json()
        # print(type(data))
        # print(data)
        return data['message']
    except Exception as e:
        mb.showerror('Ошибка',f'Ошибка при обращении к API: {e}')
        return None


def prog():
    progress['value'] = 0
    progress.start(30)
    window.after(3000,show_image)


window = Tk()
window.title('Картинки с собачками')
window.geometry('360x420')

label = ttk.Label()
label.pack(pady=5)

button = ttk.Button(text='Загрузить изображение', command=prog)
button.pack(pady=5)

progress = ttk.Progressbar(mode='determinate',length=300)
progress.pack(pady=5)

width_label = ttk.Label(text='Ширина: ')
width_label.pack(side='left',padx=(10,0))
width_spinbox = ttk.Spinbox(from_=200,to=500,increment=50,width=5)
width_spinbox.pack(side='left',padx=(0,10))

height_label = ttk.Label(text='Высота: ')
height_label.pack(side='left',padx=(10,0))
height_spinbox = ttk.Spinbox(from_=200,to=500,increment=50,width=5)
height_spinbox.pack(side='left',padx=(0,10))




window.mainloop()

'''
Получаем изображение собачек с сайта https://dog.ceo,
исользуя API и изучаем формат JSON
'''
from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk
import requests
from io import BytesIO
#
#
#
# def show_image():
#     image_url = get_image()
#     if image_url:
#         try:
#             # Получаем картинку в виде бинарного файла по url
#             # и преобразовываем в изображение и сжимаем до размера
#             # 640x480
#             response = requests.get(image_url)
#             img_data = BytesIO(response.content)
#             img = Image.open(img_data)
#             img.thumbnail((640,480))
#             img=ImageTk.PhotoImage(img)
#             label.config(image=img)
#             label.image = img
#         except Exception as e:
#             tkinter.messagebox.showerror('Error',f' Не удалось получить изображение: {e}')
#
#
# def get_image():
#     try:
#         response = requests.get('https://dog.ceo/api/breeds/image/random')
#         # print(response)
#         data = response.json()
#         # print(type(data))
#         # print(data)
#         return data['message']
#     except Exception as e:
#         tkinter.messagebox.showerror('Error',f'Ошибка при обращении к API: {e}')
#
#
window = Tk()
window.title('Картинки с собачками')
window.geometry('360x420')

label = ttk.Label()
label.pack(pady=5)

button = ttk.Button(text='Загрузить изображение', command=show_image)
button.pack(pady=5)

window.mainloop()

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

# Функция авторизации
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Простой пример проверки логина и пароля
    if username == "user" and password == "1234":
        messagebox.showinfo("Успех", "Авторизация успешна!")
        open_profile()
    else:
        messagebox.showerror("Ошибка", "Неправильный логин или пароль")

# Открытие профиля пользователя после успешной авторизации
def open_profile():
    auth_frame.grid_forget()  # Скрыть форму авторизации
    profile_frame.grid(row=0, column=0)  # Показать профиль

# Создаем основное окно
root = Tk()
root.title("Авторизация")
root.geometry("400x300")
root.configure(bg="#f0f0f0")  # Задаем цвет фона

# Фрейм для формы авторизации
auth_frame = Frame(root, bg="#dfe6e9")
auth_frame.grid(row=0, column=0, padx=10, pady=10)

Label(auth_frame, text="Логин:", bg="#dfe6e9").grid(row=0, column=0, pady=10)
entry_username = Entry(auth_frame)
entry_username.grid(row=0, column=1, pady=10)

Label(auth_frame, text="Пароль:", bg="#dfe6e9").grid(row=1, column=0, pady=10)
entry_password = Entry(auth_frame, show="*")
entry_password.grid(row=1, column=1, pady=10)

Button(auth_frame, text="Войти", command=login, bg="#0984e3", fg="white").grid(row=2, column=0, columnspan=2, pady=20)

# Фрейм для профиля
profile_frame = Frame(root, bg="#81ecec")

Label(profile_frame, text="Добро пожаловать, user!", font=("Arial", 16), bg="#81ecec").grid(row=0, column=0, pady=10)

# Фотография пользователя
user_image = ImageTk.PhotoImage(Image.open("photo1.jpeg").resize((100, 100)))
Label(profile_frame, image=user_image, bg="#81ecec").grid(row=1, column=0, pady=10)

Button(profile_frame, text="Выход", command=root.quit, bg="#d63031", fg="white").grid(row=2, column=0, pady=20)

# Запуск программы
root.mainloop()

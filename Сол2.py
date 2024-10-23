from tkinter import *
from PIL import ImageTk, Image

# Список блюд и их описания
food_data = {
    "Пицца": {"image": "food1.jpg", "description": "Попкорн в тарелке."},
    "Суши": {"image": "food2.jpg", "description": "Курица с манго."},
    "Бургер": {"image": "food3.jpg", "description": "Каре ягненка."},
    "Салат": {"image": "food4.jpg", "description": "Тарелка ягод."},
    "Паста": {"image": "food5.jpg", "description": "Фруктовый салат."}
}

# Функция для отображения выбранного блюда
def display_food(selected_food):
    food = food_data[selected_food]
    img = ImageTk.PhotoImage(Image.open(food["image"]).resize((150, 150)))
    food_image_label.config(image=img)
    food_image_label.image = img
    food_description_label.config(text=food["description"])

# Создаем основное окно
root = Tk()
root.title("Меню еды")
root.geometry("500x400")
root.configure(bg="#fab1a0")  # Фон светло-розового цвета

# Заголовок приложения
Label(root, text="Выберите блюдо", font=("Arial", 18), bg="#fab1a0").grid(row=0, column=0, pady=20)

# Список для выбора блюда
food_listbox = Listbox(root, height=5, font=("Arial", 14))
for food in food_data.keys():
    food_listbox.insert(END, food)
food_listbox.grid(row=1, column=0, padx=20)

# Кнопка для подтверждения выбора
Button(root, text="Показать блюдо", command=lambda: display_food(food_listbox.get(ACTIVE)), bg="#0984e3", fg="white").grid(row=2, column=0, pady=20)

# Отображение выбранного блюда
food_image_label = Label(root, bg="#fab1a0")
food_image_label.grid(row=3, column=0, pady=10)

# Описание блюда
food_description_label = Label(root, text="", font=("Arial", 14), bg="#fab1a0")
food_description_label.grid(row=4, column=0, pady=10)

# Запуск программы
root.mainloop()

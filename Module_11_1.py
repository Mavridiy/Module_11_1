import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageOps


# Чтение данных из CSV файла
df = pd.read_csv('data.csv')
print("Данные из файла:")
print(df)

# Анализ данных о продажах
total_sales = df['Продажи'].sum()
average_sales = df['Продажи'].mean()
print(f"\nОбщая сумма продаж: {total_sales}")
print(f"Среднее значение продаж: {average_sales}")

# Визуализация данных о продажах
plt.figure(figsize=(10, 5))
plt.plot(df['Год'], df['Продажи'], marker='o', linestyle='-', color='b')
plt.title('Продажи по годам')
plt.xlabel('Год')
plt.ylabel('Продажи')
plt.grid(True)
plt.xticks(df['Год'])
plt.show()

# Анализ данных о городах
print("\nОбщая информация о городах:")
print(df[['Город', 'Население', 'Площадь']])

# Общая сумма населения
total_population = df['Население'].sum()
print(f"\nОбщее население всех городов: {total_population}")

# Статистические характеристики по населению и площади
print("\nСтатистические характеристики:")
print(df[['Население', 'Площадь']].describe())

print("___                          ___")
input("Нажмите ENTER для продолжения...")
print("___                          ___")

# Открываем изображение
image_path = 'Figure_1.png'
img = Image.open(image_path)

# Показываем оригинальное изображение
img.show()
# Пропорциональное изменение размера
img.thumbnail((300, 300))  # Максимальные размеры 300x300 пикселей
img.show()

# Сохраняем измененное изображение
img.save('resized_Figure_1.png')

# Получаем размеры оригинального изображения
width, height = img.size

# Обрезаем изображение (убираем 50 пикселей снизу)
cropped_image = img.crop((0, 0, width, height - 50))
cropped_image.show()

# Сохраняем обрезанное изображение
cropped_image.save('cropped_Figure_1.png')

# Применяем эффект серого цвета
gray_image = ImageOps.grayscale(img)
gray_image.show()

# Сохраняем измененное изображение
gray_image.save('gray_Figure_1.png')

# Проверяем, находится ли изображение в режиме RGBA и преобразуем его
if img.mode == 'RGBA':
    background = Image.new('RGB', img.size, (255, 255, 255))
    background.paste(img, (0, 0), img.split()[3])
    img = background
# Сохраняем изображение как JPEG
output_path = 'output_image.jpg'
img.save(output_path, format='JPEG')

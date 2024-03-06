import turtle

def draw_branch(t, length, level):
    # Базовий випадок: якщо рівень рекурсії досягнув 0, припиняємо рекурсію
    if level == 0:
        return

    # Малюємо гілку довжиною length
    t.forward(length)

    # Поворот вліво на 45 градусів
    t.left(45)

    # Рекурсивний виклик для малювання лівої гілки
    draw_branch(t, length * 0.6, level - 1)

    # Поворот вправо на 90 градусів
    t.right(90)

    # Рекурсивний виклик для малювання правої гілки
    draw_branch(t, length * 0.6, level - 1)

    # Поворот вліво на 45 градусів
    t.left(45)

    # Повертаємось на початкову точку
    t.backward(length)

def draw_pifagoras_tree(level):
    # Створення об'єкту-черепашки
    t = turtle.Turtle()

    # Налаштування вікна для візуалізації
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")

    # Швидкість руху черепашки (0 - найшвидше, 10 - найповільніше)
    t.speed(0)

    # Підняти перо (не малювати)
    t.penup()

    # Початкова позиція черепашки
    t.setpos(0, -300)

    # Поворот вверх на 90 градусів
    t.left(90)

    # Опустити перо (малювати)
    t.pendown()

    # Колір гілок
    t.color("green")

    # Малюємо гілки дерева
    draw_branch(t, 200, level)

    # Зупинка вікна і очікування подій
    screen.mainloop()

if __name__ == "__main__":
    # Запит рівня рекурсії від користувача
    level = int(input("Введіть рівень рекурсії для фрактала дерева Піфагора: "))

    # Виклик функції для малювання фрактала з заданим рівнем рекурсії
    draw_pifagoras_tree(level)
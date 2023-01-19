dt = 0.05  # Шаг по времени
ax, ay = 0, -9.81  # Ускорения вдоль осей
x, y = 0, 0  # Начальные координаты
vx, vy = 10, 10  # Начальные скорости


def update_coordinates():
    global x, y, vx, vy
    while y >= 0:
        # Обновляем скорости
        vx += ax * dt
        vy += ay * dt
        # Обновляем координаты
        x += vx * dt
        y += vy * dt
        # Точки траектории печатаем округленными до 3 знака
        print(round(x, 3), round(y, 3))

update_coordinates()
dt = 0.05  # Шаг по времени
ax, ay = 0, -9.81  # Ускорения вдоль осей
x, y = 0, 0  # Начальные координаты
vx, vy = 10, 10  # Начальные скорости
coords = []
velocities = []
coords_arr = []
velocities_arr = []

def update_coordinates():
    global x, y, vx, vy, coords_arr, velocities_arr

    while y >= 0:
        # Обновляем скорости
        vx += ax * dt
        vy += ay * dt
        # Обновляем координаты
        x += vx * dt
        y += vy * dt
        # Точки траектории печатаем округленными до 3 знака
        coords = [round(x, 3), round(y, 3)]
        velocities = [vx, vy]
        print(coords, '  ---  ', velocities) #решил красиво вывести
        coords_arr.append(coords)
        velocities_arr.append(coords)

update_coordinates()

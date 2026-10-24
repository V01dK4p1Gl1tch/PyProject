from body import Body
from constants import ASTRONOMICAL_UNIT
from physics import gravitational_force, acceleration
import matplotlib.pyplot as plt


# 1. Задаём список из ЛЮБОГО количества тел
sun = Body("Солнце", 1.989e30, 0, 0, 0, 0)

earth = Body(
    "Земля",
    mass=5.972e24,
    x=ASTRONOMICAL_UNIT,
    y=0,
    vx=0,
    vy=29_780  # Орбитальная скорость Земли вокруг Солнца (~29.78 км/с)
)

moon = Body(
    "Луна",
    mass=7.348e22,
    x=ASTRONOMICAL_UNIT + 384_400_000,
    y=0,
    vx=0,
    vy=29_780 + 1_022  # Скорость Земли + скорость Луны относительно Земли
)

satellite = Body(
    "Спутник",
    mass=1000,
    x=ASTRONOMICAL_UNIT + 42_164_000,  # Геостационарная орбита (42 164 км от центра Земли)
    y=0,
    vx=0,
    vy=29_780 + 3_075  # Скорость Земли + орбитальная скорость спутника (~3.07 км/с)
)

bodies = [sun, earth, moon, satellite]


# 2. Функция одного шага симуляции для N тел
def step_simulation(bodies: list[Body], dt: float) -> None:
    n = len(bodies)
    # Список для накопления суммарных сил [fx, fy] для каждого тела
    forces = [[0.0, 0.0] for _ in range(n)]

    # Считаем силы между всеми уникальными парами (i, j)
    for i in range(n):
        for j in range(i + 1, n):
            fx, fy = gravitational_force(bodies[i], bodies[j])

            # Прибавляем силу первому телу
            forces[i][0] += fx
            forces[i][1] += fy

            # По III закону Ньютона вычитаем ту же силу у второго тела
            forces[j][0] -= fx
            forces[j][1] -= fy

    # Когда ВСЕ силы посчитаны — обновляем скорости и координаты всех тел
    for i, body in enumerate(bodies):
        ax, ay = acceleration(body, forces[i][0], forces[i][1])
        body.update(ax, ay, dt)


# 3. Запускаем цикл симуляции (например, на 28 суток с шагом 10 секунд)
dt = 10
total_steps = 240_000

for step in range(total_steps):
    step_simulation(bodies, dt)

    # Записываем точки для графика раз в 100 шагов (каждые 1000 секунд)
    if step % 100 == 0:
        for body in bodies:
            # Если хотим смотреть орбиты вокруг Земли — передаём (earth.x, earth.y)
            # Если вокруг Солнца — просто body.record_position()
            body.record_position(earth.x, earth.y)


# 4. Универсальный вывод и отрисовка всех тел в цикле
for body in bodies:
    print(f"{body.name}: x={body.x:.2e}, y={body.y:.2e}, vx={body.vx:.1f}, vy={body.vy:.1f}")

    # Пропускаем Солнце на графике системы Земли, чтобы оно не растягивало масштаб на 150 млн км
    if body.name != "Солнце":
        xs, ys = zip(*body.history)
        plt.plot(xs, ys, label=body.name)

plt.axis("equal")
plt.legend()
plt.grid(True)
plt.show()
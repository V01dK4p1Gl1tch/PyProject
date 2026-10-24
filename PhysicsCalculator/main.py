from body import Body
from physics import gravitational_force, acceleration
import matplotlib.pyplot as plt


earth = Body(5.972e24, 0, 0, 0, 0)
moon = Body(7.348e22, 384400000, 0, 0, 1022)

dt = 1
moon_positions = []
earth_positions = []

for _ in range(2400000):
    force_earth_x, force_earth_y = gravitational_force(earth, moon)
    force_moon_x, force_moon_y = gravitational_force(moon, earth)


    acceleration_earth_x, acceleration_earth_y = acceleration(
        earth,
        force_earth_x,
        force_earth_y
    )

    acceleration_moon_x, acceleration_moon_y = acceleration(
        moon,
        force_moon_x,
        force_moon_y
    )

    earth.update(
        acceleration_earth_x,
        acceleration_earth_y,
        dt
    )
    earth_positions.append((earth.x, earth.y))

    moon.update(
        acceleration_moon_x,
        acceleration_moon_y,
        dt
    )
    moon_positions.append((
    moon.x - earth.x,
    moon.y - earth.y
))


print("Земля:")
print("x =", earth.x)
print("y =", earth.y)
print("vx =", earth.vx)
print("vy =", earth.vy)

print()

print("Луна:")
print("x =", moon.x)
print("y =", moon.y)
print("vx =", moon.vx)
print("vy =", moon.vy)

moon_x = []
moon_y = []

for position in moon_positions:
    moon_x.append(position[0])
    moon_y.append(position[1])

plt.plot(moon_x, moon_y)
plt.axis("equal")
plt.show()
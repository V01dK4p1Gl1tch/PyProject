from constants import GRAVITATIONAL_CONSTANT
import math


def gravitational_force(body1, body2) -> tuple[float, float]:
    dx = body2.x - body1.x
    dy = body2.y - body1.y

    distance = math.hypot(dx, dy)
    if distance == 0:
        return 0.0, 0.0

    force = GRAVITATIONAL_CONSTANT * (body1.mass * body2.mass) / (distance ** 2)

    force_x = force * (dx / distance)
    force_y = force * (dy / distance)

    return force_x, force_y


def acceleration(body, force_x: float, force_y: float) -> tuple[float, float]:
    return force_x / body.mass, force_y / body.mass
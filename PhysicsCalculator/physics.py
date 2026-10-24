from constants import GRAVITATIONAL_CONSTANT
import math


def gravitational_force(body1, body2):
    x_distance = body2.x - body1.x
    y_distance = body2.y - body1.y

    distance = math.sqrt(
        x_distance ** 2
        + y_distance ** 2
    )

    direction = (
        x_distance / distance,
        y_distance / distance
    )

    force = GRAVITATIONAL_CONSTANT * (
        body1.mass * body2.mass
    ) / distance ** 2

    force_x = force * direction[0]
    force_y = force * direction[1]

    if distance == 0:
        return 0, 0

    return force_x, force_y

def acceleration(body, force_x, force_y):
    acceleration_x = force_x/body.mass
    acceleration_y = force_y/body.mass

    return acceleration_x, acceleration_y
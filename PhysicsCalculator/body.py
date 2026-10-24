class Body:
    def __init__(
        self,
        name: str,
        mass: float,
        x: float,
        y: float,
        vx: float,
        vy: float
    ) -> None:
        self.name = name
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.history: list[tuple[float, float]] = []

    def update(self, acceleration_x: float, acceleration_y: float, dt: float) -> None:
        self.vx += acceleration_x * dt
        self.vy += acceleration_y * dt

        self.x += self.vx * dt
        self.y += self.vy * dt

    def record_position(self, ref_x: float = 0.0, ref_y: float = 0.0) -> None:
        # Сохраняем позицию (можно относительно другого тела, например Земли)
        self.history.append((self.x - ref_x, self.y - ref_y))
class Body:
    def init(
        self,
        mass: float,
        x: float,
        y: float,
        vx: float,
        vy: float
    ) -> None:
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self, acceleration_x: float, acceleration_y: float, dt: float) -> None:
        self.vx += acceleration_x * dt
        self.vy += acceleration_y * dt

        self.x += self.vx * dt
        self.y += self.vy * dt
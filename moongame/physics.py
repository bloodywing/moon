class Gravity:
    ms2 = 0
    atmo = 0

    def speed_after_x_duration(self, duration: int) -> float:
        return (self.ms2 * duration ^ 2) / 2

    def distance_after_x_duration(self, duration: int) -> float:
        return self.ms2 * duration


class EarthGravity(Gravity):
    ms2 = 9.807
    atmo = 80 * 1000


class MoonGravity(Gravity):
    ms2 = 1.62


class MarsGravity(Gravity):
    ms2 = 3.711

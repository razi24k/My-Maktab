class Newton:

    def __init__(self, movement, time):
        self.movement = movement
        self.time = time

    def speed(self):
        return self.movement / self.time

    @staticmethod
    def acceleration(speed_change, time):
        return speed_change / time

    @staticmethod
    def power(mass, speed_change, time):
        return mass * (speed_change / time)

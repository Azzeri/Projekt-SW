import time


class Vehicle:
    position = 0  # Meters
    speed = 0  # Meters per second
    minSpeed = 0
    maxSpeed = 300

    def increaseSpeed(self):
        if self.speed + 10 < self.maxSpeed:
            self.speed += 10
        else:
            self.speed = self.maxSpeed
        print('Aktualna prędkość: ' + str(self.speed))

    def decreaseSpeed(self):
        if self.speed - 10 >= self.minSpeed:
            self.speed -= 10
        else:
            self.speed = self.minSpeed
        print('Aktualna prędkość: ' + str(round(self.speed)))

    def updatePosition(self):
        currentSpeedInMps = self.speed * 0.277777778
        self.position += currentSpeedInMps
        print('\nAktualna pozycja: ' + str(self.position))
        time.sleep(1)

    def reset(self):
        self.position = 0
        self.speed = 0

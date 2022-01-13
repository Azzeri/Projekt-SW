import time


class Vehicle:
    position = 0  # Meters
    speed = 0  # Meters per second
    minSpeed = 0
    maxSpeed = 300

    def increaseSpeed(self, value):
        if self.speed + value < self.maxSpeed:
            self.speed += value
        else:
            self.speed = self.maxSpeed

    def decreaseSpeed(self, value):
        if self.speed - value >= self.minSpeed:
            self.speed -= value
        else:
            self.speed = self.minSpeed

    def updatePosition(self):
        currentSpeedInMps = self.speed * 0.277777778
        self.position += currentSpeedInMps
        print(self.position)
        time.sleep(1)
    
    def reset(self):
        self.position = 0
        self.speed = 0

class WaveController:
    closestLights = None
    nextLightsIndex = None

    def __init__(self, allowedSpeed):
        self.allowedSpeed = allowedSpeed

    def checkIfVehicleExceededSpeed(self, vehicle):
        if vehicle.speed > self.allowedSpeed:
            return True
        else:
            return False

    def compareVehicleAndLightsPosition(self, vehicle, lights):
        for index in range(len(lights)):
            if vehicle.position >= lights[index].position:
                self.closestLights = lights[index]
                if index != len(lights) - 1:
                    self.nextLightsIndex = index + 1

    def reset(self):
        self.closestLights = None
        self.nextLightsIndex = None
from Vehicle import Vehicle
from TrafficLights import TrafficLights
from WaveController import WaveController
# koment

vehicle = Vehicle()
mainController = WaveController(50)
trafficLights = [
    TrafficLights(200, 'green'),
    TrafficLights(500, 'green'),
    TrafficLights(800, 'green'),
    TrafficLights(1100, 'green')
]

vehicle.increaseSpeed(650)

while True:
    vehicle.updatePosition()
    if vehicle.position >= trafficLights[len(trafficLights) - 1].position:
        vehicle.reset()
        mainController.reset()
        break
    else:
        mainController.compareVehicleAndLightsPosition(vehicle, trafficLights)
        if(mainController.closestLights):
            print('mamy swiatla ' + str(mainController.closestLights.position))
            if mainController.checkIfVehicleExceededSpeed(vehicle) == True:
                trafficLights[mainController.nextLightsIndex].color = 'red'
            print('nastepne swiatla ' + str( trafficLights[mainController.nextLightsIndex].position) + ' kolor: ' + trafficLights[mainController.nextLightsIndex].color)

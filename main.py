from Vehicle import Vehicle
from TrafficLights import TrafficLights
from WaveController import WaveController
from gpiozero import LED, Button

buttonIncrease = Button(17)
buttonDecrease = Button(4)
ledRed = LED(22)
ledGreen = LED(27)

ledGreen.off()
ledRed.off()

# buttonIncrease.when_pressed = ledGreen.on
# buttonIncrease.when_released = ledGreen.off

vehicle = Vehicle()
mainController = WaveController(50)
trafficLights = [
    TrafficLights(200, 'green'),
    TrafficLights(500, 'green'),
    TrafficLights(800, 'green'),
    TrafficLights(1100, 'green')
]

# vehicle.increaseSpeed(650)
buttonIncrease.when_pressed = vehicle.increaseSpeed(10)
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

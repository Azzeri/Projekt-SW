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
    TrafficLights(1, 200, 'green'),
    TrafficLights(2, 500, 'green'),
    TrafficLights(3, 800, 'green'),
    TrafficLights(4, 1100, 'green')
]

# vehicle.increaseSpeed(650)
buttonIncrease.when_pressed = vehicle.increaseSpeed
buttonDecrease.when_pressed = vehicle.decreaseSpeed
while True:
    vehicle.updatePosition()
    if vehicle.position >= trafficLights[len(trafficLights) - 1].position:
        vehicle.reset()
        mainController.reset()
        break
    else:
        mainController.compareVehicleAndLightsPosition(vehicle, trafficLights)
        if(mainController.closestLights):
            print('Dojechałeś do świateł nr' + str(mainController.closestLights.number))
            if mainController.checkIfVehicleExceededSpeed(vehicle) == True:
                trafficLights[mainController.nextLightsIndex].color = 'red'
            print('Numer następnych świateł: ' + str( trafficLights[mainController.nextLightsIndex].number) + ' Kolor: ' + trafficLights[mainController.nextLightsIndex].color)

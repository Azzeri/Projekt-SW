from Vehicle import Vehicle
from TrafficLights import TrafficLights
from WaveController import WaveController
from gpiozero import LED, Button

buttonIncrease = Button(17)
buttonDecrease = Button(4)
ledRed = LED(22)
ledGreen = LED(27)

ledGreen.on()
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
        for light in trafficLights:
            light.reset()
        break
    else:
        mainController.compareVehicleAndLightsPosition(vehicle, trafficLights)
        if(mainController.closestLights):
            print('Przejecjałeś światła nr ' + str(mainController.closestLights.number) + ' na kolorze ' + mainController.closestLights.color)
            if mainController.checkIfVehicleExceededSpeed(vehicle) == True:
                trafficLights[mainController.nextLightsIndex].color = 'red'
            if trafficLights[mainController.nextLightsIndex].color == 'red':
                ledGreen.off()
                ledRed.on()
            else:
                ledGreen.on()
                ledRed.off()
            print('Numer następnych świateł: ' + str( trafficLights[mainController.nextLightsIndex].number) + ' Kolor: ' + trafficLights[mainController.nextLightsIndex].color)


import threading
import time
class TrafficLights:

    def __init__(self, number, position, color):
        self.number = number
        self.position = position
        self.color = color

    def reset(self):
        self.color = 'green'

    def switchLightsColor(self):
        t1 = threading.Thread(target=self.wait)
        t1.start()
        t1.join()
        self.color = 'green'

    def wait():
        time.sleep(3)
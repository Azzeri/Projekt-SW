class TrafficLights:

    def __init__(self, number, position, color):
        self.number = number
        self.position = position
        self.color = color

    def reset(self):
        self.color = 'green'
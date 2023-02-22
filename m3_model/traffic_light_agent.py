from mesa import Agent


class TrafficLightAgent(Agent):
    TRAFFIC_LIGHT_COLOURS = ('red', 'green')

    def __init__(self, unique_id, colour, model):
        super().__init__(unique_id, model)
        self.colour = colour

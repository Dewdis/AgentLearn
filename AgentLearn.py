class Agent:
    def __init__(self, name):
        self.name = name
        print("Agent '" + name + "' is created!")

    def measure(self, environment):
        print("Agent '" + self.name + "': MEASURE method is undefined!")
        pass

    def action(self):
        print("Agent '" + self.name + "': ACTION method is undefined!")
        pass


class Environment:
    agents = []

    def __init__(self, name):
        self.name = name
        print("Environment '" + self.name + "' is created!")
        self.visualize()

    def visualize(self):
        print("Environment '" + self.name + "': VISUALIZATION method is undefined!")
        pass

    def visualize_agent(self, agent):
        pass

    def spawn_agent(self, agent):
        self.agents.append(agent)
        print("Agent '" + agent.name + "' is SPAWNED in environment '" + self.name + "'")

    def measure(self, agent):
        print("Environment '" + self.name + "': MEASURE method is undefined!")
        pass

    def effect(self, agent, action):
        print("Environment '" + self.name + "': EFFECT method is undefined!")
        pass

    def model_step(self):
        # TODO: firstly - control, secondary - EFFECT
        # (for multiple agents)
        for agent in self.agents:
            agent.measure(self)
            self.effect(agent, agent.action())
        self.visualize()
        for agent in self.agents:
            self.visualize_agent(agent)

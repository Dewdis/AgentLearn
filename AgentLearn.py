import time
import matplotlib

# TODO:
# 1. One Agent can't simultaneously live
# in more than one Environment.
# 2. Agents from independent developers
# can't work in Environments from other
# developers.

"""
Base Agent class.
Template for Agent's logic.
Agent's "physical" interaction with Environment
is described in "Environment" instances.
"""
class Agent:
    attitude, position = None, None

    def __init__(self, name):
        self.name = name
        print("Agent '" + name + "' is created!")

    def measure(self, environment):
        print("Agent '" + self.name + "': MEASURE method is undefined!")
        pass

    def get_reward(self, reward):
        print("Agent '" + self.name + "': GET_REWARD method is undefined!")
        pass

    def action(self):
        print("Agent '" + self.name + "': ACTION method is undefined!")
        pass


"""
Base Environment class.
Template for Environment's logic
and Environment / Agent "physics".
Describes "physical" Environment interaction
and "physical" Agent's body.
"""
class Environment:
    agents = []

    def __init__(self, name):
        self.name = name
        print("Environment '" + self.name + "' is created!")
        self.visualize_map()

    def visualize_map(self):
        print("Environment '" + self.name + "': VISUALIZE_MAP method is undefined!")
        pass

    def visualize_agent(self, agent):
        print("Environment '" + self.name + "': VISUALIZE_AGENT method is undefined!")
        pass

    def visualize(self):
        self.visualize_map()
        for agent in self.agents:
            self.visualize_agent(agent)

    def spawn_agent(self, agent):
        self.agents.append(agent)
        print("Agent '" + agent.name + "' is SPAWNED in environment '" + self.name + "'")

    def measure(self, agent):
        print("Environment '" + self.name + "': MEASURE method is undefined!")
        pass

    def calc_reward(self, agent):
        print("Environment '" + self.name + "': CALC_REWARD method is undefined!")
        return None

    def effect(self, agent, action):
        print("Environment '" + self.name + "': EFFECT method is undefined!")
        pass

    def model_step(self):
        # TODO: firstly - control, secondary - EFFECT
        # (for multiple agents)
        for agent in self.agents:
            agent.measure(self.measure(agent))
            agent.get_reward(self.calc_reward(agent))
            self.effect(agent, agent.action())
        self.visualize()

    def simulate(self, T, delay):
        for t in range(T):
            self.model_step()
            try:
                matplotlib.pyplot.draw()
                matplotlib.pyplot.pause(delay)
            except Exception as GraphicsException:
                print("\nERROR: matplotlib can't draw image")
                print(GraphicsException)
                print("Probably, window was closed")
                exit(0)
            #time.sleep(delay)

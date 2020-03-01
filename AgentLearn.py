import time

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
    def __init__(self, name):
        self.name = name
        print("Agent '" + name + "' is created!")

    def measure(self, environment):
        print("Agent '" + self.name + "': MEASURE method is undefined!")
        pass

    def get_prize(self):
        print("Agent '" + self.name + "': GET_PRIZE method is undefined!")
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
        self.visualize()

    def visualize_map(self):
        print("Environment '" + self.name + "': VISUALIZE_MAP method is undefined!")
        pass

    def visualize_agent(self, agent):
        print("Environment '" + self.name + "': VISUALIZE_AGENT method is undefined!")
        pass

    def __visualize(self):
        self.visualize_map()
        for agent in self.agents:
            self.visualize_agent(agent.__attitude, agent.__position)

    def __spawn_agent(self, agent):
        self.agents.append(agent)
        print("Agent '" + agent.name + "' is SPAWNED in environment '" + self.name + "'")

    def measure(self, agent):
        print("Environment '" + self.name + "': MEASURE method is undefined!")
        pass

    def effect(self, agent, action):
        print("Environment '" + self.name + "': EFFECT method is undefined!")
        pass

    def __model_step(self):
        # TODO: firstly - control, secondary - EFFECT
        # (for multiple agents)
        for agent in self.agents:
            agent.measure(self.measure(agent.__attitude, agent.__position))
            agent.get_prize(self.calc_prize(agent))
            self.effect(agent, agent.action())
        self.__visualize()

    def __simulate(self, T, delay):
        for t in range(T):
            self.__model_step()
            time.delay(delay)

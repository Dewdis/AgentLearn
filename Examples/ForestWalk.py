import matplotlib
import matplotlib.pyplot

import sys; sys.path.append("..")
import AgentLearn


T = 10


print("'ForestWalk' Example is started")


class Agent(AgentLearn.Agent):
    pass


class Environment(AgentLearn.Environment):
    """
    0 --> forest
    1 --> sand
    2 --> stone
    3 --> water
    """
    map = [
        [2,2,2,2,2,2,2,2],
        [2,0,0,0,0,0,0,2],
        [2,0,1,1,1,1,0,2],
        [2,0,1,3,3,1,0,2],
        [2,0,1,1,3,1,0,2],
        [2,0,0,1,1,1,0,2],
        [2,0,0,0,0,0,0,2],
        [2,2,2,2,2,2,2,2]
    ]

    def visualize(self):
        # print(matplotlib.get_backend())
        matplotlib.rcParams["toolbar"] = "None"
        matplotlib.pyplot.gcf().canvas.set_window_title(self.name)
        #matplotlib.pyplot.get_current_fig_manager().full_screen_toggle()
        matplotlib.pyplot.axis("off")
        colors = ["#88B04B", "#EFC050", "#DFCFBE", "#92A8D1"]
        bounds = [0,1,2,3,4]
        cmap = matplotlib.colors.ListedColormap(colors)
        norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
        matplotlib.pyplot.imshow(self.map, cmap=cmap, norm=norm)
        matplotlib.pyplot.show()


robot = Agent("Roma")
world = Environment("Forest")
world.spawn_agent(robot)

for t in range(0, T):
    world.model_step()

# AgentLearn
Packet for research in autonomous agent's AI

# What is Reinforcement Learning?
Reinforcement Learning is a part of Machine Learning. Idea is catched from psychology. We have Agent, Environment and Prize to maximize.

# Mathematical References
- http://www.machinelearning.ru/wiki/index.php?title=Обучение_с_подкреплением (Russian)

# Guide
## Agent:
    Parameters:
    - __attitude
    - __position
    Methods:
    - Agent.measure(data_from_sensors)
    - Agent.get_prize(prize)
    - Agent.action()
## Environment:
    - __visualize()
    - __spawn_agent()
    - __model_step()
    - __simulate()
    - visualize_map()
    - visualize_agent()
    - measure()
    - effect()

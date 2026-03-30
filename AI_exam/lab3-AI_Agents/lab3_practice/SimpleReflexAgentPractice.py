import random

class Environment:
    def __init__(self):
        # A. Random initial state
        self.state = random.choice(['Dirty', 'Clean'])

    def get_percept(self):
        return self.state

    def update_state_randomly(self):
        # B. Randomly change the state after each step
        self.state = random.choice(['Dirty', 'Clean'])

class SimpleReflexAgent:
    def __init__(self):
        pass

    def act(self, percept):
        if percept == 'Dirty':
            return 'Clean the room'
        else:
            return 'Room is already clean'

def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)

        print(f"Step {step + 1}: Percept - {percept}, Action - {action}")

        # If dirty, agent cleans it
        if percept == 'Dirty':
            environment.state = 'Clean'

        # Environment changes unpredictably
        environment.update_state_randomly()

# Create agent and environment
agent = SimpleReflexAgent()
environment = Environment()

# Run simulation for 5 steps
run_agent(agent, environment, 5)

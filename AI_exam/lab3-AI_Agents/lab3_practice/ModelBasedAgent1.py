class ModelBasedAgent:
    def __init__(self):
        # The model keeps track of the internal state (memory)
        self.model = {}

    def update_model(self, percept):
        # The agent stores the current state of the room in its memory
        self.model['current'] = percept
        print(f"  [Internal State Updated]: {self.model}")

    def predict_action(self):
        # Decision making based on the internal model
        if self.model.get('current') == 'Dirty':
            return 'Clean the room'
        else:
            return 'Room is clean'

    def act(self, percept):
        # Update memory first, then decide on an action
        self.update_model(percept)
        return self.predict_action()


class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        # Returns what the agent currently 'sees'
        return self.state

    def clean_room(self):
        # Updates the physical state of the environment
        self.state = 'Clean'


def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)

        print(f"Step {step + 1}: Percept - {percept}, Action - {action}")

        # If the agent chooses to clean, the environment's state changes
        if action == 'Clean the room':
            environment.clean_room()
        print("-" * 30)


# Create instances of the agent and the environment
agent = ModelBasedAgent()
environment = Environment(state='Dirty')

# Run the simulation for 5 steps
run_agent(agent, environment, 5)
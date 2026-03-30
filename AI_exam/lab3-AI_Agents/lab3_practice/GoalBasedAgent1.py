class GoalBasedAgent:
    def __init__(self):
        # The ultimate target state the agent wants to achieve
        self.goal = 'Clean'

    def formulate_goal(self, percept):
        """Logic to decide what the current goal should be based on the percept."""
        if percept == 'Dirty':

            self.goal = 'Clean'
        else:
            self.goal = 'Maintain'

    def act(self, percept):
        """Chooses an action that leads toward the goal."""
        self.formulate_goal(percept)

        if self.goal == 'Clean':
            return 'Clean the room'
        else:
            return 'Room is clean'


class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'


def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)

        print(f"Step {step + 1}: Percept - {percept} | Action - {action}")

        # If the action performed leads to the goal state, update environment
        if action == 'Clean the room':
            environment.clean_room()

        print("-" * 40)


# Create instances
agent = GoalBasedAgent()
environment = Environment(state='Dirty')

# Run the agent for 5 steps
run_agent(agent, environment, 5)
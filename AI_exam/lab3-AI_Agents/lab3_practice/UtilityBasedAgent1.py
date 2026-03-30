class UtilityBasedAgent:
    def __init__(self):
        # Utility defines the 'happiness' or 'value' of a state
        # Clean is high reward (+10), Dirty is a penalty (-10)
        self.utility = {'Dirty': -10, 'Clean': 10}

    def calculate_utility(self, percept):
        """Returns the utility value of the current state."""
        return self.utility[percept]

    def select_action(self, percept):
        """Chooses the action that results in the highest utility."""
        if percept == 'Dirty':
            return 'Clean the room'
        else:
            return 'No action needed'

    def act(self, percept):
        # In a real utility agent, it would compare utilities of different
        # possible future states, but here we select the best known action.
        action = self.select_action(percept)
        return action


class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'


def run_agent(agent, environment, steps):
    total_utility = 0
    print(f"{'Step':<8} | {'Percept':<8} | {'Action':<18} | {'Utility':<8}")
    print("-" * 50)

    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)
        utility = agent.calculate_utility(percept)

        total_utility += utility

        print(f"{step + 1:<8} | {percept:<8} | {action:<18} | {utility:<8}")

        if action == 'Clean the room':
            environment.clean_room()

    print("-" * 50)
    print(f"Total Cumulative Utility: {total_utility}")


# --- Execution ---
# Create instances of agent and environment
agent = UtilityBasedAgent()
environment = Environment(state='Dirty')

# Run the agent in the environment for 5 steps
run_agent(agent, environment, 5)
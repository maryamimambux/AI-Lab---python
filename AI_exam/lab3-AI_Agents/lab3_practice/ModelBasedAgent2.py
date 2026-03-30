class Environment:
    def __init__(self, rain='No', windows_open='Open'):
        self.rain = rain
        self.windows_open = windows_open

    def get_percept(self):
        """Returns the current percept (rain status and window status)."""
        return {'rain': self.rain, 'windows_open': self.windows_open}

    def close_windows(self):
        """Closes the windows if they are open."""
        if self.windows_open == 'Open':
            self.windows_open = 'Closed'

class ModelBasedAgent:
    def __init__(self):
        # The internal model tracks the history/state of the environment
        self.model = {'rain': 'No', 'windows_open': 'Open'}

    def act(self, percept):
        """Decides action based on the model and current percept."""
        # Update the internal model with the current percept
        self.model.update(percept)

        # Check the model to decide action
        if self.model['rain'] == 'Yes' and self.model['windows_open'] == 'Open':
            return 'Close the windows'
        else:
            return 'No action needed'

def run_agent(agent, environment, steps):
    print(f"{'Step':<10} | {'Percept':<30} | {'Action':<20} | {'Window State'}")
    print("-" * 85)

    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)

        # Apply the agent's action to the environment
        if action == 'Close the windows':
            environment.close_windows()

        print(f"Step {step + 1:<5} | {str(percept):<30} | {action:<20} | {environment.windows_open}")


# 1. Initialize Agent
agent = ModelBasedAgent()

# 2. Create environment (It's raining and windows are open)
environment = Environment(rain='Yes', windows_open='Open')

# 3. Run the agent in the environment for 5 steps
run_agent(agent, environment, 5)
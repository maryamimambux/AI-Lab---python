import random


class LearningBasedAgent:
    def __init__(self, actions):
        # Q-table stores the learned values of (state, action) pairs
        self.Q = {}
        self.actions = actions
        self.alpha = 0.1  # Learning rate: how much new info overrides old info
        self.gamma = 0.9  # Discount factor: importance of future rewards
        self.epsilon = 0.1  # Exploration rate: probability of trying a random action

    def get_Q_value(self, state, action):
        # Default to 0.0 if the state-action pair hasn't been seen yet
        return self.Q.get((state, action), 0.0)

    def select_action(self, state):
        # Epsilon-greedy strategy: explore vs exploit
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)  # Explore (Random)
        else:
            # Exploit (Choose action with highest Q-value)
            return max(self.actions, key=lambda a: self.get_Q_value(state, a))

    def learn(self, state, action, reward, next_state):
        """Updates the Q-value based on the Bellman Equation."""
        old_Q = self.get_Q_value(state, action)
        best_future_Q = max([self.get_Q_value(next_state, a) for a in self.actions])

        # Q-Learning Formula
        new_Q = old_Q + self.alpha * (reward + self.gamma * best_future_Q - old_Q)
        self.Q[(state, action)] = new_Q

    def act(self, state):
        return self.select_action(state)


class Environment:
    def __init__(self, state='Dirty'):
        self.state = state

    def get_percept(self):
        return self.state

    def clean_room(self):
        self.state = 'Clean'
        return 10  # High reward for cleaning

    def no_action_reward(self):
        return 0  # Neutral reward


def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)

        # Execute action and get reward
        if action == 'Clean the room' and percept == 'Dirty':
            reward = environment.clean_room()
        else:
            reward = environment.no_action_reward()

        print(f"Step {step + 1}: Percept - {percept}, Action - {action}, Reward - {reward}")

        # Observe the result of the action
        next_percept = environment.get_percept()

        # The agent learns from the transition
        agent.learn(percept, action, reward, next_percept)


# --- Execution ---
# Define possible actions
actions = ['Clean the room', 'No action needed']

# Create instances
agent = LearningBasedAgent(actions)
environment = Environment(state='Dirty')

# Run for 5 steps
run_agent(agent, environment, 5)

# Show what the agent learned (The Q-Table)
print("\nFinal Learned Q-Table Values:")
for (state, action), value in agent.Q.items():
    print(f"State: {state} | Action: {action} | Q-Value: {value:.4f}")
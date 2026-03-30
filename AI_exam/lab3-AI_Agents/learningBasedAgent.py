# learning based agent
# Improves decisions over time using rewards + feedback

# CONCEPTS
"""
=== 1. ===
Q-Table : stores "How good is an action"
Higher the value better the Action
-----------------------------
State	Action	       Value
-----------------------------
Dirty	Clean	       10
Dirty	Do nothing	   -5
-----------------------------

=== 2. ===
Reward : "Feedback after action"
Good action → +10
Bad action → -10

=== 3. ===
Exploration : "Trying new things"
Example: “Let me try NOT cleaning… what happens?”

=== 4. ===
Exploitation : "Using what you already know"
Example: “Cleaning gives +10 → always do that”

=== 5. ===
Balance : "Smart agent does both: Sometimes explore, Mostly exploit"

"""

"""
#----------------------------------------------------------------------------
import random

class LearningBasedAgent:
    def __init__(self, actions):
        self.Q = {}  # Q-table - Initialy EMPTY , Agent knows nothing initially
        
        self.actions = actions # ['Clean', 'Do nothing']
        
        # Learning rate. Small → slow learning, Large → fast but unstable
        self.alpha = 0.1   
        
        # Discount factor. Future importance, If High → cares about future rewards
        self.gamma = 0.9   
        
        # Exploration rate, 10% chance → explore, 90% → use best known action
        self.epsilon = 0.1
 
    def select_action(self, state):
        # Explore with epsilon probability
        # How it Works?????
        # It chooses "Random number between 0 and 1"
        
        # And if that (Random number) < (Epsilon i.e. 0.1)
        # then Try something random(new)
        
        if random.uniform(0, 1) < self.epsilon: 
            return random.choice(self.actions)  
            
        # Otherwise refer to Q-table and Choose BEST ACTION 
        else:
            # Pick best known action for this state
            return max(self.actions, key=lambda a: self.get_Q_value(state, a))
    
    
    def learn(self, state, action, reward, next_state):
    
        # Update Q-table based on what we learned
        
        old_Q = self.get_Q_value(state, action) # ** Old knowledge **
        
        # ** This is the Q-learning formula **
        best_future_Q = max([self.get_Q_value(next_state, a) for a in self.actions])
        
        
        # New Value = Old knowledge + Adjustment based on: reward and future reward
        
        self.Q[(state, action)] = old_Q + self.alpha * (reward + self.gamma * best_future_Q - old_Q)

"""

import random

class LearningBasedAgent:
    def __init__(self, actions):
        self.Q = {}  # Q-table
        self.actions = actions
        self.alpha = 0.1   # Learning rate
        self.gamma = 0.9   # Discount factor
        self.epsilon = 0.2 # Exploration rate

    def get_Q_value(self, state, action):
        # this (state, action) can be considered as KEY
        # Q = { ('Dirty', 'Clean'): 10,
        #       ('Dirty', 'Do nothing'): -5 }

        # Look in Q-table for (state, action)
        # If it exists → return its value,If NOT → return 0

        # As in Q table NOTHING is Stored. So, Output = 0
        # After LEARNING self.Q = {('Dirty', 'Clean'): 10} :
        # this self.Q.get((state, action), 0) , Output = 10

        return self.Q.get((state, action), 0)

    def select_action(self, state):
        # Exploration vs Exploitation

        # Explore with epsilon probability
        # How it Works?????
        # It chooses "Random number between 0 and 1"

        # And if that (Random number) < (Epsilon i.e. 0.1)
        # then Try something random(new)
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)  # Explore
        else:

            # Otherwise refer to Q-table and Choose BEST ACTION
            return max(self.actions, key=lambda a: self.get_Q_value(state, a))  # Exploit

    def learn(self, state, action, reward, next_state):
        old_Q = self.get_Q_value(state, action)

        # Best future Q-value
        best_future_Q = max([self.get_Q_value(next_state, a) for a in self.actions])

        # Q-learning formula
        new_Q = old_Q + self.alpha * (reward + self.gamma * best_future_Q - old_Q)

        # ** This is where Q-table updated! **
        self.Q[(state, action)] = new_Q


# ----------- ENVIRONMENT SIMULATION -----------

def get_reward(state, action):
    if state == 'Dirty' and action == 'Clean':
        return 10
    elif state == 'Clean' and action == 'Clean':
        return -5  # unnecessary cleaning
    else:
        return 0


# ----------- MAIN PROGRAM -----------

actions = ['Clean', 'Do nothing']
agent = LearningBasedAgent(actions)

states = ['Dirty', 'Clean']

# Training loop
for episode in range(50):
    state = random.choice(states)

    action = agent.select_action(state)

    reward = get_reward(state, action)

    # Simulate next state
    if action == 'Clean':
        next_state = 'Clean'
    else:
        next_state = state

    agent.learn(state, action, reward, next_state)

# ----------- TEST AFTER LEARNING -----------

print("\nLearned Q-Table:")
for key, value in agent.Q.items():
    print(f"{key}: {round(value, 2)}")

print("\nAgent Decisions After Learning:")
for state in states:
    action = agent.select_action(state)
    print(f"State: {state} → Action: {action}")

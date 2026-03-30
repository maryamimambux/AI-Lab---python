# utility based agent
# Not just achieving goals, but maximizing satisfaction (utility).

# Analogy: Choosing a phone - you want good camera, long battery,
# reasonable price. You calculate which gives the best overall value.

"""

class UtilityBasedAgent:
    def __init__(self):
        # ** Assign values(numbers) to different states
        self.utility = {'Dirty': -10, 'Clean': 10}

    # ** Evaluate each state/action
    # "" It Simply returns PERCEPT'S corresponding utility value
    def calculate_utility(self, percept):
        return self.utility[percept]

    # Choose the highest utility
    def select_action(self, percept):
        if percept == 'Dirty':
            return 'Clean the room'  # Gives +10 utility
        else:
            return 'No action'       # Maintains +10 utility



# ============== IMPROVED ==============

class UtilityBasedAgent:
    def __init__(self):
        # Utility values for states
        self.utility = {
            'Dirty': -10,
            'Clean': 10
        }

    def calculate_utility(self, state):
        return self.utility[state]

    def select_action(self, percept):
        # If we CLEAN, result state becomes 'Clean'
        utility_if_clean = self.calculate_utility('Clean')

        # If we DO NOTHING, state stays same
        utility_if_do_nothing = self.calculate_utility(percept)

        # Choose action with higher utility
        if utility_if_clean > utility_if_do_nothing:
            return 'Clean the room'
        else:
            return 'Do nothing'


# ----------- MAIN PROGRAM -----------

agent = UtilityBasedAgent()

grid = ['Clean', 'Dirty', 'Clean']

for i in range(len(grid)):
    percept = grid[i]
    action = agent.select_action(percept)

    print(f"Location {i+1}: {percept}")
    print(f"Action: {action}")
    print("-------------------")


"""
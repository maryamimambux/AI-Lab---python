# goal based agent
# Has a specific goal and chooses actions that help achieve it.

# Analogy: You want to get an A in a course (goal).
# You study, attend classes, do homework - all actions serve the goal.

# It has Memory but very limited. It only Remembers GOAL
# But Model-Based remembers world state/history
"""

class GoalBasedAgent:
    def __init__(self):
        self.goal = 'Clean'  # ** The agent's ultimate objective **

    def formulate_goal(self, percept):
        # ** Compare current state with goal
        # and change GOAL according to environment's current state

        if percept == 'Dirty':
            self.goal = 'Clean'
        else:
            self.goal = 'No action needed'

    def act(self, percept):
        # Before you ACT, check Environment and DECIDE GOAL accordingly
        # Hence we are using ** self.formulate_goal() function

        self.formulate_goal(percept)

        # ONCE You know GOAL, Agent Acts based on it
        if self.goal == 'Clean':
            return 'Clean the room'
        else:
            return 'Room is clean'

"""


# model based agent
# Keep track of what happened before(memory)

# Analogy: Before going outside, you check the weather app
# AND remember that it rained yesterday, so you take an umbrella.

"""

class ModelBasedAgent:
    def __init__(self):
        # ** model - stores past information **
        self.model = {'rain': 'No', 'windows_open': 'Open'}

    def act(self, percept):
        # ** Update model with current percept **
        self.model.update(percept)

        # Use model to decide action
        if self.model['rain'] == 'Yes' and self.model['windows_open'] == 'Open':
            return 'Close windows'
        else:
            return 'No action needed'

"""


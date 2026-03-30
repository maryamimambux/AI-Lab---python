class goalBasedAgent:
    def __init__(self, rooms):
        self.rooms = rooms
        self.position = 0
        self.goal = 'Clean All Rooms.'

    def is_goal_achieved(self):
        return 'Dirty' not in self.rooms

    def formulate_goal(self):
        if self.is_goal_achieved():
            self.goal = 'Goal is Achieved.'
        else:
            self.goal = 'Need to clean remaining dirty rooms!'

    def act(self, percept):
        self.formulate_goal()

        if percept == 'Dirty':
            self.rooms[self.position] = 'Clean'
            return 'Clean Room'
        else:
            if self.position < len(self.rooms) - 1:
                self.position += 1
                return 'Move to next room'
            else:
                return 'At end, no more rooms'

    def display_status(self):
        print(f"Position: {self.position}, Rooms: {self.rooms}")
        print(f"Goal: {self.goal}")


class Environment:
    def __init__(self, rooms):
        self.rooms = rooms.copy()
        self.position = 0

    def get_percept(self):
        return self.rooms[self.position]

    def clean_room(self, position):
        self.rooms[position] = 'Clean'


def run_agent(agent, environment, max_steps=7):
    step = 0

    # ✅ FIXED CONDITION HERE
    while not agent.is_goal_achieved() and step < max_steps:
        environment.position = agent.position
        percept = environment.get_percept()
        action = agent.act(percept)

        if action == 'Clean Room':
            environment.clean_room(agent.position)

        print(f"Step {step + 1}: Position {agent.position}, Percept: {percept}, Action: {action}")
        agent.display_status()
        print("-" * 50)
        step += 1

    if agent.is_goal_achieved():
        print("SUCCESS! All rooms are clean!")
    else:
        print("Max steps reached without achieving goal")


# Run the simulation
initial_rooms = ['Dirty', 'Clean', 'Dirty', 'Dirty', 'Clean']
agent = goalBasedAgent(initial_rooms.copy())
environment = Environment(initial_rooms)
run_agent(agent, environment)

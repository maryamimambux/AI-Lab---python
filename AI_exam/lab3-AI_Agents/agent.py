
"""
class Agent:
        def __init__(self):
            self.name = 'Vaccum'
            self.status = 'off'

        def act(self, percept):
            if(percept == 'Dirty' and self.status == 'on'):
                print('Cleaning ...')
            elif(percept == 'Dirty' and self.status == 'off'):
                print("Can't Clean! Beacause Vaccum Cleaner is OFF.")
                flag = input("Turn it ON [y/n]: ")
                if(flag.lower() == 'y'):
                    self.status = 'on'
                    self.act(percept)
                else:
                    print("Exiting ...")
            else:
                print('Already Clean!')


reflex_agent = Agent()

grid = ['Clean', 'Dirty', 'Clean']
for id in range(3):
    reflex_agent.act(grid[id]) """



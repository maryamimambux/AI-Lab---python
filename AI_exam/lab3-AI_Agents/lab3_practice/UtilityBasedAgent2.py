class Environment:
    def __init__(self, movies):
        # movies: A dictionary {title: review_score}
        self.movies = movies

    def get_percept(self):
        """Returns the list of movies and their review scores."""
        return self.movies

class UtilityBasedAgent:
    def __init__(self, mood_factor):
        # mood_factor is a float (0 to 1) representing preference strength
        self.mood_factor = mood_factor

    def calculate_utility(self, review_score):
        """Computes utility: Utility = (review score) * (mood factor)"""
        return review_score * self.mood_factor

    def act(self, percept):
        """Chooses the movie with the highest utility value."""
        best_movie = None
        max_utility = -1

        print(f"{'Movie':<10} | {'Review':<8} | {'Calculated Utility':<15}")
        print("-" * 40)

        for movie, score in percept.items():
            current_utility = self.calculate_utility(score)
            print(f"{movie:<10} | {score:<8} | {current_utility:<15.2f}")

            if current_utility > max_utility:
                max_utility = current_utility
                best_movie = movie

        return best_movie, max_utility


def run_agent(agent, environment):
    # 1. Get perception from environment
    percept = environment.get_percept()

    # 2. Agent decides the best action (movie to watch)
    movie, utility_score = agent.act(percept)

    print("-" * 40)
    print(f"Decision: The agent chose to watch '{movie}' with a utility of {utility_score:.2f}")



# Initialize movies and their review scores (1-10 scale)
movie_data = {'Movie A': 7, 'Movie B': 9, 'Movie C': 5}
environment = Environment(movie_data)

# Initialize agent with a mood factor (e.g., 0.8)
agent = UtilityBasedAgent(mood_factor=0.8)

# Run the simulation
run_agent(agent, environment)
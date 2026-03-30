"""

A logistics company is optimizing its delivery truck space by selecting the most valuable set of packages
that fit within a weight limit. Each package has a specific weight and value, and the company needs to maximize
total value while ensuring the total weight does not exceed the truck’s capacity.
To solve this problem, you will implement a **Genetic Algorithm (GA)**.
Some parts of the algorithm are already provided, and your task is to complete the missing functions.

You must implement the following functions to complete the GA:
1. create_random_individual(num_items) - Generate a random binary list representing a possible solution
(1 = item included, 0 = item excluded).
2. initialize_population(pop_size, num_items) - Create an initial population of pop_size
individuals using create_random_individual().
3. select_parents(population, fitness_scores) - Select the top 50% of the population based on
fitness for reproduction.
4. crossover(parent1, parent2) - Implement single point crossover.
5. implement_single_point_crossover

"""

import random

# -----------------------------
# 1. Sample data (items)
# -----------------------------
weights = [2, 3, 4, 5, 9]
values  = [3, 4, 8, 8, 10]
capacity = 15

# -----------------------------
# 2. Create random individual
# -----------------------------
def create_random_individual(num_items):
    return [random.randint(0, 1) for _ in range(num_items)]

# -----------------------------
# 3. Initialize population
# -----------------------------
def initialize_population(pop_size, num_items):
    return [create_random_individual(num_items) for _ in range(pop_size)]

# -----------------------------
# 4. Fitness function
# (VERY IMPORTANT)
# -----------------------------
def fitness(individual):
    total_weight = 0
    total_value = 0

    for i in range(len(individual)):
        if individual[i] == 1:
            total_weight += weights[i]
            total_value += values[i]

    # If overweight → invalid solution
    if total_weight > capacity:
        return 0

    return total_value

# -----------------------------
# 5. Select parents (top 50%)
# -----------------------------
def select_parents(population):
    sorted_population = sorted(population, key=fitness, reverse=True)
    return sorted_population[:len(sorted_population)//2]

# -----------------------------
# 6. Single-point crossover
# -----------------------------
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2

# -----------------------------
# 7. Mutation (important in GA)
# -----------------------------
def mutate(individual, mutation_rate=0.1):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # flip bit
    return individual

# -----------------------------
# 8. GA Main function
# -----------------------------
def genetic_algorithm(pop_size, generations):
    num_items = len(weights)

    # Step 1: initial population
    population = initialize_population(pop_size, num_items)

    best_solution = None
    best_fitness = 0

    for gen in range(generations):

        # Step 2: evaluate best
        for ind in population:
            fit = fitness(ind)
            if fit > best_fitness:
                best_fitness = fit
                best_solution = ind

        # Step 3: select parents
        parents = select_parents(population)

        # Step 4: create next generation
        next_generation = []

        while len(next_generation) < pop_size:
            p1 = random.choice(parents)
            p2 = random.choice(parents)

            c1, c2 = crossover(p1, p2)

            next_generation.append(mutate(c1))
            next_generation.append(mutate(c2))

        population = next_generation[:pop_size]

        print(f"Generation {gen+1} Best Value: {best_fitness}")

    return best_solution, best_fitness

# -----------------------------
# 9. Run GA
# -----------------------------
best_solution, best_value = genetic_algorithm(pop_size=10, generations=20)

print("\nBest Solution:", best_solution)
print("Best Value:", best_value)

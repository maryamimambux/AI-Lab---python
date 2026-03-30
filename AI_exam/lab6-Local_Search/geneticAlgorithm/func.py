"""
Q3. Implement a Genetic Algorithm (GA) to maximize the function
f(x)=x^2-1

within the range [0,31].
Each solution should be represented as a 5-bit binary string, since
25 = 322^5 = 3225 = 32, covering all possible values of x. The algorithm
should start by generating a random population of binary-encoded values.
Each individual in the population should be evaluated based on its
fitness, which is determined by computing

f(x)=x^2-1.

The algorithm should then apply natural selection, retaining only the
fittest individuals based on their fitness scores.
Next, selected parents should undergo single-point crossover,
where a random point in their binary representation is chosen,
and their bits are swapped to create new offspring.
To introduce genetic diversity, each offspring should undergo
single-point mutation, where a randomly chosen bit is flipped (0→1 or 1→0)
with a small probability.
The process should continue for a fixed number of generations or
until the population converges to an optimal solution.
The algorithm should finally return the best x value found along
with its corresponding f(x) value, demonstrating how GA effectively
optimizes the function over successive generations.
"""

import random

# function
def f(x):
    return x*x - 1

# create initial population (6 individuals)
population = [
    ''.join(str(random.randint(0,1)) for _ in range(5))
    for _ in range(6)
]

# decode binary to decimal
def decode(ch):
    return int(ch, 2)

# selection (best 2)
def select(pop):
    return sorted(pop, key=lambda c: f(decode(c)), reverse=True)[:2]

# crossover (single point)
def crossover(p1, p2):
    if random.random() < 0.8:
        point = random.randint(1, 4)
        return p1[:point] + p2[point:]
    return p1

# mutation (flip bits)
def mutate(ch):
    ch = list(ch)
    for i in range(len(ch)):
        if random.random() < 0.05:
            if ch[i] == '0':
                ch[i] = '1'
            else:
                ch[i] = '0'
    return ''.join(ch)

# GA loop
for _ in range(50):

    p1, p2 = select(population)

    new_pop = [p1, p2]

    while len(new_pop) < 6:
        child = crossover(p1, p2)
        child = mutate(child)
        new_pop.append(child)

    population = new_pop

# best solution
best = max(population, key=lambda c: f(decode(c)))

print("Best Binary:", best)
print("x =", decode(best))
print("f(x) =", f(decode(best)))


"""
*** [AI Lab EXAM - B (30/03/2026) by Ms.Ramsha Jat] ***
Q3. [6 marks] A software company is developing an optimization module
that can automatically find the best input for a given mathematical
function. You are tasked with finding the maximum value of the
function  f(x) = x^2 - 3x + 4 , where x  is an integer between
0 and 15. To solve this, you decide to implement a Genetic Algorithm
(GA).

The algorithm will represent potential values of x as binary
chromosomes of 4 bits, and it will maintain a population of 4
individuals. The GA will use roulette wheel selection for
parent selection, single-point crossover to produce offspring,
and a mutation probability of 0.1 applied to each bit.

Your goal is to simulate the GA to evolve a population that eventually
contains the chromosome representing the maximum value of the function.
a. Encode a random initial population of 4 chromosomes in binary form.
b. Decode each chromosome into its decimal value and compute
its fitness using the function f(x) .
c. Perform one round of selection, crossover, and mutation, showing
all intermediate steps, including selected parents, crossover points,
and any mutations. d. Identify the best chromosome after this
generation and provide its decimal value and fitness.

"""
#=====================================================================
import random

# fitness function
def fitness(x):
    return x*x - 3*x + 4

# initial population (4-bit)
population = ["1010", "0111", "0001", "1100"]

# decode binary to decimal
def decode(ch):
    return int(ch, 2)

# compute fitness
fit_vals = [fitness(decode(ch)) for ch in population]

print("Initial Population:")
for ch in population:
    print(ch, "->", decode(ch), "Fitness:", fitness(decode(ch)))

# selection (roulette - simple pick best 2)
parents = sorted(population, key=lambda c: fitness(decode(c)), reverse=True)[:2]

print("\nSelected Parents:", parents)

# crossover
p1, p2 = parents
point = 2

child1 = p1[:point] + p2[point:]
child2 = p2[:point] + p1[point:]

# mutation
def mutate(ch):
    ch = list(ch)
    for i in range(len(ch)):
        if random.random() < 0.1:
            ch[i] = '1' if ch[i] == '0' else '0'
    return ''.join(ch)

child1 = mutate(child1)
child2 = mutate(child2)

new_pop = [child1, child2]

print("\nNew Population:")
for ch in new_pop:
    print(ch, "->", decode(ch), "Fitness:", fitness(decode(ch)))

# best
best = max(new_pop, key=lambda c: fitness(decode(c)))

print("\nBest Chromosome:", best)
print("Decimal:", decode(best))
print("Fitness:", fitness(decode(best)))

#=====================================================================

"""
**  [AI Lab EXAM - B (17/03/2025) by Ms.Ramsha Jat] **
Implement a Genetic Algorithm (GA) to maximize the function
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


#=====================================================================
"""

BEGINNER QUESTION 1: Maximum of a Simple Function
Problem: Find the maximum value of f(x) = -x² + 10x where x is an integer between 0 and 31. Use 5-bit binary representation.

Parameters:
Population size: 6 individuals
Selection: Roulette wheel
Crossover: Single-point (probability 0.8)
Mutation: 0.05 per bit
Generations: 50

Tasks:
What is the theoretical maximum? (Calculate by hand)
Write the GA to find it

"""


import random

# main function
def f(x):
    return -x**2 + 10*x

# generating random numbers for initial Population
# What it doing? -> generate 5 random bits → convert to string
population = [
    ''.join(str(random.randint(0,1)) for _ in range(5))
    for _ in range(5)
]

#def decode(bits):
#        return int(''.join(str(b) for b in bits), 2)
# easy ->
def decode(ch):
    return int(ch, 2)

def select(pop):
    return sorted(pop, key=lambda c: f(decode(c)), reverse=True)[:2]

def crossover(p1, p2):
    if random.random() < 0.8:
        point = random.randint(1, 5-1)
        return p1[:point] + p2[point:]
    return p1

def mutate(ch):
    ch = list(ch) # converted to list for ease
    for i in range(len(ch)):
        r = random.random() # number between 0 and 1
        if r < 0.05:
            if ch[i] == '0':
                ch[i] = '1'
            else:
                ch[i] = '0'

    return ''.join(ch) # convert back the list to string

print(population)

# GA loop
for _ in range(50):
    p1, p2 = select(population)

    new_pop = [p1, p2]

    while len(new_pop) < 6:
        child = crossover(p1, p2)
        child = mutate(child)
        new_pop.append(child)

    population = new_pop


print(population)

# best solution
best = max(population, key=lambda c: f(decode(c)))

print("Best Binary:", best)
print("x =", decode(best))
print("f(x) =", f(decode(best)))



#================================================================================
"""

BEGINNER QUESTION: Minimization Problem
Problem: Find the minimum value of f(x) = x² - 8x + 12 where x is integer between 0 and 15. Use 4-bit binary.

Parameters:
Population: 4 individuals
Selection: Tournament (size 3)
Crossover: Two-point crossover
Mutation: 0.1 per bit
Run for 100 generations
Hint: Since we're MINIMIZING, fitness should be lower = better

"""
import random

def f(x):
    return x**2 - 8*x + 12

population = [[random.randint(0,1) for _ in range(4)] for _ in range(4)]

def decode(ch):
    return int(ch, 2)

# minimization → convert to fitness
def fitness(x):
    return -f(x)

def select(pop):
    sample = random.sample(pop, 3)
    return min(sample, key=lambda c: f(decode(c)))

def crossover(p1, p2):
    if random.random() < 0.8:
        a = random.randint(1, 2)
        b = random.randint(2,3)
        if a>b :
            a,b = b,a
        return p1[:a] + p2[a:b] + p1[b:]
    return p1


# mutation
def mutate(ch):
    ch = list(ch)
    for i in range(len(ch)):
        if random.random() < 0.1:
            ch[i] = '1' if ch[i] == '0' else '0'
    return ''.join(ch)

# GA loop
for _ in range(100):

    new_pop = []

    while len(new_pop) < 4:
        p1 = select(population)
        p2 = select(population)

        child = crossover(p1, p2)
        child = mutate(child)

        new_pop.append(child)

    population = new_pop

# best solution
best = min(population, key=lambda c: f(decode(c)))

print("Best Binary:", best)
print("x =", decode(best))
print("f(x) =", f(decode(best)))
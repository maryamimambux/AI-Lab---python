import random

teachers = ["T1","T2","T3","T4","T5"]
courses = ["C1","C2","C3","C4","C5"]

POP_SIZE = 6
GENES = 25
GENERATIONS = 200

# ---------------------------
# Create random chromosome
# ---------------------------
def create_chromosome():
    return [(random.choice(teachers), random.choice(courses)) for _ in range(GENES)]

# ---------------------------
# Fitness Function
# ---------------------------
def fitness(chrom):
    penalty = 0

    # Constraint 1: Teacher clash (simplified)
    # (Here each slot is unique already → ignore clash between rooms)

    # Constraint 2: Each course exactly 3 times
    course_count = {c:0 for c in courses}
    for t,c in chrom:
        course_count[c] += 1

    for c in courses:
        penalty += abs(course_count[c] - 3) * 5

    # Constraint 3: No >3 consecutive classes per teacher
    for t in teachers:
        count = 0
        for gene in chrom:
            if gene[0] == t:
                count += 1
                if count > 3:
                    penalty += 8
            else:
                count = 0

    return 1 / (1 + penalty)

# ---------------------------
# Selection (Top 2)
# ---------------------------
def select(pop):
    return sorted(pop, key=lambda c: fitness(c), reverse=True)[:2]

# ---------------------------
# Crossover
# ---------------------------
def crossover(p1, p2):
    point = random.randint(1, GENES-1)
    return p1[:point] + p2[point:]

# ---------------------------
# Mutation
# ---------------------------
def mutate(chrom):
    for i in range(GENES):
        if random.random() < 0.1:
            chrom[i] = (random.choice(teachers), random.choice(courses))
    return chrom

# ---------------------------
# GA Execution
# ---------------------------
population = [create_chromosome() for _ in range(POP_SIZE)]

for gen in range(GENERATIONS):
    p1, p2 = select(population)

    child1 = mutate(crossover(p1, p2))
    child2 = mutate(crossover(p2, p1))

    population = [p1, p2, child1, child2] + population[:2]

# ---------------------------
# Best Solution
# ---------------------------
best = max(population, key=lambda c: fitness(c))

print("Best Timetable (first 10 slots shown):")
for i in range(10):
    print(best[i])

print("Fitness:", fitness(best))

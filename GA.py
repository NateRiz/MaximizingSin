from random import uniform, random, choice, seed
from math import sin
from matplotlib import pyplot as plt



def main():
    # ConstParameters
    POP_SIZE = 30
    MAX_GENS = 30

    population = [uniform(0, 30) for _ in range(POP_SIZE)]
    current_generation = 0

    while current_generation < MAX_GENS:
        current_generation += 1
        population = get_next_population(population)
        graph(population, current_generation)  # Show the graph every generation
        mutate(population)


def get_fitness(x):
    return pow(sin(1.2 * x), 3) - sin(x)


def get_next_population(population):
    next_gen = []
    while len(next_gen) < len(population) * 0.8:
        a, b = choice(population), choice(population)
        winner = max(a, b, key=lambda x: get_fitness(x))
        next_gen.append(winner)
    while len(next_gen) < len(population):
        next_gen.append(uniform(0, 30))
    return next_gen


def mutate(population):
    MUTATION_CHANCE = 0.2
    for i, p in enumerate(population):
        if random() < MUTATION_CHANCE:
            population[i] = clamp(p + uniform(-1, 1))


def clamp(x):
    if x < 0:
        return 0
    if x > 30:
        return 30
    return x

def graph(population, generation):
    x = [i/100 for i in range(3000)]
    y = [get_fitness(i) for i in x]

    fig = plt.figure()

    plt.plot(x, y)
    plt.scatter(population, [get_fitness(p) for p in population])
    plt.ylabel("Fitness")
    plt.xlabel("Individual")

    fig.savefig(F'plot{generation}.png')
    plt.close(fig)

if __name__ == "__main__":
    seed(1)
    main()

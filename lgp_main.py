import random
import sys

import initialization
import evaluation
import parent_select
import crossover
import mutation

def main():
    pop_size = 100
    tournament_size = 3
    xover_rate = 0.8
    evaluation_limit = 10000

    # initialize & evaluation
    evaluation_num = 0                          # initialize the generation counter
    population = initialization.init(pop_size)  # initialize population
    fitness = []                                # initialize fitness list
    for ind in population:                      # for each individual
        fitness.append(evaluation.fitness(ind)) # append fitness of individual
    print("generation", evaluation_num, ": best fitness", float(min(fitness)), "average fitness", float(sum(fitness)/len(fitness)))

    # main loop
    while evaluation_limit > evaluation_num:    # run for each evaluation
        # parent selection
        parent1, parent2, replacements = parent_select.tournament(fitness, tournament_size)                 # select parents and replacements
        
        # crossover
        offspring1, offspring2 = crossover.crossover(population[parent1], population[parent2], xover_rate)  # generate offspring

        # mutating offspring
        if random.random() <= 0.75:                             # 75% of the time macro mutate offspring 1
            offspring1 = mutation.macro_mutation(offspring1)
        else:                                                   # 25% of the time micro mutate offspring 1
            offspring1 = mutation.micro_mutation(offspring1)
        if random.random() <= 0.75:                             # 75% of the time macro mutate offspring 2
            offspring2 = mutation.macro_mutation(offspring2)
        else:                                                   # 25% of the time micro mutate offspring 2
            offspring2 = mutation.micro_mutation(offspring2)

        # survivor selection
        population[replacements[0]] = offspring1                        # swap offspring 1 in replacement 1 spot
        population[replacements[1]] = offspring2                        # swap offspring 2 in replacement 2 spot
        fitness[replacements[0]]    = evaluation.fitness(offspring1)    # add offspring 1 fitness to replacement 1 fitness spot
        evaluation_num = evaluation_num + 1 # add evaluation
        fitness[replacements[1]]    = evaluation.fitness(offspring2)    # add offspring 2 fitness to replacement 2 fitness spot
        evaluation_num = evaluation_num + 1 # add evaluation

        # print every 100 evaluations
        if evaluation_num % 100 == 0:
            print("generation", evaluation_num, ": best fitness", float(min(fitness)), "average fitness", float(sum(fitness)/len(fitness))) 

    # find best program
    top = sys.float_info.max
    best = -1
    for i in range(len(population)):
        if fitness[i] < top:
            top = fitness[i]
            best = population[i]
        if fitness[i] == top and len(evaluation.intron_remove(population[i])) < len(evaluation.intron_remove(best)):
            top = fitness[i]
            best = population[i]
    # only use the effective instructions
    best_effective = evaluation.intron_remove(best) 
    best_removed = []
    for inst in best_effective:
        best_removed.append(best[inst])
    # print final function
    print("best individual:", best_removed)
    print("best fitness:", evaluation.fitness(best))

main()
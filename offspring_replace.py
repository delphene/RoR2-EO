def offspring_replace(population, fitness, offspring, offspring_fitness, replacements):
    for i in range(len(replacements)):  # for each offspring
        population[replacements[i]] = offspring[i]      # replace replacement individual with offspring
        fitness[replacements[i]] = offspring_fitness[i] # replace fitness of replacement with fitness of offspring
        
    return population, fitness  # return new population and fitness
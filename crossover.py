import random

def crossover(parent1, parent2, xover_rate):
    point1 = random.randint(0, len(parent1)-1)  # choose first crossover point
                                                # choose second crossover point within 10 of the first
    point2 = random.randint((point1-10) if (point1-10) >= 0 else 0, (point1+10) if (point1+10) <= len(parent1)-1 else len(parent1)-1)

    if random.random() <= xover_rate:   # xover_rate % of the time offspring1 is crossover
        offspring1  = parent1[point1:] + parent2[:point1]   # crossover at first point
        if len(offspring1) > 50 or len(offspring1) < 5:     # if the new offspring1 is outside the bounds of an instruction
            offspring1 = parent1.copy() # offspring1 is copy of parent1
    else:                               # 1 - xover_rate % of the time offspring1 is copy of parent1
        offspring1 = parent1.copy()
    
    if random.random() <= xover_rate:   # xover_rate % of the time offspring1 is crossover
        offspring2  = parent1[point2:] + parent2[:point2]   # crossover at second point
        if len(offspring2) > 50 or len(offspring1) < 5:     # if the new offspring2 is outside the bounds of an instruction
            offspring2 = parent2.copy() # offspring2 is copy of parent2
    else:                               # 1 - xover_rate % of the time offspring2 is copy of parent2
        offspring2 = parent2.copy()
 
    return offspring1, offspring2       # return offspring
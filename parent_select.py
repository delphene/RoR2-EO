import random

def tournament(fitness, tournament_size):
    selection = random.sample(range(len(fitness)), 2*tournament_size)   # choose 2*tournament_size individuals from the population
    half = int(tournament_size)     # get the halfway point of the chosen individuals
    selection1 = selection[:half]   # selection for parent and replacement 1 from first half
    selection2 = selection[half:]   # selection for parent and replacement 2 from second half
    
    # best individual from each selection
    parent = [[selection1[0]],[selection2[0]]]
    fit_p = [fitness[selection1[0]],fitness[selection2[0]]]
    # worst individual from each selection
    replace = [[selection1[0]],[selection2[0]]]
    fit_r = [fitness[selection1[0]],fitness[selection2[0]]]
    for i in range(1, len(selection1)):
        # Check best first parent
        if fitness[selection1[i]] < fit_p[0]:
            parent[0] = [selection1[i]]
            fit_p[0] = fitness[selection1[i]]
        elif fitness[selection1[i]] == fit_p[0]:
            parent[0].append(selection1[i])
        # Check best second parent
        if fitness[selection2[i]] < fit_p[1]:
            parent[1] = [selection2[i]]
            fit_p[1] = fitness[selection2[i]]
        elif fitness[selection2[i]] == fit_p[1]:
            parent[1].append(selection2[i])
        # Check worst first replacement
        if fitness[selection1[i]] > fit_r[0]:
            replace[0] = [selection1[i]]
            fit_r[0] = fitness[selection1[i]]
        elif fitness[selection1[i]] == fit_r[0]:
            replace[0].append(selection1[i])
        # Check worst second replacement
        if fitness[selection2[i]] > fit_r[1]:
            replace[1] = [selection2[i]]
            fit_r[1] = fitness[selection2[i]]
        elif fitness[selection2[i]] == fit_r[1]:
            replace[1].append(selection2[i])
    
    # Set parent 1
    if len(parent[0]) > 1:
        parent1 = random.choice(parent[0])
    else:
        parent1 = parent[0][0]
    # Set parent 2
    if len(parent[1]) > 1:
        parent2 = random.choice(parent[1])
    else:
        parent2 = parent[1][0]
    # Set replacement 1
    if len(replace[0]) > 1:
        replacements = [random.choice(replace[0])]
    else:
        replacements = [replace[0][0]]
    # Set replacement 2
    if len(replace[1]) > 1:
        replacements.append(random.choice(replace[1]))
    else:
        replacements.append(replace[1][0])

    return parent1, parent2, replacements
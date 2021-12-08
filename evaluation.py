import sys

def fitness(individual):    # calculate the fitness of an individual
    efficient = intron_remove(individual)   # get list of efficient instructions
    if len(efficient) == 0:                 # if no efficient instructions
        return sys.float_info.max           # fitness is max
    fitness = 0                             # initialize fitness
    errors = []                             # initialize list of squared errors
    with open("trainingSamples.txt") as file:   # open training sample data
        for line in file:                       # for each training sample
            r1, r2, value = line.split("\t")    # set r1 as x1, r2 as x2 and value as the calculated value
            try:
                r1 = float(r1)          # convert r1 to float
                r2 = float(r2)          # convert r2 to float
                value = float(value)    # convert value to float
            except ValueError:          # ValueError if values are not floats (this will skip the first line)
                continue                # skip line
            r0 = r1 # initialize r0 as x1 (r1)
            r3 = r1 # initialize r3 as x1 (r1)
            r4 = r1 # initialize r4 as x1 (r1)
            r = {'r0':r0, 'r1':r1, 'r2':r2, 'r3':r3, 'r4':r4, '1':1, '2':2, '3':3, '4':4, '5':5}    # dictionary holds current values for access from instructions
            for inst in efficient:              # for each efficient instruction
                set = individual[inst][0]       # calculation variable is first value in instruction
                var1 = individual[inst][1]      # first variable is second value in instruction
                op = individual[inst][2]        # operand is third value in instruction
                var2 = individual[inst][3]      # second variable is fourth value in instruction
                if op == '+':                   # if the operation is +
                    r[set] = r[var1] + r[var2]  # complete instruction
                elif op == '-':                 # if the operation is -
                    r[set] = r[var1] - r[var2]  # complete instruction
                elif op == '*':                 # if the operation is *
                    r[set] = r[var1] * r[var2]  # complete instruction
                elif op == '%':                 # if the operation is %
                    if r[var2] != 0:            # if not dividing by 0
                        r[set] = r[var1] % r[var2]  # complete instruction
                    else:
                        r[set] = 0
            
            errors.append((value-r[set])**2)   # append the error squared

    fitness = sum(errors)   # fitness is sum of errors
    return round(fitness,2) # return fitness

def intron_remove(individual):  # find the effective instructions in an individual
    # find the final time r0 (output regester) is set. the final instruction
    cut = -1        # initialize cut point is -1
    for i in range(len(individual)-1,-1,-1):    # for each instruction starting from the last
        if individual[i][0] == "r0":            # if the instruction is setting r0 (the output regester)
            cut = i # set the cut point to the current i
            break   # stop checking
    if cut == -1:   # if the cut point wasnt found
        return []   # return empty list
    
    variables = {"r0","r3","r4"}    # variables
    in_use = set()                  # variables that will be used in effective instructions
    if individual[cut][1] in variables: # add the first value of the final instruction if it is a variable 
        in_use.add(individual[cut][1])
    if individual[cut][3] in variables: # add the second value of the final instruction if it is a variable 
        in_use.add(individual[cut][3])
    
    efficient = [cut]   # add the final instruction to list of efficient instructions
    for i in range(cut-1,-1,-1):                # loop throught instructions from the final instruction to the first
        if individual[i][0] in in_use:          # if this register will be used in the future
            efficient.append(i)                 # append the instruction index to efficient instructions
            in_use.remove(individual[i][0])     # remove the set regester from in_use
            if individual[i][1] in variables:   # if the first value is a variable
                in_use.add(individual[i][1])    # add this to in_use (the value of this matters)
            if individual[i][3] in variables:   # if the second value is a variable
                in_use.add(individual[i][3])    # add this to in_use (the value of this matters)
                
    efficient.reverse() # reverse the list
    return efficient    # return the list
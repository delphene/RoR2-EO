import random

def macro_mutation(offspring):
    # macro mutation: remove instruction or insert new instruction
                                                    # delete 50% of the time, if the length is 50 always delete, only delete if length is greater than 5 else insert
    if (random.random() <= 0.5 or len(offspring) > 49) and len(offspring) > 5:
        inst = random.randint(0,len(offspring)-1)   # choose random index (instruction) from offspring
        del offspring[inst]                         # delete the instruction
    else:                       # insert 50% of the time
        point = random.randint(0,len(offspring))    # choose insertion point
                                                    # create random instruction
        inst = [random.choice(['r0','r3','r4']), random.choice(['r0','r3','r4','r1','r2']), random.choice(['+','-','*','%']), random.choice(['r0','r3','r4','r1','r2','1','2','3','4','5'])]
        if point < len(offspring):                  # if the point is within the offspring, insert new instruction
            offspring.insert(point,inst)
        else:                                       # if the point is at the end of the offspring, append the new instruction 
            offspring.append(inst)

    return offspring    # return mutated offspring
    
def micro_mutation(offspring):
    # micro mutation: change one element (register or operator)
    inst = random.randint(0,len(offspring)-1)   # choose random instruction from offspring
    mutated = random.randint(0,3)               # choose which variable to change
    if mutated == 0:                            # mutate the calculation regester
        set = ['r0','r3','r4']                  # set of all regesters
        set.remove(offspring[inst][mutated])    # remove the current regester from the choices (dont want to mutate to the same regester)
        new_inst = offspring[inst].copy()       # copy current instruction
        new_inst[mutated] = random.choice(set)  # set the regester to a new value
        offspring[inst] = new_inst              # set the instruction to the new instruction
    elif mutated == 1:
        regs = ['r0','r1','r2','r3','r4']
        regs.remove(offspring[inst][mutated])
        new_inst = offspring[inst].copy()
        new_inst[mutated] = random.choice(regs)
        offspring[inst] = new_inst
    elif mutated == 2:
        ops = ['+','-','*','%']
        ops.remove(offspring[inst][mutated])
        new_inst = offspring[inst].copy()
        new_inst[mutated] = random.choice(ops)
        offspring[inst] = new_inst
    elif mutated == 3:
        if offspring[inst][1] in {'r0','r3','r4'}:  # if the first variable is a calculation regester
            vars = ['1','2','3','4','5','r1','r2']  # new variable does not include the calculation regesters
        else:                                       # if the first variable is an input regester
            vars = ['1','2','3','4','5','r0','r1','r2','r3','r4']   # new variable can be any value
        if offspring[inst][mutated] in vars:
            vars.remove(offspring[inst][mutated])
        new_inst = offspring[inst].copy()
        new_inst[mutated] = random.choice(vars)
        offspring[inst] = new_inst
    
    return offspring
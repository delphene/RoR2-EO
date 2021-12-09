import random
import math
from globals import *

class Player():
    def __init__(self, stats, values):
        # STATS
        # self.health = 90
        # self.damage = 12
        # self.regen = 1
        # self.armor = 0
        # self.speed = 7
        
        self.health = stats['health']
        self.damage = stats['damage']
        self.regen = stats['regen']
        self.armor = stats['armor']
        self.speed = stats['speed']

        # OPTIMIZER
        self.values = values

        # FITNESS
        self.fitness = -1
    
    def evaluate(self, individual, init_diff, total_stages):
        '''
        each individual will have tiers of items, though each set of stages the player will get a portion of the items from the respective teir
        choices are made based on inherited properties (clear %, open chests, use shrine of combat)
        '''
        # stat copies
        health = self.health
        damage = self.damage
        regen = self.regen
        armor = self.armor
        speed = self.speed
        # initial difficulty changes
        if init_diff == 'drizzle':
            regen_mult = 1.5
            self.armor += 70
        elif init_diff == 'monsoon':
            regen_mult = 0.6
        # coeff values
        diff_values = {'drizzle':1, 'rainstorm':2, 'monsoon':3}
        time_factor = 0.0506 * diff_values[init_diff]
        # initialize
        stage = 1
        time = 0
        
        # MAIN LOOP
        while stage < total_stages+1:
            # The only exception to this rule is the first stage, which always has a monster credit amount of 0.

            # reset values
            money = 0
            activated_mountain_shrines = 0

            # SET VALUES 
            map = random.sample(STAGES[stage])[0]                               # choose map
            stage_factor = 1.15**stage
            coeff = (time * time_factor) * stage_factor                         # calculate coeff
            enemy_level = 1 + (coeff)/0.33                                      # effect on enemy level
            money_cost = coeff**1.25                                            # effect on money cost
            # enemy_xp_reward = coeff * monster_value * reward_multiplier         # effect on enemy xp reward
            # enemy_gold_reward = 2 * coeff * monster_value * reward_multiplier   # effect on enemy reward
            shrine_director_credits = 100 * coeff                               # shrine of combat income coeff

            # spawning interactables
            interactables_credits = SCENE_DIRECTOR[map]['Interactables']
            while interactables_credits > 0:
                # choose and spawn interactable
            # spawning monsters
            monsters_credits = SCENE_DIRECTOR[map]['Monsters']
            monsters = []
            monster_num = 0
            while monsters_credits >= 8 and monster_num < 40: # can never be elite or too cheap
                monsters.append()
                monster_num += 1
            
            # maybe values on the equipment optimize time % per stage, 

            # MAIN
            fast_director_credits = 0
            fast_director_spawn = 0.0
            slow_director_credits = 0
            slow_director_spawn = 0.0
            completion_time = 0.0       # seconds
            completion = 0.0            # percent
            fast_monster = None         # choice of monster card
            while completion <= self.values[stage]: # if the completion % chosen by the agent is reached
                # Update values
                coeff = (time * time_factor) * stage_factor # calculate coeff
                fast_director_credits += 0.75 * (1 + 0.4*coeff) # * (player_count + 1)/2
                slow_director_credits += 0.75 * (1 + 0.4*coeff) # * (player_count + 1)/2
                enemy_level = 1 + (coeff)/0.33              # effect on enemy level
                money_cost = coeff**1.25                    # effect on money cost
                
                # Check the timer fast
                if fast_director_spawn <= 0:
                    # Check for overcrowding
                    if monsters < 40:   # Success
                        # Prepare a wave
                        # if spawn card and no fail
                            # prepare wave with that card
                        # elif no card or fail
                            # select spawn card         # how???
                            fast_monster = random.sample(MONSTER_SPAWN_CARD)
                            while fast_monster[0] == 'Champions':
                                fast_monster = random.sample(MONSTER_SPAWN_CARD)
                        # determine elite tier # the highest available tier that can be afforded
                        # if chosen tier is above 0
                            # pick random affix
                        # fast_spawn_counter = 0
                    else:               # Fail
                        # Spawn
                        if fast_spawn_counter < 6 and conditions and cost <= fast_director_credits and not (fast_director_credits < 6 * cost and max(ELITE_MULTIPLIERS) * cost < 72000):
                            # Prepare the spawn
                            if fast_director_credits >= min(ELITE_MULTIPLIERS) * cost:          # if the director can afford the lowest elite type
                                if fast_director_credits >= max(ELITE_MULTIPLIERS) * cost:      # if the director can also afford the highest elite type then get a high elite
                                    fast_director_credits -= max(ELITE_MULTIPLIERS) * cost                                                                      # spend credits
                                    elite = random.sample(ELITE_MULTIPLIERS[min(ELITE_MULTIPLIERS)])                                                            # choose elite type
                                    monsters.append(elite['Health'] * [MONSTERS[fast_monster]['Health'], elite['Damage'] * MONSTERS[fast_monster]['Damage'], reward, xpreward])   # add monster with elite multipliers
                                else:                                                           # if the director can not afford the highest elite type then get a low elite
                                    fast_director_credits -= min(ELITE_MULTIPLIERS) * cost                                                                      # spend credits
                                    elite = random.sample(ELITE_MULTIPLIERS[min(ELITE_MULTIPLIERS)])                                                            # choose elite type
                                    monsters.append(elite['Health'] * [MONSTERS[fast_monster]['Health'], elite['Damage'] * MONSTERS[fast_monster]['Damage'], reward, xpreward])   # add monster with elite multipliers
                            else:                                                               # if the director can no afford the lowest elite type then get a normal monster
                                # spawn normal
                                fast_director_credits -= cost                                                           # spend credits
                                monsters.append([MONSTERS[fast_monster]['Health'], MONSTERS[fast_monster]['Damage'], reward, xpreward])   # add monster
                        # else: skip and no spend credits
                    fast_director_spawn = random.uniform(completion_time+4.5,completion_time+9.0)   # choose new wave timer
                


                if slow_director_spawn <= 0:
                    if monsters < 40:
                        # spawn monster
                    else:
                        # prepare wave
                    slow_director_spawn = random.uniform(completion_time+22.5,completion_time+30.0)

                # spawn barrels and give completion% of gold to player
                # cloaked_chest
                # rusty_lockbox

                # if the player dies end run
                if health <= 0:
                    break

                completion_time += 0.5
                fast_director_spawn -= 0.5
                slow_director_spawn -= 0.5

            # BOSS
            boss_time = 0
            teleporter_boss_director_credits = 600 * math.sqrt(coeff) * (1 + activated_mountain_shrines)
            teleporter_director_credits = 0

            # Whenever a Combat Director deactivates, it transfers 40% of its remaining credits to another random active Director and discards the rest.
            if random.random() > 50:
                teleporter_director_credits += 0.4 * fast_director_credits
            else:
                teleporter_boss_director_credits += 0.4 * fast_director_credits
            if random.random() > 50:
                teleporter_director_credits += 0.4 * slow_director_credits
            else:
                teleporter_boss_director_credits += 0.4 * slow_director_credits

            # cant spawn stone golemns
            if random.random() > 0.1:   # decrease health based on the number of "Armor-Piercing Rounds" the player has
                #spawn horde
            else:
                #spawn boss

            while boss_health > 0:
                coeff = (time * time_factor) * stage_factor
                teleporter_director_credits += 2 * (1 + 0.4*coeff) # * (player_count + 1)/2
                # if the player dies end run
                if health <= 0:
                    break
                time += boss_time

            mobs = teleporter_director.mobs             # list of mobs during charging

            # time += completion_time + boss_time + charge_time
            stage += 1

        return fitness
import random
from evaluation import Player

def init(pop_size, total_stages):
    white       =   ['Armor-Piercing Rounds','Backup Magazine','Bison Steak','Bundle of Fireworks','Bustling Fungus','Cautious Slug','Crowbar','Energy Drink',
                    'Focus Crystal','Gasoline','Lens-Maker\'s Glasses', 'Medkit','Monster Tooth','Paul\'s Goat Hoof','Personal Shield Generator',   
                    'Repulsion Armor Plate','Rusted Key','Soldier\s Syringe','Sticky Bomb','Stun Grenade','Topaz Brooch','Tougher Times','Tri-tip Dagger','Warbanner']
    green       =   ['AtG Missile Mk. 1','Bandoiler','Berzerker\'s Pauldron','Chronobauble','Death Mark','Fuel Cell','Ghor\'s Tome','Harvester\'s Scythe',
                    'Hopoo Feather','Infusion','Kjaro\'s Band','Leeching Seed','Lepton Daisy','Old Guillotine','Old War Stealthkit','Predatory Instincts',  
                    'Razorwire','Red Whip','Rose Buckler','Runald\'s Band','Squid Polyp','Ukulele','War Horn','Wax Quail','Will-o\'-the-whisp']
    red         =   ['57 Leaf Clover','Aegis','Alien Head','Brainstalks','Brilliant Behemoth','Ceremonial Dagger','Defensive Microbots','Dio\'s Best Friend', 
                    'Frost Relic','H3AD-5T v2', 'Happiest Mask','Hardlight Afterburner', 'Interstellar Desk Plant','N\'kuhana\'s Opinion','Rejuvenation Rack', 
                    'Resonance Disc','Sentient Meat Hook','Shattering Justice','Soulbound Catalyst','Unstable Tesla Coil','Wake of Vultures']
    yellow      =   ['Artifact Key','Charged Perforator','Empathy Cores','Genisis Loop','Halcyon Seed','Irradiant Pearl','Little Disciple','Mired Urn',
                    'Molten Perforator','Pearl','Planula','Queen\'s Gland','Shatterspleen','Titanic Knurl']
    equipment   =   ['Blast Shower','Disposable Missile Launcher','Eccentric Vase','Foreign Fruit','Forgive Me Please','Fuel Array','Gnarled Woodsprite','Gorag\'s Opus',
                    'Jade Elephant','Milky Chrysalis','Ocular HUD','Preon Accumulator','Primordial Cube','Radar Scanner','Recycler','Royal Capacitor','Sawmerang',
                    'Super Massive Leech','The Back-up','The Crowdfunder','Volcanic Egg']
    chests      =   ['Small Chest','large','Legendary Chest','Equipment Barrel','Multishop Terminal White','Multishop Terminal (Green)',
                    'Equipment Triple Shop','Damage Chest','Healing Chest','Utility Chest','Adaptive Chest']
    shrines     =   ['Shrine of Blood','Shrine of the Mountain','Shrine of Combat','Shrine of the Woods','Altar of Gold','Shrine of Chance']
    # drones      =   ?

    items = white + green + red + yellow + equipment
    
    population  =   []
    
    for _ in range(pop_size):   # create individual pop_size number of times

        values = {}
        for item in items:
            values[item] = random.random()

        for chest in chests:
            values[chest] = random.random()

        for stage in range(total_stages):
            values[stage] = random.random()

        for shrine in shrines:
            values[shrine] = random.random()

        population.append(Player(values))  # append individual to population

    return population   # return population
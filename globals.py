MAP =   {   'Distant Roost'         :{'Chests':45,'Barrels':10,'Shrines':10,'Rare':0.4,'Basic Monsters':4,'Minibosses':2,'Champions':2},
            'Titanic Plains'        :{'Chests':45,'Barrels':10,'Shrines':10,'Rare':0.4,'Basic Monsters':4,'Minibosses':2,'Champions':2},
            'Wetland Aspect'        :{'Chests':45,'Barrels':10,'Shrines':10,'Rare':0.4,'Basic Monsters':4,'Minibosses':2,'Champions':2},
            'Abandoned Aqueduct'    :{'Chests':45,'Barrels':10,'Shrines':8 ,'Rare':0.4,'Basic Monsters':3,'Minibosses':2,'Champions':2},
            'Rallypoint Delta'      :{'Chests':45,'Barrels':10,'Shrines':7 ,'Rare':0.4,'Basic Monsters':3,'Minibosses':3,'Champions':2},
            'Scorched Acres'        :{'Chests':45,'Barrels':10,'Shrines':7 ,'Rare':0.4,'Basic Monsters':3,'Minibosses':3,'Champions':2},
            'Abyssal Depths'        :{'Chests':45,'Barrels':10,'Shrines':10,'Rare':0.4,'Basic Monsters':3,'Minibosses':2,'Champions':2},
            'Siren\'s Call'         :{'Chests':45,'Barrels':10,'Shrines':10,'Rare':0.4,'Basic Monsters':4,'Minibosses':2,'Champions':2},
            'Sky Meadow'            :{'Chests':45,'Barrels':10,'Shrines':10,'Rare':0.4,'Basic Monsters':3,'Minibosses':2,'Champions':2},
            'Guilded Coast'         :{'Basic Monsters':3,'Minibosses':3,'Champions':2},

            'Sundered Grove'        :{'Chests':45,'Barrels':10,'Shrines':10,'Rare':0.4,'Basic Monsters':4,'Minibosses':2,'Champions':2} # not in data
        }

STAGES =    {   1:{'Distant Roost', 'Titanic Plains'}, 
                2:{'Abandoned Aqueduct', 'Wetland Aspect'},
                3:{'Rallypoint Delta', 'Scorched Acres'},
                4:{'Abyssal Depths', 'Siren\'s Call', 'Sundered Grove'},
                5:{'Sky Meadow'},
                10:{'Gilded Coast', 'Bulwark\'s Ambry'}
            }

SCENE_DIRECTOR =    {   'Distant Roost'         :{'Interactables':180,'Monsters':100},
                        'Titanic Plains'        :{'Interactables':220,'Monsters':100},
                        'Wetland Aspect'        :{'Interactables':280,'Monsters':100},
                        'Abandoned Aqueduct'    :{'Interactables':220,'Monsters':100},
                        'Rallypoint Delta'      :{'Interactables':280,'Monsters':100},
                        'Scorched Acres'        :{'Interactables':280,'Monsters':100},
                        # Note that whenever the "vault" of Abyssal Depths is open, the Scene Director is granted 160 additional interactable credits. 
                        'Abyssal Depths'        :{'Interactables':400,'Monsters':230},
                        'Siren\'s Call'         :{'Interactables':400,'Monsters':230},
                        'Sky Meadow'            :{'Interactables':520,'Monsters':300},
                        'Guilded Coast'         :{'Interactables':0  ,'Monsters':200},

                        'Sundered Grove'        :{'Interactables':180,'Monsters':100}   # not in data
                    }

# ELITE_MULTIPLIERS = {   'Blazing'       :{'cost':6 ,'health':4 ,'damage':2},
#                         'Overloading'   :{'cost':6 ,'health':4 ,'damage':2},
#                         'Glacial'       :{'cost':6 ,'health':4 ,'damage':2},
#                         'Malachite'     :{'cost':36,'health':18,'damage':6}, # Stage 5 and on
#                         'Celestine'     :{'cost':36,'health':18,'damage':6}, # Stage 5 and on
#                     }

ELITE_MULTIPLIERS = {   6   :{{'type':'Blazing','health':4 ,'damage':2}, {'type':'Overloading','health':4 ,'damage':2}, {'type':'Glacial','health':4 ,'damage':2}},
                        36  :{{'type':'Malachite','health':18,'damage':6}, {'type':'Celestine','health':18,'damage':6}} # Stage 5 and on
                    }

CHEST_SPAWN_CARD = {    'Barrel'                        : ['Barrel',1, 10,{}],
                        'Small Chest'                   : ['Chests',15,24,{}],
                        'Damage Chest'                  : ['Chests',15,2, {}],
                        'Healing Chest'                 : ['Chests',15,2, {}],
                        'Utility Chest'                 : ['Chests',15,2, {}],
                        'Large Chest'                   : ['Chests',30,4, {'stage':4}],
                        'Adaptive Chest'                : ['Chests',20,1, {'map':{'Rallypoint Delta', 'Scorched Acres', 'Siren\'s Call', 'Sundered Grove', 'Abyssal Depths'}}],
                        'Legendary Chest'               : ['Rare'  ,50,2, {}],
                        'Equipment Barrel'              : ['Chests',1, 2, {}],
                        'Multishop Terminal White'      : ['Chests',20,8, {'map':{'Bulwark\'s Ambry', 'Distant Roost', 'Titanic Plains', 'Wetland Aspect', 'Abandoned Aqueduct', 'Rallypoint Delta', 'Scorched Acres'}}], 
                        'Multishop Terminal (Green) 1'  : ['Chests',40,1, {'map':{'Wetland Aspect', 'Abandoned Aqueduct'}}],
                        'Multishop Terminal (Green) 4'  : ['Chests',40,4, {'map':{'Abyssal Depths', 'Siren\'s Call', 'Sundered Grove', 'Sky Meadow'}}],
                        'Equipment Triple Shop'         : ['Chests',2, 2, {'map':{'Scorched Acres', 'Sky Meadow'}}],
                        'Cloaked Chest'                 : ['Rare'  ,10,6, {}],
                        'Lunar Pod 1'                   : ['Chests',25,1,{'map':{'Distant Roost', 'Abandoned Aqueduct', 'Rallypoint Delta', 'Scorched Acres', 'Abyssal Depths', 'Siren\'s Call', 'Sky Meadow', 'Wetland Aspect', 'Sundered Grove'}}],
                        'Lunar Pod 2'                   : ['Chests',25,2,{'map':{'Titanic Plains'}}]
                    }

DRONE_SPAWN_CARD =  {   'Gunner Drone 2'        : ['Drones',15,2,{'map':{}}],
                        'Gunner Drone 7'        : ['Drones',15,7,{'map':{}}],
                        'Healing Drone'         : ['Drones',15,7,{'map':{}}],
                        'Missile Drone 3'       : ['Drones',20,3,{'map':{}}],
                        'Missile Drone 7'       : ['Drones',20,7,{'map':{}}],
                        'Incinerator Drone 1'   : ['Drones',30,1,{'map':{}}],
                        'Incinerator Drone 2'   : ['Drones',30,2,{'map':{}}],
                        'Equipment Drone'       : ['Drones',15,2,{'map':{}}],
                        'Emergency Drone'       : ['Drones',30,2,{'map':{}}],
                        'TC-280 Drone'          : ['Drones',40,1,{'map':{}}],
                        'Gunner Turret'         : ['Misc',  10,7,{'map':{}}],
                        'Radio Scanner'         : ['Rare',  1 ,2,{'map':{'Sky Meadow','Sundered Grove','Abyssal Depths','Siren\'s Call','Scorched Acres','Rallypoint Delta','Wetland Aspect','Abandoned Aqueduct','Titanic Plains','Distant Roost'}}]
                    }

PRINTER_SPAWN_CARD =    {   'Scrapper'                  : ['Printers',5,2,{'map':{}}],
                            '3D Printer (White)'        : ['Printers',5,2,{'map':{}}],
                            '3D Printer (Green)'        : ['Printers',10,2,{'map':{}}],
                            'Mili-Tech Printer'         : ['Printers',15,2,{'map':{}}],
                            '3D Printer (Overgrown)'    : ['Printers',10,2,{'map':{}}]
                        }

SHRINE_SPAWN_CARD = {   'Shrine of Blood 3'         : ['Shrines',20,3, {'map':{'Bulwark\'s Ambry','Distant Roost','Rallypoint Delta','Abandoned Aqueduct'}}],
                        'Shrine of Blood  30'       : ['Shrines',20,30,{'map':{'Wetland Aspect','Siren\'s Call','Scorched Acres'}}],
                        'Shrine of Chance 4'        : ['Shrines',20,4, {'map':{'Bulwark\'s Ambry','Distant Roost','Abyssal Depths','Rallypoint Delta','Titanic Plains','Abandoned Aqueduct','Sundered Grove','Sky Meadow'}}],
                        'Shrine of Chance 40'       : ['Shrines',20,40,{'map':{'Wetland Aspect','Scorched Acres'}}],
                        'Shrine of Combat 2'        : ['Shrines',20,2, {'map':{'Abandoned Aqueduct','Rallypoint Delta'}}],
                        'Shrine of Combat 3'        : ['Shrines',20,3, {'map':{'Titanic Plains','Abyssal Depths', 'Sundered Grove', 'Sky Meadow'}}],
                        'Shrine of Order'           : ['Shrines',30,1, {'map':{'Rallypoint Delta'}}],
                        'Altar of Gold'             : ['Rare'   ,1, 2, {}],
                        'Shrine of the Mountain 1'  : ['Shrines',20,1, {'map':{'Distant Roost','Titanic Plains','Abandoned Aqueduct','Abyssal Depths','Sky Meadow'}}],
                        'Shrine of the Mountain 10' : ['Shrines',20,10,{'map':{'Wetland Aspect','Siren\'s Call'}}],
                        'Shrine of the Woods 2'     : ['Shrines',15,2, {'map':{'Bulwark\'s Ambry','Distant Roost'}}],
                        'Shrine of the Woods 10'    : ['Shrines',15,10,{'map':{'Scorched Acres'}}],
                        'Shrine of the Woods 20'    : ['Shrines',15,20,{'map':{'Siren\'s Call'}}],
                        'Cleansing Pool'            : ['Shrines',5 ,3 ,{'map':{'Wetland Aspect', 'Scorched Acres', 'Siren\'s Call'}}]
                    }

MONSTER_SPAWN_CARD =    {   'Alloy Vulture'     : ['Basic Monster',28,1,  {'map':{'Scorched Acres', 'Siren\'s Call'}}],
                            'Beetle'            : ['Basic Monster',8, 1,  {'map':{'Distant Roost', 'Titanic Plains', 'Wetland Aspect', 'Abandoned Aqueduct', 'Scorched Acres', 'Siren\'s Call'}}],
                            'Hermit Crab'       : ['Basic Monster',25,0.5,{'stage':{2},'map':{'Titanic Plains', 'Abyssal Depths'}}],
                            'Imp'               : ['Basic Monster',28,1,  {'map':{'Rallypoint Delta', 'Scorched Acres', 'Abyssal Depths'}}],
                            'Jellyfish'         : ['Basic Monster',10,1,  {'map':{'Distant Roost', 'Titanic Plains', 'Wetland Aspect', 'Siren\'s Call', 'Bulwark\'s Ambry'}}],
                            'Lemurian'          : ['Basic Monster',11,1,  {'map':{'Distant Roost', 'Titanic Plains', 'Wetland Aspect', 'Abandoned Aqueduct', 'Rallypoint Delta', 'Abyssal Depths', 'Gilded Coast', 'Bulwark\'s Ambry'}}],
                            'Lesser Wisp'       : ['Basic Monster',10,1,  {'map':{'Distant Roost', 'Titanic Plains', 'Wetland Aspect', 'Abandoned Aqueduct', 'Rallypoint Delta', 'Scorched Acres', 'Sky Meadow', 'Bulwark\'s Ambry'}}],
                            'Mini Mushrum'      : ['Basic Monster',40,1,  {'map':{'Sky Meadow'}}],

                            'Beetle Guard'      : ['Minibosses',40, 1,{'map':{'Abandoned Aqueduct', 'Scorched Acres'}}],
                            'Bighorn Bison'     : ['Minibosses',40, 1,{'map':{'Rallypoint Delta'}}],
                            'Brass Contraption' : ['Minibosses',60, 1,{'map':{'Wetland Aspect', 'Abyssal Depths', 'Siren\'s Call', 'Sky Meadow'}}],
                            'Clay Templar 115'  : ['Minibosses',115,1,{'map':{'Scorched Acres'}}],
                            'Clay Templar 160'  : ['Minibosses',160,1,{'map':{'Abandoned Aqueduct'}}],
                            'Elder Lemurian 115': ['Minibosses',115,1,{'map':{'Abyssal Depths', 'Siren\'s Call', 'Sky Meadow', 'Bulwark\'s Ambry'}}],
                            'Elder Lemurian 230': ['Minibosses',230,1,{'map':{'Gilded Coast'}}],
                            'Greater Wisp'      : ['Minibosses',200,1,{'map':{'Distant Roost', 'Titanic Plains', 'Abandoned Aqueduct', 'Rallypoint Delta', 'Scorched Acres', 'Abyssal Depths', 'Siren\'s Call', 'Sky Meadow', 'Gilded Coast'}}],
                            'Parent'            : ['Minibosses',100,1,{'map':{'Sky Meadow'}}],
                            'Stone Golem 30'    : ['Minibosses',30, 1,{'map':{'Gilded Coast'}}],
                            'Stone Golem 40'    : ['Minibosses',40, 1,{'map':{'Distant Roost', 'Titanic Plains', 'Wetland Aspect', 'Rallypoint Delta', 'Bulwark\'s Ambry'}}],
                            'Void Reaver'       : ['Minibosses',300,1,{'map':{'Rallypoint Delta', 'Siren\'s Call', 'Sky Meadow'}}],

                            'Beetle Queen'      : ['Champions',600, 1,{'map':{'Distant Roost', 'Titanic Plains', 'Wetland Aspect', 'Abandoned Aqueduct'}}],
                            'Clay Dunestrider'  : ['Champions',600, 1,{'map':{'Abandoned Aqueduct', 'Rallypoint Delta', 'Scorched Acres'}}],
                            'Grovetender'       : ['Champions',800, 1,{'map':{'Scorched Acres'}}],
                            'Imp Overlord'      : ['Champions',800, 1,{'map':{'Rallypoint Delta', 'Scorched Acres', 'Abyssal Depths'}}],
                            'Magma Worm'        : ['Champions',800, 1,{'map':{'Rallypoint Delta', 'Abyssal Depths', 'Siren\'s Call', 'Sky Meadow', 'Bulwark\'s Ambry'}}],
                            'Overloading Worm'  : ['Champions',4000,1,{'map':{'Rallypoint Delta', 'Abyssal Depths', 'Sky Meadow', 'Bulwark\'s Ambry'}}],
                            'Scavenger'         : ['Champions',2000,1,{'map':{'Bulwark\'s Ambry','Sky Meadow','Sundered Grove','Abyssal Depths','Siren\'s Call','Scorched Acres','Rallypoint Delta','Wetland Aspect','Abandoned Aqueduct','Titanic Plains','Distant Roost'}}],
                            'Solus Control Unit': ['Champions',800, 1,{'map':{'Siren\'s Call', 'Sky Meadow'}}],
                            'Stone Titan 500'   : ['Champions',500, 1,{'map':{'Gilded Coast'}}],
                            'Stone Titan 600'   : ['Champions',600, 1,{'map':{'Bulwark\'s Ambry','Distant Roost', 'Titanic Plains', 'Wetland Aspect', 'Abandoned Aqueduct', 'Abyssal Depths'}}],
                            'Wandering Vagrant' : ['Champions',600, 1,{'map':{'Distant Roost', 'Titanic Plains', 'Wetland Aspect', 'Siren\'s Call', 'Bulwark\'s Ambry'}}]
                        }

MONSTERS =  {   'Alloy Vulture'     : {'Health':140 ,'Damage':15},
                'Beetle'            : {'Health':80  ,'Damage':12},
                'Hermit Crab'       : {'Health':100 ,'Damage':12},
                'Imp'               : {'Health':140 ,'Damage':10},
                'Jellyfish'         : {'Health':60  ,'Damage':5},
                'Lemurian'          : {'Health':80  ,'Damage':12},
                'Lesser Wisp'       : {'Health':35  ,'Damage':3.5},
                'Mini Mushrum'      : {'Health':290 ,'Damage':16},

                'Beetle Guard'      : {'Health':480 ,'Damage':12},
                'Bighorn Bison'     : {'Health':480 ,'Damage':12},
                'Brass Contraption' : {'Health':300 ,'Damage':10},
                'Clay Templar'      : {'Health':700 ,'Damage':16},
                'Elder Lemurian'    : {'Health':900 ,'Damage':16},
                'Greater Wisp'      : {'Health':750 ,'Damage':13},
                'Parent'            : {'Health':585 ,'Damage':16},
                'Stone Golem'       : {'Health':480 ,'Damage':20},
                'Void Reaver'       : {'Health':1900 ,'Damage':12},

                'Beetle Queen'      : {'Health':2100 ,'Damage':25},
                'Clay Dunestrider'  : {'Health':2100 ,'Damage':20},
                'Grovetender'       : {'Health':2800 ,'Damage':23},
                'Imp Overlord'      : {'Health':2800 ,'Damage':16},
                'Magma Worm'        : {'Health':2400 ,'Damage':10},
                'Overloading Worm'  : {'Health':12000 ,'Damage':50},
                'Scavenger'         : {'Health':3800 ,'Damage':4},
                'Solus Control Unit': {'Health':2500 ,'Damage':15},
                'Stone Titan'       : {'Health':2100 ,'Damage':40},
                'Wandering Vagrant' : {'Health':2100 ,'Damage':6.5}
            }
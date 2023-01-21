
adjacent_areas = {
    'Apple Orchard': ['Town 1'],
    'Town 1': ['Apple Orchard', 'Farm', 'Forest Outskirts'],
    'Farm': ['Town 1', 'Wolf Den I', 'Beach I'],
    'Forest Outskirts': ['Town 1', 'Forest I', 'Boat 1'],

    'Forest I': ['Forest Outskirts', 'Forest II'],
    'Forest II': ['Forest I', 'Forest III', 'Witch Hut'],
    'Forest III': ['Forest II'],

    'Wolf Den I': ['Farm', 'Wolf Den II'],
    'Wolf Den II': ['Wolf Den I', 'Wolf Den III'],
    'Wolf Den III': ['Wolf Den II'],

    'Beach I': ['Farm', 'Beach II', 'Krakow\'s Cave'],
    'Beach II': ['Beach I', 'Beach III'],
    'Beach III': ['Beach II'],

    'Witch Hut': ['Forest II'],
    'Krakow\'s Cave': ['Beach I'],
    'Boat 1': ['Forest Outskirts'],
}

emojis = {
    'Apple Orchard': '🍎',
    'Town 1': '🏠',
    'Farm': '🌾',
    'Forest Outskirts': '🏞️',
    'Forest I': '🌲',
    'Forest II': '🌲',
    'Forest III': '🌲',
    'Wolf Den I': '🐺',
    'Wolf Den II': '🐺',
    'Wolf Den III': '🐺',
    'Beach I': '🏖️',
    'Beach II': '🏖️',
    'Beach III': '🏖️',
    'Boat 1': '⛵️',
    'Krakow\'s Cave': '🏛',
    'Witch Hut': ':hut:',
}
boosts = {
    'shiny elixir': {"stats": [['XP', 25]], "time": 60},
    'lucky elixir': {"stats": [['LOOT', 25]], "time": 60},

    'red elixir': {"stats": [['DMG', 5]], "time": 20},
    'gray elixir': {"stats": [['DEF', 5]], "time": 20},
    'green elixir': {"stats": [['HP', 10]], "time": 20},
    'blue elixir': {"stats": [['MP', 10]], "time": 20},

    'knight elixir': {"stats": [['%.CRIT.DMG', 10], ['%.CRIT', 5]], "time": 30},
    'mage elixir': {"stats": [['%.SPELL.DMG', 10], ['%.SPELL.COST', 30]], "time": 30},
    'brawler elixir': {"stats": [['DEF', 10], ['MAX HP', 15]], "time": 30},
    'bard elixir': {"stats": [['HEAL', 20], ['MAX MP', 15]], "time": 30},
}
heals = {
    'crystal apple': [['HP', 1000]],
    'crystal berry': [['MP', 1000]],
    'apple': [['HP', 10]],
    'blueberry': [['MP', 10]],
    'spud': [['HP', 10], ['MP', 10]],
    'wolf meat': [['HP', 25], ['MP', 8]],
    'shellfish': [['HP', 35], ['MP', 15]],

    'small hp potion': [['HP', 50]],
    'small mp potion': [['MP', 50]],
    'medium hp potion': [['HP', 100]],
    'medium mp potion': [['MP', 100]],
    'large hp potion': [['HP', 200]],
    'large mp potion': [['MP', 200]],
    'small mixed potion': [['HP', 30], ['MP', 30]],
    'medium mixed potion': [['HP', 70], ['MP', 70]],
    'large mixed potion': [['HP', 150], ['MP', 150]],
    'fries': [['HP', 15], ['MP', 15]],
    'apple pie': [['HP', 25], ['EF', ['regeneration', 1, 3]]],
    'blueberry pie': [['MP', 25], ['EF', ['attunement', 1, 3]]],
    'potato salad': [['MP', 20], ['HP', 20], ['EF', ['defence', 1, 3]]],
    'wolf pasty': [['HP', 45], ['MP', 25], ['EF', ['warrior spirit', 2, 2]]],
    'stroganoff': [['HP', 50]],
    'seafood kebab': [['HP', 50], ['MP', 10]],
    'fish n chips': [['HP', 50], ['MP', 25], ['EF', ['defence', 3, 3]]],
    'silva salad': [['HP', 35], ['MP', 60], ['EF', ['regeneration', 3, 4]]],
    'honey apples': [['HP', 30], ['MP', 30], ['EF', ['attunement', 3, 3]]],
}
hero_items = ['crystal apple','crystal berry','campfire','magic wallet','midas ring','phase wings','knight elixir','brawler elixir','bard elixir','mage elixir']

shop_items = ['apple','blueberry','spud','small hp potion','medium hp potion','large hp potion','small mp potion','medium mp potion','large mp potion','small mixed potion','medium mixed potion','large mixed potion','joke book','wooden shield','leather armour','leather helmet','leather gloves','wooden wand','small bell','wooden sword']
krakow_shop_items = ['mystic conch','seafood kebab', 'fish n chips', 'sleeping bag', 'medium mixed potion', 'stick sword',]
witch_shop_items = ['red elixir','blue elixir','green elixir','gray elixir','shiny elixir','lucky elixir']

items = {
    #max 4 elixirs at 1 time
    'shiny elixir': {'desc': '+25% xp, 60 mins', 'buy': [[350, 'aurum'], [10, 'shiny pearl'], [35, 'magic dust']], 'sell': [[400, 'aurum']]},
    'lucky elixir': {'desc': '+25% loot chance, 60 mins', 'buy': [[350, 'aurum'],[5, 'magic fang'], [35, 'magic dust']], 'sell': [[400, 'aurum']]},
    'knight elixir': {'desc': '+10% CRIT.DMG, +5% CRIT, 30 mins', 'buy': [[4, 'hero coin']], 'sell': [[400, 'aurum']]},
    'mage elixir': {'desc': '+10% SPELL.DMG, -30% SPELL MP COST, 30 mins', 'buy': [[4, 'hero coin']], 'sell': [[400, 'aurum']]},
    'brawler elixir': {'desc': '+10% DEF, +15% MAX HP, 30 mins', 'buy': [[4, 'hero coin']], 'sell': [[400, 'aurum']]},
    'bard elixir': {'desc': '+20% HEALING, +15% MAX MP, 30 mins', 'buy': [[4, 'hero coin']], 'sell': [[400, 'aurum']]},

    'red elixir': {'desc': '+5% DMG, 20 mins', 'buy': [[150, 'aurum'],[20, 'blood'], [15, 'magic dust']], 'sell': [[400, 'aurum']]},
    'gray elixir': {'desc': '+5% DEF, 20 mins', 'buy': [[12, 'scale'],[110, 'aurum'], [10, 'magic dust']], 'sell': [[400, 'aurum']]},
    'green elixir': {'desc': '+10% MAX HP, 20 mins', 'buy': [[90, 'aurum'],[20, 'leaf'], [10, 'magic dust']], 'sell': [[400, 'aurum']]},
    'blue elixir': {'desc': '+10% MAX MP, 20 mins', 'buy': [[90, 'aurum'],[10, 'blueberry'], [10, 'magic dust']], 'sell': [[400, 'aurum']]},


    'crystal berry': {'desc': 'Heals 1000 mp', 'buy': [[2, 'hero coin']], 'sell': [[100, 'aurum']]},
    'crystal apple': {'desc': 'Heals 1000 hp, "don\'t get lost in the crystal dimension"', 'buy': [[5, 'hero coin']], 'sell': [[100, 'aurum']]},
    'campfire': {'desc': 'Heals up to 75% HP and 65% MP outside of battle', 'buy': [[20, 'hero coin']], 'sell': [[100, 'aurum']]},
    'magic wallet': {'desc': 'Lose less aurum on death (3%)', 'buy': [[15, 'hero coin']], 'sell': [[100, 'aurum']]},
    'midas ring': {'desc': 'Automatically sells monster loot. Upgrades increase sell value, +5% item sell value, +1 DEF', 'buy': [[20, 'hero coin']], 'sell': [[100, 'aurum']]},
    'phase wings': {'desc': 'Travel anywhere in the island in an instant (type area name in /travel)', 'buy': [[25, 'hero coin']], 'sell': [[100, 'aurum']]},
    'hero coin': {'desc': 'A premium currency for only true heroes', 'buy': [[100, 'aurum']], 'sell': [[100, 'aurum']]},
    'magic fang': {'desc': 'A fang from a mighty wild beast', 'buy': [[600, 'aurum']], 'sell': [[ 150,'aurum']]},
    'magic tentacle': {'desc': 'A huge slimy tentacle from a great sea creature', 'buy': [[1000, 'aurum']], 'sell': [[ 200,'aurum']]},
    'magic branch': {'desc': 'A evergowing branch that smells of 1000 flowers', 'buy': [[1600, 'aurum']], 'sell': [[ 250,'aurum']]},

    'kraken ink': {'desc': 'The ink of a legendary creature from a distant time. Perhaps an ancient ancestor of King Polypus', 'buy': [[100000,'aurum']], 'sell': [[ 5,'hero coin']]},
    'peach sap': {'desc': 'Basically tree blood. It might be edible but also might be poisonous. Eat it anyway', 'buy': [[100000,'aurum']], 'sell': [[ 1,'hero coin']]},
    'minae': {'desc': 'An enchanted material that is used to upgrade any item, can drop from any monster', 'buy': [[100,5]], 'sell': [[ 1,'aurum']]},
    'magic dust': {'desc': 'Sparkling dust dropped from powerful monsters. Used for buying/upgrading spells', 'buy': [[100,'aurum']], 'sell': [[ 1,'aurum']]},
    
    'egg': {'desc': 'Can be used in cooking, drops from crows', 'buy': [[5,'aurum']], 'sell': [[ 1,'aurum']]},
    'stick': {'desc': 'Can be used in crafting, drops from crows and badgers', 'buy': [[4,'aurum']], 'sell': [[ 1,'aurum']]},
    'feather': {'desc': 'Can be used in crafting, drops from crows', 'buy': [[6,'aurum']], 'sell': [[ 1,'aurum']]},
    'badger fur': {'desc': 'Can be used in crafting, drops from badgers', 'buy': [[8,'aurum']], 'sell': [[ 2,'aurum']]},
    'leaf' : {'desc': 'Can be used in crafting, drops from manihots', 'buy': [[10,'aurum']], 'sell': [[ 3,'aurum']]},
    'wheat': {'desc': 'Can be used in cooking, drops from scarecrows', 'buy': [[14,'aurum']], 'sell': [[ 4,'aurum']]},
    'scale': {'desc': 'Can be used in crafting, drops from snakes', 'buy': [[18,'aurum']], 'sell': [[ 5,'aurum']]},
    'snake fang': {'desc': 'Can be used in crafting, drops from snakes', 'buy': [[20,'aurum']], 'sell': [[ 6,'aurum']]},
    'fungus': {'desc': 'Can be used in crafting, drops from boletus', 'buy': [[24,'aurum']], 'sell': [[ 7,'aurum']]},
    'truffle spores': {'desc': 'Valuable resource, drops from boletus', 'buy': [[40,'aurum']], 'sell': [[ 15,'aurum']]},
    'blood': {'desc': 'Can be used in crafting, drops from bats', 'buy': [[20,'aurum']], 'sell': [[ 6,'aurum']]},
    'bat wing': {'desc': 'Can be used in crafting, drops from bats', 'buy': [[30,'aurum']], 'sell': [[ 8,'aurum']]},
    'wolf fur': {'desc': 'Can be used in crafting, drops from wolves and wolf pups', 'buy': [[32,'aurum']], 'sell': [[ 7,'aurum']]},
    'wolf paw': {'desc': 'Can be used in crafting, rarely drops from wolves', 'buy': [[50,'aurum']], 'sell': [[ 23,'aurum']]},
    'sparkly sand': {'desc': 'Can be used in crafting, drops from seit\'aads', 'buy': [[36,'aurum']], 'sell': [[ 9,'aurum']]},
    'spicy sand': {'desc': 'Can be used in cooking, drops from seit\'aads', 'buy': [[20,'aurum']], 'sell': [[ 12,'aurum']]},
    'crab shell': {'desc': 'Can be used in crafting, drops from crabs', 'buy': [[40,'aurum']], 'sell': [[ 10,'aurum']]},
    'clam shell': {'desc': 'Can be used in crafting, drops from clams', 'buy': [[50,'aurum']], 'sell': [[ 12,'aurum']]},
    'shiny pearl': {'desc': 'Can be used in crafting, drops rarely from clams', 'buy': [[60,'aurum']], 'sell': [[ 26,'aurum']]},
    'pearl thread': {'desc': 'Can be used in crafting, drops from clams', 'buy': [[48,'aurum']], 'sell': [[ 11,'aurum']]},
    'bear fur': {'desc': 'Can be used in crafting, drops from bears', 'buy': [[52,'aurum']], 'sell': [[ 12,'aurum']]},
    'bear claw': {'desc': 'Can be used in crafting, drops rarely from bears', 'buy': [[60,'aurum']], 'sell': [[ 28,'aurum']]},
    'wisp essence': {'desc': 'Can be used in crafting, drops from silva wisps', 'buy': [[56,'aurum']], 'sell': [[ 13,'aurum']]},
    'silva flower': {'desc': 'Can be used in crafting, drops from silva wisps', 'buy': [[44,'aurum']], 'sell': [[ 18,'aurum']]},
    'wasp wing': {'desc': 'Can be used in crafting, drops from aculeos', 'buy': [[60,'aurum']], 'sell': [[ 12,'aurum']]},
    'honey': {'desc': 'Can be used in cooking, drops from aculeos', 'buy': [[70,'aurum']], 'sell': [[ 22,'aurum']]},
    'wasp stinger': {'desc': 'Can be used in crafting, drops from aculeos', 'buy': [[64,'aurum']], 'sell': [[ 16,'aurum']]},
    'flour': {'desc': 'Widley used in cooking', 'buy': [[30,'aurum']], 'sell': [[ 8,'aurum']]},

    'sleeping bag': {'desc': 'Use this to rest and 50% of HP and MP. Unlimited uses', 'buy': [[2000,'aurum']], 'sell': [[ 1000,'aurum']]},
    'mystic conch': {'desc': 'Teleports the user to Beach III', 'buy': [[3000,'aurum']], 'sell': [[ 1500,'aurum']]},
    'apple': {'desc': 'Heals 10 hp (3 turn cooldown if in battle) drops from crows', 'buy': [[10,'aurum']], 'sell': [[ 3,'aurum']]},
    'blueberry': {'desc': 'Heals 15 mp (3 turn cooldown if in battle) drops from badgers', 'buy': [[20,'aurum']], 'sell': [[ 6,'aurum']]},
    'spud': {'desc': 'Heals 10 hp and 10 mp (3 turn cooldown if in battle) drops from manihots', 'buy': [[25,'aurum']], 'sell': [[ 10,'aurum']]},
    'wolf meat': {'desc': 'Heals 25 hp and 8 mp (3 turn cooldown if in battle) drops from wolves', 'buy': [[30,'aurum']], 'sell': [[ 15,'aurum']]},
    'shellfish': {'desc': 'Heals 35 hp and 15 mp (3 turn cooldown if in battle) drops from crabs and clams', 'buy': [[40,'aurum']], 'sell': [[ 20,'aurum']]},
    'fries': {'desc': 'Heals 15 hp and 15 mp', 'buy': [[60,'aurum']], 'sell': [[ 30,'aurum']]},
    'apple pie': {'desc': 'Heals 25 hp + Regeneration(1) for 2 turns', 'buy': [[60,'aurum']], 'sell': [[ 30,'aurum']]},
    'blueberry pie': {'desc': 'Heals 25 mp + Attunement(1) for 2 turns', 'buy': [[80,'aurum']], 'sell': [[ 40,'aurum']]},
    'potato salad': {'desc': 'Heals 20 hp and 20 mp + Defence(1) for 3 turns', 'buy': [[140,'aurum']], 'sell': [[ 70,'aurum']]},
    'wolf pasty': {'desc': 'Heals 45 hp and 25 mp + Warrior Spirit(2) for 2 turns', 'buy': [[170,'aurum']], 'sell': [[ 85,'aurum']]},
    'stroganoff': {'desc': 'Heals 50 hp', 'buy': [[150,'aurum']], 'sell': [[ 75,'aurum']]},
    'seafood kebab': {'desc': 'Heals 50 hp and 10 mp', 'buy': [[160,'aurum']], 'sell': [[ 80,'aurum']]},
    'fish n chips': {'desc': 'Heals 50 hp and 25 mp + Defence(3) for 3 turns', 'buy': [[170,'aurum']], 'sell': [[ 85,'aurum']]},
    'silva salad': {'desc': 'Heals 35 hp and 60 mp + Regeneration(3) for 4 turns', 'buy': [[120,'aurum']], 'sell': [[ 60,'aurum']]},
    'honey apples': {'desc': 'Heals 30 hp and 30 mp + Attunement(3) for 3 turns', 'buy': [[120,'aurum']], 'sell': [[ 60,'aurum']]},

    'small hp potion': {'desc': 'Heals 50 hp (3 turn cooldown if in battle) drops from monsters', 'buy': [[100,'aurum']], 'sell': [[ 40,'aurum']]},
    'medium hp potion': {'desc': 'Heals 100 hp (3 turn cooldown if in battle) drops rarely from monsters', 'buy': [[250,'aurum']], 'sell': [[ 100,'aurum']]},
    'large hp potion': {'desc': 'Heals 200 hp (3 turn cooldown if in battle)', 'buy': [[750,'aurum']], 'sell': [[ 250,'aurum']]},
    'small mp potion': {'desc': 'Heals 50 mp (3 turn cooldown if in battle) drops from monsters', 'buy': [[100,'aurum']], 'sell': [[ 40,'aurum']]},
    'medium mp potion': {'desc': 'Heals 100 mp (3 turn cooldown if in battle) drops rarely from monsters', 'buy': [[250,'aurum']], 'sell': [[ 100,'aurum']]},
    'large mp potion': {'desc': 'Heals 200 mp (3 turn cooldown if in battle) drops from bosses', 'buy': [[750,'aurum']], 'sell': [[ 250,'aurum']]},
    'small mixed potion': {'desc': 'Heals 30 hp and 30 mp (3 turn cooldown if in battle)', 'buy': [[130,'aurum']], 'sell': [[ 50,'aurum']]},
    'medium mixed potion': {'desc': 'Heals 70 hp and 70 mp (3 turn cooldown if in battle) drops from bosses', 'buy': [[350,'aurum']], 'sell': [[ 130,'aurum']]},
    'large mixed potion': {'desc': 'Heals 150 hp and 150 mp (3 turn cooldown if in battle) drops from bosses', 'buy': [[900,'aurum']], 'sell': [[ 350,'aurum']]},
    
    'joke book': {'desc': '+10% more SPELL DMG. Must be LVL 1 to use', 'buy': [[100,'aurum']], 'sell': [[ 60,'aurum']]},
    'wooden shield': {'desc': '+10 DEF. Must be LVL 1 to use', 'buy': [[100,'aurum']], 'sell': [[ 60,'aurum']]},
    'leather armour': {'desc': '+10 DEF. Must be LVL 1 to use', 'buy': [[100,'aurum']], 'sell': [[ 60,'aurum']]},
    'leather helmet': {'desc': '+5 DEF. Must be LVL 1 to use', 'buy': [[50,'aurum']], 'sell': [[ 30,'aurum']]},
    'leather gloves': {'desc': '+5 DMG, +2 HP. Must be LVL 1 to use', 'buy': [[50,'aurum']], 'sell': [[ 30,'aurum']]},
    'wooden wand': {'desc': '+6 DMG. Must be LVL 1 to use', 'buy': [[50,'aurum']], 'sell': [[ 30,'aurum']]},
    'small bell': {'desc': '+5 DMG, +4 MP. Must be LVL 1 to use', 'buy': [[50,'aurum']], 'sell': [[ 30,'aurum']]},
    'wooden sword': {'desc': '+5 DMG, +2 DEF. Must be LVL 1 to use', 'buy': [[50,'aurum']], 'sell': [[ 30,'aurum']]},
    'stick sword': {'desc': '+1 DMG. Must be a noob to use', 'buy': [[5000,'aurum']], 'sell': [[ 1,'aurum']]},

    'feather blade' : {'desc': '+5 DMG, +1% CRIT. Must be LVL 1 to use', 'buy': [[100,'aurum']], 'sell': [[ 50,'aurum']]},
    'fluffy hat': {'desc': '+5 DEF, +3 HP. Must be LVL 1 to use', 'buy': [[105,'aurum']], 'sell': [[ 55,'aurum']]},
    'leaf crown': {'desc': '+10 DEF, +5 MP. Must be LVL 2 to use', 'buy': [[130,'aurum']], 'sell': [[ 75,'aurum']]},
    'fang knuckledusters': {'desc': '+10 DMG, +5 DEF. Must be LVL 5 to use', 'buy': [[130,'aurum']], 'sell': [[ 75,'aurum']]},
    'sparking wand': {'desc': '+8 DMG, +4% CRIT. Must be LVL 3 to use', 'buy': [[150,'aurum']], 'sell': [[ 85,'aurum']]},
    'scaled shield': {'desc': '+8 DEF +5 HP. Must be LVL 5 to use', 'buy': [[160,'aurum']], 'sell': [[ 90,'aurum']]},
    'fungus armour': {'desc': '+10 DEF, +3 DMG. Must be LVL 5 to use', 'buy': [[200,'aurum']], 'sell': [[ 120,'aurum']]},
    'wolf gloves': {'desc': '+12 DMG, +10 HP. Must be LVL 10 to use', 'buy': [[200,'aurum']], 'sell': [[ 120,'aurum']]},
    'wolfskin drums': {'desc': '+12 DMG, +5% CRIT, +15% more CRIT DMG. Must be LVL 10 to use', 'buy': [[210,'aurum']], 'sell': [[ 125,'aurum']]},
    'blood staff' : {'desc': '+12 DMG, +10% more SPELL DMG. Must be LVL 10 to use', 'buy': [[230,'aurum']], 'sell': [[ 135,'aurum']]},
    'fur tunic': {'desc': '+15 DEF, +10 HP. Must be LVL 10 to use', 'buy': [[250,'aurum']], 'sell': [[ 150,'aurum']]},
    'bat hat' : {'desc': '+15 DEF, +10 HP. Must be LVL 10 to use', 'buy': [[230,'aurum']], 'sell': [[ 135,'aurum']]},
    'hunters hood': {'desc': '+4 DEF, +3 DMG, +4% CRIT. Must be LVL 10 to use', 'buy': [[250,'aurum']], 'sell': [[ 150,'aurum']]},
    'glass sword': {'desc': '+16 DMG, +7% CRIT. Must be LVL 17 to use', 'buy': [[300,'aurum']], 'sell': [[ 170,'aurum']]},
    'crab armour': {'desc': '+20 DEF, +10 HP, +10 MP. Must be LVL 17 to use', 'buy': [[350,'aurum']], 'sell': [[ 200,'aurum']]},
    'mermaid harp': {'desc': '+18 DMG, +15% more SPELL DMG. Must be LVL 20 to use', 'buy': [[400,'aurum']], 'sell': [[ 250,'aurum']]},
    'shell shield': {'desc': '+15 DEF, +4 DMG, +5 HP. Must be LVL 20 to use', 'buy': [[350,'aurum']], 'sell': [[ 200,'aurum']]},
    'magic crystal orb': {'desc': '+8 DMG, +12% more SPELL DMG. Must be LVL 20 to use', 'buy': [[370,'aurum']], 'sell': [[ 220,'aurum']]},
    'pearlescent wand': {'desc': '+20 DMG, +25% more CRIT DMG. Must be LVL 24 to use', 'buy': [[400,'aurum']], 'sell': [[ 250,'aurum']]},
    'bear hat': {'desc': '+25 DEF, +10 MP. Must be LVL 27 to use', 'buy': [[450,'aurum']], 'sell': [[ 300,'aurum']]},
    'grizzly gloves': {'desc': '+25 DMG +10% CRIT, +10 MP. Must be LVL 27 to use', 'buy': [[450,'aurum']], 'sell': [[ 300,'aurum']]},
    'wisp wand': {'desc': '+25 DMG, +15 HP. Must be LVL 30 to use', 'buy': [[500,'aurum']], 'sell': [[ 350,'aurum']]},
    'spirit flute': {'desc': '+28 DMG, +10 HP, +5% more SPELL DMG. Must be LVL 30 to use', 'buy': [[500,'aurum']], 'sell': [[ 350,'aurum']]},
    'wasp suit': {'desc': '+35 DEF, +10 MP, +10 DMG. Must be LVL 30 to use', 'buy': [[550,'aurum']], 'sell': [[ 400,'aurum']]},
    'stinging blade': {'desc': '+30 DMG, +9% CRIT, +20% more CRIT DMG. Must be LVL 30 to use', 'buy': [[600,'aurum']], 'sell': [[ 450,'aurum']]},

    'ruby ring': {'desc': '+5 DEF, +20% loot chance. Must be LVL 10 to use', 'buy': [[800,'aurum']], 'sell': [[ 400,'aurum']]},
    'aqua ring': {'desc': '+10 MP, +10% XP gain. Must be LVL 20 to use', 'buy': [[2000,'aurum']], 'sell': [[ 1000,'aurum']]},
    'nature ring': {'desc': '+7 HP. Must be LVL 3 to use', 'buy': [[400,'aurum']], 'sell': [[ 200,'aurum']]},

    'howling horn': {'desc': '+25 DMG, +6% CRIT, +17% more SPELL DMG, +8 HP. Must be LVL 15 to use', 'buy': [[1000,'aurum']], 'sell': [[ 500,'aurum']]},
    'wolf head': {'desc': '+25 DEF, +20 HP, +2% CRIT, +10 MP. Must be LVL 15 to use', 'buy': [[1000,'aurum']], 'sell': [[ 500,'aurum']]},
    'eye of the wolf': {'desc': '+15 DEF, +8% CRIT, +25% more CRIT DMG +5 MP. Must be LVL 15 to use', 'buy': [[1000,'aurum']], 'sell': [[ 500,'aurum']]},

    'coral sword': {'desc': '+32 DMG, +12% CRIT, +25% more CRIT DMG, +10% more SPELL DMG. Must be LVL 25 to use', 'buy': [[1500,'aurum']], 'sell': [[ 750,'aurum']]},
    'tentacle chestplate': {'desc': '+42 DEF, +5 DMG, +25 HP, +25 MP. Must be LVL 25 to use', 'buy': [[1500,'aurum']], 'sell': [[ 750,'aurum']]},
    'inky ring': {'desc': '+35 DEF, +25 MP, Immunity to "Broken Armour". Must be LVL 25 to use', 'buy': [[1500,'aurum']], 'sell': [[ 750,'aurum']]},

    'trunk vambrace': {'desc': '+36 DMG, +26 DEF, +10 % CRIT DMG, +12 HP. Must be LVL 35 to use', 'buy': [[2000,'aurum']], 'sell': [[ 1000,'aurum']]},
    'grass blade': {'desc': '+35 DMG, + 20% CRIT, +5 HP, +20 MP. Must be LVL 35 to use', 'buy': [[2000,'aurum']], 'sell': [[ 1000,'aurum']]},
    'dark rose wand': {'desc': '+40 DMG, +15% more SPELL DMG, +20 MP. Must be LVL 35 to use', 'buy': [[2000,'aurum']], 'sell': [[ 1000,'aurum']]},
    'emerald lute': {'desc': '+38 DMG, +20 HP, +10% more SPELL DMG, +35 MP. Must be LVL 35 to use', 'buy': [[2000,'aurum']], 'sell': [[ 1000,'aurum']]},

    'thornbark robes': {'desc': '+54 HP, +13 DMG, +20 DEF, +10% more CRIT DMG. Must be LVL 35 to use', 'buy': [[2000,'aurum']], 'sell': [[ 1000,'aurum']]},


}

item_types = {
    'sword': ['blade', 'knife', 'sword', 'razor', 'dagger'],
    'glove': ['fists', 'vambrace', 'gloves', 'gauntlets', 'knuckledusters'],
    'helmet': ['hood','cap', 'helmet', 'hat', 'helm', 'head', 'headgear', 'crown'],
    'shield': ['shield', 'buckler', 'kite', 'of', 'towershield', 'roundshield', 'wolf'],
    'wand': ['wand', 'staff', 'rod', 'cane', 'rose'],
    'armour': ['armour', 'chestplate', 'tunic', 'robes', 'chainmail', 'platemail', 'rags', 'scalemail', 'suit'],
    'instrument': ['bell', 'horn', 'drum', 'flute', 'lute', 'piano', 'violin', 'harp', 'guitar', 'banjo', 'drums', 'cymbals'],
    'ring': ['loop', 'ring'],
    'mystic': ['book', 'orb', 'lantern', 'tome', 'spellbook', 'crystal'],
    'food': ['mystic conch','crystal apple','crystal berry','campfire','sleeping bag', 'shellfish', 'potato salad', 'wolf pasty', 'fries', 'apple pie', 'blueberry pie', 'stroganoff','seafood kebab','fish n chips','silva salad', 'honey apples' ,'wolf meat','apple', 'spud', 'blueberry', 'small hp potion', 'medium hp potion', 'large hp potion', 'small mp potion', 'medium mp potion', 'large mp potion', 'small mixed potion', 'medium mixed potion', 'large mixed potion'],
}

statable_types = ['sword', 'glove', 'helmet', 'shield', 'wand', 'armour', 'instrument', 'ring', 'mystic']

stackable_types = ['consumable', 'resource']

#lvl is for level requirment
default_stats = {
    'midas ring': [['DEF', 1],['LVL', 0]],
    'nature ring': [['HP', 7],['LVL', 3]],
    'ruby ring': [['DEF', 5],['LVL', 10]],
    'aqua ring': [['MP', 10],['LVL', 20]],
    'inky ring':[['DEF', 35], ['MP', 25],['LVL', 25]],

    'stick sword': [['DMG', 1],['LVL', 0]],
    'wooden sword': [['DMG', 5],['DEF', 2],['LVL', 1]],
    'wooden shield': [['DEF', 10],['LVL', 1]],
    'wooden wand': [['DMG', 6],['LVL', 1]],
    'leather gloves': [['HP', 2],['DMG', 5],['LVL', 1]],
    'leather helmet': [['DEF', 5],['LVL', 1]],
    'leather armour': [['DEF', 10],['LVL', 1]],
    'small bell': [['MP', 4],['DMG', 5],['LVL', 1]],
    'joke book': [['%.SPELL.DMG', 10],['LVL', 1]],
    'feather blade' : [['DMG', 5], ['%.CRIT', 1],['LVL', 1]],
    'fluffy hat': [['DEF', 5], ['HP', 3],['LVL', 1]],
    'leaf crown': [['DEF', 10], ['MP', 5],['LVL', 2]],
    'fang knuckledusters': [['DMG', 10], ['DEF', 5],['LVL', 5]],
    'sparking wand': [['DMG', 8], ['%.CRIT', 4],['LVL', 3]],
    'scaled shield': [['DEF', 8], ['HP', 5],['LVL', 5]],
    'fungus armour': [['DEF', 10], ['DMG', 2],['LVL', 5]],
    'bat hat': [['DEF', 15], ['HP', 10],['LVL', 10]],
    'hunters hood': [['DEF', 4], ['DMG', 3], ['%.CRIT', 4],['LVL', 10]],
    'fluffy hat': [['DEF', 5], ['HP', 3],['LVL', 1]],
    'wolf gloves': [['DMG', 12], ['DEF', 8], ['HP', 10],['LVL', 10]],
    'wolfskin drums': [['DMG', 12], ['%.CRIT', 5], ['%.CRIT.DMG', 15],['LVL', 10]],
    'blood staff' : [['DMG', 12], ['%.SPELL.DMG', 10],['LVL', 10]],
    'fur tunic': [['DEF', 17], ['HP', 10],['LVL', 10]],
    'glass sword':[['DMG', 16], ['%.CRIT', 7],['LVL', 17]],
    'crab armour': [['DEF', 22], ['HP', 10], ['MP', 10],['LVL', 17]],
    'mermaid harp': [['DMG', 18], ['%.SPELL.DMG', 15],['LVL', 20]],
    'shell shield': [['DEF', 15], ['DMG', 4], ['HP', 5],['LVL', 20]],
    'magic crystal orb': [['DMG', 8], ['%.SPELL.DMG', 12],['LVL', 20]],
    'pearlescent wand': [['DMG', 20], ['%.CRIT.DMG', 25],['LVL', 24]],
    'bear hat': [['DEF', 25], ['MP', 10],['LVL', 27]],
    'grizzly gloves': [['DMG', 25], ['%.CRIT', 10], ['MP', 10],['LVL', 27]],
    'wisp wand':[['DMG', 25], ['HP', 15],['LVL', 30]],
    'spirit flute':[['DMG', 28], ['HP', 10], ['%.SPELL.DMG', 5],['LVL', 30]],
    'wasp suit': [['DEF', 35], ['MP', 10], ['DMG', 10],['LVL', 30]],
    'stinging blade':[['DMG', 30], ['%.CRIT', 9], ['%.CRIT.DMG', 20],['LVL', 30]],

    'howling horn': [['DMG', 25], ['%.CRIT', 6], ['%.SPELL.DMG', 17], ['HP', 8],['LVL', 15]],
    'wolf head': [['DEF', 25], ['HP', 20], ['%.CRIT', 2], ['MP', 10],['LVL', 15]],
    'eye of the wolf':[['DEF', 15], ['%.CRIT', 8], ['%.CRIT.DMG', 25], ['MP', 5],['LVL', 15]],

    'coral sword': [['DMG', 32], ['%.CRIT', 12], ['%.CRIT.DMG', 25], ['%.SPELL.DMG', 10],['LVL', 25]],
    'tentacle chestplate': [['DEF', 42], ['DMG', 5], ['HP', 25], ['MP', 25],['LVL', 25]],

    'trunk vambrace': [['DMG', 36], ['DEF', 26], ['%.CRIT.DMG', 10], ['HP', 12],['LVL', 35]],
    'grass blade': [['DMG', 35],['%.CRIT', 20], ['HP', 5],['MP', 20], ['LVL', 35]],
    'dark rose wand': [['DMG', 40],['%.SPELL.DMG', 15],['MP', 20], ['LVL', 35]],
    'emerald lute': [['DMG', 38],['HP',20],['%.SPELL.DMG', 10],['MP', 35], ['LVL', 35]],

    'thornbark robes': [['HP', 54], ['DMG', 13], ['DEF', 20], ['%CRIT.DMG', 10], ['LVL', 35]],
}

chef_recipes = {
    'flour': [['wheat', 2], ['aurum', 3]],
    'fries': [['spud', 2], ['aurum', 5]],
    'apple pie': [['flour', 2], ['apple', 4], ['egg', 1]],
    'blueberry pie': [['flour', 2], ['blueberry', 4], ['egg', 1]],
    'potato salad': [['spud', 3],['leaf', 5],['apple', 1]],
    'wolf pasty': [['spud', 2], ['wolf meat', 3], ['flour', 2]],
    'stroganoff': [['truffle spores', 3], ['wolf meat', 2]],
    'seafood kebab': [['spicy sand', 3], ['shellfish', 2]],
    'fish n chips': [['fries', 2], ['shellfish', 2]],
    'silva salad': [['silva flower', 3], ['leaf', 6]],
    'honey apples': [['apple', 3], ['honey', 2]]
}

smith_costs = {
    'feather blade' : [['feather', 5], ['stick', 2]],
    'fluffy hat': [['badger fur', 5], ['blueberry', 1]],
    'leaf crown': [['spud', 5], ['leaf', 5]],
    'nature ring': [['stick', 10], ['leaf', 10], ['aurum', 175]],
    'fang knuckledusters': [['snake fang', 10], ['leaf', 7]],
    'sparking wand': [['wheat', 8], ['stick', 5]],
    'scaled shield': [['snake fang', 8], ['scale', 10]],
    'fungus armour': [['fungus', 12], ['scale', 10]],
    'wolf gloves': [['wolf paw', 2], ['wolf fur', 5]],
    'wolfskin drums': [['wolf fur', 8], ['bat wing', 6]],
    'blood staff' : [['bat wing', 4], ['blood', 10]],
    'hunters hood': [['wolf fur', 7], ['blood', 15]],
    'bat hat' : [['bat wing', 12], ['fluffy hat', 1]],
    'ruby ring': [['blood', 16], ['wolf paw', 1], ['aurum', 375]],
    'fur tunic': [['wolf fur', 10], ['blood', 5], ['badger fur', 5]],
    'glass sword': [['sparkly sand', 10], ['stick', 5]],
    'crab armour': [['crab shell', 10], ['sparkly sand', 5]],
    'mermaid harp': [['sparkly sand', 10], ['pearl thread', 5]],
    'shell shield': [['clam shell', 10], ['crab shell', 5]],
    'magic crystal orb': [['shiny pearl', 8], ['pearl thread', 10]],
    'aqua ring': [['shiny pearl', 10], ['sparkly sand', 15], ['aurum', 825]],
    'pearlescent wand': [['shiny pearl', 10], ['stick', 5]],
    'bear hat': [['bear fur', 10], ['wolf fur', 5]],
    'grizzly gloves': [['bear fur', 5], ['bear claw', 4]],
    'wisp wand': [['wisp essence', 10], ['wheat', 5]],
    'spirit flute': [['wisp essence', 14], ['pearl thread', 5]],
    'wasp suit': [['wasp wing', 10], ['wasp stinger', 3]],
    'stinging blade': [['wasp stinger', 5], ['wisp essence', 8]],
}

area_mobs = {
    'Apple Orchard': [['crow', 100]],
    'Town 1': None,
    'Farm': [['manihot', 56],['enchanted manihot', 4], ['scarecrow', 40]],
    'Forest Outskirts': [['crow', 40], ['badger', 60]],

    'Forest I': [['grizzly bear', 85], ['enchanted grizzly bear', 5], ['badger', 10]],
    'Forest II': [['silva wisp', 66],['grizzly bear', 29], ['enchanted grizzly bear', 1], ['enchanted silva wisp', 4]],
    'Forest III': [['aculeo', 65], ['silva wisp', 31], ['enchanted silva wisp', 4]],

    'Wolf Den I': [['serpens', 65], ['boletus', 31], ['enchanted boletus', 4]],
    'Wolf Den II': [['suco', 51],['enchanted suco', 4], ['enchanted boletus', 1], ['wolf pup', 30],['boletus', 14]],
    'Wolf Den III': [['wolf', 56],['enchanted wolf', 4], ['wolf pup', 40]],

    'Krakow\'s Cave': [['krakow',100]],
    'Beach I': [['seitaad',61],['enchanted seitaad',4], ['crab', 35]],
    'Beach II': [['crab', 60], ['seitaad', 17],['enchanted seitaad', 3], ['clam', 19], ['enchanted clam', 1]],
    'Beach III': [['crab', 55], ['clam', 42], ['enchanted clam', 3]],

    'Boat 1': None,
}

monsters = {
    'crow': 'Lowest level monster. They can be found in the Apple Orchard and the Forest Outskirts.',
    'badger': 'These little blueberry munching badgers can be found in Forest I and the Forest Outskirts.',
    'manihot': 'Kind of like walking potatoes. They can be found in the Farm.',
    'scarecrow': 'This is why there are no crows in the farm. They can be found in the Farm.',
    'serpens': 'Ssssuch sssneaky ssnakes can be found in Wolf Den I.',
    'boletus': 'These are really fun-guys *wink face*. They can be found in Wolf Den I',
    'suco': 'They are essentially mini vampires. They can be found in Wolf Den II',
    'wolf pup': 'These are the little baby wolves. They can be found in Wolf Den II and Wolf Den III',
    'wolf': 'These are.. not so little wolves. They can be found in Wolf Den III',
    'blood wolf': 'The minions of the Alpha Wolf, Strong but fragile. They can be found in Wolf Den III Boss Battle',
    'seitaad': 'Mighty magical.. sandcastles? They can be found in Beach I and Beach II',
    'crab': 'Tough and tanky crabs. They can be found in Beach II and Beach III',
    'clam': 'Pew pew.. They shoot pearls. They can be found in Beach II and Beach III',
    'grizzly bear': 'These are the biggest and strongest (and only) bears. They can be found in Forest I and Forest II',
    'silva wisp': 'Camoflauge against the leaves. They can be found in Forest II and Forest III',
    'aculeo': 'Ew a big, fat ugly wasp. They can be found in Forest III',
    
    'enchanted manihot': 'Rare and stronger version of the manihot. They can be found rarely in the Farm.',
    'enchanted boletus': 'These are not so fun-guys :/ They can be found rarely in Wolf Den I',
    'enchanted suco': 'They are the colour of blood. They can be found rarely in Wolf Den II',
    'enchanted wolf': 'Very hungry wolves. They can be found rarely in Wolf Den III',
    'enchanted seitaad': 'The ultimate sandcastles. They can be found rarely in Beach I and Beach II',
    'enchanted clam': 'They shoot pearls like bullets. They can be found rarely in Beach II and Beach III',
    'enchanted grizzly bear': 'So fluffy. They can be found rarely in Forest I and Forest II',
    'enchanted silva wisp': 'Almighty spirits of the forest. They can be found rarely in Forest II and Forest III',

    'alpha wolf': 'The Boss of the wolves. They can be found in Wolf Den III',
    'alpha wolf (hard)': 'The Boss of the wolves. They can be found in Wolf Den III',
    'alpha wolf (extreme)': 'The Boss of the wolves. They can be found in Wolf Den III',

    'king polypus': 'The corrupted King of the sea. They can be found in Beach III',
    'king polypus (hard)': 'The corrupted King of the sea. They can be found in Beach III',
    'king polypus (extreme)': 'The corrupted King of the sea. They can be found in Beach III',

    'visius ent': 'The Overseer of the forest. They can be found in Forest III',
    'visius ent (hard)': 'The Overseer of the forest. They can be found in Forest III',
    'visius ent (extreme)': 'The Overseer of the forest. They can be found in Forest III',
    'krakow': 'A mysterious fellow. Always up for a duel. They can be found in Krakow\'s Cave',
}

mob_stats = {
    ' ': {'XP': 0, 'LVL': 0, 'DMG': 0, 'DEF': 0, 'HP': 0, 'CRIT': 0, 'CRIT.DMG': 0, 'SPELL.CD': 0, 'SPELL': []},
    'crow': {'XP': 5, 'LVL': 1, 'DMG': 2, 'DEF': 5, 'HP': 10, 'CRIT': 3,'CRIT.DMG': 50, 'SPELL.CD': 0, 'SPELL': []},
    'badger': {'XP': 12, 'LVL': 3, 'DMG': 4, 'DEF': 10, 'HP': 20, 'CRIT': 2,'CRIT.DMG': 50, 'SPELL.CD': 0, 'SPELL': []},
    'manihot': {'XP': 20, 'LVL': 5, 'DMG': 5, 'DEF': 16, 'HP': 26, 'CRIT': 2,'CRIT.DMG': 50, 'SPELL.CD': 0, 'SPELL': []},
        'enchanted manihot': {'XP': 40, 'LVL': 5, 'DMG': 6, 'DEF': 26, 'HP': 46, 'CRIT': 12,'CRIT.DMG': 50, 'SPELL.CD': 0, 'SPELL': []},
    'scarecrow': {'XP': 26, 'LVL': 7, 'DMG': 7, 'DEF': 22, 'HP': 32, 'CRIT': 6,'CRIT.DMG': 50, 'SPELL.CD': 0, 'SPELL': []},
    'serpens': {'XP': 35, 'LVL': 8, 'DMG': 10, 'DEF': 14, 'HP': 30, 'CRIT': 2,'CRIT.DMG': 50, 'SPELL.CD': 5, 'SPELL': ['paralyse']},
        'enchanted boletus': {'XP': 90, 'LVL': 10, 'DMG': 14, 'DEF': 55, 'HP': 66, 'CRIT': 9,'CRIT.DMG': 50, 'SPELL.CD': 3, 'SPELL': ['poison spores']},
    'boletus': {'XP': 45, 'LVL': 10, 'DMG': 9, 'DEF': 35, 'HP': 41, 'CRIT': 2,'CRIT.DMG': 50, 'SPELL.CD': 5, 'SPELL': ['poison spores']},
    'suco': {'XP': 56, 'LVL': 12, 'DMG': 12, 'DEF': 30, 'HP': 42, 'CRIT': 7,'CRIT.DMG': 70, 'SPELL.CD': 4, 'SPELL': ['life drain']},
        'enchanted suco': {'XP': 112, 'LVL': 12, 'DMG': 18, 'DEF': 40, 'HP': 62, 'CRIT': 15,'CRIT.DMG': 70, 'SPELL.CD': 2, 'SPELL': ['life drain']},
    'wolf pup': {'XP': 67, 'LVL': 14, 'DMG': 12, 'DEF': 42, 'HP': 54, 'CRIT': 5,'CRIT.DMG': 50, 'SPELL.CD': 0, 'SPELL': []},
    'wolf': {'XP': 80, 'LVL': 17, 'DMG': 14, 'DEF': 50, 'HP': 60, 'CRIT': 5,'CRIT.DMG': 80, 'SPELL.CD': 3, 'SPELL': ['viscious bite']},
    'blood wolf': {'XP': 30, 'LVL': 20, 'DMG': 13, 'DEF': 10, 'HP': 50, 'CRIT': 30,'CRIT.DMG': 40, 'SPELL.CD': 1, 'SPELL': ['viscious bite', 'life drain']},
        'enchanted wolf': {'XP': 160, 'LVL': 17, 'DMG': 20, 'DEF': 70, 'HP': 90, 'CRIT': 10,'CRIT.DMG': 80, 'SPELL.CD': 2, 'SPELL': ['viscious bite','life drain']},
    'seitaad': {'XP': 95, 'LVL': 21, 'DMG': 17, 'DEF': 70, 'HP': 70, 'CRIT': 5,'CRIT.DMG': 50, 'SPELL.CD': 3, 'SPELL': ['sand spray']},
        'enchanted seitaad': {'XP': 190, 'LVL': 21, 'DMG': 25, 'DEF': 80, 'HP': 100, 'CRIT': 5,'CRIT.DMG': 100, 'SPELL.CD': 2, 'SPELL': ['sand spray']},
    'crab': {'XP': 102, 'LVL': 24, 'DMG': 19, 'DEF': 88, 'HP': 82, 'CRIT': 10,'CRIT.DMG': 60, 'SPELL.CD': 0, 'SPELL': []},
    'clam': {'XP': 125, 'LVL': 28, 'DMG': 23, 'DEF': 115, 'HP': 90, 'CRIT': 13,'CRIT.DMG': 80, 'SPELL.CD': 4, 'SPELL': ['penetrating pearl']},
        'enchanted clam': {'XP': 250, 'LVL': 28, 'DMG': 25, 'DEF': 120, 'HP': 120, 'CRIT': 20,'CRIT.DMG': 50, 'SPELL.CD': 2, 'SPELL': ['penetrating pearl','sand spray']},
    'grizzly bear': {'XP': 150, 'LVL': 32, 'DMG': 24, 'DEF': 130, 'HP': 100, 'CRIT': 5,'CRIT.DMG': 50, 'SPELL.CD': 0, 'SPELL': []},
        'enchanted grizzly bear': {'XP': 300, 'LVL': 32, 'DMG': 32  , 'DEF': 165, 'HP': 130, 'CRIT': 15,'CRIT.DMG': 50, 'SPELL.CD': 0, 'SPELL': []},
    'silva wisp': {'XP': 180, 'LVL': 35, 'DMG': 29, 'DEF': 115, 'HP': 105, 'CRIT': 10,'CRIT.DMG': 65, 'SPELL.CD': 6, 'SPELL': ['forest song']},
        'enchanted silva wisp': {'XP': 360, 'LVL': 35, 'DMG': 35, 'DEF': 140, 'HP': 125, 'CRIT': 20,'CRIT.DMG': 65, 'SPELL.CD': 2, 'SPELL': ['forest song','poison stinger']},
    'aculeo': {'XP': 210, 'LVL': 38, 'DMG': 31, 'DEF': 125, 'HP': 114, 'CRIT': 10,'CRIT.DMG': 100, 'SPELL.CD': 4, 'SPELL': ['poison stinger']},

    'alpha wolf': {'XP': 350, 'LVL': 20, 'DMG': 27, 'DEF': 60, 'HP': 450, 'CRIT': 10,'CRIT.DMG': 70, 'SPELL.CD': 6, 'SPELL': ['wolf dash', 'blood stare']},
    'alpha wolf (hard)': {'XP': 600, 'LVL': 27, 'DMG': 34, 'DEF': 80, 'HP': 630, 'CRIT': 10,'CRIT.DMG': 80, 'SPELL.CD': 5, 'SPELL': ['wolf pounce', 'call of the leader', 'blood stare', 'blood stare']},
    'alpha wolf (extreme)': {'XP': 1000, 'LVL': 35, 'DMG': 42, 'DEF': 105, 'HP': 850, 'CRIT': 20,'CRIT.DMG': 90, 'SPELL.CD': 3, 'SPELL': ['wolf pounce', 'shriek of the leader', 'blood gaze']},

    'tentacle': {'XP': 1, 'LVL': 30, 'DMG': 18, 'DEF': 55, 'HP': 140, 'CRIT': 15,'CRIT.DMG': 300, 'SPELL.CD': 3, 'SPELL': ['tentacle wrap', 'regeneration']},
    'king polypus': {'XP': 550, 'LVL': 30, 'DMG': 36, 'DEF': 100, 'HP': 750, 'CRIT': 3,'CRIT.DMG': 100, 'SPELL.CD': 6, 'SPELL': ['ink cloud', 'tidal wave', 'bubble blast']},
    'king polypus (hard)': {'XP': 1100, 'LVL': 37, 'DMG': 45, 'DEF': 120, 'HP': 1050, 'CRIT': 6,'CRIT.DMG': 110, 'SPELL.CD': 4, 'SPELL': ['ink cloud', 'tentacle bloom', 'tentacle bloom', 'tidal wave', 'bubble blast']},
    'king polypus (extreme)': {'XP': 1900, 'LVL': 45, 'DMG': 53, 'DEF': 135, 'HP': 1300, 'CRIT': 10,'CRIT.DMG': 120, 'SPELL.CD': 3, 'SPELL': ['ink cloud', 'tentacle bloom', 'tsunami', 'bubble blast']},
    
    'visius ent': {'XP': 800, 'LVL': 40, 'DMG': 49, 'DEF': 135, 'HP': 1250, 'CRIT': 18,'CRIT.DMG': 25, 'SPELL.CD': 6, 'SPELL': ['beast pound', 'leaf tornado', 'earthquake', 'overgrowth']},
    'visius ent (hard)': {'XP': 1550, 'LVL': 47, 'DMG': 58, 'DEF': 148, 'HP': 1575, 'CRIT': 20,'CRIT.DMG': 35, 'SPELL.CD': 5, 'SPELL': ['beast charge', 'stinger storm', 'leaf tornado','earthquake', 'overgrowth', 'overgrowth']},
    'visius ent (extreme)': {'XP': 3000, 'LVL': 55, 'DMG': 68, 'DEF': 160, 'HP': 1800, 'CRIT': 22,'CRIT.DMG': 50, 'SPELL.CD': 3, 'SPELL': ['beast charge', 'stinger storm', 'earthquake', 'overgrowth', 'overgrowth']},


    'krakow': {'XP': 200, 'LVL': 25, 'DMG': 31, 'DEF': 74, 'HP': 209, 'CRIT': 9,'CRIT.DMG': 50, 'SPELL.CD': 2, 'SPELL': ['fireball','earthquake','regeneration','magic shield']},
}

enemy_spells = {
    'paralyse': {'name': 'paralyse', 'dmg': 0, 'chance': 33, 'potence': 1, 'duration': 1, 'effect': 'paralysis', 'target': 'player', 'desc':'The snake does a strange dance that can paralyse you. 15% chance to inflict **paralysis** for 1 turn.'},
    'poison spores': {'name': 'poison spores', 'dmg': 11, 'chance': 50, 'potence': 1, 'duration': 2, 'effect': 'poison', 'target': 'player', 'desc':'The air is filled with poisonous spores and gas. 50% chance to inflict **poison** for 2 turns, 11 DMG.'},
    'life drain': {'name': 'life drain', 'dmg': 15, 'chance': 70, 'potence': 1, 'duration': 2, 'effect': 'bleeding', 'target': 'player', 'desc':'Vampiric fangs suck the blood from your enemies. 20% chance to inflict **bleeding** for 2 turns, 15 DMG, heals half the amount of damage dealt.'},
    'viscious bite': {'name': 'viscious bite', 'dmg': 18, 'chance': 50, 'potence': 2, 'duration': 2, 'effect': 'bleeding', 'target': 'player', 'desc':'A powerful bite that sinks deep into your flesh. 50% chance to inflict **bleeding** for 2 turns, 18 DMG.'},
    'sand spray': {'name': 'sand spray', 'dmg': 20, 'chance': 50, 'potence': 1, 'duration': 1, 'effect': 'blindness', 'target': 'player', 'desc':'Blinding sand is sprayed on your face. 50% chance to inflict **blindness**, 20 DMG.'},
    'penetrating pearl': {'name': 'penetrating pearl', 'dmg': 25, 'chance': 35, 'potence': 1, 'duration': 1, 'effect': 'broken armour', 'target': 'player', 'desc':'A pearl penetrates through you ignoring 80% of armour. 35% chance to inflict **broken armour** for 1 turn, 25 DMG.'},
    'forest song': {'name': 'forest song', 'dmg': 30, 'chance': 100, 'potence': 1, 'duration': 3, 'effect': 'regeneration', 'target': 'allies', 'desc':'A mysterious magical song lifts the spirits of your enemies. 100% chance to inflict **regeneration** to enemies, 30 DMG.'},
    'regeneration': {'name': 'regenration', 'dmg': 1, 'chance': 100, 'potence': 3, 'duration': 5, 'effect': 'regeneration', 'target': 'allies', 'desc':'100% chance to inflict **regeneration** to allies'},
    'magic shield': {'name': 'magic shield', 'dmg': 1, 'chance': 100, 'potence': 1, 'duration': 4, 'effect': 'defence', 'target': 'allies', 'desc':'100% chance to inflict **defence** allies'},
    'poison stinger': {'name': 'poison stinger', 'dmg': 35, 'chance': 65, 'potence': 2, 'duration': 4, 'effect': 'poison', 'target': 'player', 'desc':'A deadly Aculeo stinger injects you with venom. 65% chance to inflict **poison** for 4 turns, 35 DMG.'},
    
    'wolf dash': {'name': 'wolf dash', 'dmg': 30, 'chance': 0, 'potence': 1, 'duration': 0, 'effect': '', 'target': 'player', 'desc':'The Alpha Wolf runs at you with full speed. 30 DMG.'},
    'wolf pounce': {'name': 'wolf pounce', 'dmg': 40, 'chance': 50, 'potence': 1, 'duration': 2, 'effect': 'dizziness', 'target': 'player', 'desc':'The Alpha Wolf jumps at you with full speed. 40 DMG.'},
    'call of the leader': {'name': 'call of the leader', 'dmg': 5, 'chance': 100, 'potence': 1, 'duration': 0, 'effect': '', 'target': 'player', 'desc':'A ghastly howl calls for reinforcements. Revives the wolves in battle, 5 DMG.'},
    'shriek of the leader': {'name': 'call of the leader', 'dmg': 40, 'chance': 65, 'potence': 1, 'duration': 1, 'effect': 'broken armour', 'target': 'player', 'desc':'A ghastly shreak calls for reinforcements. It is so loud that it shatters armour, 40 DMG.'},
    'blood stare': {'name': 'blood stare', 'dmg': 10, 'chance': 100, 'potence': 3, 'duration': 4, 'effect': 'bleeding', 'target': 'player', 'desc':'The intimidating stare of the Alpha Wolf makes you bleed. 100% chance to inflict **bleeding** for 4 turns, 10 DMG.'},
    'blood gaze': {'name': 'blood gaze', 'dmg': 50, 'chance': 100, 'potence': 7, 'duration': 5, 'effect': 'bleeding', 'target': 'player', 'desc':'The beastial gaze of the Alpha Wolf makes you bleed. 100% chance to inflict **bleeding** for 5 turns, 50 DMG.'},
    
    'fireball': {'name': 'fireball', 'dmg': 41, 'chance': 40, 'potence': 2, 'duration': 3, 'effect': 'burning', 'target': 'player', 'desc':'A flaming ball hurtles towards you. 40% chance to inflict **burning(2)** for 3 turns, 41 DMG.'},

    'bubble blast': {'name': 'bubble blast', 'dmg': 20, 'chance': 80, 'potence': 2, 'duration': 3, 'effect': 'blindness', 'target': 'player', 'desc':'The water around you begins to foam and bubble. 80% chance to inflict **blindness** for 3 turns, 20 DMG.'},
    'tidal wave': {'name': 'tidal wave', 'dmg': 40, 'chance': 40, 'potence': 2, 'duration': 4, 'effect': 'dizziness', 'target': 'player', 'desc':'A huge powerful wave wipes over you. 40% chance to inflict **dizziness** for 4 turns, 40 DMG.'},
    'tsunami': {'name': 'tsunami', 'dmg': 40, 'chance': 60, 'potence': 3, 'duration': 5, 'effect': 'dizziness', 'target': 'player', 'desc':'A huge powerful wave wipes over you. 60% chance to inflict **dizziness** for 5 turns, 60 DMG.'},
    'ink cloud': {'name': 'ink cloud', 'dmg': 5, 'chance': 100, 'potence': 1, 'duration': 2, 'effect': 'broken armour', 'target': 'player', 'desc':'Some strange cloud of ink begins to dissolve your armour. 100% chance to inflict **broken armour** for 2 turns,  5 DMG.'},
    'tentacle wrap': {'name': 'ink cloud', 'dmg': 46, 'chance': 70, 'potence': 1, 'duration': 1, 'effect': 'paralysis', 'target': 'player', 'desc':'A tentacle begins to wrap around you. 70% chance to inflict **paralysis** for 1 turns,  46 DMG.'},
    'tentacle bloom': {'name': 'tentacel bloom', 'dmg': 1, 'chance': 100, 'potence': 0, 'duration': 0, 'effect': '', 'target': 'player', 'desc':'A tentacle emerges from the sand, 1 DMG.'},

    'leaf tornado': {'name': 'leaf tornado', 'dmg': 15, 'chance': 75, 'potence': 3, 'duration': 4, 'effect': 'poison', 'target': 'player', 'desc':'Sharp leaves swirl around the air. 75% chance to inflict **poison** for 4 turns, 15 DMG.'},
    'stinger storm': {'name': 'stinger storm', 'dmg': 40, 'chance': 100, 'potence': 5, 'duration': 4, 'effect': 'poison', 'target': 'player', 'desc':'Sharp stingers swirl around the air. 100% chance to inflict **poison** for 4 turns, 15 DMG.'},
    'beast pound': {'name': 'beast pound', 'dmg': 65, 'chance': 60, 'potence': 3, 'duration': 3, 'effect': 'dizziness', 'target': 'player', 'desc':'Visius Ent stomps you with two massive trunks. 60% chance to inflict **dizziness** for 3 turns, 65 DMG.'},
    'beast charge': {'name': 'beast charge', 'dmg': 75, 'chance': 65, 'potence': 1, 'duration': 3, 'effect': 'broken armour', 'target': 'player', 'desc':'Visius Ent charges at you you with two massive trunks. 65% chance to inflict **broken armour** for 3 turns, 75 DMG.'},
    'overgrowth': {'name': 'overgrowth', 'dmg': 1, 'chance': 85, 'potence': 3, 'duration': 3, 'effect': 'defence', 'target': 'allies', 'desc':'Vines grow around the battle field blocking attacks. 1 DMG.'},
    'earthquake': {'name': 'earthquake', 'dmg': 35, 'chance': 80, 'potence': 1, 'duration': 2, 'effect': 'paralysis', 'target': 'player', 'desc':'The ground beneath you shakes and shatters. 80% chance to inflict **paralysis** for 2 turns, 35 DMG.'},
}

spells = {
    #t1
    'fireball': {'name': 'fireball', 'tier': 1, 'dmg_percent': 120, 'chance': 25, 'potence': 1, 'duration': 3, 'effect': 'burning', 'target': 'enemy', 'cost': 8, 'upgrade': {'DMG%': 6, 'CHANCE': 5, 'DURATION': 0, 'POTENCE': 0}, 'desc':'A classic for all rpgs, the fireball has a chance to burn targets.'},
    'super punch': {'name': 'super punch', 'tier': 1, 'dmg_percent': 110, 'chance': 40, 'potence': 1, 'duration': 3, 'effect': 'dizziness', 'target': 'enemy', 'cost': 7, 'upgrade': {'DMG%': 5, 'CHANCE': 10, 'DURATION': 0, 'POTENCE': 0}, 'desc':'A knockout punch that can make monsters dizzy for a few turns.'},
    'magic shield': {'name': 'magic shield', 'tier': 1, 'dmg_percent': 0, 'chance': 100, 'potence': 1, 'duration': 3, 'effect': 'defence', 'target': 'player', 'cost': 10, 'upgrade': {'DMG%': 0, 'CHANCE': 0, 'DURATION': 1, 'POTENCE': 0}, 'desc':'Create a shield of magic that will reduce the strength of incoming attacks.'},
    'poison cloud': {'name': 'poison cloud', 'tier': 1, 'dmg_percent': 30, 'chance': 50, 'potence': 1, 'duration': 2, 'effect': 'poison', 'target': 'multi', 'cost': 11, 'upgrade': {'DMG%': 3, 'CHANCE': 3, 'DURATION': 0, 'POTENCE': 1}, 'desc':'Summon a cloud of poisonous gas to intoxicate monsters.'},
    'regeneration': {'name': 'regeneration', 'tier': 1, 'dmg_percent': 0, 'chance': 100, 'potence': 1, 'duration': 5, 'effect': 'regeneration', 'target': 'player', 'cost': 18, 'upgrade': {'DMG%': 0, 'CHANCE': 0, 'DURATION': 0, 'POTENCE': 1}, 'desc':'Gradually heal yourself with magic in battle.'},
    #t2
    'earthquake': {'name': 'earthquake', 'tier': 2, 'dmg_percent': 40, 'chance': 30, 'potence': 1, 'duration': 1, 'effect': 'paralysis', 'target': 'multi', 'cost': 19, 'upgrade': {'DMG%': 5, 'CHANCE': 5, 'DURATION': 0, 'POTENCE': 0}, 'desc':'Shake the ground beneath your enemies bringing them to the floor.'},
    'sharp arrow': {'name': 'sharp arrow', 'tier': 2, 'dmg_percent': 135, 'chance': 30, 'potence': 3, 'duration': 4, 'effect': 'bleeding', 'target': 'enemy', 'cost': 21, 'upgrade': {'DMG%': 7, 'CHANCE': 3, 'DURATION': 0, 'POTENCE': 0}, 'desc':'Shoot a sharp arrow that bursts the veins of any monster and can make them bleed.'},
    'warriors rune': {'name': 'warriors rune', 'tier': 2, 'dmg_percent': 0, 'chance': 100, 'potence': 1, 'duration': 4, 'effect': 'warrior spirit', 'target': 'player', 'cost': 18, 'upgrade': {'DMG%': 0, 'CHANCE': 0, 'DURATION': 0, 'POTENCE': 1}, 'desc':'Call upon ancient warriors to give you strength.'},
    'burning rage': {'name': 'burning rage', 'tier': 2, 'dmg_percent': 120, 'chance': 80, 'potence': 1, 'duration': 3, 'effect': 'rage', 'target': 'player', 'cost': 15, 'upgrade': {'DMG%': 4, 'CHANCE': 4, 'DURATION': 0, 'POTENCE': 1}, 'desc':'Burn from the inside out with pure rage that boils your blood.'},
    'life drain': {'name': 'life drain', 'tier': 2, 'dmg_percent': 105, 'chance': 50, 'potence': 1, 'duration': 2, 'effect': 'bleeding', 'target': 'enemy', 'cost': 17, 'upgrade': {'DMG%': 5, 'CHANCE': 0, 'DURATION': 0, 'POTENCE':0}, 'desc':'Heal from the blood of your foes.'},
    
    #t3
    'meteor strike': {'name': 'meteor strike', 'tier': 3, 'dmg_percent': 68, 'chance': 40, 'potence': 2, 'duration': 1, 'effect': 'burning', 'target': 'multi', 'cost': 32, 'upgrade': {'DMG%': 4, 'CHANCE': 6, 'DURATION': 1, 'POTENCE': 0}, 'desc':'Send meteors from the sky hurling towards your enenmies.'},
    'icicle': {'name': 'icicle', 'tier': 3, 'dmg_percent': 140, 'chance': 40, 'potence': 1, 'duration': 2, 'effect': 'dizziness', 'target': 'enemy', 'cost': 24, 'upgrade': {'DMG%': 8, 'CHANCE': 3, 'DURATION': 0, 'POTENCE': 1}, 'desc':'Launch a frozen spike at your enemy, stunning them.'},
    'mighty protector': {'name': 'mighty protector', 'tier': 3, 'dmg_percent': 0, 'chance': 100, 'potence': 1, 'duration': 4, 'effect': 'protector', 'target': 'player', 'cost': 19, 'upgrade': {'DMG%': 0, 'CHANCE': 0, 'DURATION': 1, 'POTENCE': 0}, 'desc':'Absorb all incoming attacks to protect your allies.'},
    'shield shatter': {'name': 'shield shatter', 'tier': 3, 'dmg_percent': 90, 'chance': 80, 'potence': 1, 'duration': 1, 'effect': 'broken armour', 'target': 'enemy', 'cost': 35, 'upgrade': {'DMG%': 10, 'CHANCE': 2, 'DURATION': 1, 'POTENCE':0}, 'desc':'Strike your enemy\'s armour and watch it crumble.'},
    
    }

spell_final_costs = {
    'fireball': [['wheat',30],['magic dust', 200]],
    'super punch': [['bear claw', 6],['magic dust', 250]],
    'magic shield': [['clam shell', 20],['magic dust', 280]],
    'poison cloud': [['wasp stinger', 10],['magic dust', 400]],
    'regeneration': [['wisp essence', 25],['magic dust', 460]],

    'earthquake': [['sparkly sand', 30],['magic dust', 300]],
    'sharp arrow': [['magic fang', 3],['magic dust', 340]],
    'warriors rune': [['glass sword', 1],['magic dust', 420]],
    'life drain': [['blood', 35],['magic dust', 520]],
    'burning rage': [['blood', 35],['magic dust', 520]],

    'meteor strike': [['magic branch', 3],['magic dust', 700]],
    'icicle': [['magic crystal orb', 1],['magic dust', 600]],
    'mighty protector': [['crab armour', 1],['magic dust', 450]],
    'shield shatter': [['magic tentacle', 5],['magic dust', 650]],
    }

spell_costs = {
    'fireball': [['aurum', 200],['magic dust', 50]],
    'super punch': [['aurum', 200],['magic dust', 40]],
    'magic shield': [['aurum', 200],['magic dust', 60]],
    'poison cloud': [['aurum', 250],['magic dust', 75]],
    'regeneration': [['aurum', 300],['magic dust', 85]],

    'earthquake': [['aurum', 550],['magic dust', 145]],
    'sharp arrow': [['aurum', 500],['magic dust', 150]],
    'warriors rune': [['aurum', 550],['magic dust', 185]],
    'burning rage': [['aurum', 700],['magic dust', 120]],
    'life drain': [['aurum', 600],['magic dust', 215]],

    'meteor strike': [['aurum', 800],['magic dust', 250]],
    'icicle': [['aurum', 700],['magic dust', 175]],
    'mighty protector': [['aurum', 300],['magic dust', 145]],
    'shield shatter': [['aurum', 900],['magic dust', 225]],
    }

conditions = {
    'paralysis': {'desc': '&% less damage on the next turn, cannot flee', 'base':90, 'inc':0},
    'dizziness': {'desc': '&% less damage on the next turn, 15% chance to miss', 'base':35-10, 'inc':10},
    'blindness': {'desc': '&% to miss the next attack', 'base':30-10, 'inc':10},
    'poison': {'desc': '-&% HP each turn', 'base':5-1, 'inc':1},
    'rage': {'desc': '+30% CRIT (+10% each level), +20% DMG, -&% HP each turn', 'base':6-2, 'inc':2},
    'burning': {'desc': '-&% HP each turn. Higher DMG reduces the burning damage', 'base':7-1.2, 'inc':1.2},
    'bleeding': {'desc': '-3% HP each turn and -&% healing potency', 'base':25-10, 'inc':10},
    'broken armour': {'desc': '-&% DEF for the next turn', 'base':70, 'inc':0},
    'regeneration': {'desc': '+&% HP each turn', 'base':3-1, 'inc':1},
    'attunement': {'desc': '+&% MP each turn', 'base':3-1, 'inc':1},
    'defence': {'desc': '+&% DEF', 'base':30-10, 'inc':10},
    'protector': {'desc': '+&% DEF * amount of members in the party, absorb all enemy attacks', 'base':15, 'inc':0},
    'warrior spirit': {'desc': '+&% DMG', 'base':30-10, 'inc':10},
}

mob_loot = {
    'krakow': [['kraken ink', 0.1, [1,1]]],
    'crow': [['egg', 50, [1,2]],['feather', 50, [1,2]],['apple', 65, [1,1]],['stick', 100, [1,2]],['minae', 50, [1,1]], ['feather blade', 10, [1,1]]],
    'badger': [['badger fur', 60, [1,3]],['blueberry', 65, [1,1]],['stick', 80, [1,1]],['minae', 50, [1,2]], ['fluffy hat', 10, [1,1]]],
    'manihot': [['leaf', 75, [1,3]],['spud', 45, [1,2]],['minae', 50, [1,3]], ['leaf crown', 9, [1,1]]],
        'enchanted manihot': [['leaf', 100, [1,6]],['magic dust', 100, [15,25]],['spud', 100, [1,4]],['minae', 50, [5,15]], ['leaf crown', 30, [1,1]]],
    
    'scarecrow': [['wheat', 63, [1,2]],['minae', 50, [1,4]]],
    'serpens': [['scale', 50, [1,2]],['snake fang', 80, [1,3]],['minae', 50, [1,5]], ['fang knuckledusters', 8, [1,1]]],
    'boletus': [['fungus', 55 ,[1,3]],['truffle spores', 35, [1,3]],['minae', 50, [1,6]]],
        'enchanted boletus': [['magic dust', 100, [25,45]],['fungus', 100 ,[1,6]],['truffle spores', 50, [3,6]],['minae', 50, [5,30]], ['fungus armour', 30, [1,1]]],
    
    'suco': [['blood', 90, [1,3]], ['bat wing', 50 ,[1,2]],['minae', 50, [1,7]], ['blood staff', 5, [1,1]]],
        'enchanted suco': [['magic dust', 100, [45,65]],['blood', 100, [1,9]], ['bat wing', 100 ,[1,2]],['minae', 50, [1,35]], ['blood staff', 30, [1,1]]],
    
    'wolf pup': [['wolf meat', 55, [1,1]],['wolf fur', 40, [1,2]],['minae', 50, [1,8]]],
    'blood wolf': [['magic dust', 65, [3,5]],['minae', 50, [1,13]], ['blood', 100, [3,5]], ['ruby ring', 5, [1,1]]],
    'wolf': [['wolf meat', 65, [1,2]],['wolf fur', 70, [2,3]], ['wolf paw', 30, [1,1]],['minae', 50, [1,9]], ['fur tunic', 5, [1,1]]],
        'enchanted wolf': [['wolf meat', 85, [1,3]],['magic dust', 100, [65,80]],['wolf fur', 100, [3,7]], ['wolf paw', 100, [2,3]],['minae', 50, [1,45]], ['fur tunic', 30, [1,1]]],
    
    'seitaad': [['sparkly sand', 100 ,[1,3]],['minae', 50, [1,10]]],
        'enchanted seitaad': [['magic dust', 100, [80,85]],['sparkly sand', 100 ,[1,10]],['minae', 50, [1,50]]],
    
    'crab': [['shellfish', 40, [1,2]],['crab shell', 63, [1,3]], ['sparkly sand', 10, [1,5]],['minae', 50, [1,11]], ['crab armour', 5, [1,1]]],
    'clam': [['shellfish', 70, [1,1]],['clam shell', 45, [1,3]], ['pearl thread', 45, [1,4]], ['shiny pearl', 35, [1,2]],['minae', 50, [1,12]], ['pearlescent wand', 5, [1,1]]],
        'enchanted clam': [['shellfish', 100, [2,3]],['magic dust', 100, [85,105]],['clam shell', 100, [1,5]], ['pearl thread', 100, [1,10]], ['shiny pearl', 100, [1,5]],['minae', 50, [1,60]], ['pearlescent wand', 30, [1,1]]],
    
    'grizzly bear': [['bear fur', 80, [1,3]], ['bear claw', 30, [1,2]],['minae', 50, [1,13]], ['bear hat', 5, [1,1]]],
        'enchanted grizzly bear': [['magic dust', 100, [105,115]],['bear fur', 100, [2,7]], ['bear claw', 100, [2,3]],['minae', 50, [1,65]], ['bear hat', 30, [1,1]]],
    
    'silva wisp': [['silva flower', 65, [1,2]],['wisp essence', 50, [1,4]],['minae', 50, [1,14]], ['spirit flute', 5, [1,1]]],
        'enchanted silva wisp': [['magic dust', 100, [115,130]],['wisp essence', 100, [1,10]],['minae', 50, [1,70]], ['spirit flute', 30, [1,1]]],
    
    'aculeo': [['honey', 50, [1,2]],['wasp wing', 80, [1,2]], ['wasp stinger', 45, [1,1]],['minae', 50, [1,15]], ['wasp suit', 5, [1,1]]],

    'alpha wolf': [['small mp potion', 50, [1,1]],['small hp potion', 50, [1,1]],['wolf fur', 100, [6,10]], ['wolf paw', 100, [1,4]],['magic dust', 100, [40,49]],['minae', 100, [35,50]],['magic fang', 100, [1,2]], ['howling horn', 2, [1,1]], ['eye of the wolf', 3, [1,1]], ['wolf head', 4, [1,1]]],
    'alpha wolf (hard)': [['small mixed potion', 50, [1,1]],['medium hp potion', 50, [1,1]],['wolf fur', 100, [6,10]], ['wolf paw', 100, [1,4]],['magic dust', 100, [65,110]],['minae', 100, [50,80]],['magic fang', 100, [1,4]], ['howling horn', 4, [1,1]], ['eye of the wolf', 6, [1,1]], ['wolf head', 8, [1,1]]],
    'alpha wolf (extreme)': [['medium hp potion', 50, [1,1]],['medium mixed potion', 30, [1,1]],['wolf fur', 100, [6,10]], ['wolf paw', 100, [1,4]],['magic dust', 100, [65,100]],['minae', 100, [75,100]],['magic fang', 100, [1,6]], ['howling horn', 8, [1,1]], ['eye of the wolf', 12, [1,1]], ['wolf head', 16, [1,1]]],
    'king polypus': [['medium mp potion', 50, [1,1]],['small mixed potion', 50, [1,1]],['shellfish', 100, [2,7]],['clam shell', 100, [3,5]],['magic dust', 100, [55,66]],['crab shell', 100, [3,5]], ['shiny pearl', 100, [1,4]],['minae', 100, [50,75]],['magic tentacle', 100, [1,2]], ['tentacle chestplate', 3, [1,1]], ['coral sword', 3, [1,1]], ['inky ring', 2, [1,1]]],
    'king polypus (hard)': [['medium mixed potion', 20, [1,1]],['medium mp potion', 70, [1,1]],['shellfish', 100, [2,7]],['clam shell', 100, [3,5]],['magic dust', 100, [125,150]],['crab shell', 100, [3,5]], ['shiny pearl', 100, [1,4]],['minae', 100, [80,105]],['magic tentacle', 100, [1,4]], ['tentacle chestplate', 7, [1,1]], ['coral sword', 6, [1,1]], ['inky ring', 4, [1,1]]],
    'king polypus (extreme)': [['large mp potion', 20, [1,1]],['medium mixed potion', 50, [1,1]],['shellfish', 100, [2,7]],['clam shell', 100, [3,5]],['magic dust', 100, [125,150]],['crab shell', 100, [3,5]], ['shiny pearl', 100, [1,4]],['minae', 100, [100,135]],['magic tentacle', 100, [1,6]], ['tentacle chestplate', 13, [1,1]], ['coral sword', 10, [1,1]], ['inky ring', 8, [1,1]]],
    'tentacle': [['magic dust', 50, [5,15]]],
    'visius ent': [['medium hp potion', 35, [1,1]],['small hp potion', 60, [1,2]],['silva salad', 40, [1,3]],['stick', 60, [10,30]],['magic dust', 100, [67,80]],['wisp essence', 100, [5,15]], ['leaf', 100, [10,25]],['minae', 100, [75,95]],['magic branch', 80, [1,2]], ['grass blade', 2, [1,1]], ['trunk vambrace', 2, [1,1]], ['dark rose wand', 1, [1,1]]],
    'visius ent (hard)': [['medium mixed potion', 50, [1,1]],['medium hp potion', 60, [1,1]],['silva salad', 60, [1,3]],['stick', 60, [10,50]],['magic dust', 100, [140,160]],['wisp essence', 100, [5,25]], ['leaf', 100, [10,35]],['minae', 100, [130,160]],['magic branch', 100, [2,3]], ['grass blade', 3, [1,1]], ['trunk vambrace', 4, [1,1]], ['dark rose wand', 2, [1,1]], ['emerald lute', 3, [1,1]], ['thornbark robes', 2, [1,1]]],
    'visius ent (extreme)': [['large mixed potion', 20, [1,1]],['large hp potion', 35, [1,1]],['medium mixed potion', 50, [1,1]],['silva salad', 80, [1,3]],['stick', 70, [10,70]],['magic dust', 100, [160,180]],['wisp essence', 100, [5,45]], ['leaf', 100, [10,50]],['minae', 100, [160,210]],['magic branch', 100, [2,5]], ['grass blade', 5, [1,1]], ['trunk vambrace', 7, [1,1]], ['dark rose wand', 4, [1,1]], ['emerald lute', 5, [1,1]], ['thornbark robes', 4, [1,1]]],
}

help_text = [
    f'''--HELP CENTER-- page 1/3
    
This is a guide for all the commands and info you need to know!

--How to play the game:

Use the chat commands to do all sorts of actions such as: fight, craft, travel and much more.

It is recommended to fight monsters that are around your LVL for the best experience. You can check what LVL the monsters are in your curent area using /area.

Use /travel to move to different areas and explore what they have to offer, some areas have shops, others even have dangerous bosses.

Use the loot collected from monsters to craft better equipment or sell it for more 'aurum' (aurum is the currency of the game)

Defeat bosses for a small chance to gain powerful loot.

Fight together with friends for a funner and easier game. Use /party-help to find out more.
Or challenge your friends to a 1v1 PVP duel. Use /pvp-help to find out more.

The world of Pereger awaits you!

use ¤help <page number> to see other pages
page 2 - Useful commands
page 3 - Other commands
page 4 - Tips
''',
    f'''--HELP CENTER-- page 2/3
    
--USEFUL COMMANDS:

¤actions - Shows the main actions you can do in your area/battle

¤inventory - Shows your inventory, equipment and aurum

¤show-stats - Shows a detailed breakdown of your stats (damage, defence, etc.) and equipment

¤travel <area> - Travel to a nearby area. Check "¤actions" for nearby areas

¤fight <amount of monsters> - Fight between 1 and 3 monsters in your current area (does not work in towns)

¤whatis <item name> - Shows information about an item

¤whois <monster name> - Shows information about a monster

¤equip <item> - Equip an item from your inventory

¤unequip <slot name> - Unequip an item from an equipment slot (such as: weapon, armour, etc.)

¤area - Shows information about the current area
''',
    f'''--HELP CENTER-- page 3/3
 
--SHOP COMMANDS (can only be used in towns):

¤shop - Shows the available shop items

¤buy <item> <amount> - Buy an item from the shop (maximum 50 at a time)

¤sell <item> <amount> - Sell an item to the shop (must unequip item if it is equipped)

< INFO: Equipment does not stack like other items so you have to sell/buy them individually >


--BLACKSMITH COMMANDS (can only be used in towns except smith-check and smith-items):

¤smith-items <page number> - Shows the available smith items to craft, cost and stats

¤smith-craft <item> - Craft an item from the "¤smith-items" list

¤smith-check <item> <amount of upgrades (default 1)> - Show the cost for upgrading an item X amount of times>

¤smith-upgrade <item> <amount of upgrades (default 1)> - Upgrade an item X amount of times

< INFO: Upgrading an item will automatically sell other items of the same kind that are not upgraded >


--TAVERN COMMANDS (can only be used in towns):

¤rest - Rest at the tavern for 25 aurum. Restores HP and MP

¤tavern-gamble <amount> - Gamble up to 1000 aurum at a time. 45% to win double money. 55% to lose it

--INFORMATION COMMANDS:

/leaderboard - Shows the Top 20 players of a category (highest: lvl, stats, aurum)

/map - Shows where you are on the map

/pvp-help - Shows PVP commands

/party-help - Shows Party commands
''',
    f'''--HELP CENTER-- page 4/4
 
--TIPS:

> fighting multiple monsters gives increased rewards (2 monsters = 30% more xp and minae, 3 monsters = 60% more xp and minae)

> the town tavern provides a cheap way to restore HP and MP between battles

> bosses have a small chance to drop rare and powerful items

> if you have a large level difference between you and monsters, you will get less xp
'''
]

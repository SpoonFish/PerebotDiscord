
import os
import datetime
import src.funcs.formulas as formulas
import random
import src.consts as consts
def generate_daily(acc):
    level = acc.level
    choices = ['cook', 'xp', 'vote', 'travel', 'monster', 'boss', 'enchanted monster', 'elixir', 'spells', 'crits']
    if level < 10:
        choices.remove('spells')
        choices.remove('elixir')
        choices.remove('enchanted monster')
        choices.remove('boss')
    elif level < 20:
        choices.remove('boss')
    other_dailies = []
    for i in range(3):
        try:
            other_dailies.append(acc.vars[f"daily{i+1}"][0][0])
        except:
            continue
    to_remove = []
    for choice in choices:
        if choice in other_dailies:
            to_remove.append(choice)

    for choice in to_remove:
        choices.remove(choice)
    daily = []
    objective_type = random.choice(choices)
    if objective_type == 'cook':
        amount = round(random.uniform(3, max(8, acc.level * 0.76 + 5)))
        if level < 3:
            foods = ['apple pie', 'blueberry pie']
        elif level < 10:
            foods = ['apple pie', 'blueberry pie', 'fries', 'potato salad']
        elif level < 17:
            foods = ['fries', 'potato salad', 'stroganoff', 'wolf pasty']
        elif level < 25:
            foods = ['potato salad', 'stroganoff', 'seafood kebab', 'fish n chips', 'wolf pasty']
        else:
            foods = ['stroganoff', 'seafood kebab', 'fish n chips', 'wolf pasty', 'silva salad', 'honey apples']
        food = random.choice(foods)
        daily = ['cook', food, 0, amount]

    
    elif objective_type == 'xp':
        amount = round(formulas.get_next_xp(acc.level)/random.uniform(5.5,7.89)/50)*50
        
        daily = ['xp', '', 0, amount]
    
    elif objective_type == 'vote':
        daily = ['vote', '', 0, 1]
    
    elif objective_type == 'travel':
        amount = round(random.randint(20,45)/3)*3
        daily = ['travel', '', 0, amount]
    elif objective_type == 'monster':
        amount = round(random.uniform(max(25,acc.level**0.5*2+20), max(35, acc.level**0.5*5 + 35)))
        daily = ['monster', '', 0, amount]
    elif objective_type == 'enchanted monster':
        amount = round(random.uniform(max(25,acc.level**0.5*2+20), max(35, acc.level**0.5*5 + 35)))
        amount = max(4, round(amount*0.087))
        daily = ['enchanted monster', '', 0, amount]
    elif objective_type == 'elixir':
        daily = ['elixir', '', 0, 1]
    elif objective_type == 'spells':
        amount = round(acc.level * random.uniform(0.75,1.05) + 15)
        daily = ['spells', '', 0, amount]
    elif objective_type == 'crits':
        amount = round(acc.level * random.uniform(0.7,95) + 13)
        daily = ['crits', '', 0, amount]
    elif objective_type == 'boss':
        amount = round(random.uniform(max(25,acc.level**0.5*2+20), max(35, acc.level**0.5*5 + 35)))
        amount = random.randint(3,max(4, round(amount*0.087)))
        if level < 26:
            bosses = ['alpha wolf']
        elif level < 34:
            bosses = ['alpha wolf', 'king polypus', 'alpha wolf (hard)']
        elif level < 42:
            bosses = ['king polypus (hard)', 'visius ent', 'alpha wolf (exteme)']
        elif level < 50:
            bosses = ['king polypus (extreme)', 'alpha wolf (extreme)', 'visius ent (hard)']
        else:
            bosses = ['alpha wolf','king polypus (extreme)', 'visius (extreme)', 'visius ent (hard)']
        boss = random.choice(bosses)
        daily = ['boss', boss, 0, amount]

    return daily

    '''
    #for bounty oops...
    elif objective_type == 'monster':
        amount = round(random.uniform(8, max(18, acc.level/2 + 15)))
        if level < 3:
            monsters = ['crow', 'badger']
        elif level < 9:
            monsters = ['crow', 'badger', 'manihot', 'scarecrow']
        elif level < 15:
            monsters = ['manihot', 'scarecrow', 'serpens', 'boletus', 'suco']
        elif level < 20:
            monsters = ['wolf pup', 'wolf', 'serpens', 'boletus', 'suco']
        elif level < 25:
            monsters = ['seitaad', 'wolf', 'serpens', 'crab', 'wolf pup']
    '''


    



def get_dailies(acc, bypass_check = False):
    try:
        quest_timers = acc.vars["quest"]
        if not bypass_check:
            times = [int(i) for i in quest_timers[0].split('/')]
            next_quest_time = datetime.datetime(times[0],times[1],times[2],times[3],times[4],times[5])
            if datetime.datetime.now() < next_quest_time:
                return
    except:
        quest_time = datetime.datetime.now()
        str_quest_time = f"{quest_time.year}/{quest_time.month}/{quest_time.day}/{quest_time.hour}/{quest_time.minute}/{quest_time.second}"
        acc.vars['quest']= [str_quest_time, str_quest_time, str_quest_time]
        quest_timers = acc.vars["quest"]
        acc.vars['daily1'] = ["","",0,1]
        acc.vars['daily2'] = ["","",0,1]
        acc.vars['daily3'] = ["","",0,1]
    quest_time = datetime.datetime.now()+datetime.timedelta(days=1)
    new_quest_time = f"{quest_time.year}/{quest_time.month}/{quest_time.day}/{quest_time.hour}/{quest_time.minute}/{quest_time.second}"
    quest_timers[0] =  new_quest_time
    acc.vars['daily1'] = generate_daily(acc)
    acc.vars['daily2'] = generate_daily(acc)
    acc.vars['daily3'] = generate_daily(acc)

def get_inv(acc, item):
    inv = acc.inventory
    for i in inv:
        if i.name == item:
            return i
    return None

def get_total_boost(acc):
    stat_boost = {"any": False, "XP": 0, "LOOT": 0, "DMG": 0, "DEF": 0, "%.CRIT": 0, "%.CRIT.DMG":0, "%.SPELL.DMG":0, "%.SPELL.COST": 0, "MAX HP": 0, "MAX MP": 0, "HEAL": 0 }
    try:
        
        boosts = acc.vars["boost"]
        for i in range(0, len(acc.vars["boost"])-1, 2):
            stat_boost['any'] = True
            elixir = boosts[i]
            stats = consts.boosts[elixir]["stats"]
            for stat in stats:
                stat_boost[stat[0]] += stat[1]
    except:
        pass
    
    return stat_boost


def get_type(item):
    if item.endswith('elixir'):
        return 'elixir'
    try:
            
        i_type = item.split(' ')[1]
        if i_type in consts.item_types['sword']:
            type = 'sword'
        elif i_type in consts.item_types['shield']:
            type = 'shield'
        elif i_type in consts.item_types['wand']:
            type = 'wand'
        elif i_type in consts.item_types['glove']:
            type = 'glove'
        elif i_type in consts.item_types['helmet']:
            type = 'helmet'
        elif i_type in consts.item_types['armour']:
            type = 'armour'
        elif i_type in consts.item_types['mystic']:
            type = 'mystic'
        elif i_type in consts.item_types['ring']:
            type = 'ring'
        elif i_type in consts.item_types['instrument']:
            type = 'instrument'
        else:
            type = 'resource'
    except: 
        type = 'resource'
    if item in consts.item_types['food']:
        type = 'consumable'
    return type
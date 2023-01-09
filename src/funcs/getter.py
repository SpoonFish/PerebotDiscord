
import os
import src.consts as consts
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

import os
import configs
import consts
def get_inv(acc, item):
    inv = acc.inventory
    for i in inv:
        if i.name == item:
            return i
    return None

def get_type(item):
    
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
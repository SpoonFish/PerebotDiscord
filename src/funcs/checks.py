
import os
import src.configs as configs
import src.consts as consts
import src.account as account

ADMINS = ['spoon_fish#0', 'jeels_#0', 'Pereger#1760', 'Pointymctest2#7442']

def admin(user):
    is_admin = user.guild_permissions.administrator or user.name+'#'+user.discriminator in ADMINS
    return is_admin

def super_admin(user):
    return user.name+'#'+user.discriminator in ADMINS

def no_server_initiated(server_name):
    return server_name not in list(map(lambda x: x.name, account.serv_list))

def channel(channel):
    channel_id = configs.get_config(channel.guild.name, 'channel')
    if channel_id == 'all':
        return True
    return channel.id == channel_id

def account_exists(user, discord_user = 1):
    if discord_user: user = user.name+'#'+user.discriminator
    
    result = user in list(map(lambda x: x.name, account.acc_list))
    return result

def check_stackable(item):
    
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
    return type in consts.stackable_types


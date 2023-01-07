import math
import src.funcs.getter as getter
import src.consts as consts
import random
class Stat:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def spell_upgrade_cost(spell):
    costs = consts.spell_costs[spell.name]
    costs = [[cost[0],round(cost[1]*((spell.lvl*2)*(0.5+spell.tier/10))/5)*5] for cost in costs]
    return costs

def get_total_xp(acc):
    level_xp = 0
    for i in range(acc.level):
        level_xp += get_next_xp(i+1)
    level_xp += acc.xp
    return level_xp


def get_next_xp(level):
    #return math.ceil(level**(2+level/20) + level*30)
    return math.ceil((level**(1.65+level/26.7) + level*40 - 7)-450*(level/51)) +30

def get_spell_slots(level):
    return 1 + math.floor((level+5)/10)

def form_dmg(dmg, crit=0, crit_dmg=0):
    dmg = dmg * random.uniform(0.9,1.1)
    if random.randint(1,1000) <= crit*10:
        crit_dmg = 1+crit_dmg/100
        dmg = round(dmg * crit_dmg)
        return dmg, 1
    else:
        dmg = round(dmg)
        return dmg, 0

def form_spell_dmg(dmg, spell_dmg=0):
    dmg = dmg * random.uniform(0.9,1.1)
    spell_dmg = 1+spell_dmg/100
    dmg = round(dmg * spell_dmg)
    return dmg

def protect(dmg, df):
    reduced = df/8.5
    dmg = max(0, dmg-reduced)
    dmg =(dmg)*(1-df/400)
    return round(max(1, dmg))

def get_stats(acc):
    stats = {'HP': max_hp(acc.level), 'MP': max_mp(acc.level), 'DMG':  2+round(acc.level/3), 'DEF': 2+round(acc.level*1.3), '%.CRIT': 2, '%.CRIT.DMG': 50, '%.SPELL.DMG': 0}
    
    def stat_adder(equipment):
        try:
            for stat in equipment.stats:
                stats[stat.name] += stat.value
        except: return
    stat_adder(acc.weapon)
    stat_adder(acc.armour)
    stat_adder(acc.helmet)
    stat_adder(acc.offhand)
    stat_adder(acc.ring)
    stats['HP'] = round(stats['HP'])
    stats['MP'] = round(stats['MP'])
    for stat in stats:
        stats[stat]= round(stats[stat], 1)
    return stats

def max_hp(level):
    return 50 + level*6 - 6

def max_mp(level):
    return 50 + level*4 - 4

def get_upgrade_lvl(stats, item):
    base = consts.default_stats[item][0][1]
    dif = (stats[0].value-base)/(base/5)
    print(dif+1)
    return dif+1
def multi_upgrade_cost(u_lvl, item, amount):
    base = consts.default_stats[item][0][1]
    new_base = base/5
    try:
        xtra1 = consts.default_stats[item][1][1]
        if consts.default_stats[item][1][0] == 'LVL':
            raise
        new_xtra1 = xtra1/10
    except:
        new_xtra1 = 0
    try:
        xtra2 = consts.default_stats[item][2][1]
        if consts.default_stats[item][2][0] == 'LVL':
            raise
        new_xtra2 = xtra2/10
    except:
        new_xtra2 = 0
    try:
        xtra3 = consts.default_stats[item][3][1]
        if consts.default_stats[item][3][0] == 'LVL':
            raise
        new_xtra3 = xtra3/10
    except:
        new_xtra3 = 0
    m_cost = 0
    u_lvl -= 1
    orig_u_lvl = u_lvl
    for i in range(amount):
        u_lvl += 1
        if u_lvl == 25:
            break
        m_cost+=new_base*25*u_lvl
        m_cost+=new_xtra1*50*u_lvl
        m_cost+=new_xtra2*75*u_lvl
        m_cost+=new_xtra3*100*u_lvl
    dif = abs(orig_u_lvl-u_lvl)
    new_base *= dif
    new_xtra1 *= dif
    new_xtra2 *= dif
    new_xtra3 *= dif

    new_base = round(new_base, 1)
    new_xtra1 = round(new_xtra1,1)
    new_xtra2 = round(new_xtra2,1)
    new_xtra3 = round(new_xtra3,1)
    if getter.get_type(item) == 'ring' and item != 'nature ring':
        m_cost = round(m_cost*5)
        
        if item == 'midas ring':
            m_cost = round(m_cost*8)
    
    print(m_cost, new_base, new_xtra1, new_xtra2, new_xtra3)
    return m_cost, new_base, new_xtra1, new_xtra2, new_xtra3
def upgrade_cost(u_lvl, item):
    base = consts.default_stats[item][0][1]
    new_base = base/5
    try:
        xtra1 = consts.default_stats[item][1][1]
        if consts.default_stats[item][1][0] == 'LVL':
            raise
        new_xtra1 = xtra1/10
    except:
        new_xtra1 = 0
    try:
        xtra2 = consts.default_stats[item][2][1]
        if consts.default_stats[item][2][0] == 'LVL':
            raise
        new_xtra2 = xtra2/10
    except:
        new_xtra2 = 0
    try:
        xtra3 = consts.default_stats[item][3][1]
        if consts.default_stats[item][3][0] == 'LVL':
            raise
        new_xtra3 = xtra3/10
    except:
        new_xtra3 = 0
    m_cost = 0
    m_cost+=new_base*25*u_lvl
    m_cost+=new_xtra1*50*u_lvl
    m_cost+=new_xtra2*75*u_lvl
    m_cost+=new_xtra3*100*u_lvl
    if getter.get_type(item) == 'ring' and item != 'nature ring':
        m_cost = round(m_cost*5)
        if item == 'midas ring':
            m_cost = round(m_cost*8)
    
    print(m_cost, new_base, new_xtra1, new_xtra2, new_xtra3)
    return m_cost, new_base, new_xtra1, new_xtra2, new_xtra3
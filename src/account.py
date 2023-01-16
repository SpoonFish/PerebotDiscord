import src.funcs.formulas as formulas
import src.consts as consts
import src.counters as counters
import src.funcs.getter as getter
import random
import datetime
import src.funcs.checks as checks

class Server():
    def __init__(self, id, name, ephemeral, channel_id):
        self.id = id
        self.name = name
        self.ephemeral = ephemeral
        self.channel_id = channel_id
class Account():
    def __init__(self, id):
        self.id = id
        self.name = ''
        self.level = 1
        self.xp = 0
        inventory = [Item('wooden sword', 1)]
        self.inventory = inventory
        self.weapon = Item('wooden sword', 1)
        self.armour = ''
        self.helmet = ''
        self.offhand = ''
        self.ring = ''
        self.hp = 50
        self.mp = 50
        self.battle = Battle(0)
        self.area = 'Apple Orchard'
        self.aurum = 100
        self.spells = []
        self.equipped_spells = []
        self.total_stats = formulas.get_stats(self)
        self.spell_slots = 1
        self.party = None
        self.vars = {}
        

class Battle():
    def __init__(self, active, turn=0, enemy=[' ',' ',' '], e_hp = [0,0,0], e_spell_cd=[-1,0,0], e_cond=[' :0',' :0',' :0'],p_cd = 0, p_cond=[], acc='', mult = 1):
        self.active = active
        self.turn = int(turn)
        self.enemy = [Monster(x, mult) for x in enemy]
        self.e_hp = [round(mult*int(x)) for x in e_hp]
        try: 
            if p_cond[0] == '' or p_cond[0] == '0': p_cond = []
        except: pass
        print(p_cond)
        self.p_cond = [[Effect(x.split(':')[0][:-1],x.split(':')[0][-1]),int(x.split(':')[1])] for x in p_cond]
        print(e_cond)
        if acc == 'SpoonF1sh#5129':
            print('lol')
        print(':0'.split(':'))
        self.e_cond = [[Effect(x.split(':')[0][:-1],x.split(':')[0][-1]),int(x.split(':')[1])] for x in e_cond]
        self.e_spell_cd = []
        if e_spell_cd == [-1,0,0]:
            for i in self.enemy:
                if i.name != ' ':
                    self.e_spell_cd.append(0)
                else:
                    if consts.mob_stats[i.name]['SPELL.CD'] > 0:
                        cd = random.randint(1, consts.mob_stats[i.name]['SPELL.CD'])
                    else:
                        cd = 0
                    self.e_spell_cd.append(cd)
        else:
            self.e_spell_cd = [int(x) for x in e_spell_cd]
        self.potion_cd = int(p_cd)
        self.amount = 3

class Effect():
    def __init__(self, name, potence):
        self.name = name
        try:
            self.potence = int(potence)
        except:
            self.potence = 0


class Spell():
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl
        self.tier = consts.spells[name]['tier']
        self.mp_cost = consts.spells[name]['cost']
        up_dmg = consts.spells[name]['upgrade']['DMG%']
        up_chance = consts.spells[name]['upgrade']['CHANCE']
        up_duration = consts.spells[name]['upgrade']['DURATION']
        up_potence = consts.spells[name]['upgrade']['POTENCE']
        self.dmg = consts.spells[name]['dmg_percent'] + up_dmg*(lvl-1)
        self.chance = consts.spells[name]['chance'] + up_chance*(lvl-1)
        self.duration = consts.spells[name]['duration'] + up_duration*(lvl-1)
        self.potence = consts.spells[name]['potence'] + up_potence*(lvl-1)
        self.effect = consts.spells[name]['effect']
        self.target = consts.spells[name]['target']

    def calc_stats(self):
        up_dmg = consts.spells[self.name]['upgrade']['DMG%']
        up_chance = consts.spells[self.name]['upgrade']['CHANCE']
        up_duration = consts.spells[self.name]['upgrade']['DURATION']
        up_potence = consts.spells[self.name]['upgrade']['POTENCE']
        self.dmg = consts.spells[self.name]['dmg_percent'] + up_dmg*(self.lvl-1)
        self.chance = consts.spells[self.name]['chance'] + up_chance*(self.lvl-1)
        self.duration = consts.spells[self.name]['duration'] + up_duration*(self.lvl-1)
        self.potence = consts.spells[self.name]['potence'] + up_potence*(self.lvl-1)

def give_item(item, amount, acc):
    fitem = Item(item, amount)
    j = 0
    
    stack = 1
    if not checks.check_stackable(item): stack = 0
    if stack:
        stacked = 0
        for i in acc.inventory:
            if i.name == item:
                acc.inventory[j].amount += amount
                stacked = 1
                break
            j += 1
        if not stacked:
            acc.inventory.append(fitem)
    else:
        acc.inventory.append(fitem)


class EnemySpell():
    def __init__(self, name):
        self.name = name
        self.potence = consts.enemy_spells[name]['potence']
        self.dmg = consts.enemy_spells[name]['dmg']
        self.chance = consts.enemy_spells[name]['chance']
        self.duration = consts.enemy_spells[name]['duration']
        self.effect = consts.enemy_spells[name]['effect']
        self.target = consts.enemy_spells[name]['target']

class Monster():
    def __init__(self, name, mult=1):
        self.name = name
        if self.name == 'player':
            return
        self.max_hp = round(mult*consts.mob_stats[name]['HP'])
        self.dmg = consts.mob_stats[name]['DMG']
        self.df = consts.mob_stats[name]['DEF']
        self.crit = consts.mob_stats[name]['CRIT']
        self.crit_dmg = consts.mob_stats[name]['CRIT.DMG']
        self.lvl = consts.mob_stats[name]['LVL']
        self.xp = consts.mob_stats[name]['XP']
        self.spells = []
        for spell in consts.mob_stats[name]['SPELL']:
            self.spells.append(EnemySpell(spell))
        

class Stat():
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Item():
    def __init__(self, name, quantity, stats = ''):
        self.name = name
        self.amount = quantity
        try:
                
            i_type = name.split(' ')[-1]
            if i_type in consts.item_types['sword']:
                self.type = 'sword'
            elif i_type in consts.item_types['shield']:
                self.type = 'shield'
            elif i_type in consts.item_types['wand']:
                self.type = 'wand'
            elif i_type in consts.item_types['glove']:
                self.type = 'glove'
            elif i_type in consts.item_types['helmet']:
                self.type = 'helmet'
            elif i_type in consts.item_types['armour']:
                self.type = 'armour'
            elif i_type in consts.item_types['mystic']:
                self.type = 'mystic'
            elif i_type in consts.item_types['ring']:
                self.type = 'ring'
            elif i_type in consts.item_types['instrument']:
                self.type = 'instrument'
            else:
                self.type = 'resource'
        except: 
            self.type = 'resource'
        if name in consts.item_types['food']:
            self.type = 'consumable'

        
        if stats == '' and self.type in consts.statable_types:
            self.stats = []
            for stat in consts.default_stats[name]:
                self.stats.append(Stat(stat[0], stat[1]))
        else:
            self.stats = stats

        if not isinstance (self.stats, str):
            self.upgrade_lvl = formulas.get_upgrade_lvl(self.stats, self.name)
        else:
            self.upgrade_lvl = 0



def create_account(user):
    name = user.name+'#'+user.discriminator
    account = Account(user.id)
    account.name = name
    account.level = 1
    account.xp = 0
    inventory = [Item('wooden sword', 1)]
    account.inventory = inventory
    account.weapon = Item('wooden sword', 1)
    account.armour = ''
    account.helmet = ''
    account.offhand = ''
    account.ring = ''
    account.target=0
    account.hp = 50
    account.mp = 50
    account.battle = Battle(0)
    account.area = 'Apple Orchard'
    account.aurum = 100
    account.spells = []
    quest_time = datetime.datetime.now() #also can be used as account creation time
    str_quest_time = f"{quest_time.year}/{quest_time.month}/{quest_time.day}/{quest_time.hour}/{quest_time.minute}/{quest_time.second}"
    account.vars = {'quest': [str_quest_time, str_quest_time, str_quest_time], 'daily1': ["","",0,1], 'daily2': ["","",0,1], 'daily3': ["","",0,1]} #for the 3 timed quests (daily, weekly, bounty)
    dailies = getter.get_dailies(account)
    account.equipped_spells = []
    account.total_stats = formulas.get_stats(account)
    account.spell_slots = formulas.get_spell_slots(account.level)
    #account.party = party_manager.get_party(name, party_manager.party_list)
    acc_list.append(account)
    write_file()

def get_account(user, discord_user = 1) -> Account:
    if discord_user:
        name = user.name+'#'+user.discriminator
    else:
        name = user
    for account in acc_list:
        if account.name == name:
            return account
    return None




def initialize_serv_file(file):
    serv_list = []
    with open(file, 'r', encoding = "utf-8") as f:
        line = ' '
        while line != '':
            server = ''
            line = f.readline().replace('\n', '')
            if line != '' and not line.startswith(' - '):
                server_id = int(line.replace(':', ''))
                print(server_id)
                lines = [f.readline() for x in range(2)]
                i = 0
                for bline in lines:
                    if bline == '': continue
                    bline = bline[bline.index(':')+2:].replace('\n', '')
                    if i == 0:
                        ephemeral = bline
                    elif i == 1:
                        channel_id = bline
                        if channel_id != 'all':
                            channel_id = int(channel_id)

                    i+=1
                server = Server(server_id, '', ephemeral, channel_id)
                serv_list.append(server)
    return serv_list

def initialize_file(file):
    acc_list = []
    with open(file, 'r', encoding = "utf-8") as f:
        line = ' '
        while line != '':
            account = ''
            line = f.readline().replace('\n', '')
            if line != '' and not line.startswith(' - '):
                account_id = int(line.replace(':', ''))
                print(account_id)
                account = Account(account_id)
                lines = [f.readline() for x in range(16)]
                for bline in lines:
                    if bline == '': continue
                    p = bline
                    bline = bline[bline.index(':')+2:].replace('\n', '')
                    lines[lines.index(p)] = bline
                print(lines)
                account.level = int(lines[0])
                account.xp = int(lines[1])
                inventory = []
                for i in lines[2].split(','):
                    i = i.split('-')
                    if len(i) > 2:
                        stats = []
                        stl = i[2:]
                        for stat in stl:
                            stat = stat.replace('+', '')
                            statv = stat.split(' ')[0]
                            statn = stat.split(' ')[1]
                            stats.append(Stat(statn, float(statv)))
                        inventory.append(Item(i[0], int(i[1]), stats))
                    else:
                        try:
                            inventory.append(Item(i[0], int(i[1])))
                        except IndexError:
                            pass
                account.inventory = inventory
                i = lines[3].split('-')
                stats = []
                stl = i[2:]
                for stat in stl:
                    stat = stat.replace('+', '')
                    statv = stat.split(' ')[0]
                    statn = stat.split(' ')[1]
                    stats.append(Stat(statn, float(statv)))
                try:
                    i = Item(i[0], int(i[1]), stats)
                except: i = ''
                account.weapon = i
                i = lines[4].split('-')
                stats = []
                stl = i[2:]
                for stat in stl:
                    stat = stat.replace('+', '')
                    statv = stat.split(' ')[0]
                    statn = stat.split(' ')[1]
                    stats.append(Stat(statn, float(statv)))
                try:
                    i = Item(i[0], int(i[1]), stats)
                except: i = ''
                account.armour = i
                i = lines[5].split('-')
                stats = []
                stl = i[2:]
                for stat in stl:
                    stat = stat.replace('+', '')
                    statv = stat.split(' ')[0]
                    statn = stat.split(' ')[1]
                    stats.append(Stat(statn, float(statv)))
                try:
                    i = Item(i[0], int(i[1]), stats)
                except: i = ''
                account.helmet = i
                i = lines[6].split('-')
                stats = []
                stl = i[2:]
                for stat in stl:
                    stat = stat.replace('+', '')
                    statv = stat.split(' ')[0]
                    statn = stat.split(' ')[1]
                    stats.append(Stat(statn, float(statv)))
                try:
                    i = Item(i[0], int(i[1]), stats)
                except: i = ''
                account.offhand = i
                i = lines[7].split('-')
                stats = []
                stl = i[2:]
                for stat in stl:
                    stat = stat.replace('+', '')
                    statv = stat.split(' ')[0]
                    statn = stat.split(' ')[1]
                    stats.append(Stat(statn, float(statv)))
                try:
                    i = Item(i[0], int(i[1]), stats)
                except: i = ''
                account.ring = i
                account.hp = int(lines[8])
                account.mp = int(lines[9])
                data = lines[10].split('-')
                if lines[10][0] == '0':
                    battle = Battle(0)
                elif lines[10][0] == '2':
                    battle = Battle(-1)
                else:
                    print(account.name)
                    battle = Battle(int(data[0]), data[1], data[2].split(','), data[3].split(','), data[4].split(','), data[5].split(','), data[6], data[7].split(','), account.name)
                    print(battle.e_cond)
                account.battle = battle
                account.area = lines[11]
                account.aurum = int(lines[12])
                account.total_stats = formulas.get_stats(account)
                spells = []
                for i in lines[13].split(','):
                    if i == '': continue
                    i = i.split('-')
                    spells.append(Spell(i[0], int(i[1])))
                account.spells = spells

                espells = []
                for j in lines[14].split(','):
                    if j == '':
                        continue
                    espells.append(j)
                try: account.target = espells[0]
                except: account.target = 0
                account.equipped_spells = espells[1:]
                
                if lines[15] != '':
                    for j in lines[15].split(';'):
                        components = j.split('-')
                        varname = components[0]
                        try:varvalue = components[1].split(',')
                        except: continue
                        for i, val in enumerate(varvalue):
                            if val.isdigit():
                                varvalue[i] = int(val)
                        account.vars[varname] = varvalue

                acc_list.append(account)
        return acc_list

def file_statter(item):
    if isinstance(item, str) or isinstance(item, list):
        return ''
    string = f'{item.name}-{item.amount}'
    for stat in item.stats:
        string += f'-+{stat.value} {stat.name}'
    return string
acc_list = initialize_file('assets/accounts.csv')
serv_list = initialize_serv_file('assets/servers.csv')
print(acc_list)
def write_serv_file(serv_list= serv_list, file = 'assets/servers.csv'):
    if 1:
        with open(file, 'w') as f:
            for server in serv_list:
                f.write(str(server.id)+':\n')
                f.write(' - Ephemeral: '+str(server.ephemeral)+'\n')
                f.write(' - ChannelId: '+str(server.channel_id)+'\n')
                

    else:
        print('Error writing file')
def write_file(acc_list = acc_list, file = 'assets/accounts.csv'):
    if 1:
        with open(file, 'w', encoding = "utf-8") as f:
            for account in acc_list:
                getter.get_dailies(account)
                try:
                    boosts = account.vars["boost"]
                    for i in range(7, 0, -2):
                        if i > len(boosts)-1:
                            continue
                        date = boosts[i]
                        now = datetime.datetime.now()
                        times = [int(i) for i in date.split('/')]
                        end_time = datetime.datetime(times[0],times[1],times[2],times[3],times[4],times[5])
                        if now > end_time:
                            account.vars["boost"].pop(i)
                            account.vars["boost"].pop(i-1)

                        if len(account.vars["boost"]) == 0:
                            account.vars.popitem("boost")



                except: pass

                #print(account.name)
                f.write(str(account.id)+':\n')
                f.write(' - Lvl: '+str(account.level)+'\n')
                f.write(' - Xp: '+str(account.xp)+'\n')
                inv = ''
                for i in account.inventory:
                    if i.type in consts.statable_types:
                        st = ''
                        for stat in i.stats:
                            st += '-+'+str(stat.value)+' '+stat.name
                        inv += i.name+'-'+str(i.amount)+st+','
                    else:
                        inv += i.name+'-'+str(i.amount)+','
                f.write(' - Inv: '+inv+'\n')
                w_s = file_statter(account.weapon)
                f.write(' - Weapon: '+w_s+'\n')
                a_s = file_statter(account.armour)
                f.write(' - Armour: '+a_s+'\n')
                h_s = file_statter(account.helmet)
                f.write(' - Helmet: '+h_s+'\n')
                o_s = file_statter(account.offhand)
                f.write(' - Offhand: '+o_s+'\n')
                r_s = file_statter(account.ring)
                f.write(' - Ring: '+r_s+'\n')
                f.write(' - Hp: '+str(account.hp)+'\n')
                f.write(' - Mp: '+str(account.mp)+'\n')
                pcond = f''
                for cond in account.battle.p_cond:
                    pcond += f'{cond[0].name}{cond[0].potence}:{cond[1]},'
                if pcond == ',':
                    pcond = ''
                else:
                    pcond = pcond[:-1]
                
                e1 = f'{account.battle.e_cond[0][0].name}{account.battle.e_cond[0][0].potence}:{account.battle.e_cond[0][1]}'
                e2 = f'{account.battle.e_cond[1][0].name}{account.battle.e_cond[1][0].potence}:{account.battle.e_cond[1][1]}'
                e3 = f'{account.battle.e_cond[2][0].name}{account.battle.e_cond[2][0].potence}:{account.battle.e_cond[2][1]}'
                if e1 == ':0': e1 = '0:0'
                if e2 == ':0': e2 = '0:0'
                if e3 == ':0': e3 = '0:0'
                econd = f'{e1},{e2},{e3}'
                bat_enemy = f'{account.battle.enemy[0].name},{account.battle.enemy[1].name},{account.battle.enemy[2].name}'
                ehp = f'{account.battle.e_hp[0]},{account.battle.e_hp[1]},{account.battle.e_hp[2]}'
                ecd = f'{account.battle.e_spell_cd[0]},{account.battle.e_spell_cd[1]},{account.battle.e_spell_cd[2]}'
                if account.battle.active == -1:
                    f.write(f' - Battle: 2-{account.battle.turn}-{bat_enemy}-{ehp}-{ecd}-{econd}-{account.battle.potion_cd}-{pcond}\n')
                
                else:
                    f.write(f' - Battle: {int(account.battle.active)}-{account.battle.turn}-{bat_enemy}-{ehp}-{ecd}-{econd}-{account.battle.potion_cd}-{pcond}\n')
                f.write(' - Area: '+account.area+'\n')
                f.write(' - Aurum: '+str(account.aurum)+'\n')
                spells = ''
                for lvl_spell in account.spells:
                    spell = lvl_spell.name
                    lvl = lvl_spell.lvl
                    spells += f'{spell}-{lvl},'
                f.write(f' - Spells: {spells}\n')
                spells = spells[:-1]
                espells = f'{account.target},'
                for espell in account.equipped_spells:
                    espells += f'{espell},'
                espells = espells[:-1]
                f.write(f' - EqSpells: {espells}\n')

                
                string = ''
                for var in account.vars:
                    string += f'{var}-'
                    for val in account.vars[var]:
                        string += f'{val},'
                    if string != '':
                        string = string[:-1]
                    string += ';'
                if string != '':
                    string = string[:-1]
                f.write(f' - Vars: {string}\n')
        if file == 'assets/accounts.csv':
            counters.SAVES += 1
            if counters.SAVES % 25 == 0:
                write_file(acc_list, 'assets/backup1.csv')
                if counters.SAVES % 250 == 0:
                    write_file(acc_list, 'assets/backup2.csv')

    else:
        print('Error writing file')


write_file(acc_list)
write_serv_file(serv_list)
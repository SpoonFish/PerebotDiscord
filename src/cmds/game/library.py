import src.consts as consts
import src.counters as counters
import src.account as account
import src.funcs.formulas as formulas
import src.funcs.checks as checks
import random
import discord
import src.party_manager as party_manager
import src.counters as counters
import math
import src.funcs.getter as getter
import src.configs as configs
import src.image_generator as image_generator
import src.pvp_manager as pvp_manager

async def upgrade(message, spell, acc, pre, hide):
    if spell not in consts.spells.keys():
        await message.respond(f'**{spell}** does not exist', ephemeral=hide)
        return
    if spell not in list(map(lambda x: x.name, acc.spells)):
        await message.respond(f'You have not bought **{spell}** yet', ephemeral=hide)
        return

    s = 0
    for pspell in acc.spells:
        if spell == pspell.name:
            spell = pspell
            if spell.lvl > 4:
                await message.respond(f'That spell is already at maximum level', ephemeral=hide)
                return
            break
        s+=1

    if spell.lvl != 4:
        costs = formulas.spell_upgrade_cost(spell)
    else:
        costs = consts.spell_final_costs[spell.name]
    valid = 1
    print(costs)
    removages = []
    not_enoughs = ''
    for cost in costs:
        if cost[0] == 'aurum':
            if acc.aurum >= cost[1]:
                removages.append(['aurum', cost[1]])
                continue
            else:
                valid = 0
                not_enoughs += f'You do not have enough **aurum**, you need {cost[1]} aurum, you have {acc.aurum} aurum\n'
        else:
            j = 0
            found = 0
            for item in acc.inventory:
                if item.name == cost[0]:
                    found = 1
                    if item.amount >= cost[1]:
                        removages.append([j, cost[1]])
                    else:
                        valid = 0
                        not_enoughs += f'You do not have enough **{cost[0]}**, you need {cost[1]} {cost[0]}, you have {item.amount} {cost[0]}\n'
                j+=1
            if not found:
                valid = 0
                not_enoughs += f'You do not have any **{cost[0]}**, you need {cost[1]} {cost[0]}\n'

    if not valid:
        await message.respond(not_enoughs, ephemeral=hide)
        return

    for remove in removages:
        print(remove)
        if remove[0] == 'aurum':
            acc.aurum -= remove[1]
        else:
            acc.inventory[remove[0]].amount -= remove[1]
            if acc.inventory[remove[0]].amount == 0:
                acc.inventory.pop(remove[0])
    
    for item in acc.inventory:
        if item.amount == 0:
            try:
                acc.inventory.remove(account.Item(item.name,item.amount))
            except:
                pass

    acc.spells[s].lvl += 1
    acc.spells[s].calc_stats()
    account.write_file()
    await message.respond(f'Upgraded **{acc.spells[s].name}** from LVL {acc.spells[s].lvl-1} to **LVL {acc.spells[s].lvl}**', ephemeral=hide)

async def buy(message, spell, acc, pre, hide):
    if spell not in consts.spells.keys():
        await message.respond(f'**{spell}** does not exist', ephemeral=hide)
        return
    if spell in list(map(lambda x: x.name, acc.spells)):
        await message.respond(f'You already have this spell', ephemeral=hide)
        return

    spell = account.Spell(spell, 1)

    if (spell.tier-1) > acc.level:
        await message.respond(f'You have not unlocked **Tier {spell.tier} spells** yet', ephemeral=hide)
        return

    costs = consts.spell_costs[spell.name]
    valid = 1
    print(costs)
    removages = []
    not_enoughs = ''
    for cost in costs:
        if cost[0] == 'aurum':
            if acc.aurum >= cost[1]:
                removages.append(['aurum', cost[1]])
                continue
            else:
                valid = 0
                not_enoughs += f'You do not have enough **aurum**, you need {cost[1]} aurum, you have {acc.aurum} aurum\n'
        else:
            j = 0
            found = 0
            for item in acc.inventory:
                if item.name == cost[0]:
                    found = 1
                    if item.amount > cost[1]:
                        removages.append([j, cost[1]])
                    else:
                        valid = 0
                        not_enoughs += f'You do not have enough **{cost[0]}**, you need {cost[1]} {cost[0]}, you have {item.amount} {cost[0]}\n'
                j+=1
            if not found:
                valid = 0
                not_enoughs += f'You do not have any **{cost[0]}**, you need {cost[1]} {cost[0]}\n'

    if not valid:
        await message.respond(not_enoughs, ephemeral=hide)
        return

    for remove in removages:
        print(remove)
        if remove[0] == 'aurum':
            acc.aurum -= remove[1]
        else:
            acc.inventory[remove[0]].amount -= remove[1]
    
    for item in acc.inventory:
        if item.amount == 0:
            try:
                acc.inventory.remove(account.Item(item.name,item.amount))
            except:
                pass

    acc.spells.append(spell)
    account.write_file()
    await message.respond(f'You bought **{spell.name}**!', ephemeral=hide)


async def spells(message, tier, acc, pre, hide):
    if tier == '':
        tier = 1
    else:
        try:
            tier = int(tier)
        except:
            await message.respond(f'{tier} is not a valid tier number', ephemeral=hide)
            return
    if (tier-1) * 10 > acc.level:
        await message.respond(f'```You can only unlock tier {tier} spells at level {tier*10-10}```', ephemeral=hide)
        return


    body = f'```\n< TIER {tier} SPELLS >\n\n'
    i = 0
    
    magic = getter.get_inv(acc, 'magic dust')
    if magic == None:
        magic = 0
    else:
        magic = magic.amount
    for spell in consts.spells:
        lvl = 1
        dmg = consts.spells[spell]['dmg_percent']
        chance = consts.spells[spell]['chance']
        effect = consts.spells[spell]['effect']
        potence = consts.spells[spell]['potence']
        duration = consts.spells[spell]['duration']
        target = consts.spells[spell]['target']
        mp = consts.spells[spell]['cost']
        for pspell in acc.spells:
            if pspell.name == spell:
                lvl = pspell.lvl
                dmg = pspell.dmg
                chance = pspell.chance
                effect = pspell.effect
                potence = pspell.potence
                duration = pspell.duration
                target = pspell.target
                mp = pspell.mp_cost
        if consts.spells[spell]['tier'] != tier:
            continue
        turn_plural = ''
        if duration > 1:
            turn_plural = 's'
        if dmg > 0:
            stat_string = f'{dmg}% DMG'
            if chance > 0:
                if target == 'multi':
                    stat_string += f' to all enemies, {chance}% chance to cause {effect}({potence}) to all enemies for {duration} turn{turn_plural}, {mp} MP'
                else:
                    stat_string += f', {chance}% chance to cause {effect}({potence}) for {duration} turn{turn_plural}, {mp} MP'

        elif chance == 100:
            if target == 'player':
                stat_string = f'Gives {effect}({potence}) to the player for {duration} turn{turn_plural}, {mp} MP'
            elif target == 'enemy':
                stat_string = f'Gives {effect}({potence}) to an enemy for {duration} turn{turn_plural}, {mp} MP'
            elif target == 'multi':
                stat_string = f'Gives {effect}({potence}) to all enemies for {duration} turn{turn_plural}, {mp} MP'
        elif chance > 0:
            if target == 'player':
                stat_string = f'{chance}% chance to give {effect}({potence}) to the player for {duration} turn{turn_plural}, {mp} MP'
            elif target == 'enemy':
                stat_string = f'{chance}% chance to give {effect}({potence}) to an enemy for {duration} turn{turn_plural}, {mp} MP'
            elif target == 'multi':
                stat_string = f'{chance}% chance to give {effect}({potence}) to all enemies for {duration} turn{turn_plural}, {mp} MP'


        
        if spell not in list(map(lambda x: x.name, acc.spells)):
            cost_str = 'BUY: '
            for cost in consts.spell_costs[spell]:
                cost_str += f'{cost[1]} {cost[0]}, '
        elif lvl < 5:
            cost_str = f'UPGRADE TO LVL {lvl+1}: '
            if lvl != 4:
                costs = formulas.spell_upgrade_cost(account.Spell(spell,lvl))
            else:
                costs = consts.spell_final_costs[spell]
            for cost in costs:
                cost_str += f'{cost[1]} {cost[0]}, '
        else:
            cost_str = 'MAX LVL  '

        cost_str = cost_str[:-2]
        if lvl < 5 and spell in list(map(lambda x: x.name, acc.spells)):
            cost_str +='\n└– '
            for upg in consts.spells[spell]['upgrade']:
                if consts.spells[spell]["upgrade"][upg] == 0:
                    continue
                statname = ''
                if upg == 'DMG%':
                    statname = '% DMG'
                elif upg == 'CHANCE':
                    statname = '% effect chance'
                elif upg == 'POTENCE':
                    statname = 'effect lvl'
                elif upg == 'DURATION':
                    statname = 'effect duration'
                cost_str += f'+{consts.spells[spell]["upgrade"][upg]} {statname}, '
            
            cost_str = cost_str[:-2]
        body += f'{spell.center(14)} (LVL {lvl}) - {stat_string.center(37)}\n{cost_str}\n\n'
        i += 1
    body += f'\nYou have {magic} magic dust\nUse `/equip-spell <spell>` and `/unequip-spell <spell>` to equip/unequip spells\nUse `/library-buy <spell>` and `/library-upgrade <spell>` to buy/upgrade spells'
    body += '\n```'
    print(body)
    await message.respond(body, ephemeral=hide)

async def craft(message, spell, acc, pre, hide):
    if spell == '':
        await message.respond(f'You need to specify an spell to craft from {pre}smith-spells', ephemeral=hide)
        return  
    i = getter.get_inv(acc, spell)
        
    if i != None and i.upgrade_lvl > 1:
        await message.respond(f'You already have an upgraded version of **{spell}**', ephemeral=hide)
        return
    valid = 1
    body = ''
    for cost in consts.smith_costs[spell]:
        aurum = 0
        if cost[0] == 'aurum':
            aurum = 1
        if aurum and int(cost[1]) > acc.aurum:
            body += f'You do not have enough **{cost[0]}** to craft **{spell}**\n'
            valid = 0
        
        elif getter.get_inv(acc, cost[0]) == None:
            if not aurum:
                body += f'You do not have any **{cost[0]}** in your inventory\n'
                valid = 0
        elif getter.get_inv(acc, cost[0]).amount < cost[1]:
            if not aurum:
                body += f'You do not have enough **{cost[0]}** to craft **{spell}**\n'
                valid = 0
    if valid == 0:
        body+=f'Use `{pre}smith spells` to see what you need\n'
        body+=f'Use `{pre}whatis <spell name>` to see where to find a resource\n'
        await message.respond(body, ephemeral=hide)
        return
    for cost in consts.smith_costs[spell]:
        j = 0
        for i in acc.inventory:
            if i.name == cost[0]:
                break
            j+=1
        if cost[0] != 'aurum': acc.inventory[j].amount -= cost[1]
        else: acc.aurum -= cost[1]
    acc.inventory.append(account.spell(spell, 1))
    account.write_file()
    await message.respond(f'You crafted a **{spell}**!', ephemeral=hide)
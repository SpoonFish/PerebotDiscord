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

async def check(message, item, amount, acc, pre, hide):
        if item == '¤':
            await message.respond(f'You need to specify an item to check', ephemeral=hide)
            return  
        i = getter.get_inv(acc, item)
        if i == None:
            await message.respond(f'You do not have **{item}** in your inventory', ephemeral=hide)
            return
        if i.upgrade_lvl >= 25:
            await message.respond(f'**{item}** is already at max upgrade level', ephemeral=hide)
            return
        if amount == '¤':
            amount = 1
        else: amount = int(amount)
        if amount + i.upgrade_lvl >= 25:
            amount -= round(amount + i.upgrade_lvl - 25)
        if amount == 1:
            f = formulas.upgrade_cost(i.upgrade_lvl, i.name)
        else:
            f = formulas.multi_upgrade_cost(i.upgrade_lvl, i.name, amount)
        
        body = f'''It will cost **{round(f[0]*2.5)} aurum** and **{round(f[0]*1.6)} minae** to upgrade **{item}** from level **{round(i.upgrade_lvl)}** to level **{min(25, round(i.upgrade_lvl) + amount)}**'''
        stats = i.stats[:-1]
        j = 1
        for stat in stats:
            body += f'\n{round(stat.value, 2)} {stat.name} -> {round(f[j]+stat.value, 2)} {stat.name}'
            j += 1
        if getter.get_type(i.name) == 'ring':
            if i.name == 'ruby ring':
                body += f'\n+{round(((1.2+(i.upgrade_lvl-1)*0.01)-1)*1000)/10}% loot chance -> +{round(((1.2+min(25, (i.upgrade_lvl+amount-1))*0.01)-1)*1000)/10}% loot chance'
            elif i.name == 'aqua ring':
                body += f'\n+{round(((1.1+(i.upgrade_lvl-1)*0.005)-1)*1000)/10}% more xp -> +{round(((1.1+min(25, (i.upgrade_lvl+amount-1))*0.005)-1)*1000)/10}% more xp'
            elif i.name == 'midas ring':
                body += f'\n+{round(((1.05+(i.upgrade_lvl-1)*0.006)-1)*1000)/10}% more sell value -> +{round(((1.05+min(25, (i.upgrade_lvl+amount-1))*0.006)-1)*1000)/10}% more sell value'
        body += f'\nupgrade level {round(i.upgrade_lvl)} -> upgrade level {min(25, round(i.upgrade_lvl) + amount)} '
        body += f'\n\nYou can upgrade this item with `{pre}smith-upgrade {item}`'
        print(body)
        await message.respond(body, ephemeral=hide)

async def upgrade(message, item, amount, acc, pre, hide):
        if item == '¤':
            await message.respond(f'You need to specify an item to upgrade', ephemeral=hide)
            return  
        i = getter.get_inv(acc, item)
        if i == None:
            await message.respond(f'You do not have **{item}** in your inventory', ephemeral=hide)
            return
        if i.upgrade_lvl >= 25:
            await message.respond(f'**{item}** is already at max upgrade level', ephemeral=hide)
            return
        if amount == '¤':
            amount = 1
        else: amount = int(amount)
        if amount == 1:
            f = formulas.upgrade_cost(i.upgrade_lvl, i.name)
        else:
            f = formulas.multi_upgrade_cost(i.upgrade_lvl, i.name, amount)
        if acc.aurum < round(f[0]*2.5):
            await message.respond(f'You do not have enough aurum to upgrade **{item}**. You need **{round(f[0]*2.5)}** aurum. You only have **{acc.aurum}** aurum', ephemeral=hide)
            return
        j = 0
        has_minae = 0
        for i in acc.inventory:
            if i.name == 'minae':
                has_minae = 1
                if i.amount < round(f[0]*1.6):
                    await message.respond(f'You do not have enough minae to upgrade **{item}**. You need **{round(f[0]*1.6)}** minae. You only have **{i.amount}** minae', ephemeral=hide)
                    return
                else:
                    break
            j+=1
        if has_minae == 0:
            await message.respond(f'You do not have enough minae to upgrade **{item}**. You need **{round(f[0]*1.6)}** minae. You do not have any minae in your inventory', ephemeral=hide)
            return
        acc.aurum -= round(f[0]*2.5)
        acc.inventory[j].amount -= round(f[0]*1.6)
        j = 0
        for i in acc.inventory:
            if i.name == item:
                break
            j+=1

        acc.inventory[j].upgrade_lvl += amount
        if acc.inventory[j].upgrade_lvl > 25:
            acc.inventory[j].upgrade_lvl = 25
        acc.inventory[j].stats[0].value += f[1]
        try: 
            if  acc.inventory[j].stats[1].name == 'LVL':
                raise
            acc.inventory[j].stats[1].value += f[2]
        except: pass
        try: 
            if  acc.inventory[j].stats[2].name == 'LVL':
                raise
            acc.inventory[j].stats[2].value += f[3]
        except: pass
        try:
            if  acc.inventory[j].stats[3].name == 'LVL':
                raise
            acc.inventory[j].stats[3].value += f[4]
        except: pass

        body = f'You upgraded **{item}** to level **{round(acc.inventory[j].upgrade_lvl)}**'
        try: 
            if acc.weapon.name == item:
                acc.weapon = acc.inventory[j]
        except: pass
        try:
            if acc.armour.name == item:
                acc.armour = acc.inventory[j]
        except: pass
        try: 
            if acc.offhand.name == item:
                acc.offhand = acc.inventory[j]
        except: pass
        try:
            if acc.ring.name == item:
                acc.ring = acc.inventory[j]
        except: pass
        try:
            if acc.helmet.name == item:
                acc.helmet = acc.inventory[j]
        except: pass
        amount = 0
        j=0
        to_pops = []
        valid = 0
        while valid == 0:
            for i in acc.inventory:
                if i.name == item:
                    if i.upgrade_lvl < 2:
                        amount += 1
                        acc.inventory.pop(j)
                        j=0
                        break
                j+=1
            if j == len(acc.inventory):
                valid = 1
        if amount > 0:
            sell_price = consts.items[item]['sell'][0]
            body += f'\nYou also sold **{amount} other {item}** for **{amount*sell_price}** aurum'
            acc.aurum += amount*sell_price
        await message.respond(body, ephemeral=hide)
        acc.total_stats = formulas.get_stats(acc)
        account.write_file()


async def items(message, page, acc, pre, hide):
        if page == '':
            page = 1
        else:
            try:
                page = int(page)
            except:
                await message.respond(f'{page} is not a valid page number', ephemeral=hide)
                return
        if page > 3:
            page = 3


        body = f'```\npage {page}/3\n\n'
        i = 0
        for item in consts.smith_costs:
            if i < (page-1)*12:
                i += 1
                continue
            if i == 12+((page-1)*12):
                break
            desc = consts.items[item]['desc']
            cost_str = ''
            for cost in consts.smith_costs[item]:
                cost_str += f'{cost[1]} {cost[0]}, '
            body += f'{item}\n - {desc}\n - {cost_str}\n\n'
            i += 1
        body += '\n```'
        print(body)
        await message.respond(body, ephemeral=hide)

async def craft(message, item, acc, pre, hide):
        if item == '':
            await message.respond(f'You need to specify an item to craft from {pre}smith-items', ephemeral=hide)
            return  
        i = getter.get_inv(acc, item)
            
        if i != None and i.upgrade_lvl > 1:
            await message.respond(f'You already have an upgraded version of **{item}**', ephemeral=hide)
            return
        valid = 1
        body = ''
        for cost in consts.smith_costs[item]:
            aurum = 0
            if cost[0] == 'aurum':
                aurum = 1
            if aurum and int(cost[1]) > acc.aurum:
                body += f'You do not have enough **{cost[0]}** to craft **{item}**\n'
                valid = 0
            
            elif getter.get_inv(acc, cost[0]) == None:
                if not aurum:
                    body += f'You do not have any **{cost[0]}** in your inventory\n'
                    valid = 0
            elif getter.get_inv(acc, cost[0]).amount < cost[1]:
                if not aurum:
                    body += f'You do not have enough **{cost[0]}** to craft **{item}**\n'
                    valid = 0
        if valid == 0:
            body+=f'Use `{pre}smith items` to see what you need\n'
            body+=f'Use `{pre}whatis <item name>` to see where to find a resource\n'
            await message.respond(body, ephemeral=hide)
            return
        for cost in consts.smith_costs[item]:
            j = 0
            for i in acc.inventory:
                if i.name == cost[0]:
                    break
                j+=1
            if cost[0] != 'aurum': acc.inventory[j].amount -= cost[1]
            else: acc.aurum -= cost[1]
        acc.inventory.append(account.Item(item, 1))
        account.write_file()
        await message.respond(f'You crafted a **{item}**!', ephemeral=hide)
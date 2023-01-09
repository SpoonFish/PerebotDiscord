import src.consts as consts
import src.counters as counters
import src.account as account
import src.funcs.formulas as formulas
import src.funcs.checks as checks
import random
import discord
import datetime
import src.party_manager as party_manager
import src.counters as counters
import math
import src.funcs.getter as getter
import src.configs as configs
import src.image_generator as image_generator
import src.pvp_manager as pvp_manager


async def travel(message, area, acc, pre, hide, button=0, channel=0):
                
    if counters.SAVES % 20 <2 and channel != 0:
        try:
            file = discord.File('assets/accounts.csv')
            await channel.send('------------------------\naccounts:', file=file)
            file = discord.File('assets/parties.csv')
            await channel.send('parties:', file=file)
            file = discord.File('assets/servers.csv')
            await channel.send('servers:', file=file)
            file = discord.File('assets/pvp.csv')
            await channel.send('pvp:', file=file)
        except: pass
    if acc.battle.active:
        if button:
            await message.response.send_message(f'You are in a battle! You cannot travel right now', ephemeral=True)
        else:
            await message.respond(f'You are in a battle! You cannot travel right now', ephemeral=True)
    else:
        if getter.get_inv(acc, 'phase wings') == None:
            for area2 in consts.adjacent_areas[acc.area]:
                if area.lower().replace('1', 'i').replace('2', 'ii').replace('3', 'iii') == area2.lower() or area.lower() == area2.lower():
                    acc.area = area2
                    account.write_file()

                    body = f'You have traveled to `{area2}`!\nTravel again to:\n'
                    for i, area2 in enumerate(consts.adjacent_areas[acc.area]):
                        body += f'*{i+1} - {area2}*\n'
                    if button:
                        await message.response.send_message(body, ephemeral=True, view=Travel())
                    else:
                        await message.respond(body, ephemeral=True, view=Travel())
                    return
        else:
            area = area.title().replace('1', 'I').replace('2', 'II').replace('3', 'III')
            if area == 'Town I':
                area = 'Town 1'
            if area == 'Boat I':
                area = 'Boat 1'
            if area in consts.adjacent_areas:
                body = f'You have traveled to `{area}`!\nTravel again to:\n'
                acc.area = area
                account.write_file()
                for i, area2 in enumerate(consts.adjacent_areas[acc.area]):
                    body += f'*{i+1} - {area2}*\n'
                if button:
                    await message.response.send_message(body, ephemeral=True, view=Travel())
                else:
                    await message.respond(body, ephemeral=True, view=Travel())
                return
        body = f'You can travel to **nearby areas**:\n'
        for i, area2 in enumerate(consts.adjacent_areas[acc.area]):
            body += f'*{i+1} - {area2}*\n'
        if button:
            await message.response.send_message(body, ephemeral=True, view=Travel())
        else:
            await message.respond(body, ephemeral=True, view=Travel())

async def equip(message, item, acc, pre, hide):
    if getter.get_inv(acc, item) == None:
        await message.respond(f'You do not have **{item}** in your inventory', ephemeral=hide)
        return
    if item == '':
        await message.respond(f'You need to specify an item. Usage: `{pre}equip <item>`\nYou can unequip an item by using `{pre}unequip <slot>`', ephemeral=hide)
        return
    i = consts.items[item]
    stats = consts.default_stats[item]
    if acc.level < stats[-1][1]:
        await message.respond(f'You need to be at least **LVL {stats[-1][1]}** to use this item!', ephemeral=hide)
        return
    typ = getter.get_type(item)
    removed = 0
    if typ == 'sword' or typ == 'wand' or typ == 'instrument' or typ == 'glove':
        if acc.weapon != '': unequipped = f'\nYou unequipped {acc.weapon.name}'
        else: unequipped = ''
        acc.weapon = getter.get_inv(acc, item)
        removed = 1
        await message.respond(f'You equipped **{item}**{unequipped}', ephemeral=hide)
    elif typ == 'shield' or typ == 'mystic':
        if acc.offhand != '': unequipped = f'\nYou unequipped {acc.offhand.name}'
        else: unequipped = ''
        acc.offhand = getter.get_inv(acc, item)
        removed = 1
        await message.respond(f'You equipped **{item}**{unequipped}', ephemeral=hide)
    elif typ == 'helmet':
        if acc.helmet != '': unequipped = f'\nYou unequipped {acc.helmet.name}'
        else: unequipped = ''
        acc.helmet = getter.get_inv(acc, item)
        removed = 1
        await message.respond(f'You equipped **{item}**{unequipped}', ephemeral=hide)
    elif typ == 'armour':
        if acc.armour != '': unequipped = f'\nYou unequipped {acc.armour.name}'
        else: unequipped = ''
        acc.armour = getter.get_inv(acc, item)
        removed = 1
        await message.respond(f'You equipped **{item}**{unequipped}', ephemeral=hide)

    elif typ == 'ring':
        if acc.ring != '': unequipped = f'\nYou unequipped {acc.ring.name}'
        else: unequipped = ''
        acc.ring = getter.get_inv(acc, item)
        removed = 1
        await message.respond(f'You equipped **{item}**{unequipped}', ephemeral=hide)
    else:
        await message.respond(f'You cannot equip that item', ephemeral=hide)
    acc.total_stats = formulas.get_stats(acc)
    if acc.mp > round(acc.total_stats["MP"]):
        acc.mp = round(acc.total_stats["MP"])
    if acc.hp > round(acc.total_stats["HP"]):
        acc.hp = round(acc.total_stats["HP"])
    account.write_file()

async def unequip(message, slot, acc, pre,hide):
    add = 0
    if slot == '':
        await message.respond(f'You need to specify a slot. Usage: `{pre}unequip <slot>`', ephemeral=hide)
        return
    if slot == 'weapon':
        if acc.weapon == '':
            await message.respond(f'You do not have a weapon equipped', ephemeral=hide)
        else:
            await message.respond(f'You unequipped **{acc.weapon.name}**', ephemeral=hide)
            add = acc.weapon
            acc.weapon = ''
    elif slot == 'offhand':
        if acc.offhand == '':
            await message.respond(f'You do not have an offhand equipped', ephemeral=hide)
        else:
            await message.respond(f'You unequipped **{acc.offhand.name}**', ephemeral=hide)
            add = acc.offhand
            acc.offhand = ''
    elif slot == 'helmet':
        if acc.helmet == '':
            await message.respond(f'You do not have a helmet equipped', ephemeral=hide)
        else:
            await message.respond(f'You unequipped **{acc.helmet.name}**', ephemeral=hide)
            add = acc.helmet
            acc.helmet = ''
    elif slot == 'armour':
        if acc.armour == '':
            await message.respond(f'You do not have an armour equipped', ephemeral=hide)
        else:
            await message.respond(f'You unequipped **{acc.armour.name}**', ephemeral=hide)
            add = acc.armour
            acc.armour = ''
    elif slot == 'ring':
        if acc.ring == '':
            await message.respond(f'You do not have a ring equipped', ephemeral=hide)
        else:
            await message.respond(f'You unequipped **{acc.ring.name}**', ephemeral=hide)
            add = acc.ring
            acc.ring = ''
    else:
        await message.respond(f'{slot} is not a valid slot. You can unequip the following slots: weapon, offhand, helmet, armour, ring', ephemeral=hide)
    acc.total_stats = formulas.get_stats(acc)
    
    if acc.mp > round(acc.total_stats["MP"]):
        acc.mp = round(acc.total_stats["MP"])
    if acc.hp > round(acc.total_stats["HP"]):
        acc.hp = round(acc.total_stats["HP"])
    account.write_file()

async def equip_spell(message, spell, acc, pre,hide):
    if acc.battle.active:
        await message.respond(f'You cannot equip/unequip spells in battle', ephemeral=hide)
        return


    if spell not in consts.spells:
        await message.respond(f'**{spell}** does not exist', ephemeral=hide)
        return

    if len(acc.equipped_spells) >= formulas.get_spell_slots(acc.level):
        await message.respond(f'You already have maximum spells equipped! Unequip one with `/unequip-spell`', ephemeral=hide)
        return

    if spell not in list(map(lambda x: x.name, acc.spells)):
        await message.respond(f'You do not own that spell ({spell})', ephemeral=hide)
        return

    if spell in acc.equipped_spells:
        await message.respond(f'You have already equipped this spell', ephemeral=hide)
        return

    acc.equipped_spells.append(spell)
    await message.respond(f'Equipped **{spell}**! \nYou are currently using {len(acc.equipped_spells)}/{formulas.get_spell_slots(acc.level)} spell slots', ephemeral=hide)
    account.write_file()

async def unequip_spell(message, spell, acc, pre, hide):
    if acc.battle.active:
        await message.respond(f'You cannot equip/unequip spells in battle', ephemeral=hide)
        return
    if spell not in consts.spells:
        await message.respond(f'**{spell}** does not exist', ephemeral=hide)
        return

    if len(acc.equipped_spells) == 0:
        await message.respond(f'You have no spells equipped!', ephemeral=hide)
        return

    if spell not in acc.equipped_spells:
        await message.respond(f'**{spell}** is not equipped', ephemeral=hide)
        return
    
    acc.equipped_spells.remove(spell)
    await message.respond(f'Unequipped **{spell}**! \nYou are currently using {len(acc.equipped_spells)}/{formulas.get_spell_slots(acc.level)} spell slots', ephemeral=hide)
    account.write_file()


async def use(message, item, amount, acc, pre, hide):
    if amount == '¤':
        amount = 1
    else:
        try:
            amount = int(amount)
        except:
            await message.respond(f'{amount} is not a valid numeric amount', ephemeral=hide)
            return
    if amount > 1 and acc.battle.active:
        await message.respond(f'You cannot use multiple items during battle', ephemeral=hide)
        return
    if item == '':
        await message.respond(f'You need to specify an item. Usage: `{pre}use <item>`', ephemeral=hide)
        return
    if getter.get_inv(acc, item) == None:
        await message.respond(f'You do not have **{item}** in your inventory', ephemeral=hide)
        return
    if getter.get_inv(acc, item).amount < amount:
        await message.respond(f'You do not have enough **{item}** in your inventory to use {amount} of them', ephemeral=hide)
        return
    if acc.battle.active and acc.battle.potion_cd > 0:
        await message.respond(f'You are on cooldown for using items! ({acc.battle.potion_cd} turns left)', ephemeral=hide)
        return
    
    if acc.battle.active:
        acc.battle.potion_cd = 3
    body = ''
    unlimited_uses = ['mystic conch', 'sleeping bag', 'campfire']
    if getter.get_type(item) == 'elixir':
        try:
            if len(acc.vars["boost"]) >= 8:
                await message.respond(f'You already have 4 boosts active. (max is 4)', ephemeral=hide)
                return
        except:
            acc.vars["boost"] = []

        for i in acc.inventory:
            if i.name == item:
                if item not in unlimited_uses:
                    if i.amount == 1:
                        acc.inventory.remove(i)
                        body += f'You used **{item}**. Check `/boosts` for your total boosts. You have none left\n'
                    else:
                        i.amount -= amount
                        body += f'You used **{item}**. Check `/boosts` for your total boosts. You have {i.amount} left\n'
                else:
                    body += f'You used **{item}**\n'

        time = consts.boosts[item]["time"]
        end_time = datetime.datetime.now()
        end_time += datetime.timedelta(minutes=time)
        str_end_time = f"{end_time.year}/{end_time.month}/{end_time.day}/{end_time.hour}/{end_time.minute}/{end_time.second}"
        boost =[item, str_end_time]
        
        await message.respond(body, ephemeral=hide)
        acc.vars["boost"] += boost
        account.write_file()
        return

    elif getter.get_type(item) == 'consumable':
        for i in acc.inventory:
            if i.name == item:
                if item not in unlimited_uses:
                    if i.amount == 1:
                        acc.inventory.remove(i)
                        body += f'You used **{item}**. You have none left\n'
                    else:
                        i.amount -= amount
                        body += f'You used **{item}**. You have {i.amount} left\n'
                else:
                    
                    if acc.battle.active:
                        body += f'You cannot use this item in battle'
                        
                        await message.respond(body, ephemeral=True)
                        return
                    body += f'You used **{item}**\n'
        heal_mult = 1
        if acc.battle.active:
            for cond in acc.battle.p_cond:
                if cond[0].name == 'bleeding':
                    heal_mult = 0.75-((cond[0].potence-1)*0.1)
                    body += f'You are bleeding. {round((1-heal_mult)*100)}% less healing\n'
        if item == 'mystic conch':
            acc.area = 'Beach III'
            body += f'Teleported to **Beach III**\n'
            
            await message.respond(body, ephemeral=hide)
            

            acc.total_stats = formulas.get_stats(acc)
            account.write_file()
            return

        if item == 'sleeping bag':

            if acc.hp < round(acc.total_stats["HP"]/2):
                acc.hp = round(acc.total_stats["HP"]/2)
            if acc.mp < round(acc.total_stats["MP"]/2):
                acc.mp = round(acc.total_stats["MP"]/2)
            if acc.hp < round(acc.total_stats["HP"]/2) and acc.mp < round(acc.total_stats["MP"]/2):
                body += f'You are already healthy enough, sleeping now will do nothing'
            else:
                body += f'Healed up to 50% HP and MP: {acc.hp}/{round(acc.total_stats["HP"])} **HP**, {acc.mp}/{round(acc.total_stats["MP"])} **MP**\n'
            
            await message.respond(body, ephemeral=hide)
            

            acc.total_stats = formulas.get_stats(acc)
            account.write_file()
            return
        elif item == 'campfire':

            if acc.hp < round(acc.total_stats["HP"]*0.75):
                acc.hp = round(acc.total_stats["HP"]*0.75)
            if acc.mp < round(acc.total_stats["MP"]*0.65):
                acc.mp = round(acc.total_stats["MP"]*0.65)
            if acc.hp < round(acc.total_stats["HP"]*0.75) and acc.mp < round(acc.total_stats["MP"]*0.65):
                body += f'You are already healthy enough, sleeping now will do nothing'
            else:
                body += f'Healed up to 75% HP and 65% MP: {acc.hp}/{round(acc.total_stats["HP"])} **HP**, {acc.mp}/{round(acc.total_stats["MP"])} **MP**\n'
            
            await message.respond(body, ephemeral=hide)
            

            acc.total_stats = formulas.get_stats(acc)
            account.write_file()
            return
        heals = consts.heals[item]
        for heal in heals:
            if heal[0] == 'HP':
                to_heal = round(heal[1]*amount*heal_mult)
                acc.hp += to_heal
                if acc.hp > round(acc.total_stats["HP"]):
                    acc.hp = round(acc.total_stats["HP"])
                    body += f'Healed to **MAX** HP --> **{acc.hp}/{round(acc.total_stats["HP"])}** HP\n'
                else:
                    body += f'Healed **{to_heal}** HP --> {acc.hp}/{round(acc.total_stats["HP"])} HP\n'
            elif heal[0] == 'MP':
                to_heal = round(heal[1]*amount*heal_mult)
                acc.mp += to_heal
                if acc.mp > round(acc.total_stats["MP"]):
                    acc.mp = round(acc.total_stats["MP"])
                    body += f'Healed to **MAX** MP --> **{acc.mp}/{round(acc.total_stats["MP"])}** MP\n'
                else:
                    body += f'Healed **{to_heal}** MP --> {acc.mp}/{round(acc.total_stats["MP"])} MP\n'
            elif heal[0] == 'EF':
                if acc.battle.active:
                    body += f'You have **{heal[1][0]}**(LVL {heal[1][1]}) for {heal[1][2]} turns'
                    has = 0
                    for i, cond in enumerate(acc.battle.p_cond):
                        if cond[0].name == heal[1][0]:
                            has = 1
                            acc.battle.p_cond[i][1] = heal[1][2]
                            break
                    if not has:
                        acc.battle.p_cond.append([account.Effect(heal[1][0],heal[1][1]), heal[1][2]])
                    

        await message.respond(body, ephemeral=hide)
        

        acc.total_stats = formulas.get_stats(acc)
        account.write_file()
    else:
        await message.respond(f'You cannot use that item', ephemeral=hide)

class Travel(discord.ui.View):

    @discord.ui.button(label="1", row=0, style=discord.ButtonStyle.success)
    async def first_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        adjacent = consts.adjacent_areas[acc.area]
        try:
            area = adjacent[0]
        except:
            await interaction.response.send_message(f'That is an invalid number!', ephemeral=True)
            return
        await travel(interaction, area, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'), button=True)

    @discord.ui.button(label="2", row=0, style=discord.ButtonStyle.success)
    async def second_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        adjacent = consts.adjacent_areas[acc.area]
        try:
            area = adjacent[1]
        except:
            await interaction.response.send_message(f'That is an invalid number!', ephemeral=True)
            return
        await travel(interaction, area, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'), button=True)

    @discord.ui.button(label="3", row=0, style=discord.ButtonStyle.success)
    async def third_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        adjacent = consts.adjacent_areas[acc.area]
        try:
            area = adjacent[2]
        except:
            await interaction.response.send_message(f'That is an invalid number!', ephemeral=True)
            return
        await travel(interaction, area, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'), button=True)
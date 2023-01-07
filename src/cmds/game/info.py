import src.consts as consts
import src.counters as counters
import src.account as account
import src.funcs.formulas as formulas
import src.funcs.checks as checks
import random
import discord
from discord.ui import Select
import src.party_manager as party_manager
import src.counters as counters
import math
import src.funcs.getter as getter
import src.configs as configs
import src.image_generator as image_generator
import src.pvp_manager as pvp_manager
def create_view(page,max_page):
    class InvArrows(discord.ui.View):
        if page > 1:
            @discord.ui.button(label="◄", row=0, style=discord.ButtonStyle.gray)
            async def first_button_callback(self, button, interaction):
                acc = account.get_account(interaction.user)
                await inv(interaction, acc, page-1, '/', configs.get_config(interaction.guild.name, 'ephemeral'), button=True)

        
        if page < max_page+1:
            @discord.ui.button(label="►", row=0, style=discord.ButtonStyle.gray)
            async def second_button_callback(self, button, interaction):
                acc = account.get_account(interaction.user)
                await inv(interaction, acc, page+1, '/', configs.get_config(interaction.guild.name, 'ephemeral'), button=True)

    return InvArrows()
async def actions(message, acc, pre, hide):
    embed = discord.Embed()
    if not acc.battle.active == 1:
            body = ''
            party = party_manager.get_party(acc.name, party_manager.party_list)
            pvp = pvp_manager.get_pvp(acc.name, pvp_manager.pvp_list)
            if pvp != None and pvp.duelists[1].name == acc.name and pvp.in_battle == 0:
                body+=f'{message.author.mention}, You have been invited to a pvp duel by **{pvp.duelists[0].name}**! use `/pvp-accept` or `/pvp-decline` to accept/decline the invitation.\n\n'
            if party != None:
                for member in party.members:
                    if member == None:
                        continue
                    elif acc.name == member.name and member.ptype == 0:
                        body+=f'{message.author.mention}, You have been invited to a party by **{party.leader}**! use `/party-accept` or `/party-decline` to accept/decline the invitation.\n\n'
            if pvp != None and pvp.in_battle:
                if pvp.duelists[1].name == acc.name:
                    opponent_num = 0
                else:
                    opponent_num = 1
                opponent = account.get_account(pvp.duelists[opponent_num].name, 0)
                embed.title = f'{message.author.name}#{message.author.discriminator}, You are in a duel with {pvp.duelists[opponent_num].name}!'
                name = f'**{opponent.name}** - {opponent.hp}/{opponent.total_stats["HP"]} HP\n'
                if pvp.turn != opponent_num:
                    body += f'\n---- It is your turn ----\n'
                else:
                    body += f'\n---- It is not your turn ----\n'
                embed.add_field(name=name, inline = False, value = body)
                body =''
                spells = 0
                for i, spell in enumerate(acc.equipped_spells):
                    spells = 1
                    for pspell in acc.spells:
                        if pspell.name == spell:
                            spell = pspell
                    body += f'{i+1} > **{spell.name.capitalize()} (LVL {spell.lvl})** - cost {spell.mp_cost} MP\n'
                for i in range(len(acc.equipped_spells) - formulas.get_spell_slots(acc.level)):
                    body += '> empty slot\n'

                if spells: embed.add_field(name="Spells:", value=body, inline = False)
                body = ''
                conditions = 0
                for i, cond in enumerate(acc.battle.p_cond):
                    conditions = 1
                    desc = consts.conditions[cond[0].name]['desc'].replace('&',str(consts.conditions[cond[0].name]['base']+(consts.conditions[cond[0].name]['inc']*cond[0].potence)))
                    body+= f'**{cond[0].name.capitalize()}** (LVL {cond[0].potence}) - {cond[1]} turns left ({desc})\n'
                
                if conditions: embed.add_field(name="Your Conditions:", value=body, inline = False)
                body = ''
                body+=f'''\nUse `{pre}pvp-attack <enemy (1 to {acc.battle.amount})>` - to attack your opponent
        Use `{pre}pvp-spell <spell (1 to {formulas.get_spell_slots(acc.level)})>`- to use a spell on your opponent
        Use `{pre}pvp-flee` - to forfeit and end the duel
        '''
                cooldown = 'to use an item. There is a 3 turn cooldown for this action'
                if acc.battle.potion_cd > 0:
                    cooldown = f'ON COOLDOWN ({acc.battle.potion_cd} turns left)'
                body += f'Use `{pre}use <item name>` - {cooldown}\n\nUsing an item does not take up a turn\n\n'
                embed.add_field(name="Actions:", value=body, inline = False)
                
                image = image_generator.generate_pvp(acc, message.author, 0)
                embed.set_image(url="attachment://image.png")
                await message.respond(embed = embed, ephemeral=hide, file=image)

                return
            embed.title = f'''You are in area: **{acc.area}**'''
            embed.description = f"Not currently in battle <:defence:1060941040879673476>"

            nearby_areas = ''
            adjacent_areas = consts.adjacent_areas[acc.area]
            for area in adjacent_areas:
                emoji = consts.emojis[area]
                nearby_areas += f'  {emoji}`{area}`\n'
            nearby_areas += "\n"
            embed.add_field(name = "Nearby Areas:", value = nearby_areas, inline= False)

            body = ''
            body += f'''\n  Use `{pre}travel` - to travel to a nearby area
    **Use** `{pre}vote` - for **free vote rewards** (check `/vote-rewards`)
    Use `{pre}map` - to see the map of the island
    Use `{pre}area` - to find out about this area
    Use `{pre}show-stats` - to see your stats and level
    Use `{pre}spells` - to see your spells
    Use `{pre}inventory` - to see your inventory'''
            embed.add_field(name = "Actions:", value = body, inline= False)
            body = ''
            if acc.area == 'Town 1' or acc.area == 'Town 2':
                body += f'''\nUse `{pre}shop` - to see the shop
Use `{pre}hero-shop` - to see the hero coin shop (premium items)
Use `{pre}smith-...` - to visit the blacksmith
Use `{pre}rest` - to restore HP an MP for 25 aurum
Use `{pre}library-...` - to see available spells''' 
                embed.add_field(name = "Town Actions:", value = body, inline= False)
            elif acc.area == 'Krakow\'s Cave':
                body += f'''\nUse `{pre}shop` - to see Krakow\'s shop
Use `{pre}fight` - to duel with Krakow'''
                embed.add_field(name = "Krakow\'s Cave:", value = body, inline= False)
            elif acc.area == 'Boat 1':
                body += f'''\nUse `{pre}ride` - to travel to island 2 (coming soon)'''
                embed.add_field(name = "Boat:", value = body, inline= False)

            elif acc.area.endswith('III'):
                body += f'''\nUse `{pre}fight <amount (1 to 3)>` - to fight monsters'''
                if acc.area == 'Forest III':
                    body += f'''\nUse `{pre}boss` - to fight **Visius Ent (lvl 40)** (must be level 35+)'''
                elif acc.area == 'Beach III':
                    body += f'''\nUse `{pre}boss` - to fight **King Polypus (lvl 30)** (must be level 25+)'''
                elif acc.area == 'Wolf Den III':
                    body += f'''\nUse `{pre}boss` - to fight **Alpha Wolf (lvl 20)** (must be level 15+)'''
                embed.add_field(name = f"{acc.area} Actions:", value = body, inline= False)

            else:
                body += f'''\nUse `{pre}fight <amount (1 to 3)>` - to fight monsters'''
                embed.add_field(name = f"{acc.area} Actions:", value = body, inline= False)
                
            embed.set_image(url="attachment://image.png")
            await message.respond(embed = embed, ephemeral=hide, file=image_generator.generate_area(acc.area))

    else:
        embed.title = f"You are in battle!"
        embed.description = f"Currently fighting monsters <:attack:1060941035456438382>"
        body = f''
        for i, monster in enumerate(acc.battle.enemy):
            if acc.battle.e_hp[i] == 0:
                if acc.battle.enemy[i].name != ' ':
                    body += f'{i+1} > {monster.name.capitalize()} - dead\n'
            elif monster.name != ' ':
                body += f'{i+1} > **{monster.name.capitalize()}** - {acc.battle.e_hp[i]}/{monster.max_hp} HP\n'

        embed.add_field(name="Monsters:", value=body, inline = False)
        body =''
        spells = 0
        for i, spell in enumerate(acc.equipped_spells):
            spells = 1
            for pspell in acc.spells:
                if pspell.name == spell:
                    spell = pspell
            body += f'{i+1} > **{spell.name.capitalize()} (LVL {spell.lvl})** - cost {spell.mp_cost} MP\n'
        for i in range(len(acc.equipped_spells) - formulas.get_spell_slots(acc.level)):
            body += '> empty slot\n'

        if spells: embed.add_field(name="Spells:", value=body, inline = False)
        body = ''
        conditions = 0
        for i, cond in enumerate(acc.battle.p_cond):
            conditions = 1
            desc = consts.conditions[cond[0].name]['desc'].replace('&',str(consts.conditions[cond[0].name]['base']+(consts.conditions[cond[0].name]['inc']*cond[0].potence)))
            body+= f'**{cond[0].name.capitalize()}** (LVL {cond[0].potence}) - {cond[1]} turns left ({desc})\n'
        
        if conditions: embed.add_field(name="Your Conditions:", value=body, inline = False)
        body = ''
        body+=f'''\nUse `{pre}attack <enemy (1 to {acc.battle.amount})>` - to attack an enemy
Use `{pre}use-spell <spell (1 to {formulas.get_spell_slots(acc.level)})> <enemy (1 to {acc.battle.amount})>` - to use a spell on an enemy
Use `{pre}flee` - to escape the battle (40% chance to work, 20% if fighting a boss)
'''
        cooldown = 'to use an item. There is a 3 turn cooldown for this action'
        if acc.battle.potion_cd > 0:
            cooldown = f'ON COOLDOWN ({acc.battle.potion_cd} turns left)'
        body += f'Use `{pre}use <item name>` - {cooldown}\n\nUsing an item does not take up a turn\n\n'
        embed.set_footer(text = f'TIP: Fighting multiple enemies gives bonus xp and minae')
        
        embed.add_field(name="Actions:", value=body, inline = False)
        image = image_generator.generate_battle(acc, message.author, 0)
        embed.set_image(url="attachment://image.png")
        await message.respond(embed = embed, ephemeral=hide, file=image)


async def map(message, acc, pre, hide):
    body = f'You are in **{acc.area}**\nPlayer Head = Current location'
    await message.respond(body, ephemeral=hide, file=image_generator.generate_map(acc.area))
    

async def area(message, acc, pre, hide):
    body = f'**{acc.area}**:\n\n'
    if acc.area == 'Apple Orchard':
        body += '''The Apple Orchard is peaceful place with lots of apple trees and a graveyard.
Here you can find **Crow (lvl 1)**.'''

    elif acc.area == 'Town 1':
        body += '''Town 1 is the only town of island 1, it is a hub for all adventurers.
Here you can buy and sell items; upgrade equipment and more!'''

    elif acc.area == 'Forest Outskirts':
        body += '''The Forest Outskirts have low level monsters and fruit. It is by the coast of island 1.
Here you can find **Crow (lvl 1)** and **Badger (lvl 3)**.'''

    elif acc.area == 'Farm':
        body += '''The Farm is near the dangerous Wolf Den. There have been recent wolf attacks.
Here you can find **Manihot (lvl 5)** and **Scarecrow (lvl 7)**.'''
    
    elif acc.area == 'Wolf Den I':
        body += '''This is the entrance to the Wolf Den. A dangerous cave filled with wolves and bats.
Here you can find **Serpens (lvl 8)** and **Boletus (lvl 10)**.'''
    
    elif acc.area == 'Wolf Den II':
        body += '''This is the center of the Wolf Den. there are lakes and huge rocks around.
Here you can find **Suco (lvl 12)** and **Wolf Pup (lvl 14)**.'''
    
    elif acc.area == 'Wolf Den III':
        body += '''This is the deepest part of the Wolf Den. It is a huge maze of tunnels. The alpha wolf lurks nearby...
Here you can find **Wolf Pup (lvl 14)**, **Wolf (lvl 17)** and the **Alpha Wolf (lvl 20)**.'''
    
    elif acc.area == 'Beach I':
        body += '''This is the entrance to the beach. There is lots of sand and shallow waters.
Here you can find **Seitaad (lvl 21)** and **Crab (lvl 24)**.'''
    
    elif acc.area == 'Beach II':
        body += '''This is a long stretch of sand, there are dry trees and driftwood on the shore.
Here you can find **Seitaad (lvl 21)**, **Crab (lvl 24)** and **Clam (lvl 28)**.'''
    
    elif acc.area == 'Beach III':
        body += '''A whirlpool leading to an underwater lair. The lair of king Polypus.
Here you can find **Crab (lvl 24)**, **Clam (lvl 28)** and **King Polypus (lvl 30)**.'''
    
    elif acc.area == 'Forest I':
        body += '''A path winding down a forest full of dangerous animals. The foliage gets thicker and thicker.
Here you can find **Grizzly Bear (lvl 32)** and **Badger (lvl 3)**.'''
    
    elif acc.area == 'Forest II':
        body += '''Hard to tell which way you came from here. There are a few rivers with bridges to cross over.
Here you can find **Silva Wisp (lvl 35)** and **Grizzly Bear (lvl 32)**.'''
    
    elif acc.area == 'Forest III':
        body += '''This is a small, ominous island connected to the main forest by a bridge. Something moves amongst the tall trees.
Here you can find **Silva Wisp (lvl 35)**, **Aculeo (lvl 38)** and **Visius Ent (lvl 40)**.'''
    
    elif acc.area == 'Boat 1':
        body += '''This boat can take you to other islands.. for a fee of course :)'''
    elif acc.area == 'Krakow\'s Cave':
        body += '''This cave is inhabited by Krakow. He is hiding from the beach monsters.
Krakow sells interesting items and is always up for a duel!'''

    await message.respond(body, ephemeral=hide, file=image_generator.generate_area(acc.area))
    
def statter(item):
    try:
        string = f'{item.name} ('
        for stat in item.stats:
            if stat.name == 'LVL': continue
            string += f'+{round(stat.value, 1)} {stat.name} '
        string += f'/ LVL REQ: {round(item.stats[-1].value)})'
        return string
    except:
        return ''
async def stats(message, acc, pre, hide, user):
    if user != None:
        selected_acc = account.get_account(user)
    else:
        selected_acc = acc
    h_s = statter(selected_acc.helmet)
    a_s = statter(selected_acc.armour)
    w_s = statter(selected_acc.weapon)
    o_s = statter(selected_acc.offhand)
    r_s = statter(selected_acc.ring)
    next_xp = formulas.get_next_xp(selected_acc.level)
    minae = getter.get_inv(selected_acc, 'minae')
    if minae == None:
        minae = 0
    else:
        minae = minae.amount
    magic = getter.get_inv(selected_acc, 'magic dust')
    if magic == None:
        magic = 0
    else:
        magic = magic.amount
    equipment = ''

    try: equipment+=f'`(UPGRADE {round(selected_acc.helmet.upgrade_lvl)}) Helmet` - {h_s}\n'
    except: equipment+=f'`(NO ITEM) Helmet` - {h_s}\n'
    try: equipment+=f'`(UPGRADE {round(selected_acc.armour.upgrade_lvl)}) Armour` - {a_s}\n'
    except: equipment+=f'`(NO ITEM) Armour` - {a_s}\n'
    try: equipment+=f'`(UPGRADE {round(selected_acc.weapon.upgrade_lvl)}) Weapon` - {w_s}\n'
    except: equipment+=f'`(NO ITEM) Weapon` - {w_s}\n'
    try: equipment+=f'`(UPGRADE {round(selected_acc.offhand.upgrade_lvl)}) Offhand` - {o_s}\n'
    except: equipment+=f'`(NO ITEM) Offhand` - {o_s}\n'
    try: equipment+=f'`(UPGRADE {round(selected_acc.ring.upgrade_lvl)}) Ring` - {r_s}\n'
    except: equipment+=f'`(NO ITEM) Ring` - {r_s}\n'

    body = f'''**__STATS FOR {selected_acc.name}__**\n**Equipment Stats**:
{equipment}

**Base Stats**:
`HP` - {formulas.max_hp(selected_acc.level)}
`MP` - {formulas.max_mp(selected_acc.level)}
`DMG` - {2 + round(selected_acc.level/3)}
`DEF` - {2 + selected_acc.level}'''
    body += f'''\n\n**Total Stats**:```
LVL: {selected_acc.level} ({selected_acc.xp}/{next_xp} xp)
AREA: {selected_acc.area}
AURUM: {selected_acc.aurum}
MINAE: {minae}
MAGIC DUST: {magic}

DMG: {selected_acc.total_stats["DMG"]}
DEF: {selected_acc.total_stats["DEF"]}
HP: {selected_acc.hp}/{round(selected_acc.total_stats["HP"])}
MP: {selected_acc.mp}/{round(selected_acc.total_stats["MP"])}
%.CRIT: {selected_acc.total_stats["%.CRIT"]}%
%.CRIT.DMG: {selected_acc.total_stats["%.CRIT.DMG"]+100}%
%.SPELL.DMG: {selected_acc.total_stats["%.SPELL.DMG"]+100}%
```'''
    await message.respond(body, ephemeral=hide) 

async def inv(message, acc, page, pre, hide, button=False):
    if page < 1:
        page = 1
    length = len(acc.inventory)
    if page-1 > length/20:
        page = int(length/20)
    inv_segment = acc.inventory[(page-1)*20:page*20]
    h_s = statter(acc.helmet)
    a_s = statter(acc.armour)
    w_s = statter(acc.weapon)
    o_s = statter(acc.offhand)
    r_s = statter(acc.ring)
    body = f'**{acc.name}\'s** inventory (page {page}/{int(length/20)+1}):\n\n'
    equipped = []
    try: equipped.append(acc.helmet.name)
    except: pass
    try: equipped.append(acc.armour.name)
    except: pass
    try: equipped.append(acc.weapon.name)
    except: pass
    try: equipped.append(acc.offhand.name)
    except: pass
    try: equipped.append(acc.ring.name)
    except: pass
    for i, item in enumerate(inv_segment):
        pref = ''
        suf = ''
        if item.name in equipped:
            pref = '**(E) '
            suf = '**'
        body += f'― {pref}{item.name} - {item.amount}{suf}\n'
        if i == 19:
            body += f'*+ {length - page*20} more...*\n'
    body+=f'''\n**Equipment**:
`Helmet` - {h_s}
`Armour` - {a_s}
`Weapon` - {w_s}
`Offhand` - {o_s}
`Ring` - {r_s}

You have {acc.aurum} Aurum
Use `{pre}equip <item>` to equip an item
Use `{pre}unequip <slot>` to unequip that slot
Use `{pre}use <food/potion>` to use/eat a consumable item
Use `{pre}show-stats` to see your total stats'''
    if button:
            await message.response.send_message(body, ephemeral=hide, view = create_view(page,int(length/20)))
    else: await message.respond(body, ephemeral=hide, view = create_view(page,int(length/20)))

async def whatis(message, item, acc, pre, hide):
    item = item.lower()
    if item == 'aurum':
        body = f'`Aurum is a currency widely used in the land of Pereger`\n'
        body += f'`You have {acc.aurum} aurum`\n'
        await message.respond(body)

    elif item in consts.conditions.keys():
        body = f'--CONDITION--\n'
        body += f'Info for **{item}**:\n'
        i = consts.conditions[item]['desc'].replace('&',str(consts.conditions[item]['base']+consts.conditions[item]['inc']))
        body += f'`{i}'
        inc = consts.conditions[item]['inc']
        if inc != 0:
            body += f' ({inc}% stronger per extra level)'
        body += '`\n'

        await message.respond(body, ephemeral=hide)

    elif item in consts.enemy_spells.keys():
        body = f'--SPELL--\n'
        body += f'Info for **{item}**:\n'
        i = consts.enemy_spells[item]['desc'].split('. ')
        body += f'`{i[0]}`\n{i[1]}\n'
        await message.respond(body, ephemeral=hide)

    elif item in consts.items.keys():
        body = f'--ITEM--\n'
        body += f'Info for **{item}**:\n'
        i = consts.items[item]['desc']
        b = f'{consts.items[item]["buy"][0]} {consts.items[item]["buy"][1]}' 
        s = f'{consts.items[item]["sell"][0]} {consts.items[item]["sell"][1]}' 
        body += f'`{i}`\n'
        if getter.get_inv(acc, item) == None:
            amount = 'no'
        else:
            amount = getter.get_inv(acc, item).amount
        body += f'`You have {amount} {item}`\n'
        body += f'--`Buy price: {b}`--\n'
        body += f'--`Sell price: {s}`--\n'
        t = getter.get_type(item)
        body += f'--`Type: {t}`--\n'
        if t == 'sword':
            body += f'--`CLASS: knight`--\n'
        elif t == 'wand':
            body += f'--`CLASS: mage`--\n'
        elif t == 'instrument':
            body += f'--`CLASS: bard`--\n'
        elif t == 'gloves':
            body += f'--`CLASS: brawler`--\n'
        elif t == 'mystic':
            body += f'--`CLASS: mage/bard`--\n'
        elif t == 'shield':
            body += f'--`CLASS: knight/brawler`--\n'

        await message.respond(body, ephemeral=hide)
    else:
        #i = item['desc']
        await message.respond(f'Item does not exist: **{item}**', ephemeral=hide)

async def whois(message, monster, acc, pre, hide):
    monster = monster.lower()
    aliases = {
        'snake': 'serpens',
        'serpent': 'serpens',
        'bat': 'suco',
        'mushroom': 'boletus',
        'potato': 'manihot',
        'bear': 'grizzly bear',
        'sandcastle': 'seitaad',
        'sand castle': 'seitaad',
        'silver wisp': 'silva wisp',
        'wisp': 'silva wisp',
        'wasp': 'aculeo',
        'bee': 'aculeo',
    }
    premonster = ''
    correction = 0
    if monster in aliases.keys():
        premonster = monster
        monster = aliases[monster]
        correction = 1
    if monster in consts.monsters.keys():
        body = ''
        if correction:
            body += f'Monster does not exist: **{premonster}**\n'
            body += f'Did you mean? **{monster}**:\n\n'
        body += f'Info for **{monster}**:\n\n'
        i = consts.monsters[monster]
        body += f'`{i}`\n'
        l = ''
        for x in consts.mob_loot[monster]:
            l+= f'{x[1]}% - {x[0]}'
            if x[2][1] ==1 and x[2][0] == 1:
                l+='\n'
            elif x[2][1] == x[2][0]:
                l+=f' ({x[2][0]})\n'
            elif x[2][1] != x[2][0]:
                l+=f' ({x[2][0]} - {x[2][1]})\n'
        s = ''
        for stat in consts.mob_stats[monster].keys():
            if stat != 'SPELL.CD' and stat != 'XP' and stat != 'SPELL':
                s += f'`{stat}` - {consts.mob_stats[monster][stat]}\n'
        body += f'`Possible loot:\n{l}`\n'
        x = consts.mob_stats[monster]['XP']
        body += f'`Base XP: {x}`\n\n'
        body += f'**Stats:**\n{s}\n'
        for i,spell in enumerate(consts.mob_stats[monster]['SPELL']):
            if i == 0:
                body += f'**Spells:**\n'
            spell = consts.mob_stats[monster]['SPELL'][i]
            body += f'`{spell}`\n'


        await message.respond(body, ephemeral=hide, file=image_generator.generate_icon(monster))
    else:
        #i = item['desc']
        await message.respond(f'Monster does not exist: **{monster}**', ephemeral=hide)

async def help(message, page, acc, pre, hide):
    if page == '¤':
        page = 1
    try: index = int(page)-1
    except: await message.respond(f'Page must be a number, not {page}', ephemeral=hide)
    body = '```\n'
    body += consts.help_text[index].replace('¤', pre)
    body += '\n```'
    await message.respond(body, ephemeral=hide)

async def spells(message, acc, pre, hide):
    if len(acc.spells) > 0:
        body = f'''\n**{acc.name}'s Spells**'''
        for spell in acc.spells:
            body += f'\n{spell.name} - LVL {spell.lvl}'

        body += f'\n\n**Equipped Spells ({len(acc.equipped_spells)}/{formulas.get_spell_slots(acc.level)})**:'
        for espell in acc.equipped_spells:
            body += f'\n{espell}'
        for i in range(formulas.get_spell_slots(acc.level) - len(acc.equipped_spells)):
            body += f'\n< empty slot >'
        body += f'\n\nUse `/library-spells <tier>` to find information about a spell in the library in town'
        body += f'\nUse `/equip-spell <spell>` and `/unequip-spell <spell>` to equip/unequip spells'
        await message.respond(body, ephemeral=hide)
    else:
        await message.respond('You do not have any spells! You can buy them in the /library in town.', ephemeral=hide)

async def leaderboard(message, acc, pre, hide, user, lb_type='Highest Level', button=0):
    if user != None: nametag = user.name+'#'+user.discriminator

    
    key = formulas.get_total_xp
    if lb_type == 'Highest level':
        key = formulas.get_total_xp
    elif lb_type == 'Most Aurum':
        def x(acc): return acc.aurum
        key = x 
    elif lb_type == 'Most Votes':
        def x(acc): 
            try:
                return acc.vars['votes'][0]
            except:
                return 0
        key = x 
    elif lb_type == 'Best Stats':
        def score_stats(acc):
            stats = acc.total_stats
            score  = ((stats['DMG']*2+stats['DEF'])*2+stats['HP']+stats['MP'])    *    ((stats['%.CRIT']+200)/200)*((stats['%.SPELL.DMG']+200)/200)*((stats['%.CRIT.DMG']+150)/200)
            return score
        key = score_stats

    sorted_accs = list(reversed(sorted(account.acc_list, key=key)))
    acc_index = [a.name for a in sorted_accs].index(acc.name)
    if user != None:
        try: user_index = [a.name for a in sorted_accs].index(nametag)
        except:
            
            if button:
                await message.response.send_message(f'User does not exist: **{nametag}**', ephemeral=True)
            else:
                await message.respond(f'User does not exist: **{nametag}**', ephemeral=True)

        user_lb = sorted_accs[user_index]
    else:
        user_lb = None
    acc_lb = sorted_accs[acc_index]
    sorted_accs = sorted_accs[:20]
    


    lb = '```\n'
    for i, lbacc in enumerate(sorted_accs):
        name_num = f'#{i+1}: {lbacc.name}'
        space = ' '*(25-len(name_num))
        if lb_type == 'Highest Level':
            lb += f'{name_num} {space} - LVL: {lbacc.level}, XP: {lbacc.xp}/{formulas.get_next_xp(lbacc.level)}'
        elif lb_type == 'Most Aurum':
            lb += f'{name_num} {space} - {lbacc.aurum} aurum'
        elif lb_type == 'Most Votes':
            lb += f'{name_num} {space} - {x(lbacc)} votes'
        elif lb_type == 'Best Stats':
            lb += f'{name_num} {space} - SCORE {round(score_stats(lbacc))}'
        #if i % 2 == 0:
        #    lb = '**'+lb+'**'
        lb += '\n'


    lb += '\nYour account:\n'
    name_num = f'#{acc_index+1}: {acc.name}'
    space = ' '*(25-len(name_num))
    if lb_type == 'Highest Level':
        lb += f'{name_num} {space} - LVL: {acc.level}, XP: {acc.xp}/{formulas.get_next_xp(acc.level)}'
    elif lb_type == 'Most Aurum':
        lb += f'{name_num} {space} - {acc.aurum} aurum'
    elif lb_type == 'Most Votes':
        lb += f'{name_num} {space} - {x(acc)} votes'
    elif lb_type == 'Best Stats':
        lb += f'{name_num} {space} - SCORE {round(score_stats(acc))}'

    if user_lb != None:
        lb += '\n\nRequested User\'s account:\n'
        name_num = f'#{user_index+1}: {nametag}'
        space = ' '*(25-len(name_num))
        if lb_type == 'Highest Level':
            lb += f'{name_num} {space} - LVL: {user_lb.level}, XP: {user_lb.xp}/{formulas.get_next_xp(user_lb.level)}'
        elif lb_type == 'Most Aurum':
            lb += f'{name_num} {space} - {user_lb.aurum} aurum'
        elif lb_type == 'Most Votes':
            lb += f'{name_num} {space} - {x(user_lb)} votes'
        elif lb_type == 'Best Stats':
            lb += f'{name_num} {space} - SCORE {round(score_stats(user_lb)/100)}'


    lb += '```\n**Leaderboard Category:**'
    select = Select(
        placeholder='Choose a category...',
        options=[
        discord.SelectOption(label='Highest Level', emoji='<:xp:1060941047280193646>', default=(lb_type=='Highest Level')),
        discord.SelectOption(label='Most Aurum', emoji='<:aurum:1059950170927812698>', default=(lb_type=='Most Aurum')),
        discord.SelectOption(label='Best Stats', emoji='<:attack:1060941035456438382>', default=(lb_type=='Best Stats')),
        discord.SelectOption(label='Most Votes', emoji='<:hero_coin:1059952396786225202>', default=(lb_type=='Most Votes')),
    ])
    async def lb_callback(interaction):
        await leaderboard(interaction, acc, pre, hide, user, lb_type=select.values[0], button=1)
    select.callback = lb_callback
    view = discord.ui.View()
    view.add_item(select)
    if button:
        await message.response.send_message(lb, ephemeral=hide, view=view)
    else:
        await message.respond(lb, ephemeral=hide, view=view)
        

async def report(message, acc, pre, hide, bug, guild_chan):
    if len(bug) < 12:
        await message.respond('Report is too short please add sufficient detail about the problem. Sending random messages can result in getting **banned**', ephemeral=True)
        return
    
    await guild_chan.send(f'`{acc.name}` - {bug}')
    await message.respond(f'Successfully sent report: `{bug}`!', ephemeral=True)

async def discord_inv(message, acc, pre, hide):
    if 1:
        channel = await message.author.create_dm()
        await channel.send('https://discord.gg/xJkK2DtPZ5')
        await message.respond('Sent a DM of the invite to the Perebot discord server to you (If this did not work check your DM settings)', ephemeral=True)
    else:
        await message.respond('Something went wrong! (Check your DM settings)', ephemeral=True)

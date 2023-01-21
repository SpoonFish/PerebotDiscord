import src.consts as consts
import src.counters as counters
import src.account as account
import src.quest_manager as q_manager
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

def create_fight_view(battle):
    class Fight(discord.ui.View):
        fbosses = ['alpha wolf', "king polypus", "visius ent"]
        bosses = []
        for i in fbosses:
            bosses.append(i)
            bosses.append(f"{i} (hard)")
            bosses.append(f"{i} (extreme)")
        boss = battle.enemy[1].name in bosses
        if boss:
            bossname = battle.enemy[1].name[:-1]
            index = bossname.rfind(' ')
            difficulty = bossname[index+2:]
            if difficulty != 'extreme' and difficulty != 'hard':
                difficulty = 'normal'
            @discord.ui.button(label=f"Fight {battle.enemy[1].name}", row=0, style=discord.ButtonStyle.success)
            async def third_button_callback(self, button, interaction, difficulty=difficulty):
                acc = account.get_account(interaction.user)
                await fight(interaction, 3, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'), 1, 1, difficulty)
    
        
        if not boss:
            @discord.ui.button(label="Fight 1", row=0, style=discord.ButtonStyle.success)
            async def first_button_callback(self, button, interaction):
                acc = account.get_account(interaction.user)
                await fight(interaction, 1, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'), button=True)


            @discord.ui.button(label="Fight 2", row=0, style=discord.ButtonStyle.success)
            async def second_button_callback(self, button, interaction):
                acc = account.get_account(interaction.user)
                await fight(interaction, 2, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'), button=True)


            @discord.ui.button(label="Fight 3", row=0, style=discord.ButtonStyle.success)
            async def third_button_callback(self, button, interaction):
                acc = account.get_account(interaction.user)
                await fight(interaction, 3, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'), button=True)
    return Fight()



def create_attack_view(battle):
    enemies = battle.e_hp
    class Attack(discord.ui.View):
        if enemies[0]:
            @discord.ui.button(label="1", emoji="<:attack:1060941035456438382>", row=0, style=discord.ButtonStyle.primary)
            async def first_button_callback(self, button, interaction):
                acc = account.get_account(interaction.user)
                await attack(interaction, 1, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'), button=True)


        if enemies[1]:
            @discord.ui.button(label="2", emoji="<:attack:1060941035456438382>", row=0, style=discord.ButtonStyle.primary)
            async def second_button_callback(self, button, interaction):
                acc = account.get_account(interaction.user)
                await attack(interaction, 2, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'), button=True)


        if enemies[2]:
            @discord.ui.button(label="3", emoji="<:attack:1060941035456438382>", row=0, style=discord.ButtonStyle.primary)
            async def third_button_callback(self, button, interaction):
                acc = account.get_account(interaction.user)
                await attack(interaction, 3, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'), button=True)

        if enemies[0]:
            @discord.ui.button(label="Spell 1", row=1, style=discord.ButtonStyle.danger)
            async def first_buttons_callback(self, button, interaction):
                acc = account.get_account(interaction.user)
                acc.target = 1
                await choose_spell(interaction, acc, configs.get_config(interaction.guild.name, 'ephemeral'))


        if enemies[1]:
            @discord.ui.button(label="Spell 2", row=1, style=discord.ButtonStyle.danger)
            async def second_buttons_callback(self, button, interaction):
                acc = account.get_account(interaction.user)
                acc.target = 2
                await choose_spell(interaction, acc, configs.get_config(interaction.guild.name, 'ephemeral'))


        if enemies[2]:
            @discord.ui.button(label="Spell 3", row=1, style=discord.ButtonStyle.danger)
            async def third_buttons_callback(self, button, interaction):
                acc = account.get_account(interaction.user)
                acc.target = 3
                await choose_spell(interaction, acc, configs.get_config(interaction.guild.name, 'ephemeral'))
    return Attack()
class AttackPvp(discord.ui.View):

    @discord.ui.button(emoji="<:attack:1060941035456438382>", row=0, style=discord.ButtonStyle.primary)
    async def first_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        await pvp_attack(interaction, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'), button=True)

    @discord.ui.button(label="Spell", row=1, style=discord.ButtonStyle.danger)
    async def sfirst_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        acc.target = 1
        await choose_spell(interaction, acc, True, True)

class SpellPvp(discord.ui.View):

    
    @discord.ui.button(label="1", row=0, style=discord.ButtonStyle.secondary)
    async def first_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        try:
            await pvp_spell(interaction, acc.equipped_spells[0], True, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'))
        except:
            await interaction.response.send_message(f'That spell does not exist', ephemeral=True)

    @discord.ui.button(label="2", row=0, style=discord.ButtonStyle.secondary)
    async def second_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        try:
            await pvp_spell(interaction, acc.equipped_spells[1], True, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'))
        except:
            await interaction.response.send_message(f'That spell does not exist', ephemeral=True)


    @discord.ui.button(label="3", row=0, style=discord.ButtonStyle.secondary)
    async def third_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        try:
            await pvp_spell(interaction, acc.equipped_spells[2], True, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'))
        except:
            await interaction.response.send_message(f'That spell does not exist', ephemeral=True)


    @discord.ui.button(label="4", row=0, style=discord.ButtonStyle.secondary)
    async def fourth_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        try:
            await pvp_spell(interaction, acc.equipped_spells[3], True, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'))
        except:
            await interaction.response.send_message(f'That spell does not exist', ephemeral=True)


    @discord.ui.button(label="5", row=0, style=discord.ButtonStyle.secondary)
    async def fifth_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        try:
            await pvp_spell(interaction, acc.equipped_spells[4], True, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'))
        except:
            await interaction.response.send_message(f'That spell does not exist', ephemeral=True)




class Spell(discord.ui.View):

    
    @discord.ui.button(label="1", row=0, style=discord.ButtonStyle.secondary)
    async def first_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        await spell(interaction, acc.equipped_spells[0], acc.target, True, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'))
        try:
            pass
            
        except:
            await interaction.response.send_message(f'That spell does not exist', ephemeral=True)

    @discord.ui.button(label="2", row=0, style=discord.ButtonStyle.secondary)
    async def second_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        await spell(interaction, acc.equipped_spells[1], acc.target, True, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'))
        try:
            pass
        except:
            await interaction.response.send_message(f'That spell does not exist', ephemeral=True)


    @discord.ui.button(label="3", row=0, style=discord.ButtonStyle.secondary)
    async def third_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        try:
            await spell(interaction, acc.equipped_spells[2], acc.target, True, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'))
        except:
            await interaction.response.send_message(f'That spell does not exist', ephemeral=True)


    @discord.ui.button(label="4", row=0, style=discord.ButtonStyle.secondary)
    async def fourth_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        try:
            await spell(interaction, acc.equipped_spells[3], acc.target, True, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'))
        except:
            await interaction.response.send_message(f'That spell does not exist', ephemeral=True)


    @discord.ui.button(label="5", row=0, style=discord.ButtonStyle.secondary)
    async def fifth_button_callback(self, button, interaction):
        acc = account.get_account(interaction.user)
        try:
            await spell(interaction, acc.equipped_spells[4], acc.target, True, acc, '/', configs.get_config(interaction.guild.name, 'ephemeral'))
        except:
            await interaction.response.send_message(f'That spell does not exist', ephemeral=True)



async def fight(message, amount, acc, pre, hide, boss=0, button=0, difficulty = 'normal'):
    pvp = pvp_manager.get_pvp(acc.name, pvp_manager.pvp_list)
    party = party_manager.get_party(acc.name, party_manager.party_list)

    if pvp != None:
        if pvp.in_battle:
            await message.response.send_message('You cannot start a battle in a pvp duel!', ephemeral = True)
            return
        if pvp.duelists[0].name == acc.name:
            
            await message.response.send_message('You have invited someone to duel so you cannot start a battle. Use `/pvp-cancel` to cancel the request', ephemeral = True)
            return

    if acc.battle.active:
        if sum(acc.battle.e_hp) == 0:
            acc.battle = account.Battle(0)
    if acc.battle.active:
        
        if button:
            await message.response.send_message('You are already in battle!')
        else:await message.respond(f'You are already in a battle', ephemeral=hide)
        return
    if amount == '¤' or acc.area == 'Krakow\'s Cave':
        amount = 1
    

    if boss == 0: amount = int(amount)
    if boss == 0 and (amount < 1 or amount > 3):
        await message.respond(f'Number of monsters must be from 1 to 3', ephemeral=hide)
        return
    monsters = []
    if boss == 0:
        try: mon1 = consts.area_mobs[acc.area][0]
        except: 
            if button:
                await message.response.send_message(f'You cannot fight in this area ({acc.area})', ephemeral=hide)
            else: await message.respond(f'You cannot fight in this area ({acc.area})', ephemeral=hide)
            return
        try:
            mon2 = consts.area_mobs[acc.area][1]
        except: mon2 = [0,0]
        try:
            mon3 = consts.area_mobs[acc.area][2]
        except: mon3 = [0,0]
        try:
            mon4 = consts.area_mobs[acc.area][3]
        except: mon4 = [0,0]
        try:
            mon5 = consts.area_mobs[acc.area][4]
        except: mon5 = [0,0]

        chance1 = mon1[1]
        chance2 = mon2[1] + chance1
        chance3 = mon3[1] + chance2
        chance4 = mon4[1] + chance3
        chance5 = mon5[1] + chance4
        print(mon1[1], mon2[1], mon3[1], mon4[1], mon5[1])
        if mon1[1]+mon2[1]+mon3[1]+mon4[1]+mon5[1] != 100:
            await message.respond(f'Error in monster chances', ephemeral=hide)
            return
        for i in range(amount):
            rnd = random.randint(1, 100)
            print(rnd)
            if rnd <= chance1:
                monsters.append(mon1[0])
            elif rnd <= chance2:
                monsters.append(mon2[0])
            elif rnd <= chance3:
                monsters.append(mon3[0])
            elif rnd <= chance4:
                monsters.append(mon4[0])
            elif rnd <= chance5:
                monsters.append(mon5[0])
    else:
        if acc.area == 'Wolf Den III':
            if party == None:
                if acc.level < 15:
                    await message.respond(f'You need to be at least level 15 to fight the Alpha Wolf', ephemeral=hide)
                    return
            else:
                valid = 1
                for member in party.members:
                    if member != None and account.get_account(member.name, 0).level < 15:
                        valid = 0

                if not valid:
                    await message.respond(f'All party members must be at least level 15 to fight the Alpha Wolf', ephemeral=hide)
                    return
            if difficulty == 'normal':
                monsters.append('blood wolf')
                monsters.append('alpha wolf')
                monsters.append('blood wolf')
            elif difficulty == 'hard':
                monsters.append('wolf')
                monsters.append('alpha wolf (hard)')
                monsters.append('wolf')
            elif difficulty == 'extreme':
                monsters.append('enchanted wolf')
                monsters.append('alpha wolf (extreme)')
                monsters.append('enchanted wolf')
        elif acc.area == 'Beach III':
            if party == None:
                if acc.level < 25:
                    await message.respond(f'You need to be at least level 25 to fight **King Polypus**', ephemeral=hide)
                    return
            else:
                valid = 1
                for member in party.members:
                    if member != None and account.get_account(member.name, 0).level < 25:
                        valid = 0

                if not valid:
                    await message.respond(f'All party members must be at least level 25 to fight **King Polypus**', ephemeral=hide)
                    return
            if difficulty == 'normal':
                monsters.append(' ')
                monsters.append('king polypus')
                monsters.append(' ')
            elif difficulty == 'hard':
                monsters.append(' ')
                monsters.append('king polypus (hard)')
                monsters.append(' ')
            elif difficulty == 'extreme':
                monsters.append('tentacle')
                monsters.append('king polypus (extreme)')
                monsters.append('tentacle')
        elif acc.area == 'Forest III':
            if party == None:
                if acc.level < 35:
                    await message.respond(f'You need to be at least level 35 to fight **Visius Ent**', ephemeral=hide)
                    return
            else:
                valid = 1
                for member in party.members:
                    if member != None and account.get_account(member.name, 0).level < 35:
                        valid = 0

                if not valid:
                    await message.respond(f'All party members must be at least level 35 to fight **Visius Ent**', ephemeral=hide)
                    return
            if difficulty == 'normal':
                monsters.append(' ')
                monsters.append('visius ent')
                monsters.append(' ')
            elif difficulty == 'hard':
                monsters.append('silva wisp')
                monsters.append('visius ent (hard)')
                monsters.append('silva wisp')
            elif difficulty == 'extreme':
                monsters.append('enchanted silva wisp')
                monsters.append('visius ent (extreme)')
                monsters.append('enchanted silva wisp')
        else:
            if button:message.response.send_message(f'There is no boss in this area: ({acc.area})', ephemeral=hide)
            else:await message.respond(f'There is no boss in this area: ({acc.area})', ephemeral=hide)
            return

    body = 'You will fight:\n'
    j = 0
    for i in monsters:
        j += 1
        lvl = consts.mob_stats[i]['LVL']
        if boss == 0 or j != 2:
            body += f'**{i.title()}** (lvl **{lvl}**)\n'
        else:
            
            body += f'< **{i.capitalize()}** (lvl **{lvl}**) > **BOSS**\n'

    while len(monsters) < 3:
        monsters.append(' ')

    body += f'\nUse `{pre}actions` to see your battle actions!'

    enemy_hps = [consts.mob_stats[x]['HP'] for x in monsters]
    enemy_cds = []
    for i in range (3):
        cd = consts.mob_stats[monsters[0]]['SPELL.CD']
        if cd > 1:
            enemy_cds.append(random.randint(2, cd))
        else:
            enemy_cds.append(cd)
    hp_mult = 1
    if party != None:
        hp_mult = (party.size-1)*0.4+1
        if party.leader != acc.name:
            await message.respond(f'Only the party leader can start a battle', ephemeral=hide)
            return
        else:
            req_area = acc.area
            valid = 1
            for member in party.members:
                if member != None and member.ptype == 1:
                    macc = account.get_account(member.name, 0)
                    if macc.area != req_area:
                        valid = 0
                    else:continue

            if not valid:
                
                if button:
                    await message.response.send_message(f'All party members must be in the same area to fight', ephemeral=hide)
                else: await message.respond(f'All party members must be in the same area to fight', ephemeral=hide)
                return

            i = party_manager.party_list.index(party)
            party_manager.party_list[i].in_battle = 1
            waiting = []
            for member in party.members:
                if member != None and member.ptype == 1:
                    waiting.append(1)
                else:
                    waiting.append(0)

            party_manager.party_list[i].waiting_on = waiting
            party_manager.write_file(party_manager.party_list)
            for member in party.members:
                if member != None and member.ptype == 1:
                    macc = account.get_account(member.name, 0)
                    macc.battle = account.Battle(1, 0, monsters, enemy_hps, enemy_cds, [' :0',' :0',' :0'], 0, [], mult = hp_mult)

    else:
        acc.battle = account.Battle(1, 0, monsters, enemy_hps, enemy_cds, [' :0',' :0',' :0'], 0, [], mult = hp_mult)
    account.write_file()

    if button:
        await message.response.send_message(body, ephemeral=hide, view=create_attack_view(acc.battle))
    else:await message.respond(body, ephemeral=hide, view=create_attack_view(acc.battle))


def pass_turn(acc, party):
    if acc.battle.potion_cd > 0:
        acc.battle.potion_cd -= 1
    for i, cond in enumerate(acc.battle.p_cond):
        if cond != '':
            if cond[1] > 1:
                acc.battle.p_cond[i][1] -= 1
            else:
                acc.battle.p_cond.pop(i)
    if party != None:
        for member in party.members:
            if member != None and member.ptype == 1 and member.name != acc.name:
                macc = account.get_account(member.name, 0)
                if macc.battle.potion_cd > 0:
                    macc.battle.potion_cd -= 1
                for i, cond in enumerate(macc.battle.p_cond):
                    if cond != '':
                        if cond[1] > 1:
                            macc.battle.p_cond[i][1] -= 1
                        else:
                            macc.battle.p_cond.pop(i)

                
    for i, econd in enumerate(acc.battle.e_cond):
        if econd[1] > 1:
            acc.battle.e_cond[i][1] -= 1
        else:
            acc.battle.e_cond[i] = [account.Effect('', 0),0]
    for i, cd in enumerate(acc.battle.e_spell_cd):
        if cd > 0:
            acc.battle.e_spell_cd[i] -= 1
        else:
            acc.battle.e_spell_cd[i] = max(0,random.randint(consts.mob_stats[acc.battle.enemy[i].name]['SPELL.CD']-1, consts.mob_stats[acc.battle.enemy[i].name]['SPELL.CD']+1))
    body = ''
    for i, enemy in enumerate(acc.battle.enemy):
        if acc.battle.e_hp[i] > 0 and isinstance(enemy, account.Monster):
            body += e_attack(acc, enemy, i, party)
    #acc.mp = min(acc.total_stats['MP'], acc.mp + 3)

    return body
    
def e_attack(acc, enemy, i, party):
    special = ''

    if party != None:
        max_membs = 0
        weakest_acc = None
        for member in party.members:
            if member != None and member.ptype == 1:
                macc = account.get_account(member.name, 0)
                if weakest_acc == None:
                    weakest_acc = macc
                else:
                    if weakest_acc.hp > macc.hp:
                        weakest_acc = macc
                if macc.hp > 0:
                    max_membs += 1
        rand = random.randint(1,max(max_membs+1,1))
        if rand != max_membs+1:
            victim = account.get_account(party.members[rand-1].name, 0)
        else:
            victim = weakest_acc
        vic_name = victim.name
        
        for member in party.members:
            if member != None and member.ptype == 1:
                macc = account.get_account(member.name, 0)
                for cond in macc.battle.p_cond:
                    if cond[0].name == 'protector':
                        victim = macc
                        vic_name = macc.name
    else:
        victim = acc
        vic_name = 'You'

    cond = acc.battle.e_cond[i]
    if cond[1] > 0:

        dmg = 0
        if party != None: hp_mult = (party.size-1)*0.4+1
        else: hp_mult = 1
        max_hp = round(hp_mult*consts.mob_stats[enemy.name]['HP'])
        lvl = consts.mob_stats[enemy.name]['LVL']
        heal = 0
        if cond[0].name == 'rage':
            dmg = max_hp*(0.06+((cond[0].potence-1)*0.02))
            dmg = round(min(dmg, math.ceil(lvl)))
            special = f'**Rage** deals them **{dmg}** damage'
        if cond[0].name == 'poison':
            dmg = max_hp*(0.05+((cond[0].potence-1)*0.01))
            dmg = round(min(dmg, math.ceil(lvl)))
            special = f'**Poison** deals them **{dmg}** damage'
        elif cond[0].name == 'regeneration':
            heal = max_hp*(0.05+((cond[0].potence-1)*0.01))
            heal = round(min(heal, math.ceil(lvl*1.2)))
            special = f'**Regeneration** heals **{heal}** health'
        elif cond[0].name == 'burning':
            dmg = max_hp*(0.07+((cond[0].potence-1)*0.012))
            dmg = round(min(dmg, math.ceil(lvl*1.2)))
            special = f'**Burning** deals them **{dmg}** damage'
        elif cond[0].name == 'bleeding' and not enemy.name.startswith('alpha wolf'):
            dmg = max_hp/30
            dmg = round(min(dmg, lvl))
            special = f'**Bleeding** deals them **{dmg}** damage'
        if acc.battle.e_hp[0]+acc.battle.e_hp[1]+acc.battle.e_hp[2] > 0:
            acc.battle.e_hp[i] = max(1, acc.battle.e_hp[i] - dmg)
            acc.battle.e_hp[i] = min(max_hp, acc.battle.e_hp[i] + heal)


    if consts.mob_stats[enemy.name]['SPELL.CD'] != 0 and acc.battle.e_spell_cd[i] == 0:
        
        if party != None: hp_mult = (party.size-1)*0.4+1
        else: hp_mult = 1
        spell = random.choice(enemy.spells)
        dmg = spell.dmg
        if dmg > 0:
            dmg, _ = formulas.form_dmg(dmg)

            boost = getter.get_total_boost(victim)
            df = victim.total_stats['DEF']
            
            df = victim.total_stats['DEF']*(1+boost['DEF']/100)
            if spell.name == 'penetrating pearl':
                df *= 0.2

            elif spell.name == 'tentacle bloom':
                if party != None: hp_mult = (party.size-1)*0.4+1
                else: hp_mult = 1
                if random.randint(0,1):
                    acc.battle.enemy[0] = account.Monster('tentacle')
                    acc.battle.e_cond[0] = [account.Effect('', 0),0]
                    acc.battle.e_hp[0] = round(hp_mult*consts.mob_stats['tentacle']['HP'])
                else:
                    acc.battle.enemy[2] = account.Monster('tentacle')
                    acc.battle.e_cond[2] = [account.Effect('', 0),0]
                    acc.battle.e_hp[2] = round(hp_mult*consts.mob_stats['tentacle']['HP'])
            elif spell.name == 'call of the leader':
                if party != None: hp_mult = (party.size-1)*0.4+1
                else: hp_mult = 1
                acc.battle.enemy[0] = account.Monster('wolf')
                acc.battle.enemy[2] = account.Monster('wolf')
                acc.battle.e_cond[0] = [account.Effect('', 0),0]
                acc.battle.e_cond[2] = [account.Effect('', 0),0]
                acc.battle.e_hp[0] = round(hp_mult*consts.mob_stats['wolf']['HP'])
                acc.battle.e_hp[2] = round(hp_mult*consts.mob_stats['wolf']['HP'])
            elif spell.name == 'shriek of the leader':
                if party != None: hp_mult = (party.size-1)*0.4+1
                else: hp_mult = 1
                acc.battle.enemy[0] = account.Monster('enchanted wolf')
                acc.battle.enemy[2] = account.Monster('enchanted wolf')
                acc.battle.e_cond[0] = [account.Effect('', 0),0]
                acc.battle.e_cond[2] = [account.Effect('', 0),0]
                acc.battle.e_hp[0] = round(hp_mult*consts.mob_stats['enchanted wolf']['HP'])
                acc.battle.e_hp[2] = round(hp_mult*consts.mob_stats['enchanted wolf']['HP'])

            for cond in victim.battle.p_cond:
                if cond[0].name == 'broken armour':
                    df = max(0, round(df*0.3))
                elif cond[0].name == 'defence':
                    df = round(df*(1.3+((cond[0].potence-1)*0.1)))
                elif cond[0].name == 'protector':
                    if party != None:
                        df = round(df*(1+(0.15*party.size)))
                    else:
                        df = round(df*(1.15))

            dmg = formulas.protect(dmg, df)


            if spell.name == 'life drain':
                acc.battle.e_hp[i] += dmg
                special = f'{enemy.name.title()} gained **{dmg}** HP. '
                if acc.battle.e_hp[i] > round(hp_mult*consts.mob_stats[enemy.name]['HP']):
                    acc.battle.e_hp[i] = round(hp_mult*consts.mob_stats[enemy.name]['HP'])

            dmg_body = f'{vic_name} took **{dmg}** damage. {special}'
        else:
            dmg_body = ''

        cond = acc.battle.e_cond[i]
        if cond[0].name == 'paralysis':
            dmg = max(1, round(dmg*0.1))

        elif cond[0].name == 'dizziness':
            dmg = max(1, round(dmg*(0.65-((cond[0].potence-1)*0.1))))
            if random.randint(1,100) <= 15:
                dmg = 0
                print(dmg)
                crit = '. They missed!'

        elif cond[0].name == 'blindness':
            if random.randint(1,100) <= (30+((cond[0].potence-1)*10)):
                dmg = 0
                crit = '. They missed!'

        
        victim.hp = max(0, victim.hp - dmg)

        rnd = random.randint(1, 100)
        effected = 0
        if rnd <= spell.chance:
            if spell.target == 'player':
                if spell.effect != '':
                    has = 0
                    immune = 0
                    if spell.effect == 'broken armour' and (victim.ring != '' and victim.ring.name == 'inky ring'):
                        immune = 1
                        effected = 0
                    if not immune:
                        for i, cond in enumerate(victim.battle.p_cond):
                            if cond[0].name == spell.effect:
                                has = 1
                                victim.battle.p_cond[i][1] = spell.duration
                                break
                        if not has:
                            victim.battle.p_cond.append([account.Effect(spell.effect,spell.potence), spell.duration])
                        effected = 1
                else:
                    effected = 0
            elif spell.target == 'allies':
                for j in range(len(acc.battle.e_cond)):
                    acc.battle.e_cond[j][0].name = spell.effect
                    acc.battle.e_cond[j][0].potence = spell.potence 
                    acc.battle.e_cond[j][1] = spell.duration
        effect_body = ''
        if effected:
            effect_body += f'{vic_name}, You have **{spell.effect}** for **{spell.duration}** turns.'
        elif dmg == 0 and spell.effect != '':
            effect_body += 'Spell failed!'

        body = f'{i+1} > **{acc.battle.e_hp[i]}/{enemy.max_hp} - {enemy.name}** used spell: **{spell.name}**. {dmg_body}{effect_body}\n'
    else:
        dmg, crit = formulas.form_dmg(enemy.dmg, enemy.crit, enemy.crit_dmg)
        
        boost = getter.get_total_boost(victim)
        df = victim.total_stats['DEF']*(1+boost['DEF']/100)

        for cond in acc.battle.p_cond:
            if cond[0].name == 'broken armour':
                df = max(0, round(df*0.3))
            elif cond[0].name == 'defence':
                df = round(df*(1.3+((cond[0].potence-1)*0.1)))
            elif cond[0].name == 'protector':
                df = round(df*(1.5))

        dmg = formulas.protect(dmg, df)

        cond = acc.battle.e_cond[i]
        if cond[0].name == 'paralysis':
            dmg = max(1, round(dmg*0.1))

        elif cond[0].name == 'dizziness':
            dmg = max(1, round(dmg*(0.65-((cond[0].potence-1)*0.1))))
            if random.randint(1,100) <= 15:
                dmg = 0
                crit = '. They missed!'

        elif cond[0].name == 'blindness':
            if random.randint(1,100) <= (30+((cond[0].potence-1)*10)):
                dmg = 0
                crit = '. They missed!'

        victim.hp = max(0, victim.hp - dmg)
        if crit:
            crit = ' **Critical hit!**'
            q_manager.check_quest(acc, 'crits', '', 1)
        else:
            crit = ''

        body = f'{i+1} > **{acc.battle.e_hp[i]}/{enemy.max_hp} - {enemy.name}** attacked {vic_name} with **{dmg}** damage.{crit} {special}\n'
    return body

def reward(acc, monster, party):
    msg = ''
    mult = 0.5
    for i in acc.battle.enemy:
        if i.name != ' ':
            mult += 0.3
    for i in acc.battle.enemy:
        fbosses = ['alpha wolf', "king polypus", "visius ent"]
        bosses = []
        for j in fbosses:
            bosses.append(j)
            bosses.append(f"{j} (hard)")
            bosses.append(f"{j} (extreme)")
        if i.name in bosses:
            mult = 1
    q_manager.check_quest(acc, 'monster', '', 1)
    if monster.startswith('enchanted') and acc.battle.enemy[1].name != 'alpha wolf (extreme)':
        q_manager.check_quest(acc, 'enchanted monster', '', 1)
    q_manager.check_quest(acc, 'monster', monster, 1)
    q_manager.check_quest(acc, 'boss', monster, 1)
    boost = getter.get_total_boost(acc)
    lvl_diff = abs(acc.level - consts.mob_stats[monster]['LVL'])
    xp_mult = 1
    if lvl_diff > 2:
        xp_mult = max(0.1, 1-(lvl_diff -2)/5)
    
    for i in acc.battle.enemy:
        if i.name in bosses:
            xp_mult = max(0.1, 1-(lvl_diff -4)/5)
    if acc.ring != '' and acc.ring.name == 'aqua ring':
        xp_mult *= 1.1+(acc.ring.upgrade_lvl-1)*0.005
    xp = round(consts.mob_stats[monster]['XP']*mult*xp_mult*(1+boost["XP"]/100))
    q_manager.check_quest(acc, 'xp', '', xp)
    acc.xp += xp
    for loot in consts.mob_loot[monster]:
        rnd = random.randint(1, 10000)/100
        chance = loot[1]
        if acc.ring != '' and acc.ring.name == 'ruby ring':
            chance = chance*(1.2+(acc.ring.upgrade_lvl-1)*0.01)
            chance = chance*(1+boost["LOOT"]/100)
        if rnd <= chance:
            item = loot[0]
            aurum = 0
            for i in acc.inventory:
                if i.name == item:
                    if i.upgrade_lvl > 1:
                        aurum = consts.items[item]['sell'][0][0]
            if acc.ring != '' and acc.ring.name == 'midas ring':
                amount = random.randint(loot[2][0], loot[2][1])
                aurum = round(consts.items[item]['sell'][0][0]* 1.05+(acc.ring.upgrade_lvl-1)*0.006)*amount
            if aurum == 0:
                if item == 'minae':
                    amount = round(random.uniform(loot[2][0], loot[2][1])*mult)
                else:
                    amount = random.randint(loot[2][0], loot[2][1])
                fitem = account.Item(item, amount)
                stack = 1
                j = 0
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
            else:
                item = 'aurum'
                amount = aurum
                acc.aurum += aurum
            msg += f'*+{amount} {item}*, '
    msg += f'*+{xp} XP*'
    
    if party != None:
        for member in party.members:
            if member != None and member.ptype == 1 and member.name != acc.name:
                macc = account.get_account(member.name, 0)
                
                
                lvl_diff = abs(macc.level - consts.mob_stats[monster]['LVL'])
                xp_mult = 1
                if lvl_diff > 2:
                    xp_mult = max(0.1, 1-(lvl_diff -2)/5)
                
                for i in macc.battle.enemy:
                    if i.name in ['alpha wolf', 'king polypus', 'visius ent']:
                        xp_mult = max(0.1, 1-(lvl_diff -4)/5)
                if macc.ring != '' and macc.ring.name == 'aqua ring':
                    xp_mult *= 1.1+(macc.ring.upgrade_lvl-1)*0.005
                xp = round(consts.mob_stats[monster]['XP']*mult*xp_mult)
                macc.xp += xp
                msg += f', __*{macc.name} +{xp} XP*__'
    return msg

        

async def attack(message, enemy, acc, pre, hide, flee=0, button=0, spell=0, channel=0):
    party = party_manager.get_party(acc.name, party_manager.party_list)
    pvp = pvp_manager.get_pvp(acc.name, pvp_manager.pvp_list)
    in_pvp = False
    if pvp != None:
        in_pvp = True
        if pvp.duelists[1].name == acc.name and pvp.in_battle == 0:
            in_pvp = False

    if in_pvp:
        await message.response.send_message(f'Please use `/pvp-attack` or `/pvp-spell` to fight in a pvp match', ephemeral=True)
        return


    if party != None:
        for j, member in enumerate(party.members):
            if member != None and member.ptype == 1 and member.name == acc.name:
                if acc.hp <= 0:
                    if button:
                        await message.response.send_message(f'You are dead and cannot attack', ephemeral=hide)
                    else: await message.respond(f'You are dead and cannot attack', ephemeral=hide)
                    i = party_manager.party_list.index(party)
                    party_manager.party_list[i].waiting_on[j] = 0
                    party_manager.write_file(party_manager.party_list)
                    return

                if party.waiting_on[j] == 0:
                    if button:
                        await message.response.send_message(f'You have already attacked on this turn', ephemeral=hide)
                    else: await message.respond(f'You have already attacked on this turn', ephemeral=hide)
                    return
                else:
                    break

    you = 'You'
    if party != None:
        you = party.members[j].name


    if enemy == '¤':
        if acc.battle.e_hp[0] > 0:
            enemy = 1
        elif acc.battle.e_hp[1] > 0:
            enemy = 2
        elif acc.battle.e_hp[2] > 0:
            enemy = 3
        else:
            acc.battle = account.Battle(0)
    acc.target = enemy
    print(acc.battle.e_spell_cd)
    if not acc.battle.active:
        if button:
            await message.response.send_message('You are not in battle!', ephemeral=hide)
        else: await message.respond(f'You are not in a battle', ephemeral=hide)
        return
    e = int(enemy)-1
    if e < 0 or e >= acc.battle.amount:
        if button:
            await message.response.send_message(f'You can only attack enemies 1 to {acc.battle.amount}', ephemeral=hide)
        else: await message.respond(f'You can only attack enemies 1 to {acc.battle.amount}', ephemeral=hide)
        return
    if acc.battle.e_hp[e] == 0:
        if button:
            await message.response.send_message(f'That enemy is dead or doesn\'t exist. Check `{pre}actions`', ephemeral=hide)
        else: await message.respond(f'That enemy is dead or doesn\'t exist. Check `{pre}actions`', ephemeral=hide)
        return

    boost = getter.get_total_boost(acc)
    if not spell:
        extra_crit = 0
        for cond in acc.battle.p_cond:
            if cond[0].name == 'rage':
                extra_crit = 30

        dmg, crit = formulas.form_dmg(acc.total_stats['DMG'],acc.total_stats['%.CRIT']+boost["%.CRIT"]+extra_crit,acc.total_stats['%.CRIT.DMG']+boost["%.CRIT.DMG"])
        
        dmg = round(dmg *(1+boost["DMG"]/100))
        
        df = acc.battle.enemy[e].df
        cond = acc.battle.e_cond[e]
        if cond[0].name == 'broken armour':
            df = max(0, round(df*0.3))
        elif cond[0].name == 'defence':
            df = round(df*(1.3+((cond[0].potence-1)*0.1)))
        
        elif cond[0].name == 'protector':
            df = round(df*(1.5))

        dmg = formulas.protect(dmg, df)

        if crit:
            crit = '. **Critical hit!**'
            q_manager.check_quest(acc, 'crits', '', 1)
        else:
            crit = ''

        for cond in acc.battle.p_cond:
            if cond[0].name == 'paralysis':
                dmg = max(1, round(dmg*0.1))

            elif cond[0].name == 'dizziness':
                dmg = max(1, round(dmg*(0.65-((cond[0].potence-1)*0.1))))
                if random.randint(1,100) <= 15:
                    dmg = 0
                    crit = '. You missed!'

            
            elif cond[0].name == 'warrior spirit':
                dmg = round(dmg*(1.3+((cond[0].potence-1)*0.1)))
            elif cond[0].name == 'rage':
                dmg = round(dmg*(1.2))

            elif cond[0].name == 'blindness':
                if random.randint(1,100) <= (30+((cond[0].potence-1)*10)):
                    dmg = 0
                    crit = '. You missed!'

        print(acc.battle.e_hp[e])
        print(dmg)
        if flee == 0:acc.battle.e_hp[e] = max(0, acc.battle.e_hp[e] - dmg)
        print(acc.battle.e_hp[e])
        print(dmg)
        
        if flee: body = f'{message.author.name}#{message.author.discriminator}, You failed to escape and missed a turn!\n'
        else: 
            if button:
                body = f'{message.user.name}#{message.user.discriminator}, {you} attacked **{acc.battle.enemy[e].name}** with **{dmg}** damage{crit}\n'
            else: body = f'{message.author.name}#{message.author.discriminator}, {you} attacked **{acc.battle.enemy[e].name}** with **{dmg}** damage{crit}\n'
        if acc.battle.e_hp[e] <= 0:
            rewards = reward(acc, acc.battle.enemy[e].name, party)
            body += f'**{acc.battle.enemy[e].name}** is dead --- {rewards}\n'
            #acc.battle.enemy[e] = account.Monster(' ')
            acc.battle.e_hp[e] = 0

    else:
        for pspell in acc.spells:
            if pspell.name == spell:
                spell = pspell
        dmg = formulas.form_spell_dmg(acc.total_stats['DMG']*(spell.dmg/100),acc.total_stats['%.SPELL.DMG']+boost["%.SPELL.DMG"])
        dmg = round(dmg *(1+boost["DMG"]/100))
        crit = None

        acc.mp -= round(spell.mp_cost*(1-boost["%.SPELL.COST"]))

        q_manager.check_quest(acc, 'spells', '', 1)
        if spell.target != 'multi':
            df = acc.battle.enemy[e].df
            cond = acc.battle.e_cond[e]
            if cond[0].name == 'broken armour':
                df = max(0, round(df*0.3))
            elif cond[0].name == 'defence':
                df = round(df*(1.3+((cond[0].potence-1)*0.1)))
            
            elif cond[0].name == 'protector':
                df = round(df*(1.5))
            
            dmg = formulas.protect(dmg, df)
            print(dmg)
            for cond in acc.battle.p_cond:
                if cond[0].name == 'paralysis':
                    dmg = max(1, round(dmg*0.1))

                elif cond[0].name == 'dizziness':
                    dmg = max(1, round(dmg*(0.65-((cond[0].potence-1)*0.1))))
                    if random.randint(1,100) <= 15:
                        dmg = 0
                        crit = f'. {you} missed!'

                

            
                elif cond[0].name == 'warrior spirit':
                    dmg = round(dmg*(1.3+((cond[0].potence-1)*0.1)))
                elif cond[0].name == 'rage':
                    dmg = round(dmg*(1.2))

                elif cond[0].name == 'blindness':
                    if random.randint(1,100) <= (30+((cond[0].potence-1)*10)):
                        dmg = 0
                        crit = f'. {you} missed!'
            print(dmg)
            special = ''
            if spell.name == 'life drain':
                acc.hp = min(acc.total_stats['HP'], round(acc.hp+min(acc.level*1.3,dmg//2)*(1+boost["HEAL"]/100)))
                special = f' {you} stole {round(min(acc.level*1.3,dmg//2)*(1+boost["HEAL"]/100))} hp!'
            acc.battle.e_hp[e] = max(0, acc.battle.e_hp[e] - dmg)
            if crit != f'. {you} missed!':
                rnd = random.randint(1, 100)
                effected = 0
                if rnd <= spell.chance:
                    if spell.target == 'player':
                        if spell.effect != '':
                            has = 0
                            immune = 0
                            if spell.effect == 'broken armour' and (acc.ring != '' and acc.ring.name == 'inky ring'):
                                immune = 1
                                effected = 0
                            if not immune:
                                for i, cond in enumerate(acc.battle.p_cond):
                                    if cond[0].name == spell.effect:
                                        has = 1
                                        acc.battle.p_cond[i][1] = spell.duration+1
                                        break
                                if not has:
                                    acc.battle.p_cond.append([account.Effect(spell.effect,spell.potence), spell.duration])
                                effected = 1
                        else:
                            effected = 0
                    elif spell.target == 'enemy':
                        effected = 2
                        acc.battle.e_cond[e][0].name = spell.effect
                        acc.battle.e_cond[e][0].potence = spell.potence 
                        acc.battle.e_cond[e][1] = spell.duration+1
                effect_body = ''
                if effected == 2:
                    dmg_body = f'{you} attacked **{acc.battle.enemy[e].name}** with **{spell.name}**. It dealt **{dmg}** damage'
                    effect_body += f'. They have **{spell.effect}** for **{spell.duration}** turns.'
                elif effected == 1:
                    dmg_body = ''
                    effect_body += f'{you} used **{spell.name}** and have **{spell.effect}** for **{spell.duration}** turns.'
                elif dmg == 0 and spell.name != '':
                    dmg_body = ''
                    effect_body += 'Spell failed!'
                elif not effected:
                    dmg_body = f'{you} attacked **{acc.battle.enemy[e].name}** with **{spell.name}**. It dealt **{dmg}** damage'
                    effect_body += f'.'



               
                body = f'{message.user.name}#{message.user.discriminator}, {dmg_body}{effect_body}{special}\n'
                if acc.battle.e_hp[e] <= 0:
                    rewards = reward(acc, acc.battle.enemy[e].name, party)
                    body += f'**{acc.battle.enemy[e].name}** is dead --- {rewards}\n'
                    #acc.battle.enemy[e] = account.Monster(' ')
                    acc.battle.e_hp[e] = 0
        

            else:
                body = f'{you} missed!'
        else:
            body = f'{message.user.name}#{message.user.discriminator}, '
            for e, enemy in enumerate(acc.battle.enemy):
                if acc.battle.e_hp[e] <= 0: continue
                dmg, crit = formulas.form_dmg(acc.total_stats['DMG']*(spell.dmg/100),0,0)
                df = acc.battle.enemy[e].df
                cond = acc.battle.e_cond[e]
                if cond[0].name == 'broken armour':
                    df = max(0, round(df*0.3))
                elif cond[0].name == 'defence':
                    df = round(df*(1.3+((cond[0].potence-1)*0.1)))
                elif cond[0].name == 'protector':
                    df = round(df*(1.5))
                
                dmg = formulas.protect(dmg, df)

                for cond in acc.battle.p_cond:
                    if cond[0].name == 'paralysis':
                        dmg = max(1, round(dmg*0.1))

                    elif cond[0].name == 'dizziness':
                        dmg = max(1, round(dmg*(0.65-((cond[0].potence-1)*0.1))))
                        if random.randint(1,100) <= 15:
                            dmg = 0
                            crit = f'. {you} missed!'

                    elif cond[0].name == 'blindness':
                        if random.randint(1,100) <= (30+((cond[0].potence-1)*10)):
                            dmg = 0
                            crit = f'. {you} missed!'
                acc.battle.e_hp[e] = max(0, acc.battle.e_hp[e] - dmg)
                if crit != f'. {you} missed!':
                    rnd = random.randint(1, 100)
                    effected = 0
                    if rnd <= spell.chance:
                        
                        effected = 2
                        acc.battle.e_cond[e][0].name = spell.effect
                        acc.battle.e_cond[e][0].potence = spell.potence 
                        acc.battle.e_cond[e][1] = spell.duration+1
                    effect_body = ''
                    if effected == 2:
                        dmg_body = f'{you} attacked **{acc.battle.enemy[e].name}** with **{spell.name}**. It dealt **{dmg}** damage'
                        effect_body += f'. They have **{spell.effect}** for **{spell.duration}** turns.'
                    elif effected == 1:
                        dmg_body = ''
                        effect_body += f'{you} used **{spell.name}** and have **{spell.effect}** for **{spell.duration}** turns.'
                    elif dmg == 0 and spell.name != '':
                        dmg_body = ''
                        effect_body += 'Spell failed!'
                    elif not effected:
                        dmg_body = f'{you} attacked **{acc.battle.enemy[e].name}** with **{spell.name}**. It dealt **{dmg}** damage'
                        effect_body += f'.'



                    
                    body += f'{dmg_body}{effect_body}\n'
                    if acc.battle.e_hp[e] <= 0:
                        rewards = reward(acc, acc.battle.enemy[e].name, party)
                        body += f'**{acc.battle.enemy[e].name}** is dead --- {rewards}\n'
                        #acc.battle.enemy[e] = account.Monster(' ')
                        acc.battle.e_hp[e] = 0

                else:
                    body += f'{you} missed!'
    


    body += '\n'
    
    if party != None:
        party.waiting_on[j] = 0
    if party == None or party.waiting_on == [0,0,0]:
        body += pass_turn(acc, party)
        if party != None:
            
            waiting = []
            for member in party.members:
                if member != None and member.ptype == 1 and account.get_account(member.name, 0).hp > 0:
                    waiting.append(1)
                else:
                    waiting.append(0)
            i = party_manager.party_list.index(party)
            party_manager.party_list[i].waiting_on = waiting
            print(waiting)
            body += '\n**--------------------------\n*Next turn*\n--------------------------**\n'

    if acc.hp > 0:
        for cond in acc.battle.p_cond: #lol
            dmg = 0
            mpdmg = 0
            hpheal = 0
            mpheal = 0
            if cond[0].name == 'rage':
                dmg = acc.total_stats["HP"]*(0.06+((cond[0].potence-1)*0.02))
                dmg = round(min(dmg, math.ceil(acc.level)))
                body += f'**Rage** deals **{dmg}** damage'
            elif cond[0].name == 'poison':
                dmg = acc.total_stats["HP"]*(0.05+((cond[0].potence-1)*0.01))
                dmg = round(min(dmg, math.ceil(acc.level/1.2)))
                body += f'**Poison** deals **{dmg}** damage\n'
            elif cond[0].name == 'regeneration':
                hpheal = acc.total_stats["HP"]*(0.03+((cond[0].potence-1)*0.01))*(1+boost["HEAL"]/100)
                hpheal = round(hpheal)
                body += f'**Regeneration** heals **{hpheal}** HP\n'
            elif cond[0].name == 'attunement':
                mpheal = acc.total_stats["MP"]*(0.03+((cond[0].potence-1)*0.01))*(1+boost["HEAL"]/100)
                mpheal = round(mpheal)
                body += f'**Attunement** heals **{mpheal}** MP\n'
            elif cond[0].name == 'burning':
                dmg = acc.total_stats["HP"]*(0.07+((cond[0].potence-1)*0.012))
                dmg = round(min(dmg, acc.level))
                body += f'**Burning** deals **{dmg}** damage'
            elif cond[0].name == 'bleeding':
                dmg = acc.total_stats["HP"]/30
                dmg = round(min(dmg, acc.level/1.2))
                body += f'**Bleeding** deals **{dmg}** damage\n'
            if acc.battle.e_hp[0]+acc.battle.e_hp[1]+acc.battle.e_hp[2] > 0:
                acc.hp = max(0, acc.hp - dmg)
                acc.hp = min(acc.total_stats['HP'], acc.hp + hpheal)
                acc.mp = max(0, acc.mp - mpdmg)
                acc.mp = min(acc.total_stats['MP'], acc.mp + mpheal)


    body += '\n'
    body += f'HP: {acc.hp}/{round(acc.total_stats["HP"])}\n'
    body += f'MP: {acc.mp}/{round(acc.total_stats["MP"])}\n'
    dead = 0
    end_battle = 0
    if acc.hp == 0:

        if getter.get_inv(acc, 'magic wallet') == None: 
            acc.aurum = round(max(0, acc.aurum - acc.aurum/10))
            if you == 'You':
                body += f'You are dead! You lost **{round(acc.aurum/10)}** aurum (10%), respawned in Town 1\n'
            else:
                body += f'{you} died! They lost **{round(acc.aurum/10)}** aurum (10%), respawned in Town 1\n'
        else:
            acc.aurum = round(max(0, acc.aurum - acc.aurum*0.03))
            if you == 'You':
                body += f'You are dead! You lost **{round(acc.aurum*0.03)}** aurum (3%), respawned in Town 1\n'
            else:
                body += f'{you} died! They lost **{round(acc.aurum*0.03)}** aurum (3%), respawned in Town 1\n'

        dead = 1
        valid = 1
        if party != None:
            for member in party.members:
                if member != None and member.ptype == 1:
                    if account.get_account(member.name, 0).hp > 0:
                        valid = 0
        if valid: end_battle = 1
    elif acc.battle.e_hp[0]+acc.battle.e_hp[1]+acc.battle.e_hp[2] == 0:
        body += f'You won the battle!\n'
        #av_lvl = round((consts.mob_stats[acc.battle.enemy[0].name]['LVL']+consts.mob_stats[acc.battle.enemy[1].name]['LVL']+consts.mob_stats[acc.battle.enemy[1].name]['LVL'])/acc.battle.amount)
        end_battle = 1
    else:
        end_battle = 0





    needed = formulas.get_next_xp(acc.level)
    if acc.xp >= needed:
        acc.xp = 0
        acc.level += 1
        if acc.hp != 0:
            didya = 'Fully healed HP and MP'
        else:
            didya = ''
        if button:
            body += f'\n\n**{message.user.mention}**, {you} leveled up to level **{acc.level}**!\n{didya}'

        else:body += f'\n\n**{message.author.mention}**, {you} leveled up to level **{acc.level}**!\n{didya}'

        acc.total_stats = formulas.get_stats(acc)
        if acc.hp != 0:
            acc.hp = acc.total_stats['HP']
            acc.mp = acc.total_stats['MP']
    
    if button:
        image = image_generator.generate_battle(acc,message.user,spell)
    else:
        image = image_generator.generate_battle(acc,message.author,spell)


    if end_battle == 1:
        if button:
            await message.response.send_message(body, ephemeral=hide, view=create_fight_view(acc.battle), file=image)
        else:
            await message.respond(body, ephemeral=hide, view=create_fight_view(acc.battle), file=image)
    else:
        if button:
            await message.response.send_message(body, ephemeral=hide, view=create_attack_view(acc.battle), file=image)
        else:
            await message.respond(body, ephemeral=hide, view=create_attack_view(acc.battle), file=image)


    if end_battle:
        acc.battle = account.Battle(0)
        acc.mp += round(acc.total_stats['MP']/13)
        acc.mp = min(acc.total_stats['MP'], acc.mp)
        
        if party != None:
            for j, member in enumerate(party.members):
                if member != None and member.ptype == 1:
                    macc = account.get_account(member.name, 0)
                    if macc.hp <= 0:
                        macc.area = 'Town 1'
                        macc.hp = macc.total_stats['HP']
                        macc.mp = macc.total_stats['MP']
                    if macc.name != acc.name:
                        macc.mp += round(macc.total_stats['MP']/13)
                        macc.mp = min(macc.total_stats['MP'], macc.mp)
    if dead:
        
        if party != None:
            for j, member in enumerate(party.members):
                if member != None and member.ptype == 1:
                    macc = account.get_account(member.name, 0)
        if party == None:
            acc.area = 'Town 1'
            acc.hp = acc.total_stats['HP']
            acc.mp = acc.total_stats['MP']


    
    if party != None:
        for j, member in enumerate(party.members):
            if member != None and member.ptype == 1:
                macc = account.get_account(member.name, 0)
                macc.battle.e_hp = acc.battle.e_hp
                macc.battle.e_cond = acc.battle.e_cond
                macc.battle.e_spell_cd = acc.battle.e_spell_cd
                macc.battle.enemy = acc.battle.enemy
                if end_battle:
                    i = party_manager.party_list.index(party)
                    party_manager.party_list[i].in_battle = 0
                    macc.battle = account.Battle(0)
        party_manager.write_file(party_manager.party_list)
    if message.guild_id == 934960266775502868:
        channel = message.guild.get_channel(1054119036637692024)
        if counters.SAVES % 40 <2 and channel != 0:
            try:
                file = discord.File('accounts.csv')
                await channel.send('------------------------\naccounts:', file=file)
                file = discord.File('servers.csv')
                await channel.send('servers:', file=file)
            except: pass
    account.write_file()

async def pvp_attack(message, acc, pre, hide, flee=0, button=0, spell=0, channel=0):
    pvp = pvp_manager.get_pvp(acc.name, pvp_manager.pvp_list)
    if pvp == None:
            await message.response.send_message(f'You are not in a duel', ephemeral=True)
            return

    if pvp.duelists[0].name == acc.name:
        if pvp.turn == 1:
            await message.response.send_message(f'It is not your turn to attack', ephemeral=hide)
            return
        opponent = account.get_account(pvp.duelists[1].name, 0)
    else:
        
        if pvp.turn == 0:
            await message.response.send_message(f'It is not your turn to attack', ephemeral=hide)
            return
        opponent = account.get_account(pvp.duelists[0].name, 0)
    you = 'You'
    acc.target = 2
    if opponent.hp < 1:
        if button:
            await message.response.send_message(f'**{opponent.name}** is dead', ephemeral=hide)
        else: await message.respond(f'**{opponent.name}** is dead', ephemeral=hide)
        return

    boost = getter.get_total_boost(acc)
    if not spell:
        extra_crit = 0
        for cond in conds:
            if cond[0].name == 'rage':
                extra_crit = 30

        dmg, crit = formulas.form_dmg(acc.total_stats['DMG'],acc.total_stats['%.CRIT']+boost["%.CRIT"]+extra_crit,acc.total_stats['%.CRIT.DMG']+boost["%.CRIT.DMG"])
        
        
        df = opponent.total_stats["DEF"]
        conds = opponent.battle.p_cond
        for cond in conds:
            if cond[0].name == 'broken armour':
                df = max(0, round(df*0.3))
            elif cond[0].name == 'defence':
                df = round(df*(1.3+((cond[0].potence-1)*0.1)))
            elif cond[0].name == 'protector':
                df = round(df*(1.5))

        dmg = formulas.protect(dmg, df)

        if crit:
            crit = '. **Critical hit!**'
            q_manager.check_quest(acc, 'crits', '', 1)
        else:
            crit = ''

        for cond in acc.battle.p_cond:
            if cond[0].name == 'paralysis':
                dmg = max(1, round(dmg*0.1))

            elif cond[0].name == 'dizziness':
                dmg = max(1, round(dmg*(0.65-((cond[0].potence-1)*0.1))))
                if random.randint(1,100) <= 15:
                    dmg = 0
                    crit = '. You missed!'

            
            elif cond[0].name == 'warrior spirit':
                dmg = round(dmg*(1.3+((cond[0].potence-1)*0.1)))
                
            elif cond[0].name == 'rage':
                dmg = round(dmg*(1.2))

            elif cond[0].name == 'blindness':
                if random.randint(1,100) <= (30+((cond[0].potence-1)*10)):
                    dmg = 0
                    crit = '. You missed!'
        print(opponent.hp)
        print(dmg)
        opponent.hp = max(0, opponent.hp - dmg)
        print(dmg)
        
        
        if button:
            body = f'{message.user.name}#{message.user.discriminator}, {you} attacked **{opponent.name}** with **{dmg}** damage{crit}\n'
        else: body = f'{message.author.name}#{message.author.discriminator}, {you} attacked **{opponent.name}** with **{dmg}** damage{crit}\n'
        if opponent.hp <= 0:
            body += f'**{opponent.name}** is dead!\n'
            #acc.battle.enemy[e] = account.Monster(' ')
            opponent.hp = 0

    else:
        for pspell in acc.spells:
            if pspell.name == spell:
                spell = pspell
        dmg = formulas.form_spell_dmg(acc.total_stats['DMG']*(spell.dmg/100),acc.total_stats['%.SPELL.DMG'])
        crit = None

        acc.mp -= spell.mp_cost
        q_manager.check_quest(acc, 'spells', '', 1)

        if spell.target != 'multi':
            df = opponent.total_stats['DEF']
            conds = opponent.battle.p_cond
            for cond in conds:
                if cond[0].name == 'broken armour':
                    df = max(0, round(df*0.3))
                elif cond[0].name == 'defence':
                    df = round(df*(1.3+((cond[0].potence-1)*0.1)))
                elif cond[0].name == 'protector':
                    df = round(df*(1.5))
            
            dmg = formulas.protect(dmg, df)
            print(dmg)
            for cond in acc.battle.p_cond:
                if cond[0].name == 'paralysis':
                    dmg = max(1, round(dmg*0.1))

                elif cond[0].name == 'dizziness':
                    dmg = max(1, round(dmg*(0.65-((cond[0].potence-1)*0.1))))
                    if random.randint(1,100) <= 15:
                        dmg = 0
                        crit = f'. {you} missed!'

                

            
                elif cond[0].name == 'warrior spirit':
                    dmg = round(dmg*(1.3+((cond[0].potence-1)*0.1)))
                elif cond[0].name == 'rage':
                    dmg = round(dmg*(1.2))

                elif cond[0].name == 'blindness':
                    if random.randint(1,100) <= (30+((cond[0].potence-1)*10)):
                        dmg = 0
                        crit = f'. {you} missed!'
            print(dmg)
            special = ''
            if spell.name == 'life drain':
                acc.hp = min(acc.total_stats['HP'], acc.hp+dmg//2)
                special = f' {you} stole {dmg//2} hp!'
            opponent.hp = max(0, opponent.hp - dmg)
            if crit != f'. {you} missed!':
                rnd = random.randint(1, 100)
                effected = 0
                if rnd <= spell.chance:
                    if spell.target == 'player':
                        if spell.effect != '':
                            has = 0
                            immune = 0
                            if spell.effect == 'broken armour' and (acc.ring != '' and acc.ring.name == 'inky ring'):
                                immune = 1
                                effected = 0
                            if not immune:
                                for i, cond in enumerate(acc.battle.p_cond):
                                    if cond[0].name == spell.effect:
                                        has = 1
                                        acc.battle.p_cond[i][1] = spell.duration+1
                                        break
                                if not has:
                                    acc.battle.p_cond.append([account.Effect(spell.effect,spell.potence), spell.duration])
                                effected = 1
                        else:
                            effected = 0
                    elif spell.target == 'enemy':
                        effected = 2
                        opponent.battle.p_cond.append([account.Effect(spell.effect,spell.potence), spell.duration])
                effect_body = ''
                if effected == 2:
                    dmg_body = f'{you} attacked **{opponent.name}** with **{spell.name}**. It dealt **{dmg}** damage'
                    effect_body += f'. They have **{spell.effect}** for **{spell.duration}** turns.'
                elif effected == 1:
                    dmg_body = ''
                    effect_body += f'{you} used **{spell.name}** and have **{spell.effect}** for **{spell.duration}** turns.'
                elif dmg == 0 and spell.name != '':
                    dmg_body = ''
                    effect_body += 'Spell failed!'
                elif not effected:
                    dmg_body = f'{you} attacked **{opponent.name}** with **{spell.name}**. It dealt **{dmg}** damage'
                    effect_body += f'.'



               
                body = f'{message.user.name}#{message.user.discriminator}, {dmg_body}{effect_body}{special}\n'
                if opponent.hp <= 0:
                    body += f'**{opponent.name}** is dead!\n'
                    #acc.battle.enemy[e] = account.Monster(' ')
                    opponent.hp = 0
        

            else:
                body = f'{you} missed!'
        else:
            body = f'{message.user.name}#{message.user.discriminator}, '
            
            dmg, crit = formulas.form_dmg(acc.total_stats['DMG']*(spell.dmg/100),0,0)
            df = opponent.total_stats['DEF']
            conds = opponent.battle.p_cond
            for cond in conds:
                if cond[0].name == 'broken armour':
                    df = max(0, round(df*0.3))
                elif cond[0].name == 'defence':
                    df = round(df*(1.3+((cond[0].potence-1)*0.1)))
                elif cond[0].name == 'protector':
                    df = round(df*(1.5))
            
            dmg = formulas.protect(dmg, df)

            for cond in acc.battle.p_cond:
                if cond[0].name == 'paralysis':
                    dmg = max(1, round(dmg*0.1))

                elif cond[0].name == 'dizziness':
                    dmg = max(1, round(dmg*(0.65-((cond[0].potence-1)*0.1))))
                    if random.randint(1,100) <= 15:
                        dmg = 0
                        crit = f'. {you} missed!'

                elif cond[0].name == 'blindness':
                    if random.randint(1,100) <= (30+((cond[0].potence-1)*10)):
                        dmg = 0
                        crit = f'. {you} missed!'
            opponent.hp = max(0, opponent.hp - dmg)
            if crit != f'. {you} missed!':
                rnd = random.randint(1, 100)
                effected = 0
                if rnd <= spell.chance:
                    
                    effected = 2
                    opponent.battle.p_cond.append([account.Effect(spell.effect,spell.potence), spell.duration])
                effect_body = ''
                if effected == 2:
                    dmg_body = f'{you} attacked **{opponent.name}** with **{spell.name}**. It dealt **{dmg}** damage'
                    effect_body += f'. They have **{spell.effect}** for **{spell.duration}** turns.'
                elif effected == 1:
                    dmg_body = ''
                    effect_body += f'{you} used **{spell.name}** and have **{spell.effect}** for **{spell.duration}** turns.'
                elif dmg == 0 and spell.name != '':
                    dmg_body = ''
                    effect_body += 'Spell failed!'
                elif not effected:
                    dmg_body = f'{you} attacked **{opponent.name}** with **{spell.name}**. It dealt **{dmg}** damage'
                    effect_body += f'.'



                
                body += f'{dmg_body}{effect_body}\n'
                if opponent.hp <= 0:
                    body += f'**{opponent.name}** is dead\n'
                    #acc.battle.enemy[e] = account.Monster(' ')
                    opponent.hp = 0

            else:
                body += f'{you} missed!'


    body += f'\n**{opponent.name}** - {opponent.hp}/{opponent.total_stats["HP"]} HP\n'
    body += '\n'
    '''
    if party != None:
        party.waiting_on[j] = 0
    if party == None or party.waiting_on == [0,0,0]:
        body += pass_turn(acc, party)
        if party != None:
            
            waiting = []
            for member in party.members:
                if member != None and member.ptype == 1 and account.get_account(member.name, 0).hp > 0:
                    waiting.append(1)
                else:
                    waiting.append(0)
            i = party_manager.party_list.index(party)
            party_manager.party_list[i].waiting_on = waiting
            print(waiting)
            body += '\n**--------------------------\n*Next turn*\n--------------------------**\n'
    '''


    for cond in acc.battle.p_cond: #lol
        dmg = 0
        mpdmg = 0
        hpheal = 0
        mpheal = 0
        if cond[0].name == 'rage':
            dmg = acc.total_stats["HP"]*(0.06+((cond[0].potence-1)*0.02))
            dmg = round(min(dmg, math.ceil(acc.level)))
            body += f'**Rage** deals **{dmg}** damage'
        elif cond[0].name == 'poison':
            dmg = acc.total_stats["HP"]*(0.05+((cond[0].potence-1)*0.01))
            dmg = round(min(dmg, math.ceil(acc.level/1.2)))
            body += f'**Poison** deals **{dmg}** damage\n'
        elif cond[0].name == 'regeneration':
            hpheal = acc.total_stats["HP"]*(0.03+((cond[0].potence-1)*0.01))
            hpheal = round(hpheal)
            body += f'**Regeneration** heals **{hpheal}** HP\n'
        elif cond[0].name == 'attunement':
            mpheal = acc.total_stats["MP"]*(0.03+((cond[0].potence-1)*0.01))
            mpheal = round(mpheal)
            body += f'**Attunement** heals **{mpheal}** MP\n'
        elif cond[0].name == 'burning':
            dmg = acc.total_stats["HP"]*(0.07+((cond[0].potence-1)*0.012))
            dmg = round(min(dmg, acc.level))
            body += f'**Burning** deals **{dmg}** damage'
        elif cond[0].name == 'bleeding':
            dmg = acc.total_stats["HP"]/30
            dmg = round(min(dmg, acc.level/1.2))
            body += f'**Bleeding** deals **{dmg}** damage\n'
        if opponent.hp > 0:
            acc.hp = max(0, acc.hp - dmg)
            acc.hp = min(acc.total_stats['HP'], acc.hp + hpheal)
            acc.mp = max(0, acc.mp - mpdmg)
            acc.mp = min(acc.total_stats['MP'], acc.mp + mpheal)

    
    if acc.battle.potion_cd > 0:
        acc.battle.potion_cd -= 1
    for i, cond in enumerate(acc.battle.p_cond):
        if cond != '':
            if cond[1] > 1:
                acc.battle.p_cond[i][1] -= 1
            else:
                acc.battle.p_cond.pop(i)


    body += '\n'
    body += f'HP: {acc.hp}/{round(acc.total_stats["HP"])}\n'
    body += f'MP: {acc.mp}/{round(acc.total_stats["MP"])}\n'
    dead = 0
    end_battle = 0
    if acc.hp == 0:
        opponent.aurum += pvp.prize
        acc.aurum -= pvp.prize
        body += f'{acc.name} lost the duel !, {opponent.name} won. {opponent.name} gets {pvp.prize} aurum from {acc.name}!\n'
        dead = 1
        valid = 1
        if valid: end_battle = 1
    elif opponent.hp == 0:
        opponent.aurum -= pvp.prize
        acc.aurum += pvp.prize
        body += f'{acc.name} won the duel!, {opponent.name} lost. {acc.name} gets {pvp.prize} aurum from {opponent.name}!\n'
        #av_lvl = round((consts.mob_stats[acc.battle.enemy[0].name]['LVL']+consts.mob_stats[acc.battle.enemy[1].name]['LVL']+consts.mob_stats[acc.battle.enemy[1].name]['LVL'])/acc.battle.amount)
        end_battle = 1
    else:
        end_battle = 0





    needed = formulas.get_next_xp(acc.level)
    if acc.xp >= needed:
        acc.xp = 0
        acc.level += 1
        if acc.hp != 0:
            didya = 'Fully healed HP and MP'
        else:
            didya = ''
        if button:
            body += f'\n\n**{message.user.mention}**, {you} leveled up to level **{acc.level}**!\n{didya}'

        else:body += f'\n\n**{message.author.mention}**, {you} leveled up to level **{acc.level}**!\n{didya}'

        acc.total_stats = formulas.get_stats(acc)
        if acc.hp != 0:
            acc.hp = acc.total_stats['HP']
            acc.mp = acc.total_stats['MP']
    
    if button:
        image = image_generator.generate_pvp(acc,message.user,spell)
    else:
        image = image_generator.generate_pvp(acc,message.author,spell)

    if pvp.turn == 1:
        pvp.turn = 0
    else:
        pvp.turn = 1
    if end_battle == 1:
        if button:
            await message.response.send_message(body, ephemeral=hide, file=image)
        else:
            await message.respond(body, ephemeral=hide, file=image)
    else:
        if button:
            await message.response.send_message(body, ephemeral=hide, view=AttackPvp(), file=image)
        else:
            await message.respond(body, ephemeral=hide, view=AttackPvp(), file=image)


    if end_battle:
        acc.battle = account.Battle(0)
        opponent.battle = account.Battle(0)
        acc.mp += round(acc.total_stats['MP']/13)
        acc.mp = min(acc.total_stats['MP'], acc.mp)
        pvp_manager.pvp_list.remove(pvp)
        
    if dead:
        
        
        acc.area = 'Town 1'
        acc.hp = acc.total_stats['HP']
        acc.mp = acc.total_stats['MP']

    if not dead and end_battle:
        opponent.area = 'Town 1'
        
        opponent.hp = opponent.total_stats['HP']
        opponent.mp = opponent.total_stats['MP']


    
    pvp_manager.write_file()
    account.write_file()

    
async def pvp_flee(message, acc, pre, hide):
    pvp = pvp_manager.get_pvp(acc.name, pvp_manager.pvp_list)

    if not acc.battle.active:
        await message.respond(f'You are not in a battle', ephemeral=True)
        return
    if pvp == None or pvp.in_battle == 0:
        await message.response.send_message(f'You are not in a pvp duel! Use `/flee`', ephemeral=True)
        return
        
    pvp = pvp_manager.get_pvp(acc.name, pvp_manager.pvp_list)
    if acc.name == pvp.duelists[0].name:
        opponent = account.get_account(pvp.duelists[1].name, 0)
    else:
        opponent = account.get_account(pvp.duelists[0].name, 0)
    pvp_manager.pvp_list.remove(pvp)

    opponent.battle = account.Battle(0)
    acc.battle = account.Battle(0)
    
    await message.response.send_message(f'You forfeited the pvp match!\n**{opponent.name}** won the duel, {acc.name} lost!', ephemeral=hide)


    
async def flee(message, acc, pre, hide):
    pvp = pvp_manager.get_pvp(acc.name, pvp_manager.pvp_list)
    in_pvp = False
    if pvp != None:
        in_pvp = True
        if pvp.duelists[1].name == acc.name and pvp.in_battle == 0:
            in_pvp = False

    if in_pvp:
        await message.response.send_message(f'Please use `/pvp-flee` to forfeit a pvp match', ephemeral=True)
        return
    for cond in acc.battle.p_cond:
        if cond[0].name == 'paralysis':
            await message.respond(f'You are paralysed for {cond[1]} more turns! Cannot flee', ephemeral=hide)
            return

    if not acc.battle.active:
        await message.respond(f'You are not in a battle', ephemeral=hide)
        return
    rnd = random.randint(1, 100)
    chance = 40
    for i in acc.battle.enemy:
        if i.name in ['alpha wolf', 'king polypus', 'visius ent']:
            chance = 20

    if rnd <= chance:
        await message.respond(f'You fled the battle succsessfully', ephemeral=hide)
        acc.battle = account.Battle(0)
    else:
        await attack(message, '¤', acc, pre, hide, 1)
    account.write_file()
async def pvp_spell(message, spell, button, acc, pre, hide):
    
    pvp = pvp_manager.get_pvp(acc.name, pvp_manager.pvp_list)
    if pvp == None:
            await message.response.send_message(f'You are not in a duel', ephemeral=True)
            return

    if spell not in consts.spells:
        try:
            await message.respond(f'This spell does not exist', ephemeral=hide)
        except:
            await message.response.send_message(f'This spell does not exist', ephemeral=hide)
        return
    if spell not in list(map(lambda x: x.name, acc.spells)):
        try:
            await message.respond(f'You do not own this spell', ephemeral=hide)
        except:
            await message.response.send_message(f'You do not own this spell', ephemeral=hide)
        return
    if spell not in acc.equipped_spells:
        try:
            await message.respond(f'This spell is not equipped', ephemeral=hide)
        except:
            await message.response.send_message(f'This spell is not equipped', ephemeral=hide)
        return

    for pspell in acc.spells:
        if spell == pspell.name:
            if acc.mp < pspell.mp_cost:
                await message.response.send_message(f'You do not have enough MP to cast this spell. You need **{pspell.mp_cost} MP**, you have {acc.mp} MP', ephemeral=hide)
                return

        
    if not acc.battle.active:
        try:
            await message.respond(f'You are not in a battle', ephemeral=hide)
        except:
            await message.response.send_message(f'You are not in a battle', ephemeral=hide)
        return
    await pvp_attack(message, acc, pre, hide, 1, button, spell)
    account.write_file()
async def spell(message, spell, enemy_number, button, acc, pre, hide):
    if spell not in consts.spells:
        try:
            await message.respond(f'This spell does not exist', ephemeral=hide)
        except:
            await message.response.send_message(f'This spell does not exist', ephemeral=hide)
        return
    if spell not in list(map(lambda x: x.name, acc.spells)):
        try:
            await message.respond(f'You do not own this spell', ephemeral=hide)
        except:
            await message.response.send_message(f'You do not own this spell', ephemeral=hide)
        return
    if spell not in acc.equipped_spells:
        try:
            await message.respond(f'This spell is not equipped', ephemeral=hide)
        except:
            await message.response.send_message(f'This spell is not equipped', ephemeral=hide)
        return

    for pspell in acc.spells:
        if spell == pspell.name:
            if acc.mp < pspell.mp_cost:
                await message.response.send_message(f'You do not have enough MP to cast this spell. You need **{pspell.mp_cost} MP**, you have {acc.mp} MP', ephemeral=hide)
                return

        
    if not acc.battle.active:
        try:
            await message.respond(f'You are not in a battle', ephemeral=hide)
        except:
            await message.response.send_message(f'You are not in a battle', ephemeral=hide)
        return
    await attack(message, enemy_number, acc, pre, hide, 1, button, spell)
    account.write_file()

async def choose_spell(message, acc, hide, pvp = 0):
    if pvp:
        view = SpellPvp()
        pvp = pvp_manager.get_pvp(acc.name, pvp_manager.pvp_list)
        if acc.name == pvp.duelists[0].name:
            opponent = account.get_account(pvp.duelists[1].name, 0)
        else:
            opponent = account.get_account(pvp.duelists[0].name, 0)
        spells = f'Choose a spell to use on **{opponent.name}**...'
    else:
        view = Spell()
        spells = f'Choose a spell to use on **{acc.target} - {acc.battle.enemy[acc.target-1].name}**...'
    
    for i,spell in enumerate(acc.equipped_spells):
        for pspell in acc.spells:
            if pspell.name == spell:
                spell = pspell
        spells+= f'\n**{i+1}>** *{spell.name} (LVL{spell.lvl})*'

    if len(acc.equipped_spells) == 0:
        spells = f'You have no spells equipped. You can buy spells in the `/library` in town and equip them with `/equip-spell`'
    await message.response.send_message(spells, ephemeral=True, view=view)

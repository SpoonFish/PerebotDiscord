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
async def help(message, acc, pre, hide):
    body = '''```\n
Challenge a player to a one-versus-one duel!
> You must both be in the same area to fight


/pvp-request <username+tag> - ask the player to fight

/pvp-accept - accept the pvp request

/pvp-decline - decline the pvp request

/pvp-cancel - cancel an outgoing pvp request

------

/pvp-attack - attack your opponent in a pvp duel

/pvp-spell - use a spell on your opponent

/pvp-flee - forfeit the duel
    \n```'''
    await message.respond(body, ephemeral=hide)


async def decline(message,acc,pre,hide):

    pvp = pvp_manager.get_pvp(acc.name, pvp_manager.pvp_list)
    if pvp == None or pvp.duelists[0].name == acc.name:

        await message.respond('You have not been invited to duel', ephemeral=True)
        return
    else:
        if pvp.in_battle:
            await message.respond(f'You are already in a duel! `/flee` to leave the duel', ephemeral=True)
            return

        pvp_manager.pvp_list.remove(pvp)
        
        await message.respond(f'You declined the pvp request from {pvp.duelists[0].name}', ephemeral=True)
        pvp_manager.write_file(pvp_manager.pvp_list)
        return

async def cancel(message,acc,pre,hide):

    pvp = pvp_manager.get_pvp(acc.name, pvp_manager.pvp_list)
    if not pvp.duelists[0].name == acc.name:

        await message.respond('You have invited someone to duel', ephemeral=True)
        return
    else:
        pvp_manager.pvp_list.remove(pvp)
        
        await message.respond(f'You cancelled the pvp request to {pvp.duelists[1].name}', ephemeral=True)
        pvp_manager.write_file(pvp_manager.pvp_list)
        return

async def accept(message,acc,pre,hide):
    pvp = pvp_manager.get_pvp(acc.name, pvp_manager.pvp_list)
    if pvp == None or pvp.duelists[0].name == acc.name:

        await message.respond('You have not been invited to duel', ephemeral=True)
        return
    else:
        if acc.area != account.get_account(pvp.duelists[0].name, 0).area:
            await message.respond(f'You must be in the same area to duel', ephemeral=True)
            return

        
        if acc.area == 'Town 1' or acc.area == 'Boat 1':
            await message.respond(f'You cannot duel in this area! ({acc.area})', ephemeral=True)
            return

        if acc.battle.active:
            await message.respond(f'You must be out of battle to accept a pvp request', ephemeral=True)
            return
        if acc.aurum < pvp.prize:
            await message.respond(f'You do not have enough aurum to pay if you lose, ({pvp.prize} aurum)', ephemeral=hide)
            return
        opponent = account.get_account(pvp.duelists[0].name, 0)
        if opponent.aurum < pvp.prize:
            await message.respond(f'Opponent does not have enough aurum to pay if they lose, ({pvp.prize} aurum)', ephemeral=hide)
            return
        pvp.duelists[1].accepted = 1
        pvp.in_battle = 1
        
        opponent = account.get_account(pvp.duelists[0].name, 0)
        await message.respond(f'You accepted the pvp request from {pvp.duelists[0].name}', ephemeral=True)
        await message.respond(f'{acc.name} will now fight {pvp.duelists[0].name}!', ephemeral=hide)
        acc.battle = account.Battle(-1,0,[' ','player',' '],[0,opponent.hp,0])
        opponent.battle = account.Battle(-1,0,[' ','player',' '],[0,acc.hp,0])
        pvp_manager.write_file(pvp_manager.pvp_list)
        account.write_file(account.acc_list)
        return

async def invite(message,acc, user,pre,hide, prize):
    nametag = user.name+'#'+user.discriminator

    if nametag == 'Perebot#2527':
        await message.respond('I would love to duel with you but im busy `BEEP BOOP`-ing', ephemeral=True)
        return

    if not checks.account_exists(nametag, 0):
        await message.respond('Account does not exist', ephemeral=True)
        return

    
    if acc.battle.active:
        await message.respond(f'You must be out of battle to request a pvp duel', ephemeral=True)
        return

    if acc.aurum < prize:
        await message.respond(f'You do not have enough aurum to pay if you lose, ({prize} aurum)', ephemeral=True)
        return
    opponent = account.get_account(nametag, 0)
    if opponent.aurum < prize:
        await message.respond(f'Opponent does not have enough aurum to pay if they lose, ({prize} aurum)', ephemeral=True)
        return
    pvp = pvp_manager.get_pvp(acc.name, pvp_manager.pvp_list)
    if pvp == None:
        for pvp in pvp_manager.pvp_list:
            for duelist in pvp.duelists:
                if duelist == None:
                    continue
                elif nametag == duelist.name:
                    await message.respond('This player has already been invited to duel or is in a duel', ephemeral=True)
                    return
        duelists= [
            pvp_manager.Duelist(acc.name, 1),
            pvp_manager.Duelist(nametag, 0)
        ]
        pvp_manager.pvp_list.append(pvp_manager.Pvp(duelists, 0, 0, prize))
        await message.respond(f'Created new pvp match and invited **{nametag}** to duel for {prize} aurum!', ephemeral=hide)
        pvp_manager.write_file(pvp_manager.pvp_list)
    else:
        if pvp.duelists[0].name == acc.name:
            await message.respond('You have already invited someone to duel, use `/pvp-cancel` to cancel the request', ephemeral=True)
            return
        elif pvp.duelists[1].accepted == 0:
            other = pvp.duelists[0].name
            pvp_manager.pvp_list.remove(pvp)
            duelists= [
                pvp_manager.Duelist(acc.name, 1),
                pvp_manager.Duelist(nametag, 0)
            ]
            pvp_manager.pvp_list.append(pvp_manager.Pvp(duelists, 0, 0, prize))
            await message.respond(f'Created new pvp match and invited **{nametag}** to duel for {prize} aurum! (declined a request to duel from {other})', ephemeral=hide)
            pvp_manager.write_file(pvp_manager.pvp_list)
            return
        elif pvp.duelists[1].accepted == 1:
            await message.respond('You are already in a pvp duel!', ephemeral=True)
            return








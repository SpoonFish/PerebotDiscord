import consts
import account
import funcs.formulas as formulas
import funcs.checks as checks
import random
import math
import funcs.getter as getter
import party_manager

async def help(message, acc, pre, hide):
    body = '''```\n
You can use party commands to join your friends and play together!
> You must all be in the same chat to play together.
> Only the party leader can start fights/events.
> All party members must be in the same area to fight.


/party-invite <username+tag> - invite a player to your party (must be party leader)

/party-kick <username+tag> - remove a player from the party (must be party leader)

/party-leave - leave your current party (if you are a leader, this will disband the whole party)

/party-status - get an overview on the HP/MP, area and spells of your party members

----------------------

/party-accept - accept a party invitation

/party-decline - decline a party invitation
    \n```'''
    await message.respond(body, ephemeral=hide)


async def decline(message,acc,pre,hide):

    party = party_manager.get_party(acc.name, party_manager.party_list)
    if party == None:
        await message.respond('You have no invitations', ephemeral=True)
        return
    else:
        for sparty in party_manager.party_list:
            for j, member in enumerate(sparty.members):
                if member == None:
                    continue
                elif acc.name == member.name:
                    if member.ptype == 1:
                        await message.respond(f'You have no invitations', ephemeral=True)

                    else:
                        i = party_manager.party_list.index(sparty)
                        party_manager.party_list[i].members[j] = None
                        await message.respond(f'You refused **{party.leader}**\'s invitation', ephemeral=hide)
                        party_manager.write_file(party_manager.party_list)
                    return

async def accept(message,acc,pre,hide):

    party = party_manager.get_party(acc.name, party_manager.party_list)
    if party == None:
        await message.respond('You have no invitations', ephemeral=True)
        return
    else:
        for sparty in party_manager.party_list:
            for j, member in enumerate(sparty.members):
                if member == None:
                    continue
                elif acc.name == member.name:
                    if member.ptype == 1:
                        await message.respond(f'You are already in a party', ephemeral=True)

                    else:
                        i = party_manager.party_list.index(sparty)
                        party_manager.party_list[i].members[j].ptype = 1
                        await message.respond(f'You have joined **{party.leader}**\'s party', ephemeral=hide)
                        party_manager.write_file(party_manager.party_list)
                    return

async def leave(message,acc,pre,hide):

    party = party_manager.get_party(acc.name, party_manager.party_list)
    if party == None:
        await message.respond('You are not in a party', ephemeral=True)
        return
    else:
        for sparty in party_manager.party_list:
            for j, member in enumerate(sparty.members):
                if member == None:
                    continue
                elif acc.name == member.name:
                    if member.ptype == 1:
                        i = party_manager.party_list.index(sparty)
                        if acc.name != party.leader:
                            await message.respond(f'You left **{party.leader}**\'s party', ephemeral=hide)
                            party_manager.party_list[i].members[j] = None
                        else:
                            await message.respond(f'You disbanded your party', ephemeral=hide)
                            party_manager.party_list.pop(i)
                        party_manager.write_file(party_manager.party_list)

                    else:
                        await message.respond('You are not in a party', ephemeral=True)
                    return

async def status(message,acc,pre,hide):
    party = party_manager.get_party(acc.name, party_manager.party_list)
    if party == None:
        await message.respond('You are not in a party', ephemeral=True)
        return

    body = ''
    for member in party.members:
        if member != None and member.ptype == 1:
            macc = account.get_account(member.name, 0)
            leader = ''
            if party.leader == macc.name:
                leader = '- Party Leader'

            spells = ''
            for spell in macc.spells:
                if spell.name in macc.equipped_spells:
                    spells += f'{spell.name} (LVL{spell.lvl}), '
            spells = spells[:-2]
            body += f'''**{macc.name} {leader}**
```
HP: {macc.hp}/{macc.total_stats['HP']}      DEF: {macc.total_stats['DEF']}
MP: {macc.mp}/{macc.total_stats['MP']}      DMG: {macc.total_stats['DMG']}
SPELLS: {spells}
AREA: {macc.area}
LVL: {macc.level}
```
'''
    await message.respond(body, ephemeral=hide)



async def kick(message,acc,user,pre,hide):
    nametag = user.name+'#'+user.discriminator

    party = party_manager.get_party(acc.name, party_manager.party_list)
    
    if party == None:
        await message.respond('You are not in a party', ephemeral=True)
        return


    if party.leader != acc.name:
        await message.respond('You are not the leader of the party', ephemeral=True)
        return

    if party.leader == nametag:
        await message.respond('You cannot kick yourself from the party', ephemeral=True)
        return

    else:
        for j, member in enumerate(party.members):
            if member == None:
                continue
            elif nametag == member.name:
                if member.ptype == 1:
                    i = party_manager.party_list.index(party)
                    await message.respond(f'You kicked {nametag} from the party', ephemeral=hide)
                    party_manager.party_list[i].members[j] = None
                    party_manager.write_file(party_manager.party_list)

                else:
                    await message.respond('You are not in a party', ephemeral=True)
                return
        await message.respond(f'There is no party member called {nametag}', ephemeral=True)

async def invite(message,acc, user,pre,hide):
    nametag = user.name+'#'+user.discriminator

    if nametag == 'Perebot#2527':
        await message.respond('I would love to play with you but im busy doing... um.. bot things?', ephemeral=True)
        return

    if not checks.account_exists(nametag, 0):
        await message.respond('Account does not exist', ephemeral=True)
        return

    party = party_manager.get_party(acc.name, party_manager.party_list)
    if party == None:
        for party in party_manager.party_list:
            for member in party.members:
                if member == None:
                    continue
                elif nametag == member.name:
                    await message.respond('This player is already in another party', ephemeral=True)
                    return
        members = [
            party_manager.Member(acc.name, 1),
            party_manager.Member(nametag, 0),
            None
        ]
        party_manager.party_list.append(party_manager.Party(acc.name, members, 2, 0, [0,0,0], message.guild.id, message.channel.id))
        await message.respond(f'Created new party and invited **{nametag}** to the party!', ephemeral=hide)
        party_manager.write_file(party_manager.party_list)
    else:
        for j, member in enumerate(party.members):
            if member != None and member.name == acc.name:
                if member.ptype == 0:
                    i = party_manager.party_list.index(party)
                    for party in party_manager.party_list:
                        for member in party.members:
                            if member == None:
                                continue
                            elif nametag == member.name:
                                await message.respond('This player is already in another party', ephemeral=True)
                                return
                    party_manager.party_list[i].members[j] = None
                    members = [
                        party_manager.Member(acc.name, 1),
                        party_manager.Member(nametag, 0),
                        None
                    ]
                    party_manager.party_list.append(party_manager.Party(acc.name, members, 2, 0, [0,0,0], message.guild.id, message.channel.id))
                    await message.respond(f'Created new party and invited **{nametag}** to the party! (left a party you were invited to)', ephemeral=hide)
                    party_manager.write_file(party_manager.party_list)
                    return
        if party.leader != acc.name:
            await message.respond('You are not the leader of the party', ephemeral=True)
            return

        elif party.size == 3:
            await message.respond('The party is already full', ephemeral=True)
            return

        for member in party.members:
            if member == None:
                continue
            elif nametag == member.name:
                await message.respond('This player is already in the party or has already been invited', ephemeral=True)
                return

        for sparty in party_manager.party_list:
            for j, member in enumerate(sparty.members):
                if member == None:
                    continue
                elif nametag == member.name:
                    if member.ptype == 1:
                        await message.respond('This player is already in another party', ephemeral=True)
                    else:
                        i = party_manager.party_list.index(sparty)
                        party_manager.party_list[i].members[j] = None
                    return


        i = party_manager.party_list.index(party)
        if party.members[0] == None:
            party_manager.party_list[i].members[0] = party_manager.Member(nametag, 0)
        elif party.members[1] == None:
            party_manager.party_list[i].members[1] = party_manager.Member(nametag, 0)
        elif party.members[2] == None:
            party_manager.party_list[i].members[2] = party_manager.Member(nametag, 0)
        await message.respond(f'Invited **{nametag}** to the party!', ephemeral=hide)
        party_manager.write_file(party_manager.party_list)





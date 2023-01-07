import discord
import configs
import funcs.formulas as formulas
import consts
import account
import funcs.checks as checks

async def set_channel(channel, ctx):
    if channel == 'all':
        configs.write_configs(ctx.author.guild.name, channel='all')
        await ctx.respond(f'''```
Channel for usage set to all channels
```''')
    else:
        configs.write_configs(ctx.author.guild.name, channel=channel.id)
        await ctx.respond(f'''```
Channel for usage set to {channel.name} (id: {channel.id})
```''')
    return

async def set_ephemeral(ctx, value):
    if value:
        configs.write_configs(ctx.author.guild.name, hidden='1')
        await ctx.respond(f'''```
Ephemeral messages enabled
```''')
    else:
        configs.write_configs(ctx.author.guild.name, hidden='0')
        await ctx.respond(f'''```
Ephemeral messages disabled
```''')


async def give_item(message, item, amount, acc, pre):
    if item == 'area':
        acc.area = amount
        return
    try: amount = int(amount)
    except: 
        await message.channel.send(f'Amount must be number')
        return
    if item == 'aurum':
        acc.aurum += amount
    elif item == 'lvl':
        acc.level += amount
        acc.xp = 0
        acc.total_stats = formulas.get_stats(acc)
    elif item == 'xp':
        acc.xp += amount
        needed = formulas.get_next_xp(acc.level)
        if acc.xp >= needed:
            acc.xp = 0
            acc.level += 1
            await message.channel.send(f'{message.author.mention}, You leveled up to level **{acc.level}**!')
            acc.total_stats = formulas.get_stats(acc)
    else:
        if item in consts.items:
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
            ntag = message.author.name+'#'+message.author.discriminator
            await message.channel.send(f'**{ntag}** Item **{item}** does not exist')
    
    account.write_file()
    return
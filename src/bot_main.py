import os
import discord
#
from discord.ext import commands
import random
import src.account as account
import src.configs as configs
import src.consts as consts
import src.cmds.game.chef as chef_cmds
import src.cmds.game.info as info_cmds
import src.cmds.game.trade as trade_cmds
import src.cmds.game.tavern as tavern_cmds
import src.cmds.game.battle as battle_cmds
import src.cmds.game.smith as smith_cmds
import src.cmds.game.library as library_cmds
import src.cmds.game.interact as interact_cmds
import src.cmds.game.party as party_cmds
import src.cmds.game.pvp as pvp_cmds
from src.cmds import admin
from src.funcs import checks as check
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.all()
client = commands.Bot(intents=intents , command_prefix= "/")
pre = '/'


class VoteView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        voteButton1 = discord.ui.Button(label='Vote on top.gg', style=discord.ButtonStyle.link, url='https://top.gg/bot/1004783529864998932/vote')
        voteButton2 = discord.ui.Button(label='Vote on discordbotlist.com', style=discord.ButtonStyle.link, url='https://discordbotlist.com/bots/perebot/upvote')
        self.add_item(voteButton1)
        self.add_item(voteButton2)


def is_init(ctx):
    if check.no_server_initiated(ctx.author.guild.name):
        return False
    return True

def acc_exist(ctx):
    return check.account_exists(ctx.author)

@client.slash_command(name="initiate", description='Allow the bot to be used and configured in this server')
async def initiate(ctx):
    if check.admin(ctx.author):
        if check.no_server_initiated(ctx.guild.name):
            id = ctx.guild.id
            name = ctx.guild.name
            account.serv_list.append(account.Server(id, name, 0, 'all'))
            account.write_serv_file()
            await ctx.respond('Initiated! Set up server configurations with /configure')
            return
        else:
            await ctx.respond('Server is already set up')
    else:
        await ctx.respond('You need admin permission to do this!', ephemeral=True)

@client.slash_command(name="configure-channel", description='Configure what channel the bot can be used in')
async def configure(ctx, channel: discord.TextChannel = None):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')

    if check.admin(ctx.author):
        if channel == None:
            await ctx.respond(f'''```
Configuration Commands usage:

    {pre}configure-channel <channel name> - sets the channel the bot can be used in
    {pre}configure-all_channels - sets the channel the bot can be used in to all channels
    {pre}configure-private <yes/no> - sets whether the bot sends private(ephemeral) or public messages
```''', ephemeral=hide)
        else:
           await admin.set_channel(channel, ctx) 
    #{pre}configure warning <yes/no> - warn the user if they use a command in the wrong channel
    #{pre}configure prefix <prefix, default:'/'> - change the prefix for bot commands. It is set to / by default
    #```''')
        return

@client.slash_command(name="configure-private", description='Configure if the bot sends private (for the user only) messages or public')
async def configure_ephemeral(ctx, hidden: discord.Option(bool) = None):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    yesno = hidden
    if check.admin(ctx.author):
        if yesno == None:
            await ctx.respond(f'''```
Configuration Commands usage:

    {pre}configure-channel <channel name> - sets the channel the bot can be used in
    {pre}configure-all_channels - sets the channel the bot can be used in to all channels
    {pre}configure-private <yes/no> - sets whether the bot sends private(ephemeral) or public messages
```''', ephemeral=hide)
        else:
           await admin.set_ephemeral(ctx, yesno) 
        return

@client.slash_command(name="configure-all-channels", description='Configure the bot to be used in all channels')
async def configure_all(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    if check.admin(ctx.author):
        await admin.set_channel('all', ctx) 
    else:
        await ctx.respond('You need admin permission to do this!', ephemeral=hide)

@client.slash_command(name="start", description='This command allows you create an account and play the game')
async def start(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    if acc_exist(ctx):
        await ctx.respond(f'You already have an account! Use `{pre}actions` to get started and `{pre}help` to get started!', ephemeral=hide)
        return
    else:
        account.create_account(ctx.author)
        await ctx.respond(f'Account created!\n\n**Welcome to Perebot**,\nPerebot is a bot that allows you to play an rpg game based off the game Pereger\nUse `{pre}actions` to get started and `{pre}help` to get info and see all the commands', ephemeral=hide)

@client.slash_command(name="travel", description='Travel to a nearby area')
async def travel(ctx, area: discord.Option(str)=None):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    
    if not check.channel(ctx.channel): 
        await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
   
    if not check.account_exists(ctx.author): 
        await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    if area == None:
        area = ''

    guild_chan = client.get_guild(934960266775502868).get_channel(1054119036637692024)
    await interact_cmds.travel(ctx, area, acc, pre, hide, 0, guild_chan)
@client.slash_command(name="vote", description='Shows the vote links so you can get rewards for free and support the bot :)')
async def map(ctx):
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    acc = account.get_account(ctx.author)

    await ctx.respond(f"**{acc.name}**\n*You will recieve rewards for voting based on your account level and how many times you have voted*\n\nUse `/vote-rewards` to see possible vote rewards and milestones\nUse `/hero-shop` in town to spend your hero coins\n\nYou can vote the following links:", ephemeral = True, view=VoteView())

@client.slash_command(name="vote-rewards", description='Shows possible rewards you can get when voting')
async def map(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    
    if not check.channel(ctx.channel): 
        await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
   
    if not check.account_exists(ctx.author): 
        await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    acc = account.get_account(ctx.author)
    try:
        votes = acc.vars["votes"][0]
    except:
        votes=  0
    hide = configs.get_config(ctx.guild.name, 'ephemeral')  
    await ctx.respond(f'''**__Normal vote rewards:__**
`100%` - aurum (LVL * 50, randomised by 25%)
`100%` - minae (LVL * 25, randomised by 25%)
`100%` - hero coin, amounts:
 └‐`60%` - 1
 └‐`20%` - 2
 └‐`10%` - 3
 └‐`7%` - 4
 └‐`3%` - 5

**__Milestones__**

**1st Vote** - +15 apple, +5 small hp potion

**5th Vote** - +5 apple pie, +5 blueberry pie

**10th Vote** - +50 magic dust, +5 potato salad, +1 hero coin

**20th Vote** - +150 magic dust, +1500 aurum, +3 hero coin

**30th Vote** - +250 magic dust, +2000 aurum, +1500 minae, +5 hero coin

**40th Vote** - +400 magic dust, +2500 minae, +5 hero coin, +10 silva salad

**50th Vote** - +500 magic dust, +5000 minae, +5 hero coin, +20 honey apples

You have voted {votes} times
''', ephemeral = hide)


@client.slash_command(name="map", description='Shows the map')
async def map(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    await info_cmds.map(ctx, acc, pre, hide)
@client.slash_command(name="actions", description='Shows the current main actions you can do')
async def actions(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    await info_cmds.actions(ctx, acc, pre, hide)

@client.slash_command(name="area", description='Shows information about the current area')
async def area(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    await info_cmds.area(ctx, acc, pre, hide)
@client.slash_command(name="hero-shop", description='Shows items you can buy with hero coins')
async def heroshop(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    if acc.area.startswith('Town'):
        await trade_cmds.hero_shop(ctx, acc, pre, hide)
    else:
        await ctx.respond(f'You can only use this command in the town.', ephemeral=hide)

@client.slash_command(name="shop", description='Shows items you can buy in the current area\'s shop')
async def shop(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    if acc.area.startswith('Town'):
        await trade_cmds.shop(ctx, acc, pre, hide)
    elif acc.area.startswith('Krakow'):
        await trade_cmds.krakow_shop(ctx, acc, pre, hide)
    else:
        await ctx.respond(f'You can only use this command in the town.', ephemeral=hide)

@client.slash_command(name="buy", description='Buy an item from the Town shop (Max: 50 at a time)')
async def buy(ctx, item: discord.Option(str), amount: discord.Option(int) = 1):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    if acc.area.startswith('Town') or acc.area.startswith('Krak'):
        await trade_cmds.buy(ctx, item, amount, acc, pre, hide)
    else:
        await ctx.respond(f'You can only use this command in the town.', ephemeral=hide)

@client.slash_command(name="sell", description='Sell an item (Must sell equipment individually)')
async def sell(ctx, item: discord.Option(str), amount: discord.Option(int) = 1):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    if acc.area.startswith('Town') or acc.area.startswith('Krak'):
        await trade_cmds.sell(ctx, item, amount, acc, pre, hide)
    else:
        await ctx.respond(f'You can only use this command in the town.', ephemeral=hide)

@client.slash_command(name="whatis", description='Shows information about an item, spell or condition')
async def whatis(ctx, item_spell_condition: discord.Option(str)):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    await info_cmds.whatis(ctx, item_spell_condition, acc, pre, hide)

@client.slash_command(name="whois", description='Shows information about a monster')
async def whois(ctx, monster: discord.Option(str)):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    await info_cmds.whois(ctx, monster, acc, pre, hide)

@client.slash_command(name="inv", description='Alias for /inventory. Shows your inventory, equipment and aurum')
async def inv(ctx, page: discord.Option(int) = 1):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    await info_cmds.inv(ctx, acc, page, pre, hide)
@client.slash_command(name="inventory", description='Shows your inventory, equipment and aurum')
async def inv(ctx, page: discord.Option(int) = 1):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    await info_cmds.inv(ctx, acc, page, pre, hide)

@client.slash_command(name="equip", description='Equip a weapon, armour, helmet, ring or shield/mystic item')
async def equip(ctx, item: discord.Option(str)):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    await interact_cmds.equip(ctx, item, acc, pre, hide)

select_slot = [
    discord.OptionChoice("Helmet", "helmet"),
    discord.OptionChoice("Armour", "armour"),
    discord.OptionChoice("Weapon", "weapon"),
    discord.OptionChoice("Ring", "ring"),
    discord.OptionChoice("Offhand (shield, mystic)", "offhand"),
]
@client.slash_command(name="unequip", description='Unequip an equipment slot: weapon, armour, helmet, ring or offhand')
async def unequip(ctx, slot: discord.Option(str, "Choose a slot", choices = select_slot)):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    await interact_cmds.unequip(ctx, slot, acc, pre, hide)

@client.slash_command(name="equip-spell", description='Equip a spell')
async def equip_spell(ctx, spell: discord.Option(str)):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    await interact_cmds.equip_spell(ctx, spell, acc, pre, hide)

@client.slash_command(name="unequip-spell", description='Unequip a spell')
async def unequip_spell(ctx, spell: discord.Option(str)):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    await interact_cmds.unequip_spell(ctx, spell, acc, pre, hide)

@client.slash_command(name="rest", description='Restore all HP and MP at the Town tavern')
async def tavern_rest(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    if acc.area.startswith('Town'):
        await tavern_cmds.rest(ctx, acc, pre, hide)
    else:
        await ctx.respond(f'You can only use this command in the town.', ephemeral=hide)

@client.slash_command(name="tavern-gamble", description='Gamble some aurum at the tavern. 45% chance to win double, 55% chance to lose it!')
async def tavern_gamble(ctx, aurum: discord.Option(int)):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    if acc.area.startswith('Town'):
        await tavern_cmds.gamble(ctx, aurum, acc, pre, hide)
    else:
        await ctx.respond(f'You can only use this command in the town.', ephemeral=hide)

@client.slash_command(name="smith-items", description='Show a list of items that can be crafted in the blacksmith (can be used outside town)')
async def smith_items(ctx, page: discord.Option(int)=1):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await smith_cmds.items(ctx, page, acc, pre, hide)

@client.slash_command(name="smith-check-upgrade", description='Check the cost of an upgrade (or multiple upgrades) for an item')
async def smith_check(ctx, item: discord.Option(str), upgrades: discord.Option(int)=1):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await smith_cmds.check(ctx, item, upgrades, acc, pre, hide)

@client.slash_command(name="library-upgrade", description='Upgrade a spell (max level 5)')
async def library_upgrade(ctx, spell: discord.Option(str)):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    if acc.area.startswith('Town'):
        await library_cmds.upgrade(ctx, spell, acc, pre, hide)
    else:
        await ctx.respond(f'You can only use this command in the town.', ephemeral=hide)

@client.slash_command(name="library-buy", description='Buy a spell from the library')
async def library_buy(ctx, spell: discord.Option(str)):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    if acc.area.startswith('Town'):
        await library_cmds.buy(ctx, spell, acc, pre, hide)
    else:
        await ctx.respond(f'You can only use this command in the town.', ephemeral=hide)

@client.slash_command(name="library-spells", description='Show a list of spells that can be bought in the library (can be used outside town)')
async def library_spells(ctx, tier: discord.Option(int)=1):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await library_cmds.spells(ctx, tier, acc, pre, hide)
'''
@client.slash_command(name="library-check-upgrade", description='Check the cost of an upgrade for a spell')
async def library_check(ctx, spell: discord.Option(str)):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)
    
    if acc.area.startswith('Town'):
        await library_cmds.check(ctx, spell, acc, pre, hide)
    else:
        await ctx.respond(f'You can only use this command in the town.', ephemeral=hide)
'''

@client.slash_command(name="smith-upgrade", description='Upgrade an item (max level 25)')
async def smith_upgrade(ctx, item: discord.Option(str), upgrades: discord.Option(int)=1):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    if acc.area.startswith('Town'):
        await smith_cmds.upgrade(ctx, item, upgrades, acc, pre, hide)
    else:
        await ctx.respond(f'You can only use this command in the town.', ephemeral=hide)

@client.slash_command(name="smith-craft", description='Craft an item from the item list (/smith-items)')
async def smith_craft(ctx, item: discord.Option(str)):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    if acc.area.startswith('Town'):
        await smith_cmds.craft(ctx, item, acc, pre, hide)
    else:
        await ctx.respond(f'You can only use this command in the town.', ephemeral=hide)

@client.slash_command(name="help", description='A guide for how to play, a list of commands and useful tips')
async def help(ctx, page: discord.Option(int)=1):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await info_cmds.help(ctx, page, acc, pre, hide)

@client.slash_command(name="pvp-help", description='A guide for how to use pvp commands')
async def pvphelp(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await pvp_cmds.help(ctx, acc, pre, hide)

@client.slash_command(name="spells", description='Shows your current spells and their levels')
async def spells(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await info_cmds.spells(ctx, acc, pre, hide)

@client.slash_command(name="show-stats", description='Shows a detailed breakdown of your stats from equipment and base stats. Also shows level and xp')
async def stats(ctx, user: discord.User=None):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await info_cmds.stats(ctx, acc, pre, hide, user)

@client.slash_command(name="use", description='Use an item from your inventory (3 turn cooldown fro this command in battle)')
async def use(ctx, item: discord.Option(str), amount: discord.Option(int)=1):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    await interact_cmds.use(ctx, item, amount, acc, pre, hide)

@client.slash_command(name="fight", description='Fight between 1 and 3 monsters in the current area (cannot be used in towns)')
async def fight(ctx, monsters: discord.Option(int)=1):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await battle_cmds.fight(ctx, monsters, acc, pre, hide)
select_dif = [
    discord.OptionChoice("Normal", "normal"),
    discord.OptionChoice("Hard", "hard"),
    discord.OptionChoice("Extreme", "extreme"),
]
@client.slash_command(name="boss", description='Fight the boss in the current area. Can only be used in certain areas (check /actions)')
async def boss(ctx, difficulty: discord.Option(str, "Choose a difficulty", choices = select_dif)):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)
    await battle_cmds.fight(ctx, 'boss', acc, pre, hide, 1, 0, difficulty)

@client.slash_command(name="attack", description='Attack an enemy in battle. Enter the enemy number from 1 to 3 or leave blank to automatically attack')
async def attack(ctx, enemy_number: discord.Option(int)='¤'):
    if not is_init(ctx):
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)
    
    await battle_cmds.attack(ctx, enemy_number, acc, pre, hide)

    
@client.slash_command(name="pvp-attack", description='Attack your opponent in a pvp duel')
async def pvpattack(ctx):
    if not is_init(ctx):
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)
    
    await battle_cmds.pvp_attack(ctx, acc, pre, hide)

@client.slash_command(name="use-spell", description='Attack an enemy in battle using an equipped spell')
async def use_spell(ctx, spell, enemy_number: discord.Option(int)='¤'):
    if not is_init(ctx):
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await battle_cmds.spell(ctx, spell, enemy_number, 0, acc, pre, hide)

@client.slash_command(name="pvp-spell", description='Use a spell on your opponent in a pvp duel')
async def pvpuse_spell(ctx, spell):
    if not is_init(ctx):
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await battle_cmds.pvp_spell(ctx, spell, 0, acc, pre, hide)

@client.slash_command(name="pvp-flee", description='Forfeit the pvp duel')
async def pvpflee(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await battle_cmds.pvp_flee(ctx, acc, pre, hide)

@client.slash_command(name="flee", description='Flee from the current battle with 40% chance to succeed (20% for bosses)')
async def flee(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await battle_cmds.flee(ctx, acc, pre, hide)

@client.slash_command(name="party-help", description='Shows the help page for party commands')
async def party_help(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await party_cmds.help(ctx, acc, pre, hide)

@client.slash_command(name="pvp-request", description='Invite a player to duel with you')
async def pvp_invite(ctx, user: discord.User, aurum_prize: discord.Option(int, "Enter an amount of aurum to wager. Winner takes the aurum from the loser.") = 0):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await pvp_cmds.invite(ctx, acc, user, pre, hide, aurum_prize)

@client.slash_command(name="pvp-accept", description='Accept a pvp duel request')
async def pvp_accept(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await pvp_cmds.accept(ctx, acc, pre, hide)


@client.slash_command(name="pvp-cancel", description='Cancel an outgoing pvp duel request')
async def pvp_cancel(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await pvp_cmds.cancel(ctx, acc, pre, hide)

@client.slash_command(name="pvp-decline", description='Decline a pvp duel request')
async def pvp_decline(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await pvp_cmds.decline(ctx, acc, pre, hide)

@client.slash_command(name="party-invite", description='Invite a player to your party')
async def party_invite(ctx, user: discord.User):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await party_cmds.invite(ctx, acc, user, pre, hide)

@client.slash_command(name="party-leave", description='Leave the current party')
async def party_leave(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await party_cmds.leave(ctx, acc, pre, hide)

@client.slash_command(name="party-accept", description='Accept a party invitation')
async def party_accept(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await party_cmds.accept(ctx, acc, pre, hide)

@client.slash_command(name="party-decline", description='Decline a party invitation')
async def party_decline(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await party_cmds.decline(ctx, acc, pre, hide)

@client.slash_command(name="party-status", description='Get some info about your party members')
async def party_status(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await party_cmds.status(ctx, acc, pre, hide)

@client.slash_command(name="party-kick", description='Kick a player from your party')
async def party_kick(ctx, user: discord.User):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await party_cmds.kick(ctx, acc, user, pre, hide)
    
@client.slash_command(name="leaderboard", description='See a variety of different leaderboards and your placing')
async def leaderboard_show(ctx, user: discord.User=None):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await info_cmds.leaderboard(ctx, acc, pre, hide, user)

@client.slash_command(name="report-bug-or-exploit", description='Report a bug or exploit you might have found')
async def report(ctx, bug: discord.Option(str)):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    guild_chan = client.get_guild(934960266775502868).get_channel(1053701915613089884)
    await info_cmds.report(ctx, acc, pre, hide, bug, guild_chan)

@client.slash_command(name="discord", description='Recieve a link to the official Perebot discord server')
async def discord_inv(ctx):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)
    
    await info_cmds.discord_inv(ctx, acc, pre, hide)
@client.slash_command(name="prepare-restart", description='Heavy is the head that wears the crown...')
async def prepare_restart(ctx):
    acc = account.get_account(ctx.author)
    if check.super_admin(ctx.author):
        channel = client.get_channel(1054119036637692024)
        #await channel.send('lol')
        file = discord.File('accounts.csv')
        await channel.send('accounts:', file=file)
        file = discord.File('parties.csv')
        await channel.send('parties:', file=file)
        file = discord.File('servers.csv')
        await channel.send('servers:', file=file)
        file = discord.File('pvp.csv')
        await channel.send('pvp:', file=file)
        await ctx.respond(f'```SUCCESS```')
    else:
        await ctx.respond(f'```knowledge is the greatest pain of all...```', ephemeral=True)

@client.slash_command(name="give", description='give an item to a player')
async def prepare_restart(ctx, item: discord.Option(str), amount: discord.Option(int), player: discord.User):
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    if check.super_admin(ctx.author):
        acc = account.get_account(ctx.author)
        recipient = account.get_account(player)
        if item == 'aurum':
            recipient.aurum += amount
            await ctx.respond(f'```Gave {amount} aurum to {recipient.name}```', ephemeral=hide)
            account.write_file(account.acc_list)
            return
        if item == 'level':
            recipient.level += amount
            await ctx.respond(f'```Gave {amount} levels to {recipient.name}```', ephemeral=hide)
            account.write_file(account.acc_list)
            return
        if item == 'clone':
            acc.level = recipient.level
            acc.aurum = recipient.aurum
            acc.armour = recipient.armour
            acc.weapon = recipient.weapon
            acc.ring = recipient.ring
            acc.helmet = recipient.helmet
            acc.offhand = recipient.offhand
            acc.inventory = recipient.inventory
            acc.spells = recipient.spells
            acc.spell_slots = recipient.spell_slots
            acc.equipped_spells = recipient.equipped_spells
            acc.xp = recipient.xp
            acc.hp = recipient.hp
            acc.mp = recipient.mp
            acc.total_stats = recipient.total_stats
            await ctx.respond(f'```Copied {recipient.name}\'s account```', ephemeral=hide)
            account.write_file(account.acc_list)
            return
        else:
            try:
                if item not in consts.items:
                    raise
                fitem = account.Item(item, amount)
                stack = 1
                j = 0
                if not check.check_stackable(item): stack = 0
                if stack:
                    stacked = 0
                    for i in recipient.inventory:
                        if i.name == item:
                            recipient.inventory[j].amount += amount
                            stacked = 1
                            break
                        j += 1
                    if not stacked:
                        recipient.inventory.append(fitem)
                else:
                    recipient.inventory.append(fitem)
                await ctx.respond(f'```Gave {amount} {item} to {recipient.name}```', ephemeral=hide)
                account.write_file(account.acc_list)
                return
            except:
                await ctx.respond(f'```ERROR: {item} does not exist```', ephemeral=True)
                return

    else:
        await ctx.respond(f'```leave the cheating to the cheaters...```', ephemeral=True)

@client.event
async def on_ready():

    
    for serv in account.serv_list:
        try:
            serv.name = client.get_guild(serv.id).name
        except:
            pass
    for acc in account.acc_list:
        try:
            print(acc.id)
            user = await client.fetch_user(acc.id)
            acc.name = user.name+'#'+user.discriminator
        except:
            print(f'{acc.id}: ERROR')
            pass

    print(
        f'{client.user} is connected to the following guild:\n'
    )

@client.event
async def on_message(message):
    if message.channel.id == 1059840451093483642:
        if 1:
            vote = message.content[:-1]
            index = vote.find('@')
            userid = int(vote[index+1:])
            for acc in account.acc_list:
                if userid == acc.id:
                    user = await client.fetch_user(int(userid))
                    print(user.name)
                    acc = account.get_account(user)
                    aurum = round(50*acc.level * random.uniform(0.75, 1.25))
                    minae = round(25*acc.level * random.uniform(0.75, 1.25))
                    chance = random.randint(1,100)
                    if chance <= 60:
                        herocoins = 1
                    elif chance <= 80:
                        herocoins = 2
                    elif chance <= 90:
                        herocoins = 3
                    elif chance <= 97:
                        herocoins = 4
                    else:
                        herocoins = 5
                    '''
        **1st Vote** - +15 apple, +5 small hp potion

        **5th Vote** - +5 apple pie, +5 blueberry pie

        **10th Vote** - +50 magic dust, +5 potato salad, +1 hero coin

        **20th Vote** - +150 magic dust, +1500 aurum, +3 hero coin

        **30th Vote** - +250 magic dust, +2000 aurum, +1500 minae, +5 hero coin

        **40th Vote** - +400 magic dust, +2500 minae, +5 hero coin, +10 silva salad

        **50th Vote** - +500 magic dust, +5000 minae, +5 hero coin, +20 honey apples
                    '''
                    try:
                        acc.vars['votes'][0] += 1
                    except:
                        acc.vars['votes'] = [1, 0]

                    if acc.vars['votes'][0] % 50 == 0:
                        await message.channel.send(f"**{user.name} has voted for their {acc.vars['votes'][0]}th time!**")

                    votes = acc.vars['votes'][0]
                    if votes == 10:
                        herocoins += 1
                    elif votes == 20:
                        herocoins += 3
                        aurum += 1500
                    elif votes == 30:
                        herocoins += 5
                        aurum += 2000
                        minae += 1500
                    elif votes == 40:
                        herocoins += 5
                        minae += 2500
                    elif votes == 50:
                        herocoins += 5
                        minae += 5000

                    acc.aurum += aurum
                    account.give_item('hero coin', herocoins, acc)
                    account.give_item('minae', minae, acc)
                    account.write_file(account.acc_list)
                    string = f'''**Thanks {user.name}!**
Your vote is highly appreciated by all of the Perebot community in SpoonFish Studios :)
You have now voted **__{acc.vars['votes'][0]}__** times!

Your **rewards** as a LVL {acc.level} adventurer:
 ━━ <:minae:1059950856365166752> Minae: {minae}
 ━━ <:aurum:1059950170927812698> Aurum: {aurum}
 ━━ <:hero_coin:1059952396786225202> Hero Coins: {herocoins}
'''
                    
                    if votes == 1:
                        account.give_item('apple', 15, acc)
                        account.give_item('small hp potion', 5, acc)
                        string += '''**1st Vote!**
 ━━ Apple: 15
 ━━ Small Hp Potion: 5                    
                        '''
                    elif votes == 5:
                        account.give_item('apple pie', 5, acc)
                        account.give_item('blueberry pie', 5, acc)
                        string += '''**5th Vote!**
 ━━ Apple Pie: 5
 ━━ Blueberry Pie: 5                    
                        '''
                    elif votes == 10:
                        account.give_item('magic dust', 50, acc)
                        account.give_item('potato salad', 5, acc)
                        string += '''**10th Vote!**
 ━━ Magic Dust: 50
 ━━ Potato Salad: 5                    
                        '''
                    elif votes == 20:
                        account.give_item('magic dust', 150, acc)
                        string += '''**20th Vote!**
 ━━ Magic Dust: 150             
                        '''
                    elif votes == 30:
                        account.give_item('magic dust', 250, acc)
                        string += '''**30th Vote!**
 ━━ Magic Dust: 250             
                        '''
                    elif votes == 40:
                        account.give_item('magic dust', 400, acc)
                        account.give_item('silva salad', 10, acc)
                        string += '''**40th Vote!**
 ━━ Magic Dust: 400
 ━━ Silva Salad: 10           
                        '''
                    elif votes == 50:
                        account.give_item('magic dust', 500, acc)
                        account.give_item('honey apples', 20, acc)
                        string += '''**50th Vote!**
 ━━ Magic Dust: 500
 ━━ Honey Apples: 20         
                        '''

                    string += '''
﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌﹌
'''

                    await user.send(string)
        else:
            print(f"vote fail: {vote}")
    if message.author == client.user:
        return
    if message.content.startswith('▓▒░say'):
        
        try: par1 = message.content.split(' ')[1]
        except: par1 = '¤'

        await message.channel.send(par1)
    elif message.content == '▓▒░sendfiles':
        acc = account.get_account(message.author)
        await message.delete()
        if check.super_admin(message.author):
            channel = client.get_channel(1054119036637692024)
            #await channel.send('lol')
            file = discord.File('accounts.csv')
            await channel.send('accounts:', file=file)
            file = discord.File('parties.csv')
            await channel.send('parties:', file=file)
            file = discord.File('servers.csv')
            await channel.send('servers:', file=file)
            file = discord.File('pvp.csv')
            await channel.send('pvp:', file=file)
                

    elif message.content.startswith('▓▒░'):
        await message.delete()
        acc = account.get_account(message.author)
        try: par1 = message.content.split(' ')[1]
        except: par1 = '¤'
        try: par2 = message.content.split(' ')[2]
        except: par2 = '¤'
        try: par3 = message.content.split(' ')[3]
        except: par3 = '¤'
        if par1 != 'area':
            try: 
                x = message.content.split(' ')[-1]
                par2 = int(x)
            except: par2 = '¤'
            try: 
                if par2 != '¤':
                    par1 = message.content[4:].replace(' '+message.content.split(' ')[-1], '')
                else: par1 = message.content[4:]
            except: par1 = '¤'
            print(par1, par2)
            if par2 == '¤':
                par2 = 1
        else:
            par2 = message.content[9:]
            if par2 == '':
                par2 = 'Town 1'
        await message.delete()
        if check.super_admin(message.author):
            await admin.give_item(message, par1, par2, acc, pre)

@client.slash_command(name="chef-recipes", description='Show a list of meals that can be cooked by the chef (can be used outside town)')
async def smith_items(ctx, page: discord.Option(int)=1):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    await chef_cmds.recipes(ctx, page, acc, pre, hide)
@client.slash_command(name="chef-cook", description='Craft a meal from the recipe list (/chef-recipes)')
async def chef_cook(ctx, item: discord.Option(str), amount: discord.Option(int)=1):
    if not is_init(ctx): 
        await ctx.respond(f'There are no configuration settings in this server ({ctx.author.guild.name}) yet. An admin must use /initiate to start using/configuring the bot') ;return
    if not check.channel(ctx.channel): await ctx.respond('You cannot use the bot in this channel!', ephemeral=True); return
    if not check.account_exists(ctx.author): await ctx.respond('You need to create an account first! Use `/start` to create an account', ephemeral=True); return
    hide = configs.get_config(ctx.guild.name, 'ephemeral')
    acc = account.get_account(ctx.author)

    
    if acc.area.startswith('Town'):
        await chef_cmds.cook(ctx, item, amount, acc, pre, hide)
    else:
        await ctx.respond(f'You can only use this command in the town.', ephemeral=hide)



client.run(TOKEN)


import src.consts as consts
import src.counters as counters
import src.account as account
import src.funcs.formulas as formulas
import src.funcs.checks as checks
import src.quest_manager as q_manager
import random
import discord
import src.party_manager as party_manager
import src.counters as counters
import math
import src.funcs.getter as getter
import src.configs as configs
import src.image_generator as image_generator
import src.pvp_manager as pvp_manager

async def shop(message, acc, pre,hide):
    body = f'''```
     S-H-O-P
Food:
> apple              - 10 aurum (sell: 5 aurum)
> blueberry          - 20 aurum (sell: 10 aurum)
> spud               - 30 aurum (sell: 15 aurum)

Offhand items:
> joke book          - 100 aurum (sell: 60 aurum)
> wooden shield      - 100 aurum (sell: 60 aurum)

Armours:
> leather armour     - 100 aurum (sell: 60 aurum)
> leather helmet     - 50 aurum (sell: 30 aurum)

Weapons:
> leather gloves     - 50 aurum (sell: 30 aurum)
> wooden wand        - 50 aurum (sell: 30 aurum)
> small bell         - 50 aurum (sell: 30 aurum)
> wooden sword       - 50 aurum (sell: 30 aurum)

Potions:
> small hp potion    - 100 aurum (sell: 40 aurum)
> medium hp potion  - 250 aurum (sell: 100 aurum)
> large hp potion    - 750 aurum (sell: 250 aurum)

> small mp potion    - 100 aurum (sell: 40 aurum)
> medium mp potion   - 250 aurum (sell: 100 aurum)
> large mp potion    - 750 aurum (sell: 250 aurum)

> small mixed potion - 130 aurum (sell: 50 aurum)

Use {pre}buy <item> <amount> to buy an item
Use {pre}sell <item> <amount> to sell an item
Use {pre}whatis <item> to find info on an item

You have {acc.aurum} aurum
```'''
    await message.respond(body, ephemeral=hide)
async def hero_shop(message, acc, pre,hide):
    
    herocoins = getter.get_inv(acc, 'hero coin')
    if herocoins == None: herocoins = 0
    else: herocoins = herocoins.amount
    body = f'''```
    [H] HEROES - SHOP [H]

> campfire              - 20 hero coins
> magic wallet          - 15 hero coins
> crystal apple         - 5 hero coins
> crystal berry         - 3 hero coins
> midas ring            - 20 hero coins
> phase wings           - 25 hero coins
> brawler elixir        - 4 hero coins
> bard elixir           - 4 hero coins
> knight elixir        - 4 hero coins
> mage elixir           - 4 hero coins

Use {pre}buy <item> <amount> to buy an item
Use {pre}sell <item> <amount> to sell an item
Use {pre}whatis <item> to find info on an item

You have {herocoins} hero coins
You can get hero coins by voting for the bot with /vote
```'''
    await message.respond(body, ephemeral=hide)

async def krakow_shop(message, acc, pre,hide):
    body = f'''```
    || KRAKOW\'S STORE :) ||
Food:
> seafood kebab       - 160 aurum (sell: 80 aurum)
> fish n chips        - 170 aurum (sell: 85 aurum)

Weapons:
> stick sword         - 5000 aurum (sell: 1 aurum)

Potions:
> medium mixed potion - 350 aurum (sell: 130 aurum)

Misc:
> Sleeping Bag        - 2000 aurum (sell: 1000 aurum)
> Mystic Conch        - 3000 aurum (sell: 1500 aurum)

Use {pre}buy <item> <amount> to buy an item
Use {pre}sell <item> <amount> to sell an item
Use {pre}whatis <item> to find info on an item

You have {acc.aurum} aurum
```'''
    await message.respond(body, ephemeral=hide)

async def witch_shop(message, acc, pre,hide):
    body = f'''```
   --/\/ THE BREWERY /\/--

Shiny elixir:
 - 350 aurum
 - 10 pearl
 - 35 magic dust

Lucky elixir:
 - 350 aurum
 - 5 magic fang
 - 35 magic dust

Red elixir:
 - 150 aurum
 - 20 blood
 - 15 magic dust

Gray elixir:
 - 110 aurum
 - 12 scale
 - 10 magic dust

Green elixir:
 - 90 aurum
 - 20 leaf
 - 10 magic dust

Blue elixir:
 - 90 aurum
 - 10 blueberry
 - 10 magic dust


Use {pre}buy <item> <amount> to buy an item
Use {pre}sell <item> <amount> to sell an item
Use {pre}whatis <item> to find info on an item

You have {acc.aurum} aurum
```'''
    await message.respond(body, ephemeral=hide)
    
async def buy(message, item, amount, acc, pre, hide):
    
    for i in acc.inventory:
        if i.name == item:
            if i.upgrade_lvl > 1:
                await message.respond(f'You already have an upgraded version of **{item}**', ephemeral=hide)
                return
    if item == '':
        await message.respond(f'You need to specify an item. Usage: `{pre}buy <item> <amount>`', ephemeral=hide)
        return
    if amount < 1:
        await message.respond('Amount must be greater than 0', ephemeral=hide)
        return
    if amount > 50:
        await message.respond('Amount must be less than 50 (in case you accidentally typed an insanely high number)', ephemeral=hide)
        return
    if acc.area == 'Town 1':
        if not item in consts.shop_items and not item in consts.hero_items:
            await message.respond(f'You cannot buy **{item}** at this shop', ephemeral=hide)
            return
    elif acc.area == 'Krakow\'s Cave':
        if not item in consts.krakow_shop_items:
            await message.respond(f'You cannot buy **{item}** at this shop', ephemeral=hide)
            return
    elif acc.area == 'Witch Hut':
        if not item in consts.witch_shop_items:
            await message.respond(f'You cannot buy **{item}** at this shop', ephemeral=hide)
            return
    if item in consts.items.keys():
        if amount > 1:
            if not checks.check_stackable(item):
                await message.respond(f'You cannot buy more than 1 {item} at a time', ephemeral=hide)
                return
        i = consts.items[item]
        canbuy = True
        pending_removes = []
        aurum_remove = 0
        body = ''
        for c in i['buy']:
            price = c[0]
            itemcost = c[1]
            if itemcost == 'aurum':
                if acc.aurum >= price * amount:
                    aurum_remove = price * amount
                else:
                    body += f'You do not have enough aurum to buy {amount} {item}. You need **{price * amount}** aurum You have **{acc.aurum}** aurum\n'
                    canbuy = False
            else:
                has = 0
                j = 0
                for i in acc.inventory:
                    if i.name == itemcost:
                        has = 1
                        break
                    j+=1
                if not has or acc.inventory[j].amount < price * amount:
                    canbuy = False
                    body += f'You do not have enough {itemcost} to buy {amount} {item}. You need **{price * amount}** {itemcost} You have **{acc.inventory[j].amount}** {itemcost}\n'
                    
                pending_removes.append([j, price * amount])
                

        if canbuy:
            for j in pending_removes:
                acc.inventory[j[0]].amount -= j[1]
            for j,i in enumerate(acc.inventory):
                if i.amount < 1:
                    acc.inventory.pop(j)
            acc.aurum -= aurum_remove
            account.give_item(item, amount, acc)
            if acc.area == 'Witch Hut':
                q_manager.check_quest(acc, 'elixir', '', 1)
            account.write_file()
            await message.respond(body, ephemeral=hide)
        else:
            await message.respond(body, ephemeral = hide)
    else:
        await message.respond(f'Item does not exist: **{item}**', ephemeral=hide)

async def sell(message, item, amount, acc, pre, hide):
    l = getter.get_inv(acc, item)
    try:
        if l.name == acc.weapon.name:
            await message.respond('Please unequip this item before selling it', ephemeral=hide)
            return
    except: pass
    try:
        if l.name == acc.offhand.name:
            await message.respond('Please unequip this item before selling it', ephemeral=hide)
            return
    except: pass
    try:
        if l.name == acc.armour.name:
            await message.respond('Please unequip this item before selling it', ephemeral=hide)
            return
    except: pass
    try:
        if l.name == acc.helmet.name:
            await message.respond('Please unequip this item before selling it', ephemeral=hide)
            return
    except: pass
    try:
        if l.name == acc.ring.name:
            await message.respond('Please unequip this item before selling it', ephemeral=hide)
            return
    except: pass
    if item == '':
        await message.respond(f'You need to specify an item. Usage: `{pre}sell <item> <amount>`', ephemeral=hide)
        return
    try: i = consts.items[item]
    except:
        await message.respond(f'Item does not exist: **{item}**', ephemeral=hide)
        return
    i = getter.get_inv(acc, item)
    if i == None:
        await message.respond(f'You do not have any {item}', ephemeral=hide)
        return
    price = consts.items[item]['sell'][0][0]
    itemsell = consts.items[item]['sell'][0][1]
    if amount < 1:
        await message.respond('Amount must be greater than 0', ephemeral=hide)
        return
    j = 0
    for i in acc.inventory:
        if i.name == item:
            l = acc.inventory[j]
            amount = min(l.amount, amount)
            acc.inventory[j].amount -= amount
            try:
                if l.name == acc.weapon.name:
                    acc.weapon = ''
            except: pass
            try:
                if l.name == acc.offhand.name:
                    acc.offhand = ''
            except: pass
            try:
                if l.name == acc.armour.name:
                    acc.armour = ''
            except: pass
            try:
                if l.name == acc.helmet.name:
                    acc.helmet = ''
            except: pass
            try:
                if l.name == acc.ring.name:
                    acc.ring = ''
            except: pass
            
            if l.amount == 0:
                del acc.inventory[j]
            break
        j += 1
    if itemsell == 'aurum':
        if getter.get_inv(acc, 'midas ring') != None:
                price = round(consts.items[item]['sell'][0][0]* 1.05+(getter.get_inv(acc, 'midas ring').upgrade_lvl-1)*0.06)
        acc.aurum += price * amount
    else:
        account.give_item(itemsell, price*amount, acc)
    acc.total_stats = formulas.get_stats(acc)
    account.write_file()
    await message.respond(f'You sold **{amount} {item}** for **{price * amount}** {itemsell}', ephemeral=hide)


